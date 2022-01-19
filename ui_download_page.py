import os
import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QWidget,
)

from constants import *
from tools import Log
from ui_item_song import ItemSong


class DownloadPage(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.setMinimumSize(container_width, container_height)
        self.init()

    def init(self):
        # 初始化下载目录
        user_home = os.environ["HOME"]
        self.save_dir = os.path.join(user_home, download_dir)
        if not os.path.exists(self.save_dir):
            os.mkdir(self.save_dir)
        files = os.listdir(self.save_dir)
        # 筛选出 mp3 文件
        self.mp3_files = []
        if len(files) > 0:
            for file in files:
                if file.endswith("mp3"):
                    self.mp3_files.append(file)
        Log.d("mp3_files: %s" % self.mp3_files)
        if len(self.mp3_files) > 0:
            self.setup_ui()
        else:
            self.show_empty_tip()

    def show_empty_tip(self):
        empty_tip = QLabel("还没有下载的音乐哦，快去下载吧～", self)
        empty_tip.setFixedSize(container_width, container_height)
        empty_tip.setAlignment(Qt.AlignCenter)
        empty_tip.setStyleSheet("color: #878787")

    def setup_ui(self):
        btn_play_all = QPushButton("播放全部", self)
        btn_open_dir = QPushButton("打开目录", self)
        btn_play_all.move(10, 10)
        btn_open_dir.move(100, 10)

        list_widget = QListWidget(self)
        list_widget.move(0, 50)
        list_widget.setFixedWidth(container_width)

        for i in range(len(self.mp3_files)):
            item_widget = ItemSong(self, index=i, local=True, name=self.mp3_files[i])
            item = QListWidgetItem()
            item.setSizeHint(QSize(0, item_song_height))
            list_widget.addItem(item)
            list_widget.setItemWidget(item, item_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = DownloadPage()
    w.show()
    sys.exit(app.exec())
