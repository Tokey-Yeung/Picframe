from PySide6.QtWidgets import QApplication, QMainWindow
# PySide6-uic PicframeUI.ui -o UI.py
# from ui_demo import Ui_Demo


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # self.ui = Ui_Demo()  # UI类的实例化()
        # self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication([])  # 启动一个应用
    window = MainWindow()  # 实例化主窗口
    window.show()  # 展示主窗口
    app.exec()  # 避免程序执行到这一行后直接退出