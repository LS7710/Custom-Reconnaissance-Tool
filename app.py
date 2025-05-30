import requests
from bs4 import BeautifulSoup
import re
import socket
import subprocess

def ping_site(domain):
    print(f"Pinging {domain}...")
    response = subprocess.run(['ping', '-c', '4', domain], capture_output=True, text=True)
    print(response.stdout)

def get_server_info(url):
    print("\n[+] Server Info:")
    try:
        headers = requests.get(url).headers
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

def find_hidden_pages(url, wordlist):
    print("\n[+] Brute Forcing Hidden Pages...")
    for word in open(wordlist, 'r'):
        word = word.strip()
        full_url = f"{url}/{word}"
        r = requests.get(full_url)
        if r.status_code == 200:
            print(f"Found: {full_url}")

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

# You can call all of them here in main
if __name__ == "__main__":
    target = "http://example.com"
    ping_site(target.replace("http://", "").replace("https://", ""))
    get_server_info(target)
    get_robots_txt(target)
    find_hidden_pages(target, 'common.txt')  # Use a small wordlist for testing
    find_forms(target)