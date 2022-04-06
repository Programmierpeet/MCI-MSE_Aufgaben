# UC 2.0

#%% UC 2.1 Einlesen der Daten

#Alle benötigten Bibliotheken importieren
import os
import numpy as np
import pandas as pd
import neurokit2 as nk
import json

# Überprüfen, ob Dateien vorhanden sind
list_of_new_tests = [] #Neues und leeres Array erstellen
folder_current = os.path.dirname(__file__) 
folder_input_data = os.path.join(folder_current, 'input_data') #joins the path "input_data"

def get_new_data():
    '''searching for ending ".csv" in "input_data"'''
    for file in os.listdir(folder_input_data):
        if file.endswith(".csv"):
            file_name = os.path.join(folder_input_data, file)
            subject_id = file_name.split(".")[0][-1]
            new_ecg_data = pd.read_csv(file_name)
            ## Erstellen einer Liste von Tests, die zu verarbeiten sind
            list_of_new_tests.append(new_ecg_data)
    return new_ecg_data

new_ecg_data = get_new_data() #Funktion definiert new_ecg_data
new_ecg_data["Subject_3"].plot() #Subject 3 kann geplottet werden

#%% UC 2.2 Vorverarbeiten der Daten

## Anlegen einer Zeitreihe der Herzfrequenz aus den EKG-Daten
ekg_data=pd.DataFrame()
ekg_data["ECG"] = new_ecg_data["Subject_3"]

# Find peaks
peaks, info = nk.ecg_peaks(ekg_data["ECG"], sampling_rate=1000)
#Herzschläge während des Tests (=400)
number_of_heartbeats = peaks["ECG_R_Peaks"].sum()
#Test dauert 3 Minuten: Datengröße von 180.000 durch sampling rate von 1000 hz durch 60 Sekunden (sonst Ergebnis für Sekunden)
duration_test_min = ekg_data.size/1000/60
#Durchschnittlicher Herzschlag: (400/3)
average_hr_test = number_of_heartbeats / duration_test_min
## Calculate heart rate moving average
peaks['average_HR_10s'] = peaks.rolling(window=10000).mean()*60*1000 #Window = über diesen Bereich wird Data immer wieder betrachtet (Also hier jeweils Zeitfenster von 10 Sekunden). Mean gibt duechschnitt
peaks['average_HR_10s'].plot() #Plottet den durchschnittlichen Puls über Bereich von 10 Sekunden
#%% UC 2.3 Analysieren der Daten auf Abbruch-Kriterium

#termination = False #defaultwert auf False
folder_input_data = os.path.join(folder_current, 'input_data')
#aus input_data wird subject_3.json gejoined
file_name = folder_input_data = os.path.join(folder_input_data, 'subject_3.json')
f = open(file_name)
# returns JSON object as a dictionary
subject_data = json.load(f)
##Vergleich der Maximalen Herzfrequenz mit Alter des Patienten
#höchster Puls von jeweiligen 10 Sekunden abschnitten (=186)
maximum_hr = peaks['average_HR_10s'].max()
subject_max_hr = 220 - (2022 - subject_data["birth_year"]) #generell wird gesagt, dass der maximale erreichbare Puls aus 220 - dem Alter berechnet wird
def abbruch():
    '''Ist der maximale Puls größer, als 90% des Sollwerts, wird abgebrochen'''    
    if maximum_hr > subject_max_hr*0.90:
        termination = True
    else:
        termination = False

termination = abbruch() #abbruch hängt von der Funktion ab
#%% UC 2.4 Erstellen einer Zusammenfassung
#Erstellen eines Arrays

def print_all():
    '''druckt alle nötigen Werte aus'''
    print("Summary for Subject " + str(subject_data["subject_id"]))
    print("Year of birth:  " + str(subject_data["birth_year"]))
    print("Test level power in W:  " + str(subject_data["test_power_w"]))
    print(" \n")
    print("Maximum HR was: " + str(maximum_hr))
    print("Was test terminated because exceeding HR " + str(termination))

#Ausgabe eines Zusammenfassung
print_all()

#%% UC 2.5 Visualisierung der Daten

# Opening JSON file
def opening_json():
    '''Öffnet Leistungsdaten und gibt Länge und power_watts wieder'''
    folder_input_data = os.path.join(folder_current, 'input_data')
    file_name =  os.path.join(folder_input_data, 'power_data_3.txt')
    power_data_watts = open(file_name).read().split("\n")
    power_data_watts.pop(-1) #Löscht letztes Element aus power data watts
    return len(power_data_watts), power_data_watts.pop(-1) #länge und PowerWatts werdern returnt

_ , power_data_watts = opening_json() #Nur P.D.W.
length_of_data, _  = opening_json() #Nur Länge
#Drucken der Länge
print(length_of_data)
#print(power_data_watts)
# %%
## Erstellung eines Plots
def downsample_peaks():
    '''Schwächung der Spitzen'''
    peaks_downsampled = peaks[peaks.index % 1000 == 0]  
    peaks_downsampled = peaks_downsampled.reset_index(drop=True)
    peaks_downsampled = peaks_downsampled.drop(["ECG_R_Peaks"],axis=1)
    peaks_downsampled["Power (Watt)"] = pd.to_numeric(power_data_watts)
    return peaks_downsampled

peaks_downsampled = downsample_peaks()
#plotting downsampled peaks
peaks_downsampled.plot()


#%% UC 2.6 Manuelle Eingabe eines Abbruchkritierums

## Abfrage an Nutzer:in, ob Abgebrochen werden soll

def manueller_abbruch():
    '''Wird False verändert, so wird der Test als ungültig erklärt und abgebrochen'''
    manual_termination = False
    manual_termination = input("Is this test invalid? (leave blank if valid): ")
    if manual_termination != False:
        termination = True

manual_termination = manueller_abbruch()

#%% UC 2.7 Speichern der Daten


# Speichern der Daten.
data = {"User ID": subject_data["subject_id"], "Reason for test termation": manual_termination, "Average Heart Rate": average_hr_test, "Maximum Heart Rate": subject_max_hr, "Test Length (s)": len(power_data_watts), "Test Power (W)": subject_data["test_power_w"], "Average Power": peaks_downsampled["Power (Watt)"].mean()}
#to be saved data
json_data_to_save = json.dumps(data)
    
def search_dir():
    '''derzeitiger Ordner wird geöffnet und Pfad angelegt'''
    folder_current = os.path.dirname(__file__) 
    folder_input_data = os.path.join(folder_current, 'result_data')
    results_file = os.path.join(folder_input_data, 'data.json')
    return results_file

results_file = search_dir()
#Pfad geöffnet und als 'utf-8' encoded
with open(results_file, 'w', encoding='utf-8') as f:
    #json data abgespeichert
    json.dump(json_data_to_save, f, ensure_ascii=False, indent=4)
# %%

# Bewertung: Solide Arbeit! Für nächstes mal bitte nochmal Docstrings ansehen, dort können gerne mehr Angaben wie Input / Return Informationen gemacht werden
