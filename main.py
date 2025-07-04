import json
import requests

r = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/USD/")

data = json.loads(r.content)
kurs = float(data[0]['Rate'])

amount = float(input("So'm kiriting: "))
print(round(amount / kurs, 2))
