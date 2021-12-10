import json
import requests


def upload(filename, file, custom_headers={}):
    default_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "pyscord-storage 0.1.0",
    }

    # upload file from URL
    if file[:7] == "http://" or file[:8] == "https://":

        response = requests.post(
            "https://discord-storage.animemoe.us/upload-from-url/",
            headers=default_headers if custom_headers == {} else custom_headers,
            data={"filename": filename, "url": file},
        )

        return {"status": response.status_code, "data": json.loads(response.text)}

    else:
        # upload from file
        response = requests.post(
            "https://discord-storage.animemoe.us/upload-from-file/",
            headers=default_headers,
            data={"filename": filename},
            files={"file": open(file, "rb")},
        )

        return {"status": response.status_code, "data": json.loads(response.text)}
