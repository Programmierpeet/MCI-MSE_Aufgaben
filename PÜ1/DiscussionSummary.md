## Project background

### Purpose of project

Übersichtliche und präzise Visualisierung der Daten um eine umfassende Leistungsdiagnostik erstellen zu können. Eine zuverlässige Datenlieferung zu allen Zeitpunkten soll gewährleistet werden. Die Software sollte möglichst einfach zu bedienen sein. 

### Scope of project

Die Software umfasst eine Leistungsdiagnostik von EKG-Daten der Patient/innen durch Analyse und Visualisierung, an einem bereits bestehenden Ergometer. Der Puls wird über einen Zeitraum von drei Minuten erfasst und gespeichert. Zudem werden Daten wie Name, eine technische ID und Geburtsdatum vermerkt.

### Other background information

Eine Überprüfung auf das eingestellte Abbruchkriterium wird durch eine Analyse der Daten stets gewährleistet. Sollte es dennoch zu Problemen kommen, ist auch ein manueller Abbruch des Tests jederzeit möglich. Um einen versehentlichen Abbruch zu vermeiden werden die Daten stets bis zur Bestätigung des Abbruchs gespeichert. Erst nach dieser Bestätigung wird der Test als "abgebrochen" gewertet.

## Perspectives
### Who will use the system?

Daten können von Athleten zur privaten Leistungsverbesserung genutzt, oder in Studien von Diagnostikern eingesetzt werden, um eine präzise Leistungsdiagnostik von Probanden zu erstellen. Weiters wird es auch möglich sein, die Software im Medizinbereich von Ärzten und Patienten genutzt zu werden, um beispielsweise Herzkrankheiten zu erkennen.

### Who can provide input about the system?

Diagnostiker, welche bereits Erfahrung in der Leistungsdiagnostik besitzen und täglich damit arbeiten. Auch können wissbegierige Athleten ihrten Beitrag leisten. Zudem kann die Fachexpertise von Julian Huber oder Yunus Schmierander herangezogen werden.


## Project Objectives
### Known business rules

Namen des Nutzers, seine technische ID, sowie Geburtsdatum werden gespeichert. Diese Daten werden auch verarbeitet werden. 

### System information and/or diagrams

Beispiel von aufgezeichneten EKG Daten
![](ekg_example.png)

Aus diesem muss die Herzrate bestimmt werden.

### Assumptions and dependencies

Als Input-Data wurden drei verschiedene Datensäzte für jeweils drei verschiedene Personen generiert. Der erste Datensatz trägt den Namen "ecg_data_subject_#Nummer.csv" und lässt durch den Namen darauf schließen, dass es sich wahrscheinlich um die Daten des Elektrokardiogrammes handelt. Die Datei enthält jeweils 180`000 Daten, wobei diese meist aus einen Zahlenwert von -1 bis +1 bestehen.
Der zweite Datensatz trägt den Namen "power_data_#Nummer.txt" und besteht jeweils aus 180 Werten. Diese Werte beschreiben wahrscheinlich die von den Personen generierten Watt während des Tests. Die erste Person brachte im Durchschnitt 100 Watt zusammen, die Zweite 200 und die Dritte 300.
Als letzten Datensatz, mit dem Namen "subject_#Nummer.json", wurden generelle Informationen zu den Personen bereitgestellt. Diese umfassen ihre ID-Nummer, deren generierte Watt, Geburtsjahr und die Dauer des Testlaufs.

### Design and implementation constraints

Die Visualisierung der Daten der Probanten soll so präzise wie möglich sein, sodass es nicht zu Fehldiagnostiken kommen kann, welche der Software vorzuwerfen sind. Das Interface soll schlicht gestaltet werden und nur die wichtigsten Informationen wiedergeben.

## Risks

Da die Entwicklung der Software noch nicht im Gange ist, sind derer möglichen Fehler noch unbekannt. Fehlerquellen können aber natürlich Software, Hardware , oder auch der Nutzer sein. Zum Beispiel könnte der Nutzer die Elektroden am Körper falsch befestigen oder seine Hände vom Sensor am "Lenker" des Ergometers nehmen, sodass der Puls gar nicht, oder falsch gemessen wird.

## Known future enhancements

Die Farbpalette der Grafik soll veränderbar sein, sodass diese der Farbe des jeweiligen Ergometers angepasst werden kann. Die Software könnte auf andere Diagnostiken wie beispielsweise dem Laktatwert im Blut erweitert werden, um die Anaerobe Schwelle eines Probanten messen zu können.

## References

- [Link zur Aufgabenstellung](tbd)

## Open, unresolved or TBD issues

Vor dem Start des Projekt gibt es keine wirklichen Probleme, diese werden aber bestimmt auftreten. Zu Erledigen gilt der Download von Visual Studios und die Vervollständigung dieser Abgabe bis Sonntag, den 20.03.2022.
