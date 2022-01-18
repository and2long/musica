from functools import cached_property

from PySide6.QtCore import QObject, Signal
from PySide6.QtGui import QImage, QMouseEvent, QPixmap
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest
from PySide6.QtWidgets import QLabel


class ClickedLabel(QLabel):

    clicked_signal = Signal(int)

    def __init__(self, parent) -> None:
        super().__init__(parent=parent)
        self.index = 0

    def set_index(self, index):
        self.index = index

    def connect_customized_slot(self, func):
        self.clicked_signal.connect(func)

    def mouseReleaseEvent(self, ev: QMouseEvent) -> None:
        self.clicked_signal.emit(self.index)


class ImageDownloader(QObject):
    finished = Signal(QImage)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.manager.finished.connect(self.handle_finished)

    @cached_property
    def manager(self):
        return QNetworkAccessManager()

    def start_download(self, url):
        self.manager.get(QNetworkRequest(url))

    def handle_finished(self, reply):
        if reply.error() != QNetworkReply.NoError:
            print("error: ", reply.errorString())
            return
        image = QImage()
        image.loadFromData(reply.readAll())
        self.finished.emit(image)


class NetworkImage(QLabel):
    # https://stackoverflow.com/questions/68104165/display-image-from-url
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setScaledContents(True)
        self.downloader = ImageDownloader()
        self.downloader.finished.connect(self.handle_finished)

    def handle_finished(self, image):
        pixmap = QPixmap.fromImage(image)
        self.setPixmap(pixmap)

    def set_image_path(self, path):
        self.downloader.start_download(path)
