import requests
import os


from picture_handlers import get_date, get_picture
from dotenv import load_dotenv


def get_epic_links(auth_token):
    links = []
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    payload = {
        "api_key": auth_token,
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for resp in response.json():
        date = get_date(resp.get("date"))
        filename = f'{resp.get("image")}.png'
        links.append(f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{filename}')
    return links


def fetch_epic(auth_token):
    for url in get_epic_links(auth_token):
        get_picture(url, 'images', params={'api_key': auth_token})


if __name__ == '__main__':  
    load_dotenv()
    auth_token = os.getenv('NASA_API_KEY')
    fetch_epic(auth_token)
