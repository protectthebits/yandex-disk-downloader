# -*- coding: utf-8 -*-
import requests
import os
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

# API base URL
API_BASE = "https://cloud-api.yandex.net/v1/disk/public/resources"


def list_files(public_key, path=""):
    """Recursively list all files in a public Yandex.Disk folder."""
    files = []
    params = {"public_key": public_key, "path": path}
    response = requests.get(API_BASE, params=params)
    response.raise_for_status()
    data = response.json()

    if "_embedded" in data:
        for item in data["_embedded"]["items"]:
            if item["type"] == "dir":
                files += list_files(public_key, item["path"])
            else:
                files.append(item)
    else:
        files.append(data)
    return files


def get_download_link(file_path, public_key):
    """Get direct download URL for a file."""
    params = {"public_key": public_key, "path": file_path}
    response = requests.get(API_BASE + "/download", params=params)
    response.raise_for_status()
    return response.json()["href"]


def download_file(file_info, public_key, base_dir, progress=None):
    """Download a single file and update progress bar."""
    file_path = file_info["path"]
    relative_path = file_path.lstrip("/")  # Ensure relative path
    local_path = os.path.join(base_dir, relative_path.replace(":", "_"))

    try:
        os.makedirs(os.path.dirname(local_path), exist_ok=True)

        print("Getting download URL for: {}".format(file_path))
        url = get_download_link(file_path, public_key)
        print("Download URL: {}".format(url))

        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(local_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

        print("Downloaded: {}".format(local_path))

        if progress:
            progress.update(1)

    except Exception as e:
        print("Error downloading {}: {}".format(file_path, e))


def main():
    # Prompt for Yandex URL
    public_url = input("Enter the Yandex Disk public URL: ").strip()
    if not public_url:
        print("Error: URL is required.")
        return
    resource_key = public_url

    # Prompt for destination folder
    destination_dir = input("Enter the destination folder (default: ./yandex_download): ").strip()
    if not destination_dir:
        destination_dir = "./yandex_download"

    # Create destination if it doesn't exist
    os.makedirs(destination_dir, exist_ok=True)

    print("Listing files...")
    all_files = list_files(resource_key)
    print("Found {} file(s)".format(len(all_files)))

    with tqdm(total=len(all_files), desc="Downloading", unit="file") as progress:
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = [
                executor.submit(download_file, file, resource_key, destination_dir, progress)
                for file in all_files
            ]
            for _ in as_completed(futures):
                pass


if __name__ == "__main__":
    main()
