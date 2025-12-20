 import asyncio
import requests
import time
import random
import argparse
import sys
from playwright.async_api import async_playwright

# ألوان الطباعة
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def print_banner():
    banner = f"""{Colors.CYAN}
      ___  ____  ___  _  _  ____ 
     / _ \(_  _)/ _ \( \( )(  __)
    ( (_) )/ _/( (_) ))  (  ) _) 
     \___/(____)\___/(_)\_)(____)
           {Colors.RED}v1.0 - By Ozone{Colors.RESET}
    """
    print(banner)

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
]

methods = ["GET", "POST", "PUT", "OPTIONS"]

async def get_cf_cookies(url):
    print(f"{Colors.YELLOW}[*] Launching Browser for: {url}{Colors.RESET}")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        try:
            print(f"[*] Opening page...")
            await page.goto(url, timeout=60000)

            try:
                await page.wait_for_selector("body", timeout=15000)
            except:
                print(f"{Colors.RED}[!] Body not loaded, grabbing cookies anyway...{Colors.RESET}")

            cookies = await context.cookies()
            cf_cookies = {c['name']: c['value'] for c in cookies}
            
            await browser.close()
            return cf_cookies
        except Exception as e:
            print(f"{Colors.RED}[!] Browser Error: {e}{Colors.RESET}")
            await browser.close()
            return {}

def fetch_with_requests(url, cookies):
    if not cookies:
        print(f"{Colors.RED}[!] No cookies captured. Skipping.{Colors.RESET}")
        return

    print(f"\n{Colors.GREEN}[+] Cookies Captured! Starting Scan...{Colors.RESET}")
    
    for method in methods:
        ua = random.choice(user_agents)
        headers = { "User-Agent": ua, "Referer": "https://www.google.com/" }
        try:
            print(f"[*] Testing {Colors.BOLD}{method}{Colors.RESET}...")
            res = requests.request(method, url, headers=headers, cookies=cookies, timeout=15, allow_redirects=False)

            print("-" * 60)
            print(f"Method: {Colors.GREEN}{method}{Colors.RESET} | Status: {res.status_code}")
            print(f"Size: {len(res.content)} bytes")
            print("-" * 60)
            time.sleep(2)
        except Exception as e:
            print(f"{Colors.RED}[!] Error in {method}: {e}{Colors.RESET}")

def run_scan(target):
    if not target.startswith("http"):
        target = "https://" + target
        
    print(f"\n{Colors.BOLD}Targeting: {target}{Colors.RESET}")
    cookies = asyncio.run(get_cf_cookies(target))
    fetch_with_requests(target, cookies)

if __name__ == "__main__":
    print_banner()
    parser = argparse.ArgumentParser(description="Ozone Cloudflare Bypass Tool")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-u', '--url', help="Target URL")
    group.add_argument('-l', '--list', help="Path to list of URLs")

    args = parser.parse_args()

    if args.url:
        run_scan(args.url)
    elif args.list:
        try:
            with open(args.list, 'r') as f:
                urls = [line.strip() for line in f if line.strip()]
            print(f"{Colors.GREEN}[*] Loaded {len(urls)} targets.{Colors.RESET}")
            for url in urls:
                run_scan(url)
        except FileNotFoundError:
            print(f"{Colors.RED}[!] File not found: {args.list}{Colors.RESET}")
