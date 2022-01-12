import sys

from PySide6.QtCore import QSize, Qt, Signal, Slot
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QVBoxLayout,
    QWidget,
)

from constants import *
from models import Song
from tools import Log, MusicTool, TimeTool

stretchs = [1, 9, 5, 3]


class DataHeader(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.setFixedSize(dataListWidth, dataListHeaderHeight)

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


class ItemSong(QWidget):
    # 双击信号
    double_click_signal = Signal(Song)

    def __init__(self, parent=None, index=0, song: Song = None) -> None:
        super().__init__(parent=parent)
        self.setFixedSize(dataListWidth, itemSongHeight)
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
        Log.d(
            "ItemSong.mouseDoubleClickEvent: {}".format(
                url_music_source.format(self.song.id)
            )
        )
        self.double_click_signal.emit(self.song)


class DataList(QWidget):
    # 条目被双击信号
    item_doubel_click_signal = Signal(Song)

    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.setFixedSize(dataListWidth, dataListHeight)
        self.header = DataHeader(self)
        self.listWidget = QListWidget(self)
        self.listWidget.move(0, dataListHeaderHeight)
        self.listWidget.setFixedSize(
            dataListWidth, dataListHeight - dataListHeaderHeight
        )

    def setData(self, value: list):
        for i in range(len(value)):
            itemWidget = ItemSong(self, index=i, song=value[i])
            itemWidget.double_click_signal.connect(self.onSongDoubelClickEvent)
            item = QListWidgetItem()
            item.setSizeHint(QSize(0, itemSongHeight))
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, itemWidget)

    @Slot(str)
    def onSearch(self, value: str):
        songCount, result = MusicTool.searchByKeyword(value)
        self.setData(result)
        self.header.setCount(songCount)

    def onSongDoubelClickEvent(self, value: Song):
        Log.d("DataList.onSongDoubelClickEvent: {}".format(value.name))
        self.item_doubel_click_signal.emit(value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = DataList()
    w.show()
    sys.exit(app.exec())
