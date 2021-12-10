import json
import requests


def upload(filename="", file="", custom_headers={}):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "pyscord-storage 0.1.3",
    }

    # upload file from URL
    if file[:7] == "http://" or file[:8] == "https://":

        url = "https://discord-storage.animemoe.us/upload-from-url/"

        payload = {
            "filename": filename,
            "url": file,
        }

        response = requests.request(
            "POST",
            url,
            headers=headers if custom_headers == {} else custom_headers,
            data=payload,
        )

        return {"status": response.status_code, "data": json.loads(response.text)}

    else:
        # upload from file
        response = requests.post(
            "https://discord-storage.animemoe.us/upload-from-file/",
            headers=headers,
            data={"filename": filename},
            files={"file": open(file, "rb")},
        )

        return {"status": response.status_code, "data": json.loads(response.text)}
