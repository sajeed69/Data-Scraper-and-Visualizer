# scraper.py

import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

def scrape_wikipedia(keyword):
    url = f"https://en.wikipedia.org/wiki/{keyword.replace(' ', '_')}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    return ' '.join([p.text for p in paragraphs[:5]])

def scrape_dynamic_site(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        content = page.content()
        browser.close()
    return content
