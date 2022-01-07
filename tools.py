import json

import requests

from constants import url_search_by_keyword
from models import Song


# QSS 工具类
class QSSTool:
    @staticmethod
    def setQssToObj(file_path, obj):
        with open(file_path, "r") as f:
            content = f.read()
            obj.setStyleSheet(content)


class MusicTool:
    @staticmethod
    def searchByKeyword(keyword) -> list:
        # 通过关键字查询
        params = {
            "offset": 0,
            "limit": 10,
            "s": keyword,
            "total": True,
            "type": 1,
        }
        r = requests.get(url_search_by_keyword, params)
        result = []
        if r.status_code == 200:
            print(r.text)
            data = json.loads(r.text)
            if data["code"] == 200:
                songCount = data["result"]["songCount"]
                for item in data["result"]["songs"]:
                    result.append(Song(data=item))
        else:
            print("请求失败，status_code: {}".format(r.status_code))
        return result


class TimeTool:
    @staticmethod
    def durationFormat(d):
        d = round(d / 1000)
        min = int(d / 60)
        sec = int(d % 60)
        return "{:0>2}:{:0>2}".format(min, sec)
