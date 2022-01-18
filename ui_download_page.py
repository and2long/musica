import os
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QWidget

from constants import *
from tools import Log


class DownloadPage(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.setMinimumSize(container_width, container_height)
        empty_tip = QLabel("还没有下载的音乐哦，快去下载吧～", self)
        empty_tip.setFixedSize(container_width, container_height)
        empty_tip.setAlignment(Qt.AlignCenter)
        empty_tip.setStyleSheet("color: #878787")

        # 初始化下载目录
        user_home = os.environ["HOME"]
        save_dir = os.path.join(user_home, download_dir)
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)

        files = os.listdir(save_dir)
        # 筛选出 mp3 文件
        mp3_files = []
        if len(files) > 0:
            for file in files:
                if file.endswith("mp3"):
                    mp3_files.append(file)
        # 存在 mp3 文件，就不显示文字提示。
        if len(mp3_files) > 0:
            empty_tip.setParent(None)
        Log.d("mp3_files: %s" % mp3_files)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = DownloadPage()
    w.show()
    sys.exit(app.exec())
