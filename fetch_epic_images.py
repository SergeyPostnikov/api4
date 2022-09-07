import argparse
import requests


def get_spacex_links():
    url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    response = requests.get(url)
    response.raise_for_status()
    return response.json().get('links').get('flickr').get('original')


def fetch_spacex_last_launch():
    for url in get_spacex_links():
        get_picture(url, 'images')

