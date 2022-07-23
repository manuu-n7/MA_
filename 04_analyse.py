"""
Mit dieser Datei kann der aufbereitete Datensätze analysiert werden!
"""

# Import
import pandas as pd
import matplotlib.pyplot as plt

# Bereinigte CSV-Datei laden
soccer = pd.read_csv('JSON-Dateien/01_final.csv')
# print(soccer.shape)             # Zeilen- und Spaltenanzahl ausgeben
# print(soccer.describe())        # Datensatzbeschreibung ausgeben
# print(soccer.head())            # Ersten fünf Zeilen ausgeben

# DataFrame filtern auf Stürmerfähigkeiten
soccer = soccer.filter(items=['playerId', 'matches', 'minutesOnField', 'goals_total',
                              'xgShot_total', 'successfulKeyPasses_total', 'assists_total',
                              'xgAssist_total', 'shots_total', 'shotsOnTarget_total',
                              'offensiveDuels_total', 'offensiveDuelsWon_total', 'touchInBox_total'])

# DataFrame erstellen und Namen vergeben
soccer = soccer[(soccer.playerId == 3324) | (soccer.playerId == 20796) |
                (soccer.playerId == 56273) | (soccer.playerId == 512607)]
soccer = soccer[(soccer.minutesOnField >= 80)]
soccer = soccer.replace(3324, "A. Morata")
soccer = soccer.replace(20796, "M. Destro")
soccer = soccer.replace(56273, "P. Mortensen")
soccer = soccer.replace(512607, "J. Brumado")
# print(soccer)

# Statistik absolute Zahlen
statistik = soccer.groupby(["playerId"]).sum()
statistik = statistik.transpose()
# print(statistik)

# Offensivzweikampfquote -----------------------------------------------------------------------------------------------

# Offensivzweikämpfe je Spieler ermitteln
duels = soccer.groupby(["playerId"]).offensiveDuels_total.sum()
# print(duels)

# Gewonnene Offensivzweikämpfe je Spieler ermitteln
duels_won = soccer.groupby(["playerId"]).offensiveDuelsWon_total.sum()
# print(duels_won)

# Offensivzweikampfquote je Spieler ermitteln
duelswonpercent = round(duels_won / duels, 2)
# print(duelswonpercent)

# Balkenchart erstellen - Offensivzweikampfquote
duelswonpercent.plot.bar(figsize=(6, 3), color="grey")
plt.rcParams['font.size'] = '10'
plt.title("⌀ Offensivzweikampfquote je Stürmer", fontsize=12)
plt.xticks(rotation=360)
plt.xlabel("Stürmer")
plt.ylabel("⌀ Offensivzweikampfquote")
plt.tight_layout()
plt.savefig('Durchschnittliche Offensivzweikampfquote.png')
plt.show()

# Schlüsselpässe -------------------------------------------------------------------------------------------------------

# Schlüsselpässe je Spieler ermitteln
key_passes = soccer.groupby(["playerId"]).successfulKeyPasses_total.sum()
# print(key_passes)

# Spiele je Spieler ermitteln
matches = soccer.groupby(["playerId"]).matches.count()
# print(matches)

# Schlüsselpässe pro Spiel je Spieler ermitteln
key_passes = round(key_passes / matches, 2)
# print(key_passes)

# Balkenchart erstellen - Schlüsselpässe pro Spiel
key_passes.plot.bar(figsize=(6, 3), color="grey")
plt.rcParams['font.size'] = '10'
plt.title("⌀ Schlüsselpässe pro Spiel je Stürmer", fontsize=12)
plt.xticks(rotation=360)
plt.xlabel("Stürmer")
plt.ylabel("⌀ Schlüsselpässe pro Spiel")
plt.tight_layout()
plt.savefig('Durchschnittliche Schlüsselpässe pro Spiel.png')
plt.show()

# xA -------------------------------------------------------------------------------------------------------------------

# xA je Spieler ermitteln
xA = soccer.groupby(["playerId"]).xgAssist_total.sum()
# print(xA)

# xA pro Spiel je Spieler ermitteln
xa_match = round(xA / matches, 2)
# print(xa_match)

# Balkenchart erstellen - xA pro Spiel
xa_match.plot.bar(figsize=(6, 3), color="grey")
plt.rcParams['font.size'] = '10'
plt.title("⌀ xA pro Spiel je Stürmer", fontsize=12)
plt.xticks(rotation=360)
plt.xlabel("Stürmer")
plt.ylabel("⌀ xA pro Spiel")
plt.tight_layout()
plt.savefig('Durchschnittliche xA pro Spiel.png')
plt.show()

