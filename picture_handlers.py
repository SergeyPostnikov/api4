import requests
import os
from os.path import splitext, join
from urllib.parse import urlparse, unquote
from datetime import datetime

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def get_filename(url):
    dt = datetime.now()
    filename = dt.strftime("%Y-%m-%d-%H-%M-%S")
    return f'{filename}{unquote(urlparse(url).path.split("/")[-1])}'


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
