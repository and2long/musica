import sys

from PySide6.QtWidgets import QApplication, QBoxLayout, QLabel, QSizeGrip, QWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MUSICA 音乐助手")
        self.setFixedSize(600, 600)

        root = QBoxLayout(QBoxLayout.TopToBottom)
        container = QBoxLayout(QBoxLayout.LeftToRight)
        bottomControlBar = QBoxLayout(QBoxLayout.LeftToRight)

        label1 = QLabel("音乐助手")
        label1.setStyleSheet("background-color: red")

        label2 = QLabel("底部栏")
        label2.setStyleSheet("background-color: grey")

        label3 = QLabel("底部栏")
        label3.setStyleSheet("background-color: orange")
        label3.setFixedHeight(70)

        container.addWidget(label1)
        container.addWidget(label2)
        bottomControlBar.addWidget(label3)

        root.addLayout(container)
        root.addLayout(bottomControlBar)

        self.setLayout(root)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
