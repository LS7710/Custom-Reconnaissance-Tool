# Custom Reconnaissance Tool

Welcome to your lightweight Python-based recon tool for ethical hacking and cybersecurity research!

This script is a one-stop command-line utility for quickly gathering key information about a website. It automates multiple passive and active information-gathering techniques to save you time and clicks.

---

## 💻 What It Does

With a single URL input, the tool performs the following checks:

- **Ping Check** — Check if the Domain is up and running
- **Server Headers** — Detects what server the site is running on
- **robots.txt Check** — Reads disallowed paths for possible information gathering
- **Hidden Page Brute Force** — Finds pages like `/admin`, `/backup`, etc.
- **Form Scanner** — Lists all `<form>` actions and methods (XSS, SQLi target indicators)
- **IDOR Fuzzer** — Searches common parameter names for possible insecure object access
- **Sensitive File Scanner** — Tries to find unsecured files `.env`, `.git/`, `backup.zip`

---

## Setup

### 1. Clone the repo or copy the script
```bash
git clone <your-repo-url>
cd Custom-Reconnaissance-Tool

