import requests
import json

def send_to_radarr(filepath):
    with open("config.json") as f:
        cfg = json.load(f)

    api = cfg["radarr_api"]
    url = cfg["radarr_url"]

    payload = {
        "title": filepath,
        "path": filepath
    }

    r = requests.post(f"{url}/api/v3/manualimport?apikey={api}", json=payload)

    return r.text
