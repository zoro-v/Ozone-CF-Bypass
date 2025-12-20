# Ozone CF-Bypass Tool 🛡️

![Ozone](https://img.shields.io/badge/Tool-Ozone-cyan?style=for-the-badge&logo=appveyor) ![Python](https://img.shields.io/badge/Python-3.8%2B-yellow?style=for-the-badge&logo=python)

**Ozone CF-Bypass** is a powerful reconnaissance tool designed to bypass Cloudflare's IUAM (I'm Under Attack Mode) and perform HTTP method testing using a real browser engine.

It automates the process of solving Cloudflare challenges via **Playwright**, captures the valid session cookies, and uses them to test server responses for various HTTP methods (GET, POST, PUT, OPTIONS).

---

## ⚡ Features

* **Bypass Protection:** Automatically solves Cloudflare JS challenges.
* **Cookie Hijacking:** Captures session cookies for authenticated requests.
* **Multi-Target Support:** Scan a single URL (`-u`) or a list of targets (`-l`).
* **Method Fuzzing:** Checks response codes for GET, POST, PUT, and OPTIONS.
* **Stealth Mode:** Rotates User-Agents to avoid detection.
* **Ozone Quality:** Clean, fast, and effective.

---

## 📦 Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/zoro-v/Ozone-CF-Bypass.git](https://github.com/zoro-v/Ozone-CF-Bypass.git)
    cd Ozone-CF-Bypass
    ```

2.  **Install dependencies:**
    ```bash
    pip install playwright requests
    ```

3.  **Install Browser Binaries:**
    ```bash
    playwright install chromium
    ```

---

## 🚀 Usage

### 1. Scan a Single Target
Use the `-u` flag to specify a single URL:
```bash
python3 cf_bypass.py -u [https://example.com](https://example.com)