# Assists --------------------------------------------------------------------------------------------------------------

# Assists je Spieler ermitteln
assists = soccer.groupby(["playerId"]).assists_total.sum()
# print(assists)

# Assists pro Spiel je Spieler ermitteln
assists_match = round(assists / matches, 2)
# print(assists_match)

# Balkenchart erstellen - Assists pro Spiel
assists_match.plot.bar(figsize=(6, 3), color="grey")
plt.rcParams['font.size'] = '10'
plt.title("⌀ Assists pro Spiel je Stürmer", fontsize=12)
plt.xticks(rotation=360)
plt.xlabel("Stürmer")
plt.ylabel("⌀ Assists pro Spiel")
plt.tight_layout()
plt.savefig('Durchschnittliche Assists pro Spiel.png')
plt.show()

# Assists pro xA -------------------------------------------------------------------------------------------------------

# Assists pro xA je Spieler ermitteln
assists_xA = round(assists / xA, 2)
# print(assists_xA)

# Balkenchart erstellen - Assists pro xA
assists_xA.plot.bar(figsize=(6, 3), color="grey")
plt.rcParams['font.size'] = '10'
plt.title("⌀ Assists pro xA je Stürmer", fontsize=12)
plt.xticks(rotation=360)
plt.xlabel("Stürmer")
plt.ylabel("⌀ Assists pro xA")
plt.tight_layout()
plt.hlines(1, -1, 4, color="black")
plt.savefig('Durchschnittliche Assists pro xA.png')
plt.show()

# Torschüsse -----------------------------------------------------------------------------------------------------------

# Torschüsse je Spieler ermitteln
shotsontarget = soccer.groupby(["playerId"]).shotsOnTarget_total.sum()
# print(shotsontarget)

# Torschüsse pro Spiel je Spieler ermitteln
shotsontarget_match = round(shotsontarget / matches, 2)
# print(shotsontarget_match)

# Balkenchart erstellen - Torschüsse pro Spiel
shotsontarget_match.plot.bar(figsize=(6, 3), color="grey")
plt.rcParams['font.size'] = '10'
plt.title("⌀ Torschüsse pro Spiel je Stürmer", fontsize=12)
plt.xticks(rotation=360)
plt.xlabel("Stürmer")
plt.ylabel("⌀ Torschüsse pro Spiel")
plt.tight_layout()
plt.savefig('Durchschnittliche Torschüsse pro Spiel.png')
plt.show()

# xG -------------------------------------------------------------------------------------------------------------------

# xG je Spieler ermitteln
xG = soccer.groupby(["playerId"]).xgShot_total.sum()
# print(xG)

# xG pro Spiel je Spieler ermitteln
xg_match = round(xG / matches, 2)
# print(xg_match)

# Balkenchart erstellen - xG pro Spiel
xg_match.plot.bar(figsize=(6, 3), color="grey")
plt.rcParams['font.size'] = '10'
plt.title("⌀ xG pro Spiel je Stürmer", fontsize=12)
plt.xticks(rotation=360)
plt.xlabel("Stürmer")
plt.ylabel("⌀ xG pro Spiel")
plt.tight_layout()
plt.savefig('Durchschnittliche xG pro Spiel.png')
plt.show()

# Tore -----------------------------------------------------------------------------------------------------------------

# Tore je Spieler ermitteln
goals = soccer.groupby(["playerId"]).goals_total.sum()
# print(goals)

# Tore pro Spiel je Spieler ermitteln
goals_match = round(goals / matches, 2)
# print(goals_match)

# Balkenchart erstellen - Tore pro Spiel
goals_match.plot.bar(figsize=(6, 3), color="grey")
plt.rcParams['font.size'] = '10'
plt.title("⌀ Tore pro Spiel je Stürmer", fontsize=12)
plt.xticks(rotation=360)
plt.xlabel("Stürmer")
plt.ylabel("⌀ Tore pro Spiel")
plt.tight_layout()
plt.savefig('Durchschnittliche Tore pro Spiel.png')
plt.show()

# Tore pro xG ----------------------------------------------------------------------------------------------------------

# Tore pro xG je Spieler ermitteln
goals_xG = round(goals / xG, 2)
# print(goals_xG)

# Balkenchart erstellen - Tore pro xG
goals_xG.plot.bar(figsize=(6, 3), color="grey")
plt.rcParams['font.size'] = '10'
plt.title("⌀ Tore pro xG je Stürmer", fontsize=12)
plt.xticks(rotation=360)
plt.xlabel("Stürmer")
plt.ylabel("⌀ Tore pro xG")
plt.hlines(1, -1, 4, color="black")
plt.tight_layout()
plt.savefig('Durchschnittliche Tore pro xG.png')
plt.show()

