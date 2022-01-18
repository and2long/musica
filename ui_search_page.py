import json
import sys

from PySide6.QtCore import QSize, Signal, Slot
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
from tools import MusicTool
from ui_item_song import ItemSong


class Header(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.setFixedSize(container_width, container_header_height)

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

            hLayout.addWidget(item, item_song_stretchs[i])

        vLayout.addLayout(hLayout)

    def setCount(self, value):
        self.count.setText("共找到{}首歌曲".format(value))


class SearchPage(QWidget):
    # 条目被双击信号
    item_doubel_click_signal = Signal(Song)

    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.setFixedSize(container_width, container_height)
        self.header = Header(self)
        self.listWidget = QListWidget(self)
        self.listWidget.verticalScrollBar().hide()
        self.listWidget.move(0, container_header_height)
        self.listWidget.setFixedSize(
            container_width, container_height - container_header_height
        )

    def setData(self, value: list):
        self.listWidget.clear()
        for i in range(len(value)):
            itemWidget = ItemSong(self, index=i, song=value[i])
            itemWidget.double_click_signal.connect(self.onSongDoubelClickEvent)
            item = QListWidgetItem()
            item.setSizeHint(QSize(0, item_song_height))
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, itemWidget)

    @Slot(str)
    def onSearch(self, value: str):
        songCount, result = MusicTool.searchByKeyword(value)
        self.setData(result)
        self.header.setCount(songCount)

    def onSongDoubelClickEvent(self, value: Song):
        self.item_doubel_click_signal.emit(value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = SearchPage()
    result = []
    with open("assets/search_result.json", "r") as f:
        content = f.read()
        data = json.loads(content)
        for item in data["result"]["songs"]:
            result.append(Song(data=item))
    w.setData(result)
    w.show()
    sys.exit(app.exec())
