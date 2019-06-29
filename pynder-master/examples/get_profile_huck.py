import requests
USER_AGENT = "Tinder/7.5.3 (iPhone; iOS 10.3.2; Scale/2.00)"

HEADERS = {
    'app_version': '6.9.4',
    'platform': 'ios',
    "content-type": "application/json",
    "app-version": "1020353",
    "User-agent": USER_AGENT,
    "Accept": "application/json"
}
url_profile = 'https://api.gotinder.com/profile'
HEADERS['X-Auth-Token'] = '1fe12968-4672-412f-883b-cdf0c516c449'
r = requests.get(url_profile, headers=HEADERS)


print(r.content)