import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QBoxLayout, QLabel, QProgressBar, QWidget

from tools import QSSTool


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MUSICA")
        self.setFixedSize(1000, 670)

        root = QBoxLayout(QBoxLayout.TopToBottom)
        root.setContentsMargins(0, 0, 0, 0)
        container = QBoxLayout(QBoxLayout.LeftToRight)
        bottomControlBar = QBoxLayout(QBoxLayout.LeftToRight)

        leftMenu = QBoxLayout(QBoxLayout.TopToBottom)
        leftMenu.setObjectName("leftMenu")

        header = QLabel("MUSICA")
        header.setFixedHeight(150)
        header.setAlignment(Qt.AlignCenter)
        header.setObjectName("header")
        leftMenu.addWidget(header)

        menu1 = QLabel("发现音乐")
        menu1.setFixedHeight(40)
        menu1.setAlignment(Qt.AlignCenter)
        menu1.setObjectName("menu1")
        leftMenu.addWidget(menu1)

        menu2 = QLabel("我的收藏")
        menu2.setFixedHeight(40)
        menu2.setAlignment(Qt.AlignCenter)
        menu2.setObjectName("menu2")
        leftMenu.addWidget(menu2)

        menu3 = QLabel("下载管理")
        menu3.setFixedHeight(40)
        menu3.setAlignment(Qt.AlignCenter)
        menu3.setObjectName("menu3")
        leftMenu.addWidget(menu3)

        leftMenu.addStretch(1)

        label2 = QLabel("内容区")

        label3 = QLabel("底部栏")
        label3.setFixedHeight(45)
        label3.setObjectName("bcb")

        pb = QProgressBar()
        pb.setValue(30)
        pb.setTextVisible(False)

        container.addLayout(leftMenu, 1)
        container.addWidget(label2, 4)
        bottomControlBar.addWidget(label3)

        root.addLayout(container)
        root.addWidget(pb)
        root.addLayout(bottomControlBar)

        self.setLayout(root)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    QSSTool.setQssToObj("main.qss", app)
    sys.exit(app.exec())
