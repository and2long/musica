import sys

from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QWidget

from constants import bottomBarHeight, windowWidth


# 底部控制栏
class BottomBar(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.setFixedSize(windowWidth, bottomBarHeight)

        label3 = QLabel("底部栏", self)
        label3.setFixedSize(windowWidth, bottomBarHeight)
        label3.setStyleSheet("background-color: #2a2a2a")

        filename = "reason.mp3"
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.player.setSource(QUrl.fromLocalFile(filename))
        self.audio_output.setVolume(100)
        self.player.play()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = BottomBar()
    w.show()
    sys.exit(app.exec())
