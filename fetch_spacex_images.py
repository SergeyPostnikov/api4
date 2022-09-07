import argparse
import requests


def get_epic_links():
    links = []
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    payload = {
        "api_key": "sKrvKPzb8Jma4bOxmW00Q679IyIEGg7CvcRq9YRU",
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for resp in response.json():
        date = get_date(resp.get("date"))
        filename = f'{resp.get("image")}.png'
        links.append(f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{filename}')
    return links


def fetch_epic():
    for url in get_epic_links():
        get_picture(url, 'images', '5U95NTyAukMS2pxYjtFU4ljejg5MX1IT4c9uB2Wu')