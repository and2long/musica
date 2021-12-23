class QSSTool:
    @staticmethod
    def setQssToObj(file_path, obj):
        with open(file_path, "r") as f:
            content = f.read()
            obj.setStyleSheet(content)