# Tore pro Ballberührung im Strafraum ----------------------------------------------------------------------------------

# Ballberührungen im Strafraum je Spieler ermitteln
touches = soccer.groupby(["playerId"]).touchInBox_total.sum()
# print(touches)

# Tore pro Ballberührung im Strafraum je Spieler ermitteln
goals_touches = round(goals / touches, 2)
# print(goals_touches)

# Balkenchart erstellen - Tore pro Ballberührung im Strafraum
goals_touches.plot.bar(figsize=(6, 3), color="grey")
plt.rcParams['font.size'] = '10'
plt.title("⌀ Tore pro Ballberührung im Strafraum", fontsize=12)
plt.xticks(rotation=360)
plt.xlabel("Stürmer")
plt.ylabel("⌀ Tore pro Ballberührung")
plt.tight_layout()
plt.savefig('Durchschnittliche Tore pro Ballberührung im Strafraum.png')
plt.show()

# Tore pro Schuss ------------------------------------------------------------------------------------------------------

# Schüsse je Spieler ermitteln
shots = soccer.groupby(["playerId"]).shots_total.sum()
# print(shots)

# Tore pro Schuss je Spieler ermitteln
goals_shots = round(goals / shots, 2)
# print(goals_shots)

# Balkenchart erstellen - Tore pro Schuss
goals_shots.plot.bar(figsize=(6, 3), color="grey")
plt.rcParams['font.size'] = '10'
plt.title("⌀ Tore pro Schuss je Stürmer", fontsize=12)
plt.xticks(rotation=360)
plt.xlabel("Stürmer")
plt.ylabel("⌀ Tore pro Schuss")
plt.tight_layout()
plt.savefig('Durchschnittliche Tore pro Schuss.png')
plt.show()

# Gewichtungen festlegen -----------------------------------------------------------------------------------------------
g_duelswon = 1            # Offensivzweikampfquote
g_keypasses = 2           # Schlüsselpässe pro Spiel
g_xa = 2                  # Expected Assists pro Spiel
g_assists = 3             # Assists pro Spiel
g_shotsontarget = 1       # Torschüsse pro Spiel
g_xg = 2                  # Expected Goals pro Spiel
g_goals = 3               # Tore pro Spiel
g_goals_touches = 1       # Tore pro Ballberührung im Strafraum
g_goals_shots = 2         # Tore pro Schuss

# Parameter mit Gewichtungen multiplizieren ----------------------------------------------------------------------------
duelswonpercent = duelswonpercent * g_duelswon
key_passes = key_passes * g_keypasses
xa_match = xa_match * g_xa
assists_match = assists_match * g_assists
shotsontarget_match = shotsontarget_match * g_shotsontarget
xg_match = xg_match * g_xg
goals_match = goals_match * g_goals
goals_touches = goals_touches * g_goals_touches
goals_shots = goals_shots * g_goals_shots

# Gewichtete Parameterwerte je Spieler zusammenfügen
impact = pd.concat([duelswonpercent, key_passes, xa_match,
                    assists_match, shotsontarget_match, xg_match,
                    goals_match, goals_touches, goals_shots], axis=1)

# Summe hinzufügen
impact['Summe'] = round(impact.sum(axis=1), 2)

# Spalten benennen
spalten = impact.columns = ["Offensivzweikampfquote", "Schlüsselpässe pro Spiel", "xA pro Spiel",
                            "Assists pro Spiel", "Torschüsse pro Spiel", "xG pro Spiel", "Tore pro Spiel",
                            "Tore pro Ballberührung im Strafraum", "Tore pro Schuss", "Summe"]
# print(impact)

"""
# Tabelle erstellen
impact = impact.transpose()
fig, ax = plt.subplots()
table = ax.table(cellText=impact.values, colLabels=impact.columns, rowLabels=spalten, loc='center')
fig.patch.set_visible(False)
ax.axis('off')
fig.tight_layout()
plt.savefig('Impact.png')
plt.show()
"""

# gestapelter Balkenchart der Parameter
del impact['Summe']
impact.plot.bar(stacked=True, figsize=(7, 4))
plt.title("Performance pro Stürmer", fontsize=12)
plt.xticks(rotation=360)
plt.xlabel("Stürmer")
plt.ylabel("Performance")
plt.legend(bbox_to_anchor=(1, 1), fontsize=8, loc="upper left")
plt.show()
