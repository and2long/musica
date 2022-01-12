import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QProgressBar, QWidget

from constants import *
from ui_bottom_bar import BottomBar
from ui_data_list import DataList
from ui_topbar import TopBar


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MUSICA")
        self.setFixedSize(windowWidth, windowHeight)
        self.setStyleSheet("background-color: #252525")
        self.setup_ui()

    def setup_ui(self):
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

        # pb = QProgressBar(self)
        # pb.setValue(30)
        # pb.setFixedWidth(windowWidth)
        # pb.setTextVisible(False)
        # pb.move(0, windowHeight - bottomBarHeight - 10)

        topbar = TopBar(self)
        topbar.move(leftMenuWidth, 0)

        dataArea = DataList(self)
        dataArea.move(leftMenuWidth, topBarHeight)
        # 连接搜索框与数据列表之间的信号
        topbar.search.connect(dataArea.onSearch)

        bottomBar = BottomBar(self)
        bottomBar.move(0, windowHeight - bottomBarHeight)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
