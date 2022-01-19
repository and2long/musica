from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QHBoxLayout, QLabel, QWidget

from constants import *
from models import Song
from tools import Log, TimeTool


class ItemSong(QWidget):
    # 双击信号
    double_click_signal = Signal(Song)

    def __init__(
        self,
        parent=None,
        index=0,
        local: bool = False,
        name: str = None,
        song: Song = None,
    ) -> None:
        super().__init__(parent=parent)
        self.setFixedSize(container_width, item_song_height)
        self.setStyleSheet("background-color: #252525")

        self.song = song
        hLayout = QHBoxLayout(self)
        hLayout.setContentsMargins(0, 0, 0, 0)
        hLayout.setSpacing(0)

        if local:
            for i in range(2):
                item = QLabel("{:0>2d}".format(index + 1) if i == 0 else name)
                if i == 0:
                    item.setAlignment(Qt.AlignCenter)
                if i == 1:
                    item.setStyleSheet("color: #AAAAAA")
                else:
                    item.setStyleSheet("color: #878787")
                hLayout.addWidget(item, item_song_stretchs[i])
        else:
            titles = [
                "",
                song.name,
                "/".join([item["name"] for item in song.artists]),
                TimeTool.duration_format(song.duration),
            ]
            for i in range(len(titles)):
                item = QLabel("{:0>2d}".format(index + 1) if i == 0 else titles[i])
                if i == 0:
                    item.setAlignment(Qt.AlignCenter)
                if i == 1:
                    item.setStyleSheet("color: #AAAAAA")
                else:
                    item.setStyleSheet("color: #878787")
                hLayout.addWidget(item, item_song_stretchs[i])

    def mouseDoubleClickEvent(self, event) -> None:
        if self.song:
            Log.d(
                "{}: {}\n{}".format(
                    self.song.name, self.song, url_music_source.format(self.song.id)
                )
            )
            self.double_click_signal.emit(self.song)

    def enterEvent(self, event) -> None:
        self.setStyleSheet("background-color: #333333")

    def leaveEvent(self, event) -> None:
        self.setStyleSheet("background-color: #252525")
