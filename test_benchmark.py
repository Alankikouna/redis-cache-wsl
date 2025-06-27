import requests
import time

url = "http://localhost:5000/data/test-key"

print("⌛ Requête #1 (attendue lente, simulation backend)...")
start = time.time()
r1 = requests.get(url)
print("Statut HTTP:", r1.status_code)
print("Contenu brut:", r1.text)  # Ajouté pour debug
try:
    print("Réponse JSON:", r1.json())
except Exception as e:
    print("Erreur JSON:", e)
print("Durée :", round(time.time() - start, 2), "secondes\n")

print("⚡ Requête #2 (attendue rapide, via cache)...")
start = time.time()
r2 = requests.get(url)
print("Statut HTTP:", r2.status_code)
print("Contenu brut:", r2.text)  # Ajouté pour debug
try:
    print("Réponse JSON:", r2.json())
except Exception as e:
    print("Erreur JSON:", e)
print("Durée :", round(time.time() - start, 2), "secondes")