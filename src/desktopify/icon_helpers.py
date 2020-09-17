import os
import requests

from pathlib import Path


def download_icon_if_not_exist(url: str, file_path: str) -> None:
    Path(Path(file_path).parent).mkdir(parents=True, exist_ok=True)

    if os.path.exists(file_path):
        return

    req = requests.get(url, allow_redirects=True)
    with open(file_path, "wb") as f:
        f.write(req.content)
