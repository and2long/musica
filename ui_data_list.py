import sys

from PySide6 import QtMultimedia
from PySide6.QtCore import QSize, Qt, QUrl, Slot
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QVBoxLayout,
    QWidget,
)

from constants import url_music_source
from models import Song
from tools import Log, MusicTool, TimeTool

stretchs = [1, 9, 5, 3]


class ItemSong(QWidget):
    mHeight = 35

    def __init__(self, parent=None, index=0, song: Song = None) -> None:
        super().__init__(parent=parent)
        self.setFixedSize(DataList.mWidth, self.mHeight)
        self.song = song

        hLayout = QHBoxLayout(self)
        hLayout.setContentsMargins(10, 0, 10, 0)
        hLayout.setSpacing(0)

        titles = [
            "",
            song.name,
            "/".join([item["name"] for item in song.artists]),
            TimeTool.durationFormat(song.duration),
        ]
        for i in range(len(titles)):
            item = QLabel("{:0>2d}".format(index + 1) if i == 0 else titles[i])
            if i == 0:
                item.setAlignment(Qt.AlignCenter)
            item.setStyleSheet("color: #878787")

            hLayout.addWidget(item, stretchs[i])

    def mouseDoubleClickEvent(self, event) -> None:
        url = url_music_source.format(self.song.id)
        Log.d("歌曲链接: {}".format(url))

        player = QtMultimedia.QMediaPlayer()
        player.setSource(QUrl(url))
        player.play()


class DataHeader(QWidget):
    mHeight = 80

    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.setFixedSize(DataList.mWidth, self.mHeight)

        self.count = QLabel()
        self.count.setStyleSheet("color: #666666; padding-left: 10px")

        vLayout = QVBoxLayout(self)
        vLayout.setContentsMargins(0, 0, 0, 0)
        vLayout.addWidget(self.count)

        hLayout = QHBoxLayout(self)
        hLayout.setContentsMargins(10, 0, 10, 0)
        hLayout.setSpacing(0)

        titles = ["", "音乐标题", "歌手", "时长"]
        for i in range(len(titles)):
            item = QLabel(titles[i])
            item.setStyleSheet("color: #878787")

            hLayout.addWidget(item, stretchs[i])

        vLayout.addLayout(hLayout)

    def setCount(self, value):
        self.count.setText("共找到{}首歌曲".format(value))


class DataList(QWidget):
    mWidth = 800
    mHeight = 575

    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.setFixedSize(self.mWidth, self.mHeight)
        self.header = DataHeader(self)
        self.listWidget = QListWidget(self)
        self.listWidget.move(0, DataHeader.mHeight)
        self.listWidget.setFixedSize(self.mWidth, self.mHeight - DataHeader.mHeight)

    def setData(self, value: list):
        for i in range(len(value)):
            itemWidget = ItemSong(self, index=i, song=value[i])
            item = QListWidgetItem()
            item.setSizeHint(QSize(0, ItemSong.mHeight))
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, itemWidget)

    @Slot(str)
    def onSearch(self, value: str):
        songCount, result = MusicTool.searchByKeyword(value)
        self.setData(result)
        self.header.setCount(songCount)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = DataList()
    w.show()
    sys.exit(app.exec())
