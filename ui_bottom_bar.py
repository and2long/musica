import sys

from PySide6.QtGui import QPixmap
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtWidgets import QApplication, QLabel, QWidget

from constants import bottomBarHeight, windowWidth
from custom_widgets import ClickedLabel
from models import Song
from tools import Log, TimeTool


# 底部控制栏
class BottomBar(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.setFixedSize(windowWidth, bottomBarHeight)

        # 是否正在播放
        self.playing = False

        # pb = QProgressBar(self)
        # pb.setValue(30)
        # pb.setFixedWidth(windowWidth)
        # pb.setTextVisible(False)
        # pb.move(0, windowHeight - bottomBarHeight - 10)

        # 专辑图片
        album = QLabel(self)
        album.setFixedSize(42, 42)
        album.setStyleSheet("background-color: grey; border-radius: 5px")
        album.move(8, 8)

        # 歌曲名
        self.song_name = QLabel(self)
        self.song_name.setStyleSheet("color: #ccc")
        self.song_name.move(61, 10)

        # 进度和时长
        self.song_duration = QLabel(self)
        self.song_duration.move(61, 32)
        self.song_duration.setStyleSheet("color: grey")

        # 播放按钮
        self.playBtn = ClickedLabel(self)
        self.playBtn.setPixmap(QPixmap("assets/images/ic_play.svg"))
        self.playBtn.setFixedSize(40, 40)
        self.playBtn.move(windowWidth / 2 - 20, bottomBarHeight / 2 - 20)
        self.playBtn.clicked_signal.connect(self.onPlayBtnClickedEvent)

        # 初始化播放器
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.audio_output.setVolume(100)
        # filename = "reason.mp3"
        # self.player.setSource(QUrl.fromLocalFile(filename))

    def onSongDoubelClickEvent(self, value: Song):
        Log.d("播放歌曲: {}".format(value))
        self.song_name.setText(
            value.name + " - " + "/".join([item["name"] for item in value.artists])
        )
        self.song_name.adjustSize()
        self.song_duration.setText("00:00 / " + TimeTool.durationFormat(value.duration))
        self.song_duration.adjustSize()

        # self.player.setSource(QUrl.fr)
        # self.player.play()

    def onPlayBtnClickedEvent(self):
        self.playing = not self.playing
        self.playBtn.setPixmap(
            QPixmap(
                "assets/images/ic_pause.svg"
                if self.playing
                else "assets/images/ic_play.svg"
            )
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = BottomBar()
    w.show()
    sys.exit(app.exec())
