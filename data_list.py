import sys

from PySide6.QtCore import QSize, Qt, Slot
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QVBoxLayout,
    QWidget,
)

from models import Song
from tools import MusicSourceTool, TimeTool

stretchs = [1, 9, 5, 3]


class ItemSong(QWidget):
    mHeight = 35

    def __init__(self, parent=None, index=0, song=None) -> None:
        super().__init__(parent=parent)
        self.setFixedSize(DataList.mWidth, self.mHeight)

        hLayout = QHBoxLayout(self)
        hLayout.setContentsMargins(10, 0, 10, 0)
        hLayout.setSpacing(0)

        titles = ["", song.name, song.name, TimeTool.durationFormat(song.duration)]
        for i in range(len(titles)):
            item = QLabel("{:0>2d}".format(index + 1) if i == 0 else titles[i])
            if i == 0:
                item.setAlignment(Qt.AlignCenter)
            item.setStyleSheet("color: #878787")

            hLayout.addWidget(item, stretchs[i])


class DataHeader(QWidget):
    mHeight = 80

    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.setFixedSize(DataList.mWidth, self.mHeight)

        count = QLabel("共找到{}首歌曲".format(300))
        count.setStyleSheet("color: #666666; padding-left: 10px")

        vLayout = QVBoxLayout(self)
        vLayout.setContentsMargins(0, 0, 0, 0)
        vLayout.addWidget(count)

        hLayout = QHBoxLayout(self)
        hLayout.setContentsMargins(10, 0, 10, 0)
        hLayout.setSpacing(0)

        titles = ["", "音乐标题", "歌手", "时长"]
        for i in range(len(titles)):
            item = QLabel(titles[i])
            item.setStyleSheet("color: #878787")

            hLayout.addWidget(item, stretchs[i])

        vLayout.addLayout(hLayout)


class DataList(QWidget):
    mWidth = 800
    mHeight = 575

    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.setFixedSize(self.mWidth, self.mHeight)
        DataHeader(self)
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
        result = MusicSourceTool.searchByKeyword(value)
        self.setData(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = DataList()
    w.show()
    sys.exit(app.exec())
