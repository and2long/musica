import sys

from PySide6.QtWidgets import QApplication, QWidget

from constants import *
from ui_bottom_bar import BottomBar
from ui_search_result import SearchResult
from ui_left_menus import LeftMenus
from ui_top_bar import TopBar


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MUSICA")
        self.setFixedSize(main_window_width, main_window_height)
        self.setStyleSheet("background-color: #252525")
        self.setup_ui()

    def setup_ui(self):
        LeftMenus(self)

        topbar = TopBar(self)
        topbar.move(left_menus_width, 0)

        dataArea = SearchResult(self)
        dataArea.move(left_menus_width, top_bar_height)

        bottomBar = BottomBar(self)
        bottomBar.move(0, main_window_height - bottom_bar_height)

        # 连接搜索框与数据列表
        topbar.search.connect(dataArea.onSearch)
        # 连接数据列表和底部控制栏
        dataArea.item_doubel_click_signal.connect(bottomBar.onSongDoubelClickEvent)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
