# fetch_cosmic.py
import os
import requests

COSMIC_URL = "https://cancer.sanger.ac.uk/cosmic/download"
OUTPUT_DIR = "../../data/cosmic"

def download_cosmic_data():
    print("NOTE: COSMIC requires registration and license acceptance.")
    print("Please manually download files from:", COSMIC_URL)
    print("Place them into:", OUTPUT_DIR)

if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    download_cosmic_data()

