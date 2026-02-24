import requests
from datetime import datetime

URL = "https://lamonede.onrender.com/"

def ping():
    try:
        response = requests.get(URL, timeout=15)
        print(f"{datetime.now()} ✅ Status: {response.status_code}")
    except Exception as e:
        print(f"{datetime.now()} ❌ Erro: {e}")

if __name__ == "__main__":
    ping()