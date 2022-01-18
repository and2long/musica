import sys

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QLabel, QLineEdit, QWidget

from constants import *


class TopBar(QWidget):

    # 定义一个信号
    search = Signal(str)

    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.setFixedSize(top_bar_width, top_bar_height)
        bg = QLabel(self)
        bg.setFixedSize(top_bar_width, top_bar_height)
        bg.setStyleSheet("background-color :#2a2a2a")
        self.setup_ui()

    def setup_ui(self):
        searchBar = QLineEdit(self)
        searchBar.setClearButtonEnabled(True)
        searchBar.setPlaceholderText("搜索音乐")
        searchBar.setFixedSize(300, 28)
        searchBar.setStyleSheet(
            "background-color: #4a4a4a;  padding-left: 15px; padding-right: 15px; border-radius: 14px"
        )
        searchBar.move(
            (main_window_width - left_menus_width) / 2 - search_box_width / 2,
            11,
        )

        # 输入框监听回车键
        searchBar.returnPressed.connect(
            lambda: self.search.emit(searchBar.text() if searchBar.text() else "周杰伦")
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = TopBar()
    w.show()
    sys.exit(app.exec())
