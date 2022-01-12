import sys

from PySide6.QtWidgets import QApplication, QWidget

from constants import *
from ui_bottom_bar import BottomBar
from ui_data_list import DataList
from ui_left_menus import LeftMenus
from ui_topbar import TopBar


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MUSICA")
        self.setFixedSize(windowWidth, windowHeight)
        self.setStyleSheet("background-color: #252525")
        self.setup_ui()

    def setup_ui(self):
        LeftMenus(self)

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
