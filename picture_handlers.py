import requests
import os
from os.path import splitext, join
from urllib.parse import urlparse, unquote
from datetime import datetime
from hashlib import blake2b
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def get_filename(url):
    filename = unquote(urlparse(url).path.split("/")[-1])
    hashed_name = blake2b(digest_size=5)
    hashed_name.update(bin(filename))
    return f'{hashed_name.hexdigest()}{filename}'


def get_ext(url):
    return splitext(get_filename(url))[1]


def get_date(datestring):
    dt = datetime.strptime(datestring, '%Y-%m-%d %H:%M:%S')
    return dt.strftime("%Y/%m/%d")


def save_picture(url, directory, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    os.makedirs(directory, exist_ok=True)

    with open(join(BASE_DIR, 'images', get_filename(url)), 'wb') as file:
        file.write(response.content)
