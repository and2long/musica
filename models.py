import json


class Song:
    def __init__(
        self, id: int = None, name: str = None, duration: int = None, data: dict = None
    ):
        if data:
            self.id = data.get("id")
            self.name = data.get("name")
            self.duration = data.get("duration")
            self.artists = data.get("artists")
        else:
            self.id = id
            self.name = name
            self.duration = duration

    def __str__(self) -> str:
        return json.dumps(
            {
                "id": self.id,
                "name": self.name,
                "duration": self.duration,
                "artists": self.artists,
            },
            ensure_ascii=False,
        )
