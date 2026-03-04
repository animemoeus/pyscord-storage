import pyscord_storage


def test_upload_from_file():
    response = pyscord_storage.upload_from_file("tests/temp/takagi.png")
    assert response.get("status") == 200


def test_upload_from_url():
    response = pyscord_storage.upload_from_url(
        "https://raw.githubusercontent.com/animemoeus/pyscord-storage/master/tests/temp/takagi.png",
    )
    assert response.get("status") == 200


async def test_async_upload_from_file():
    response = await pyscord_storage.async_upload_from_file("tests/temp/takagi.png")
    assert response.get("status") == 200


async def test_async_upload_from_url():
    response = await pyscord_storage.async_upload_from_url(
        "https://raw.githubusercontent.com/animemoeus/pyscord-storage/master/tests/temp/takagi.png",
    )
    assert response.get("status") == 200
