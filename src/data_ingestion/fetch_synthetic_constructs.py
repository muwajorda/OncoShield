# fetch_synthetic_constructs.py
import requests
from bs4 import BeautifulSoup
import os

IGEM_URL = "https://parts.igem.org/Special:Search?search=cancer"

def fetch_igem_constructs():
    print("This script fetches basic info. Deep download requires scraping permissions.")
    response = requests.get(IGEM_URL)
    soup = BeautifulSoup(response.content, "html.parser")
    
    parts = []
    for link in soup.find_all("a"):
        href = link.get("href")
        if href and "/Part:" in href:
            parts.append(f"https://parts.igem.org{href}")

    with open("../../data/synthetic_constructs/igem_links.txt", "w") as f:
        for part in sorted(set(parts)):
            f.write(part + "\n")

    print(f"Found {len(parts)} construct links. Saved to igem_links.txt.")

if __name__ == "__main__":
    os.makedirs("../../data/synthetic_constructs", exist_ok=True)
    fetch_igem_constructs()

