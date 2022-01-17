import sys

from PySide6.QtGui import QPixmap
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtWidgets import QApplication, QLabel, QWidget

from constants import bottomBarHeight, url_music_source, windowWidth
from custom_widgets import ClickedLabel, NetworkImage
from models import Song
from tools import Log, TimeTool


# 底部控制栏
class BottomBar(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.setFixedSize(windowWidth, bottomBarHeight)

        # 是否正在播放
        self.playing = False
        # 当前音乐资源
        self.song = None

        # pb = QProgressBar(self)
        # pb.setValue(30)
        # pb.setFixedWidth(windowWidth)
        # pb.setTextVisible(False)
        # pb.move(0, windowHeight - bottomBarHeight - 10)

        # 专辑图片
        self.album = NetworkImage(self)
        self.album.setFixedSize(42, 42)
        self.album.setStyleSheet("background-color: grey; border-radius: 5px")
        self.album.move(8, 8)

        # 歌曲名
        self.song_name = QLabel(self)
        self.song_name.setStyleSheet("color: #ccc")
        self.song_name.move(61, 10)

        # 进度和时长
        self.song_duration = QLabel(self)
        self.song_duration.move(61, 32)
        self.song_duration.setStyleSheet("color: grey")

        # 播放按钮
        self.btn_play = ClickedLabel(self)
        self.btn_play.setPixmap(QPixmap("assets/images/ic_play.svg"))
        self.btn_play.setFixedSize(40, 40)
        self.btn_play.move(windowWidth / 2 - 20, bottomBarHeight / 2 - 20)
        self.btn_play.clicked_signal.connect(self.onPlayBtnClickedEvent)

        self.btn_prev = ClickedLabel(self)
        self.btn_prev.setPixmap(QPixmap("assets/images/ic_prev.svg"))
        self.btn_prev.setFixedSize(12, 12)
        self.btn_prev.move(windowWidth / 2 - 57, bottomBarHeight / 2 - 6)

        self.btn_next = ClickedLabel(self)
        self.btn_next.setPixmap(QPixmap("assets/images/ic_next.svg"))
        self.btn_next.setFixedSize(12, 12)
        self.btn_next.move(windowWidth / 2 + 45, bottomBarHeight / 2 - 6)

        # 初始化播放器
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.audio_output.setVolume(100)
        # filename = "reason.mp3"
        # self.player.setSource(QUrl.fromLocalFile(filename))

    def onSongDoubelClickEvent(self, value: Song):
        self.song = value
        self.song_name.setText(
            value.name + " - " + "/".join([item["name"] for item in value.artists])
        )
        self.song_name.adjustSize()
        self.song_duration.setText("00:00 / " + TimeTool.durationFormat(value.duration))
        self.song_duration.adjustSize()

        # 切换歌曲
        self.player.setSource(url_music_source.format(value.id))
        self.player.play()
        self.playing = True
        self.set_play_btn_image()

        # 切换专辑图片
        self.album.set_image_path(value.album["artist"]["img1v1Url"])

    def onPlayBtnClickedEvent(self):
        if self.song:
            # 切换播放状态
            if self.playing:
                self.player.pause()
            else:
                self.player.play()
            # 更改播放状态标记
            self.playing = not self.playing
            # 设置播放按钮图片
            self.set_play_btn_image()

    def set_play_btn_image(self):
        self.btn_play.setPixmap(
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
