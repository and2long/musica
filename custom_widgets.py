from PySide6.QtCore import Signal
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QLabel


class ClickedLabel(QLabel):
    clicked_signal = Signal()

    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)

    def connect_customized_slot(self, func):
        self.clicked_signal.connect(func)

    def mouseReleaseEvent(self, ev: QMouseEvent) -> None:
        self.clicked_signal.emit()
