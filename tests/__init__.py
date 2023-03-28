import unittest

import pyscord_storage


class TestRequests(unittest.TestCase):
    def test_upload_from_file(self):
        response = pyscord_storage.upload_from_file("tests/temp/takagi.png")
        self.assertEqual(response.get("status"), 200)

    def test_upload_from_url(self):
        response = pyscord_storage.upload_from_url(
            "takagi.png",
            "https://cdn.discordapp.com/attachments/858938620425404426/1090196061177524234/takagi.png",
        )
        self.assertEqual(response.get("status"), 200)


if __name__ == "__main__":
    unittest.main()
