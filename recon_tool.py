import requests
from bs4 import BeautifulSoup
import platform
import subprocess
import sys

def print_banner():
    banner = r"""

   ▄████████ ███▄▄▄▄      ▄████████    ▄█   ▄█▄    ▄████████ 
  ███    ███ ███▀▀▀██▄   ███    ███   ███ ▄███▀   ███    ███ 
  ███    █▀  ███   ███   ███    ███   ███▐██▀     ███    █▀  
  ███        ███   ███   ███    ███  ▄█████▀     ▄███▄▄▄     
▀███████████ ███   ███ ▀███████████ ▀▀█████▄    ▀▀███▀▀▀     
         ███ ███   ███   ███    ███   ███▐██▄     ███    █▄  
   ▄█    ███ ███   ███   ███    ███   ███ ▀███▄   ███    ███ 
 ▄████████▀   ▀█   █▀    ███    █▀    ███   ▀█▀   ██████████ 
                                      ▀                      
    """
    print(banner)

def ping_site(domain):
    print(f"[+] Pinging {domain}...")
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    try:
        response = subprocess.run(['ping', param, '4', domain], capture_output=True, text=True)
        print(response.stdout)
    except FileNotFoundError:
        print("Ping command not found on this system.")

def get_server_info(url):
    print("\n[+] Server Info:")
    try:
        headers = requests.get(url, timeout=5).headers
        print(headers.get('Server', 'Server header not found'))
    except Exception as e:
        print(f"Error: {e}")

def get_robots_txt(url):
    print("\n[+] robots.txt:")
    try:
        r = requests.get(url + '/robots.txt')
        if r.status_code == 200:
            print(r.text)
        else:
            print("robots.txt not found.")
    except:
        print("Could not retrieve robots.txt")

def find_hidden_pages(url, wordlist_path='common.txt'):
    print("\n[+] Brute Forcing Hidden Pages...")
    try:
        with open(wordlist_path, 'r') as wordlist:
            for word in wordlist:
                word = word.strip()
                full_url = f"{url.rstrip('/')}/{word}"
                r = requests.get(full_url)
                if r.status_code == 200:
                    print(f"[+] Found: {full_url}")
    except FileNotFoundError:
        print(f"Wordlist file '{wordlist_path}' not found.")
    except Exception as e:
        print(f"Error during hidden page scan: {e}")

def find_forms(url):
    print("\n[+] Scanning for forms (possible injection points)...")
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        forms = soup.find_all('form')
        print(f"Found {len(forms)} form(s).")
        for form in forms:
            print(f"Form action: {form.get('action')}, method: {form.get('method')}")
    except Exception as e:
        print(f"Error: {e}")

def check_for_idor(url):
    print("\n[+] Checking for Possible IDOR Issues...")
    idor_payloads = ['1', '2', '3', '4', '999']
    param_keywords = ['id', 'user', 'profile', 'account', 'doc']
    for param in param_keywords:
        for value in idor_payloads:
            test_url = f"{url}?{param}={value}"
            try:
                r = requests.get(test_url)
                print(f"Tested: {test_url} - Status: {r.status_code}, Length: {len(r.text)}")
            except:
                pass

def check_unsecured_files(url):
    print("\n[+] Checking for Unsecured or Sensitive Files...")
    paths = ['.git/', '.env', '.htaccess', 'backup.zip', 'db.sql', 'config.json', 'error.log']
    for path in paths:
        try:
            r = requests.get(f"{url.rstrip('/')}/{path}", timeout=3)
            if r.status_code == 200:
                print(f"[!] Found accessible: {url}/{path}")
            elif r.status_code == 403:
                print(f"[!] Forbidden but exists (403): {url}/{path}")
        except:
            pass

def run_recon(target):
    print_banner()
    domain = target.replace("http://", "").replace("https://", "").split('/')[0]
    ping_site(domain)
    get_server_info(target)
    get_robots_txt(target)
    find_hidden_pages(target)
    find_forms(target)
    check_for_idor(target)
    check_unsecured_files(target)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target_url = sys.argv[1]
    else:
        target_url = input("Enter the target URL (e.g., http://example.com): ").strip()

    if not target_url.startswith("http"):
        target_url = "http://" + target_url

    run_recon(target_url)