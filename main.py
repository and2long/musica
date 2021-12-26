import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QProgressBar, QWidget

from topbar import TopBar


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MUSICA")
        self.setFixedSize(1000, 670)
        self.setStyleSheet("background-color: #252525")
        self.setup_ui()

    def setup_ui(self):
        Leftmenus = QLabel(self)
        Leftmenus.setFixedSize(200, 670)
        Leftmenus.setStyleSheet("background-color: #202020")

        header = QLabel("MUSICA", self)
        header.setFixedSize(200, 150)
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("font-size: 24px; background-color: #202020")

        titles = ["发现音乐", "我的收藏", "下载管理"]
        for i in range(3):
            item = QLabel(titles[i], self)
            item.setFixedSize(200, 40)
            item.setAlignment(Qt.AlignCenter)
            item.move(0, 150 + i * 40)
            if i == 0:
                item.setStyleSheet("background-color: #1b1b1b; color: #c2473a;")
            else:
                item.setStyleSheet("background-color: #202020")

        label3 = QLabel("底部栏", self)
        label3.setFixedSize(1000, 45)
        label3.setStyleSheet("background-color: #2a2a2a")
        label3.move(0, 670 - 45)

        pb = QProgressBar(self)
        pb.setValue(30)
        pb.setFixedWidth(1000)
        pb.setTextVisible(False)
        pb.move(0, 670 - 45 - 10)

        topbar = TopBar()
        topbar.setParent(self)
        topbar.move(200, 0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
