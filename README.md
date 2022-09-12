# Space Telegram

This is implementation of telegram bot, which purpose is posting random pictures from/of space

### before start you have to:
 - get personal token on https://api.nasa.gov
 - create .env file on project directory
 - make a record formatted as "NASA_API_KEY=YUORTOKEN"

 - register yourbot on botfather telegram
 - get personal token
 - add a record formatted as "TELEGRAM_API_KEY=YUORTOKEN"
 - add a record "PUB_PERIOD_HRS=4"

 then you could start installation of project.
### How to install

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
### How to use
project contain 3 module for fetch pics from 3 different api:
 - epic   -> fetch_epic_images.py
 - apod   -> fetch_apod_images.py
 - spacex -> fetch_spacex_images.py

and main app - telegram_bot.py 
#### spacex launches
fetch pictures from latest launch
```
python fetch_spacex_images.py
```
cli app
fetch pictures from paticular launch by id
for example use 5eb87d47ffd86e000604b38a
```
python fetch_spacex_images.py --launch_id  <launch_id>
```
#### apod
cli app  
fetch pictures from nasa api Astronomy Picture of the Day
```
python fetch_apod_images.py <amuont of pictures>
```
#### epic
fetch pictures from nasa api Earth Polychromatic Imaging Camera
```
python fetch_epic_images.py
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).