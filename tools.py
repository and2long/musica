import json

import requests

from models import Song


# QSS 工具类
class QSSTool:
    @staticmethod
    def setQssToObj(file_path, obj):
        with open(file_path, "r") as f:
            content = f.read()
            obj.setStyleSheet(content)


# 音乐资源工具类
class MusicSourceTool:
    @staticmethod
    def searchByKeyword(keyword):
        # 通过关键字查询
        url = "http://music.163.com/api/search/get/web?csrf_token=hlpretag=&hlposttag=&s={}&type=1&offset=0&total=true&limit=20"
        r = requests.get(url.format(keyword))
        if r.status_code == 200:
            data = json.loads(r.text)
            print("找到{}首歌曲".format(data["result"]["songCount"]))
            for item in data["result"]["songs"]:
                print(Song(data=item))
        else:
            print("请求失败，status_code: {}".format(r.status_code))
