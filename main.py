import requests
import os
from os.path import splitext
from urllib.parse import urlparse, unquote


def get_filename(url):
    return unquote(urlparse(url).path.split('/')[-1])


def get_ext(url):
    return splitext(get_filename(url))[1]


def get_picture(url, directory):
    response = requests.get(url)
    response.raise_for_status()

    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(f'images/{get_filename()}', 'wb') as file:
        file.write(response.content)


def get_spacex_links():
    url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    response = requests.get(url)
    response.raise_for_status()
    return response.json().get('links').get('flickr').get('original')


def get_apod_links(count):
    urls = []
    url = "https://api.nasa.gov/planetary/apod"
    payload = {
        "api_key": "sKrvKPzb8Jma4bOxmW00Q679IyIEGg7CvcRq9YRU",
        "count": count
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for resp in response.json():
        urls.append(resp.get("url"))
    return urls


def fetch_spacex_last_launch():
    for url in get_spacex_links():
        get_picture(url, 'images')


if __name__ == '__main__':
    # get_picture(
    #     'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg', 
    #     'images')
    # print((get_links()))
    # fetch_spacex_last_launch()
    print(get_apod_links(2))
