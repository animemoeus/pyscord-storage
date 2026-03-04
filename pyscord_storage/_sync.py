import httpx

API_URL = "https://discord-storage-serverless.animemoe.us/"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
HEADERS = {"User-Agent": USER_AGENT}


def upload_from_file(file: str) -> dict:
    with open(file, "rb") as f:
        response = httpx.post(API_URL, headers=HEADERS, files={"file": f}, follow_redirects=True)
    return {"status": response.status_code, "data": response.json()}


def upload_from_url(url: str) -> dict:
    response = httpx.post(API_URL, headers=HEADERS, files={"url": (None, url)}, follow_redirects=True)
    return {"status": response.status_code, "data": response.json()}
