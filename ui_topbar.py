import sys

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QLabel, QLineEdit, QWidget


class TopBar(QWidget):
    mWidth = 800
    mHeight = 50

    # 定义一个信号
    search = Signal(str)

    def __init__(self):
        super().__init__()
        self.setFixedSize(self.mWidth, self.mHeight)
        bg = QLabel(self)
        bg.setFixedSize(self.mWidth, self.mHeight)
        bg.setStyleSheet("background-color :#2a2a2a")
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

        # 输入框监听回车键
        searchBar.returnPressed.connect(lambda: self.search.emit(searchBar.text()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = TopBar()
    w.show()
    sys.exit(app.exec())