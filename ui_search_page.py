import json
import sys

from PySide6.QtCore import QSize, Signal, Slot
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QListWidget,
                               QListWidgetItem, QVBoxLayout, QWidget)

from constants import *
from models import Song
from tools import MusicTool, QSSTool
from ui_item_song import ItemSong


class Header(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.setFixedSize(container_width, container_header_height)
        self.count = QLabel()
        self.count.setStyleSheet("color: #666666; padding-left: 10px")

        v_layout = QVBoxLayout()
        v_layout.setContentsMargins(0, 0, 0, 0)
        v_layout.addWidget(self.count)

        h_layout = QHBoxLayout()
        h_layout.setContentsMargins(10, 0, 10, 0)
        h_layout.setSpacing(0)

        titles = ["", "音乐标题", "歌手", "时长"]
        for i in range(len(titles)):
            item = QLabel(titles[i])
            item.setStyleSheet("color: #878787")

            h_layout.addWidget(item, item_song_stretchs[i])

        v_layout.addLayout(h_layout)
        self.setLayout(v_layout)

    def format_count(self, value):
        self.count.setText("共找到{}首歌曲".format(value))


class SearchPage(QWidget):
    # 条目被双击信号
    item_double_click_signal = Signal(Song)

    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        QSSTool.set_qss_to_obj("styles/search_page.qss", self)
        self.setFixedSize(container_width, container_height)
        self.header = Header(self)
        self.listWidget = QListWidget(self)
        self.listWidget.verticalScrollBar().hide()
        self.listWidget.move(0, container_header_height)
        self.listWidget.setFixedSize(
            container_width, container_height - container_header_height
        )

    def set_data(self, value: list):
        self.listWidget.clear()
        for i in range(len(value)):
            item_widget = ItemSong(self, index=i, song=value[i])
            item_widget.double_click_signal.connect(self.on_item_double_click)
            item = QListWidgetItem()
            item.setSizeHint(QSize(0, item_song_height))
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, item_widget)

    @Slot(str)
    def on_search(self, value: str):
        count, result = MusicTool.search_by_keyword(value)
        self.set_data(result)
        self.header.format_count(count)

    def on_item_double_click(self, value: Song):
        self.item_double_click_signal.emit(value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = SearchPage()
    result = []
    with open("assets/search_result.json", "r") as f:
        content = f.read()
        data = json.loads(content)
        for item in data["result"]["songs"]:
            result.append(Song(data=item))
    w.set_data(result)
    w.show()
    sys.exit(app.exec())
