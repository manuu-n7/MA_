"""
Mit dieser Datei können die Daten aus der API von Wyscout heruntergeladen werden!
"""

# Import
import requests

# Referenzen
username = " "
password = " "
url = " "
payload = {}
headers = {'Authorization': ' '}

# Abfrage
response = requests.request("GET", url, headers=headers, data=payload)
response_text = response.text
print(response_text)

# Abfrage speichern
with open('Atalanta_PlayerStats.json', 'w') as f:
    f.write(response_text)
