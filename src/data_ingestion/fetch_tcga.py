# fetch_tcga.py
from gdc_client.download import download_files
import os

# You must install the GDC Data Transfer Tool CLI and obtain a manifest.json
# CLI: https://gdc.cancer.gov/access-data/gdc-data-transfer-tool

def download_tcga_data(manifest_path: str, output_dir: str = "../../data/tcga"):
    os.makedirs(output_dir, exist_ok=True)
    os.system(f"gdc-client download -m {manifest_path} -d {output_dir}")

if __name__ == "__main__":
    print("Requires GDC Data Transfer Tool and a valid 'manifest.json' file.")
    print("Visit https://portal.gdc.cancer.gov to generate your manifest.")

