import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QWidget

from constants import *


class LeftMenus(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        Leftmenus = QLabel(self)
        Leftmenus.setFixedSize(leftMenuWidth, windowHeight - bottomBarHeight)
        Leftmenus.setStyleSheet("background-color: #202020")

        header = QLabel("MUSICA", self)
        header.setFixedSize(leftMenuWidth, logoHeight)
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("font-size: 24px; background-color: #202020")

        titles = ["发现音乐", "我的收藏", "下载管理"]
        for i in range(3):
            item = QLabel(titles[i], self)
            item.setFixedSize(leftMenuWidth, leftMenuItemHeight)
            item.setAlignment(Qt.AlignCenter)
            item.move(0, logoHeight + i * leftMenuItemHeight)
            if i == 0:
                item.setStyleSheet("background-color: #1b1b1b; color: #c2473a;")
            else:
                item.setStyleSheet("background-color: #202020")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = LeftMenus()
    w.show()
    sys.exit(app.exec())
