import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QProgressBar, QWidget

from data_list import DataList
from topbar import TopBar


class MainWindow(QWidget):
    mWidth = 1000
    mHeight = 670
    menuWidth = 200
    menuItemHeight = 40
    bottomBarHeight = 45
    logoHeight = 150

    def __init__(self):
        super().__init__()
        self.setWindowTitle("MUSICA")
        self.setFixedSize(self.mWidth, self.mHeight)
        self.setStyleSheet("background-color: #252525")
        self.setup_ui()

    def setup_ui(self):
        Leftmenus = QLabel(self)
        Leftmenus.setFixedSize(self.menuWidth, self.mHeight)
        Leftmenus.setStyleSheet("background-color: #202020")

        header = QLabel("MUSICA", self)
        header.setFixedSize(self.menuWidth, self.logoHeight)
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("font-size: 24px; background-color: #202020")

        titles = ["发现音乐", "我的收藏", "下载管理"]
        for i in range(3):
            item = QLabel(titles[i], self)
            item.setFixedSize(self.menuWidth, self.menuItemHeight)
            item.setAlignment(Qt.AlignCenter)
            item.move(0, self.logoHeight + i * self.menuItemHeight)
            if i == 0:
                item.setStyleSheet("background-color: #1b1b1b; color: #c2473a;")
            else:
                item.setStyleSheet("background-color: #202020")

        label3 = QLabel("底部栏", self)
        label3.setFixedSize(self.mWidth, self.bottomBarHeight)
        label3.setStyleSheet("background-color: #2a2a2a")
        label3.move(0, self.mHeight - self.bottomBarHeight)

        pb = QProgressBar(self)
        pb.setValue(30)
        pb.setFixedWidth(self.mWidth)
        pb.setTextVisible(False)
        pb.move(0, self.mHeight - self.bottomBarHeight - 10)

        topbar = TopBar()
        topbar.setParent(self)
        topbar.move(self.menuWidth, 0)

        dataArea = DataList(self)
        dataArea.move(self.menuWidth, TopBar.mHeight)

        topbar.search.connect(dataArea.onSearch)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
