"""
Mit dieser Datei können die JSON-Dateien aufgespalten und bereinigt werden!
"""

# Import
import json
import pandas as pd

# JSON öffnen
with open('JSON-Dateien/Juventus Spielstats/Atalanta_PlayerStats.json', 'r') as a:
    teamseason = json.load(a)

# JSON strukturieren
with open('JSON-Dateien/Juventus Spielstats/Atalanta_PlayerStats2.json', 'w') as a:
    json.dump(teamseason, a, indent=2)

# DataFrame erstellen
df_teamstats = pd.DataFrame(teamseason['players'])

# print(df_teamstats.columns.values)
# print(df_teamstats.head())

# Spalte positions in einzelne Spalten auflösen
df_positions = df_teamstats['positions']
df_positions = pd.DataFrame(list(df_positions))
df_positions.columns = ['position1', 'position2', 'position3']
del df_teamstats['positions']
df_teamstats = df_teamstats.join(df_positions, how='outer')

# Spalte positions1 in einzelne Spalten auflösen
df_positions1 = df_teamstats['position1']
df_positions1 = pd.DataFrame(dict(df_positions1))
df_positions1 = df_positions1.transpose()
df_positions1.columns = ['position1', 'percent1']
del df_teamstats['position1']
df_teamstats = df_teamstats.join(df_positions1, how='outer')

# Spalte positions1_neu in einzelne Spalten auflösen
df_positions1_neu = df_teamstats['position1']
df_positions1_neu = pd.DataFrame(dict(df_positions1_neu))
df_positions1_neu = df_positions1_neu.transpose()
df_positions1_neu.columns = ['position1_name', 'position1_code']
del df_teamstats['position1']
df_teamstats = df_teamstats.join(df_positions1_neu, how='outer')

# Spalte positions2 in einzelne Spalten auflösen
df_positions2 = df_teamstats['position2']
df_positions2 = pd.DataFrame(dict(df_positions2))
df_positions2 = df_positions2.transpose()
df_positions2.columns = ['position2', 'percent2']
del df_teamstats['position2']
df_teamstats = df_teamstats.join(df_positions2, how='outer')

# Spalte positions2_neu in einzelne Spalten auflösen
df_positions2_neu = df_teamstats['position2']
df_positions2_neu = pd.DataFrame(dict(df_positions2_neu))
df_positions2_neu = df_positions2_neu.transpose()
df_positions2_neu.columns = ['position2_name', 'position2_code']
del df_teamstats['position2']
df_teamstats = df_teamstats.join(df_positions2_neu, how='outer')

# Spalte positions3 in einzelne Spalten auflösen 
df_positions3 = df_teamstats['position3']
df_positions3 = pd.DataFrame(dict(df_positions3))
df_positions3 = df_positions3.transpose()
df_positions3.columns = ['percent3', 'position3']
del df_teamstats['position3']
df_teamstats = df_teamstats.join(df_positions3, how='outer')

# Spalte positions3_neu in einzelne Spalten auflösen
df_positions3_neu = df_teamstats['position3']
df_positions3_neu = pd.DataFrame(dict(df_positions3_neu))
df_positions3_neu = df_positions3_neu.transpose()
df_positions3_neu.columns = ['position3_code', 'position3_name']
del df_teamstats['position3']
df_teamstats = df_teamstats.join(df_positions3_neu, how='outer')

# Spalte total in einzelne Spalten auflösen
df_total = df_teamstats['total']
df_total = pd.DataFrame(list(df_total))
del df_teamstats['total']
df_teamstats = df_teamstats.join(df_total, how='outer')

# Spalte average in einzelne Spalten auflösen
df_average = df_teamstats['average']
df_average = pd.DataFrame(list(df_average))
del df_teamstats['average']
df_teamstats = df_teamstats.join(df_average, how='left', lsuffix='_total', rsuffix='_average')

# Spalte percent in einzelne Spalten auflösen
df_percent = df_teamstats['percent']
df_percent = pd.DataFrame(list(df_percent))
del df_teamstats['percent']
df_teamstats = df_teamstats.join(df_percent, how='left', lsuffix='_1', rsuffix='_2')

# Indizes ziehen für Datensätze mit Matches = 0
indexNames = df_teamstats[df_teamstats['matches'] == 0].index
# Nicht-Spieler-Datensätze aus DataFrame löschen
df_teamstats.drop(indexNames, inplace=True)

# Speichern in CSV-Datei
df_teamstats.to_csv('JSON-Dateien/Juventus Spielstats/Atalanta.csv', index=False)
