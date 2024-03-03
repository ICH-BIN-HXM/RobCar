from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口标题
        self.setWindowTitle('Key Press Detector')

        # 创建一个按钮
        self.button = QPushButton('Click me!', self)
        self.button.setGeometry(50, 50, 200, 100)

        # 按钮点击事件连接槽函数
        self.button.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        print("Button clicked!")

    def keyPressEvent(self, event):
        print("Key pressed:")
        # 获取按键文本
        # key_text = event.text()
        # print(f"Key pressed: {key_text}")

if __name__ == '__main__':
    import sys
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
