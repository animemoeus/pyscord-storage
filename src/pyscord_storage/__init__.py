import json
import requests


def upload(filename, url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    }
    response = requests.post(
        "https://api.animemoe.us/discord-storage/",
        headers=headers,
        data={"filename": filename, "url": url},
    )

    return {"status": response.status_code, "data": json.loads(response.text)}
