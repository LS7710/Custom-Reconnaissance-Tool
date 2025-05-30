

   ▄████████ ███▄▄▄▄      ▄████████    ▄█   ▄█▄    ▄████████ 
  ███    ███ ███▀▀▀██▄   ███    ███   ███ ▄███▀   ███    ███ 
  ███    █▀  ███   ███   ███    ███   ███▐██▀     ███    █▀  
  ███        ███   ███   ███    ███  ▄█████▀     ▄███▄▄▄     
▀███████████ ███   ███ ▀███████████ ▀▀█████▄    ▀▀███▀▀▀     
         ███ ███   ███   ███    ███   ███▐██▄     ███    █▄  
   ▄█    ███ ███   ███   ███    ███   ███ ▀███▄   ███    ███ 
 ▄████████▀   ▀█   █▀    ███    █▀    ███   ▀█▀   ██████████ 
                                      ▀                      


# Custom Reconnaissance Tool

This is a quick and simple, single-command reconissance tool meant to be used through the CLI to quickly gather a handful of commonly used information from a website by pentesters and security analysts

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
```
### 2. Create a virtual enviornment (Optional but recommended)
*This step is recommended if you plan to use this on a Mac or a linux distro that uses a system-managed Python installation protected by PEP668, preventing you from installing the packages needed to make this run (requests beautifulsoup4)*

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install required libraries
```bash
pip install requests beautifulsoup4
```

## How to use

### Option 1: Run  with a URL argument
```bash
python recon_tool.py http://example.com
```
### Option 2: Let it prompt you
```bash
python recon_tool.py
# Then type the full URL when asked
```
## Wordlist for hidden pages

The tool uses a default file called common.txt to guess hidden pages.

You can:

•	Download one from SecLists

•	Or make your own like this:
```
admin
login
test
backup
uploads
```

## Ethical Reminder
It goes without saying if you plan to use this, use it responisbly and not for anything illegal
