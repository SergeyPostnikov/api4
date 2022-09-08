import argparse
import requests

from picture_handlers import get_picture


def get_spacex_links(launch_id=None):
    if launch_id is not None:
        url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    else:
        url = 'https://api.spacexdata.com/v5/launches/latest'
    response = requests.get(url)
    response.raise_for_status()
    return response.json().get('links').get('flickr').get('original')


def fetch_spacex_launch(launch_id=None):
    for url in get_spacex_links(launch_id):
        get_picture(url, 'images')


if __name__ == '__main__':
    # for test use --launch_id 5eb87d47ffd86e000604b38a
    parser = argparse.ArgumentParser()
    parser.add_argument('--launch_id', help='launch id')
    args = parser.parse_args()
    fetch_spacex_launch(args.launch_id)
    print(args.launch_id)
