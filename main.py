# Het toevoegen van de juiste libraries
import requests
import os
from dotenv import load_dotenv

print("Current directory:", os.getcwd())


load_dotenv(dotenv_path=".env")
api_id = os.getenv("api_id_nutri")
api_key = os.getenv("api_key_nutri")

# App word opgebouwd in verschillende handige functies

# functie 1 Maaltijd of ingredient opzoeken
# Gebruiker typt in bijvoorbeeld kipfilet of banaan
# Gebruiker krijgt voedingswaarden terug per 100g opgedeeld in KCAL, EIWITTEN, VETTEN EN KOOLHYDRATEN

# def zoekfunctie(zoekterm, hoeveelheid = 100):
print("App ID:", api_id)
print("App Key:", api_key)

url = "https://trackapi.nutritionix.com/v2/natural/nutrients"

headers = {
    "x-app-id": api_id,
    "x-app-key": api_key,
    "Content-Type": "application/json"
}

data = {"query": "2 eggs and a slice of bacon"}
response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print("data", response.json())
else:
    print("data not found")
    print("status code: ", response.status_code)

# functie 2 dagelijkse totaalwaarden berekenen
# Voeg meerdere maaltijden toe en houd dagtotaal bij
# Wederom opgedeeld in KCAL, EIWITTEN, VETTEN EN KOOLHYDRATEN

# functie 3 Opslaan van dagelijkse voeding in een lokaal bestaand
# bijhouden wat je vandaag en op eerdere dagen heb gegeten

# functie 4 persoonlijke macrodoelen instellen
# De app vergelijkt je huidige dagtotaal en berekend hoeveel je nog moet eten

# Daarnaast moet er ook een command line menu komen om de functies aan te roepen en terug te keren naar het menu!

# Wellicht leuke functionaliteit bij het opstarten van de app een 