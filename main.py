# Het toevoegen van de juiste libraries
import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_id = os.getenv("api_id_nutritionix")
api_key = os.getenv("api_key_nutritionix")

# App word opgebouwd in verschillende handige functies

# functie 1 Maaltijd of ingredient opzoeken
# Gebruiker typt in bijvoorbeeld kipfilet of banaan
# Gebruiker krijgt voedingswaarden terug per 100g opgedeeld in KCAL, EIWITTEN, VETTEN EN KOOLHYDRATEN

# functie 2 dagelijkse totaalwaarden berekenen
# Voeg meerdere maaltijden toe en houd dagtotaal bij
# Wederom opgedeeld in KCAL, EIWITTEN, VETTEN EN KOOLHYDRATEN

# functie 3 Opslaan van dagelijkse voeding in een lokaal bestaand
# bijhouden wat je vandaag en op eerdere dagen heb gegeten

# functie 4 persoonlijke macrodoelen instellen
# De app vergelijkt je huidige dagtotaal en berekend hoeveel je nog moet eten

# Daarnaast moet er ook een command line menu komen om de functies aan te roepen en terug te keren naar het menu!

# Wellicht leuke functionaliteit bij het opstarten van de app een 