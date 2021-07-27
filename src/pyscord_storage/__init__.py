import json
import requests


def upload(filename, file):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # upload file from URL
    if file[:7] == "http://" or file[:8] == "https://":

        response = requests.post(
            "https://discord-storage.animemoe.us/upload-from-url/",
            headers=headers,
            data={"filename": filename, "url": file},
        )

        return {"status": response.status_code, "data": json.loads(response.text)}

    # upload from file
    else:

        response = requests.post(
            "https://discord-storage.animemoe.us/upload-from-file/",
            headers=headers,
            data={"filename": filename},
            files={"file": open(file, "rb")},
        )

        return {"status": response.status_code, "data": json.loads(response.text)}
