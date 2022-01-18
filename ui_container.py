from PySide6.QtCore import Slot
from PySide6.QtWidgets import QStackedLayout, QWidget

from constants import *


class Container(QWidget):
    def __init__(self, parent) -> None:
        super().__init__(parent=parent)
        self.setFixedSize(
            main_window_width - left_menus_width, main_window_height - bottom_bar_height
        )
        self.layout = QStackedLayout()
        self.layout.setStackingMode(QStackedLayout.StackingMode.StackOne)

        self.setLayout(self.layout)

    def add(self, widget):
        self.layout.addWidget(widget)

    @Slot(int)
    def switch_page(self, index):
        self.layout.setCurrentIndex(index)
