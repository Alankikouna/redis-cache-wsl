import requests
import time

url = "http://localhost:5000/data/test-key"

print("⌛ Requête #1 (attendue lente, simulation backend)...")
start = time.time()
r1 = requests.get(url)
print("Réponse:", r1.json())
print("Durée :", round(time.time() - start, 2), "secondes\n")

print("⚡ Requête #2 (attendue rapide, via cache)...")
start = time.time()
r2 = requests.get(url)
print("Réponse:", r2.json())
print("Durée :", round(time.time() - start, 2), "secondes")
