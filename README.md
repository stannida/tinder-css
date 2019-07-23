# tinder-css

[![Binder](https://notebooks.gesis.org/binder/badge_logo.svg)](https://notebooks.gesis.org/binder/v2/gh/stannida/tinder-css/master)
# Crawler instructions
To run crawler you need to download, configure and run following github project: https://github.com/charliewolf/pynder

Steps to follow after that:

1) Import .py files from `/crawler` folder to downloaded project.
2) Get X-Auth-Token from Browser
3) Paste X-Auth-Token to all 3 files
4) Run `set_location.py` to set custom location
5) Run `get_profile.py` to get profile and make sure location is set
6) Run `fetch_users.py` to save 30 users in csv file and dislike them
 
