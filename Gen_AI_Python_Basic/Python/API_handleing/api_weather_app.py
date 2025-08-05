import json
import requests

url = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m'
# Works out site of Amdocs Network
try:
    response = requests.get(url, timeout=5)
    data = response.json()
    print(json.dumps(data, indent=4))
except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
