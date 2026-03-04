import argparse
import sys

from ._sync import upload_from_file, upload_from_url


def main():
    parser = argparse.ArgumentParser(prog="pyscord-storage", description="Upload files to Discord storage")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", metavar="PATH", help="Path to local file to upload")
    group.add_argument("--url", metavar="URL", help="Remote URL to upload")
    args = parser.parse_args()

    if args.file:
        result = upload_from_file(args.file)
    else:
        result = upload_from_url(args.url)

    data = result.get("data")
    status = result.get("status")

    if status == 200 and isinstance(data, dict) and "x_url" in data:
        print(data["x_url"])
    else:
        if isinstance(data, dict):
            print(data.get("message") or data.get("error") or str(data), file=sys.stderr)
        else:
            print(str(data), file=sys.stderr)
        sys.exit(1)
