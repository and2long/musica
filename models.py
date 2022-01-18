import json


class Song:
    def __init__(self, data):
        self.id = data.get("id")
        self.name = data.get("name")
        self.duration = data.get("duration")
        self.artists = data.get("artists")
        self.album = data.get("album")
        self.copyrightId = data.get("copyrightId")

    def __str__(self) -> str:
        return json.dumps(
            {
                "id": self.id,
                "name": self.name,
                "duration": self.duration,
                "copyrightId": self.copyrightId,
            },
            ensure_ascii=False,
        )
