import sys
from types import LambdaType

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QLabel, QLineEdit, QStackedLayout, QWidget


class TopBar(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 50)
        self.setStyleSheet("background-color: #2a2a2a")
        self.setup_ui()

    def setup_ui(self):
        searchBar = QLineEdit(self)
        searchBar.setPlaceholderText("关键字搜索")
        searchBar.setFixedSize(300, 28)
        searchBar.setStyleSheet(
            "background-color: #4a4a4a;  padding-left: 15px; padding-right: 15px; border-radius: 14px"
        )
        searchBar.move(150, 11)

        recommend = QLabel("推荐", parent=self)
        recommend.setStyleSheet("font-size: 14px")
        recommend.move(50, 14)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = TopBar()
    w.show()
    sys.exit(app.exec())
