import sys
from types import LambdaType

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QLabel, QLineEdit, QStackedLayout, QWidget


class TopBar(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 50)
        self.setup_ui()

    def setup_ui(self):
        layout = QStackedLayout()
        layout.setStackingMode(QStackedLayout.StackAll)
        label = QLabel()
        label.setStyleSheet("background-color: #2a2a2a")

        searchBar = QLineEdit()
        searchBar.setPlaceholderText("关键字搜索")
        searchBar.setFixedSize(300, 28)
        searchBar.setStyleSheet(
            "background-color: #4a4a4a;  padding-left: 15px; padding-right: 15px; border-radius: 14px"
        )

        layout.addWidget(label)
        layout.addWidget(searchBar)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = TopBar()
    w.show()
    sys.exit(app.exec())
