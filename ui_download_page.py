import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QWidget

from constants import *


class DownloadPage(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.setMinimumSize(container_width, container_height)
        label = QLabel("还没有下载的音乐哦，快去下载吧～", self)
        label.setFixedSize(container_width, container_height)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("color: #878787")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = DownloadPage()
    w.show()
    sys.exit(app.exec())
