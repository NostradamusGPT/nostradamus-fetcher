import requests

def fetch_data():
    # Beispielhafte Daten, später durch echte ersetzt
    data = {
        "source": "nostradamus-fetcher",
        "content": "Prophezeiung wurde geladen"
    }

    # Deine API-URL → anpassen wenn nötig
    url = "https://nostradamus-api.onrender.com/import"

    try:
        response = requests.post(url, json=data)
        print("Status:", response.status_code)
        print("Antwort:", response.text)
    except Exception as e:
        print("Fehler:", e)

if __name__ == "__main__":
    fetch_data()
