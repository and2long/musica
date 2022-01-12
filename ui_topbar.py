import sys

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QLabel, QLineEdit, QWidget

from constants import topBarHeight, topBarWidth


class TopBar(QWidget):

    # 定义一个信号
    search = Signal(str)

    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.setFixedSize(topBarWidth, topBarHeight)
        bg = QLabel(self)
        bg.setFixedSize(topBarWidth, topBarHeight)
        bg.setStyleSheet("background-color :#2a2a2a")
        self.setup_ui()

    def setup_ui(self):
        searchBar = QLineEdit(self)
        searchBar.setPlaceholderText("搜索音乐")
        searchBar.setFixedSize(300, 28)
        searchBar.setStyleSheet(
            "background-color: #4a4a4a;  padding-left: 15px; padding-right: 15px; border-radius: 14px"
        )
        searchBar.move(150, 11)

        recommend = QLabel("推荐", parent=self)
        recommend.setStyleSheet("font-size: 14px")
        recommend.move(50, 14)

        # 输入框监听回车键
        searchBar.returnPressed.connect(
            lambda: self.search.emit(searchBar.text() if searchBar.text() else "周杰伦")
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = TopBar()
    w.show()
    sys.exit(app.exec())
