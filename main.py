import requests


THIS_VERSION = 1

def get_version(url):
    try:
        v = requests.get(url)
    except:
        return False
    if v.status_code != 200:
        return False
    return v.content

ver = get_version("https://github.com/KablammoMan/SelfUpdater/raw/main/version.json")
while not ver:
    ver = get_version("https://github.com/KablammoMan/SelfUpdater/raw/main/version.json")

print(ver)
