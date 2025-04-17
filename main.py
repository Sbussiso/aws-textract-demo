#!/usr/bin/env python3
import os
import sys
import logging
import requests
import boto3
from dotenv import load_dotenv

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        handlers=[logging.StreamHandler()],
    )

def load_aws_credentials():
    load_dotenv()  # loads variables from .env
    aws_key = os.getenv("AWS_ACCESS_KEY")
    aws_secret = os.getenv("AWS_SECRET_KEY")
    region = os.getenv("AWS_REGION")

    if not aws_key or not aws_secret or not region:
        logging.error("Missing AWS credentials or region in environment.")
        sys.exit(1)
    return aws_key, aws_secret, region

def download_image(url):
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        return resp.content
    except requests.RequestException as e:
        logging.error(f"Failed to download image: {e}")
        sys.exit(1)

def extract_text_from_bytes(image_bytes, textract_client):
    # Call Textract to detect text
    response = textract_client.detect_document_text(
        Document={"Bytes": image_bytes}
    )
    # Collect all TEXT from LINE blocks
    lines = [
        block["Text"]
        for block in response.get("Blocks", [])
        if block["BlockType"] == "LINE"
    ]
    return lines

def main():
    setup_logging()

    # Get image URL from user input
    image_url = input("Please enter the publicly accessible URL of the image: ")
    if not image_url:
        logging.error("No image URL provided.")
        sys.exit(1)

    aws_key, aws_secret, region = load_aws_credentials()

    # Initialize Textract client
    textract = boto3.client(
        "textract",
        aws_access_key_id=aws_key,
        aws_secret_access_key=aws_secret,
        region_name=region,
    )

    logging.info("Downloading image...")
    img_bytes = download_image(image_url)

    logging.info("Calling AWS Textract...")
    lines = extract_text_from_bytes(img_bytes, textract)

    if not lines:
        logging.info("No text detected.")
        return

    logging.info("Extracted text:")
    for idx, line in enumerate(lines, 1):
        print(f"{idx:3d}: {line}")

if __name__ == "__main__":
    main()
