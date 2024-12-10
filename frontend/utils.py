
import requests

BASE_URL = "http://127.0.0.1:5000"

def obtener_datos(endpoint):
    try:
        response = requests.get(f"{BASE_URL}{endpoint}")
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print("Error al obtener datos:", e)
        return []