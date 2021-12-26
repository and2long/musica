import json

import requests

from models import Song

url = "http://music.163.com/api/search/get/web?csrf_token=hlpretag=&hlposttag=&s={}&type=1&offset=0&total=true&limit=20"
r = requests.get(url.format("林俊杰"))
if r.status_code == 200:
    data = json.loads(r.text)
    print("找到{}首歌曲".format(data["result"]["songCount"]))
    for item in data["result"]["songs"]:
        print(Song(data=item))
