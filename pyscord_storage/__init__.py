import json

import requests

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"


def upload_from_file(file):
    api_url = "https://discord-storage.animemoe.us/api/upload-from-file/"
    headers = {
        "User-Agent": USER_AGENT,
    }

    with open(file, "rb") as f:
        response = requests.request("POST", api_url, headers=headers, files={"file": f})
    return {"status": response.status_code, "data": response.json()}


def upload_from_url(filename, file_url):
    api_url = "https://discord-storage.animemoe.us/api/upload-from-url/"
    headers = {
        "User-Agent": USER_AGENT,
        "Content-Type": "application/json",
    }
    payload = json.dumps(
        {"filename": filename, "url": file_url},
    )

    response = requests.request("POST", api_url, headers=headers, data=payload)
    return {"status": response.status_code, "data": response.json()}
