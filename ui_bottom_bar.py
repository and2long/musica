import sys

from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtWidgets import QApplication, QLabel, QWidget

from constants import bottomBarHeight, windowWidth
from models import Song
from tools import Log


# 底部控制栏
class BottomBar(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.setFixedSize(windowWidth, bottomBarHeight)

        # pb = QProgressBar(self)
        # pb.setValue(30)
        # pb.setFixedWidth(windowWidth)
        # pb.setTextVisible(False)
        # pb.move(0, windowHeight - bottomBarHeight - 10)

        # 专辑图片
        album = QLabel(self)
        album.setFixedSize(42, 42)
        album.setStyleSheet("background-color: white; border-radius: 5px")
        album.move(8, 8)

        # 歌曲名
        song_name = QLabel(self)
        song_name.setText("被风吹过的夏天 - 林俊杰")
        song_name.setStyleSheet("color: #ccc")
        song_name.move(61, 10)

        # 进度和时长
        song_duration = QLabel(self)
        song_duration.setText("01:39 / 03:57")
        song_duration.move(61, 32)
        song_duration.setStyleSheet("color: grey")

        # 初始化播放器
        filename = "reason.mp3"
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.player.setSource(QUrl.fromLocalFile(filename))
        self.audio_output.setVolume(100)

    def onSongDoubelClickEvent(self, value: Song):
        Log.d("播放歌曲: {}".format(value))
        self.player.play()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = BottomBar()
    w.show()
    sys.exit(app.exec())
