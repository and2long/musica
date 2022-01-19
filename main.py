import sys

from PySide6.QtWidgets import QApplication, QWidget

from constants import *
from tools import QSSTool
from ui_bottom_bar import BottomBar
from ui_container import Container
from ui_download_page import DownloadPage
from ui_left_menus import LeftMenus
from ui_search_page import SearchPage
from ui_top_bar import TopBar


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MUSICA")
        self.setFixedSize(main_window_width, main_window_height)
        self.setup_ui()

    def setup_ui(self):
        left_menus = LeftMenus(self)

        topbar = TopBar(self)
        topbar.move(left_menus_width, 0)

        container = Container(self)
        container.move(left_menus_width, top_bar_height)

        search_page = SearchPage()
        download_page = DownloadPage()
        container.add(search_page)
        container.add(download_page)
        left_menus.index_signal.connect(container.switch_page)

        bottom_bar = BottomBar(self)
        bottom_bar.move(0, main_window_height - bottom_bar_height)

        # 连接搜索框与数据列表
        topbar.search.connect(search_page.onSearch)
        # 连接数据列表和底部控制栏
        search_page.item_doubel_click_signal.connect(bottom_bar.onSongDoubelClickEvent)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    QSSTool.set_qss_to_obj("styles/main.qss", w)
    w.show()
    sys.exit(app.exec())
