from PySide6.QtWidgets import QApplication, QMainWindow, QDoubleSpinBox, QSpinBox, QFormLayout, QGridLayout
from my_ui2 import Ui_MainWindow

class MainWindow1 (QMainWindow, Ui_MainWindow,): 
    #         super(MyWindow, self).__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
    def __init__(self) -> None:
        """
        Конструктор класса MainWindow, в нем содержатся все поля и методы, которые нужны для работы окна при запуске приложения.
        """
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.doubleSpinBox.valueChanged.connect(self.ChangeStyleSpinbox)

    def ChangeStyleSpinbox(self):
        self.doubleSpinBox.setDecimals(10)
        if 10==self.doubleSpinBox.value:
            self.doubleSpinBox.setStyleSheet(u"background-color: rgb(1, 1, 1);")
            


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow1()
    window.show()
    app.exec()