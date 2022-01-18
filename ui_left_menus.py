import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QWidget

from constants import *


class LeftMenus(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        Leftmenus = QLabel(self)
        Leftmenus.setFixedSize(left_menus_width, main_window_height - bottom_bar_height)
        Leftmenus.setStyleSheet("background-color: #202020")

        header = QLabel("MUSICA", self)
        header.setFixedSize(left_menus_width, logo_height)
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("font-size: 24px; background-color: #202020")

        for i in range(3):
            item = QLabel(left_menus_titles[i], self)
            item.setFixedSize(left_menus_width, left_menus_height)
            item.setAlignment(Qt.AlignCenter)
            item.move(0, logo_height + i * left_menus_height)
            if i == 0:
                item.setStyleSheet("background-color: #1b1b1b; color: #c2473a;")
            else:
                item.setStyleSheet("background-color: #202020")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = LeftMenus()
    w.show()
    sys.exit(app.exec())
