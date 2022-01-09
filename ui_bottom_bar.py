from typing import Optional

import PySide6
from PySide6.QtWidgets import QLabel, QWidget

from constants import bottomBarHeight, windowWidth


class BottomBar(QWidget):
    def __init__(
        self,
        parent: Optional[PySide6.QtWidgets.QWidget] = ...,
        f: PySide6.QtCore.Qt.WindowFlags = ...,
    ) -> None:
        super().__init__(parent=parent, f=f)
        self.setFixedSize(windowWidth, bottomBarHeight)

        label3 = QLabel("底部栏", self)
        # label3.setStyleSheet("background-color: #2a2a2a")
        label3.setStyleSheet("background-color: red")
