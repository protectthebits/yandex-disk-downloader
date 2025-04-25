# 📥 Yandex Disk Downloader

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-ISC-green.svg)](LICENSE)

> A lightweight Python script to recursively download **public Yandex Disk folders** with multithreaded speed and a live progress bar!

---

## ✨ Features

- Download **entire folders** shared via public Yandex Disk links
- **Preserve folder structure** locally
- **Multithreaded downloads** for faster performance (default: 5 threads)
- **Progress bar** via `tqdm`
- **Prompt for input**: URL and destination directory at runtime
- Simple, clean, and easy to use

---

## 📋 Requirements

- Python **3.6 or newer**
- Python packages:
  - `requests`
  - `tqdm`

Install requirements using pip:

```bash
pip install requests tqdm
```

---

## 🚀 Usage

Run the script:

```bash
python3 yandex-disk-downloader.py
```

You will be prompted to enter:
- The Yandex Disk public URL
- The destination folder (press Enter to use the default ./yandex_download)

Example with a public Yandex Disk URL:
```bash
Enter the Yandex Disk public URL: https://disk.yandex.com/d/YOEhWFYUKNpezA
Enter the destination folder (default: ./yandex_download):
```

---

## 🛠️ How It Works

1. The script queries the Yandex Disk API for the file list
2. Recursively walks folders and files
3. Gets direct download links
4. Downloads files using multiple threads
5. Shows real-time progress

---