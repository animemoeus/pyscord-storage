import httpx

API_URL = "https://discord-storage-serverless.animemoe.us/"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
HEADERS = {"User-Agent": USER_AGENT}


def _parse_response(response) -> dict:
    try:
        data = response.json()
    except Exception:
        data = response.text
    return {"status": response.status_code, "data": data}


async def async_upload_from_file(file: str) -> dict:
    async with httpx.AsyncClient() as client:
        with open(file, "rb") as f:
            response = await client.post(API_URL, headers=HEADERS, files={"file": f}, follow_redirects=True)
    return _parse_response(response)


async def async_upload_from_url(url: str) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.post(API_URL, headers=HEADERS, files={"url": (None, url)}, follow_redirects=True)
    return _parse_response(response)
