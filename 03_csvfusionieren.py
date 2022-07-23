"""
Mit dieser Datei können die CSV-Dateien zusammengefügt werden!
"""

# Import
import os
import glob
import pandas as pd

# Alle CSV-Dateien einlesen und ausgeben
files_joined = os.path.join('JSON-Dateien/Aarhus Spielstats/Spiele_CSV/*.csv')

# Liste zurückgeben mit allen CSV-Dateien
list_files = glob.glob(files_joined)

# Alle CSV-Dateien in einem Dataframe zusammenführen
dataframe2 = pd.concat(map(pd.read_csv, list_files), ignore_index=True)

# Spalte mit nur 1 Wert, wenn Max = Min
column_with_one_value = dataframe2.max() == dataframe2.min()

# DataFrame erstellen und Spalte benennen
df = pd.DataFrame(column_with_one_value)
df.columns = ['Column']

# Indizes ziehen für Datensätze mit Max = Min
indexNames = df[df['Column'] == True].index

# Spalten mit nur 1 Wert ausgeben, um redundante zu entfernen
print(indexNames)

# Unnötige Spalten löschen
del dataframe2['roundId']
del dataframe2['competitionId']
del dataframe2['seasonId']

# Duplikate entfernen
dataframe2 = dataframe2.drop_duplicates()

# DataFrame abspeichern
dataframe2.to_csv('JSON-Dateien/Aarhus Spielstats/Spiele_CSV/04_Fusion.csv', index=False)

# Vier Fusionsdateien einlesen
aarhus = 'JSON-Dateien/Aarhus Spielstats/Spiele_CSV/04_Fusion.csv'
juventus = 'JSON-Dateien/Juventus Spielstats/Spiele_CSV/01_Fusion.csv'
midtjylland = 'JSON-Dateien/Midtjylland Spielstats/Spiele_CSV/03_Fusion.csv'
genua = 'JSON-Dateien/Genua Spielstats/Spiele_CSV/02_Fusion.csv'

# Vier CSV-Dateien als gebündelte CSV-Datei abspeichern
dataframe1 = pd.concat(map(pd.read_csv, [aarhus, juventus, midtjylland, genua]))
dataframe1.to_csv('JSON-Dateien/01_final.csv', index=False)
