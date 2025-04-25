# 📥 Yandex Disk Public Folder Downloader

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
