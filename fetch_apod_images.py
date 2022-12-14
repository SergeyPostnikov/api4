import argparse
import requests
import os

from picture_handlers import save_picture
from dotenv import load_dotenv


def get_apod_links(auth_token, count):
    urls = []
    url = "https://api.nasa.gov/planetary/apod"
    payload = {
        "api_key":  auth_token,
        "count": count
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for resp in response.json():
        url = resp.get("url") if resp.get('media_type') == 'image' else None
        if url is not None:
            urls.append(url)
    return urls


def fetch_apod(auth_token, count):
    for url in get_apod_links(auth_token, count):
        save_picture(url, 'images')


if __name__ == '__main__':  
    load_dotenv()
    auth_token = os.environ['NASA_API_KEY']

    parser = argparse.ArgumentParser()
    parser.add_argument('--count', help='number of links', default=3)
    args = parser.parse_args()
    fetch_apod(auth_token, args.count)
