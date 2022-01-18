import sys

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QApplication, QLabel, QWidget

from constants import *
from custom_widgets import ClickedLabel


class LeftMenus(QWidget):

    # 菜单索引切换信号
    index_signal = Signal(int)

    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)

        header = QLabel("MUSICA", self)
        header.setFixedSize(left_menus_width, logo_height)
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("font-size: 24px; background-color: #252525; color: white")

        # 当前菜单索引
        self.cur_index = 0
        self.menus = []
        for i in range(len(left_menus_titles)):
            item = ClickedLabel(self)
            item.set_index(i)
            item.setFixedSize(left_menus_width, left_menus_height)
            item.setAlignment(Qt.AlignCenter)
            item.setText(left_menus_titles[i])
            item.move(0, logo_height + i * left_menus_height)
            item.connect_customized_slot(self.on_menu_checked)
            self.menus.append(item)
        self.set_style()

    def set_style(self):
        for i in range(len(self.menus)):
            if i == self.cur_index:
                self.menus[i].setStyleSheet(
                    "background-color: #1b1b1b; color: #c2473a;"
                )
            else:
                self.menus[i].setStyleSheet(
                    "background-color: #252525; color: #aaaaaa;"
                )

    def on_menu_checked(self, index):
        self.cur_index = index
        self.set_style()
        self.index_signal.emit(index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = LeftMenus()
    w.show()
    sys.exit(app.exec())
