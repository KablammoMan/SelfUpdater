import requests


THIS_VERSION = 1

def get_content(url):
    try:
        v = requests.get(url, allow_redirects=True, verify=False)
    except:
        return False
    if v.status_code != 200:
        return False
    return v.content



ver = get_content("https://github.com/KablammoMan/SelfUpdater/raw/main/version.json")
while not ver:
    ver = get_content("https://github.com/KablammoMan/SelfUpdater/raw/main/version.json")

latest_version = ver.decode()["latest_version"]

if latest_version > THIS_VERSION:
    newc = get_content("https://github.com/KablammoMan/SelfUpdater/raw/main/client.py")
    while not newc:
        newc = get_content("https://github.com/KablammoMan/SelfUpdater/raw/main/client.py")

print(newc.decode)