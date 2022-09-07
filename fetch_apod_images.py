import argparse
import requests


def get_apod_links(count):
    urls = []
    url = "https://api.nasa.gov/planetary/apod"
    payload = {
        "api_key":  "sKrvKPzb8Jma4bOxmW00Q679IyIEGg7CvcRq9YRU",
        "count": count
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for resp in response.json():
        urls.append(resp.get("url"))
    return urls


def fetch_apod():
    for url in get_apod_links(30):
        get_picture(url, 'images')