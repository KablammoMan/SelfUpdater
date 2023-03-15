import requests
import json
import subprocess
import sys


THIS_VERSION = 2

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

latest_version = json.loads(ver.decode())["latest_version"]

if latest_version > THIS_VERSION:
    newc = get_content("https://github.com/KablammoMan/SelfUpdater/raw/main/main.py")
    while not newc:
        newc = get_content("https://github.com/KablammoMan/SelfUpdater/raw/main/main.py")

    open("new.py", "x")

    open("new.py", "wb").write(newc)

    subprocess.Popen("new.py")
    exit()
else:
    print(f"WE HAVE THE LATEST VERSION - WOOHOO!!!! - {sys.argv[0]}")