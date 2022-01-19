import json
import os

import requests

from constants import DEBUG, url_search_by_keyword
from models import Song


# QSS 工具类
class QSSTool:
    @staticmethod
    def set_qss_to_obj(file_path, obj):
        with open(file_path, "r") as f:
            content = f.read()
            obj.setStyleSheet(content)


class MusicTool:
    @staticmethod
    def search_by_keyword(keyword) -> tuple:
        # 通过关键字查询
        params = {
            "offset": 0,
            "limit": 20,
            "s": keyword,
            "total": True,
            "type": 1,
        }
        r = requests.get(url_search_by_keyword, params)
        songCount = 0
        result = []
        if r.status_code == 200:
            Log.d(r.text)
            data = json.loads(r.text)
            if data["code"] == 200:
                songCount = data["result"]["songCount"]
                for item in data["result"]["songs"]:
                    result.append(Song(data=item))
        else:
            Log.d("请求失败，status_code: {}".format(r.status_code))
        return (songCount, result)


class TimeTool:
    @staticmethod
    def duration_format(d):
        d = round(d / 1000)
        min = int(d / 60)
        sec = int(d % 60)
        return "{:0>2}:{:0>2}".format(min, sec)


class Log:
    @staticmethod
    def d(obj):
        if DEBUG:
            print(obj)


class PathTool:
    @staticmethod
    def get_download_dir():
        user_home = os.environ["HOME"]
        download_dir = os.path.join(user_home, "Music/musica")
        return download_dir
