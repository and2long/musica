import sys

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QLineEdit, QWidget

from constants import *
from tools import QSSTool


class TopBar(QWidget):
    # 定义一个信号
    search = Signal(str)

    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        bg = QWidget(self)
        bg.setFixedSize(top_bar_width, top_bar_height)
        self.search_box = QLineEdit(self)
        QSSTool.set_qss_to_obj("styles/top_bar.qss", self)
        self.setup_ui()

    def setup_ui(self):
        self.search_box.setClearButtonEnabled(True)
        self.search_box.setPlaceholderText("搜索音乐")
        self.search_box.setFixedSize(300, 28)
        self.search_box.move(
            (main_window_width - left_menus_width) / 2 - search_box_width / 2, 11
        )

        # 输入框监听回车键
        self.search_box.returnPressed.connect(self.search_by_keyword)

    def search_by_keyword(self):
        self.search.emit(self.search_box.text() if self.search_box.text() else "周杰伦")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = TopBar()
    w.show()
    sys.exit(app.exec())
