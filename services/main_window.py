import os
import sys
from pathlib import Path


# Получаем абсолютный путь к текущему файлу (main_window.py)
current_file_path = Path(__file__).resolve()

# Поднимаемся на два уровня вверх, чтобы оказаться в корне проекта (my_project)
project_root = current_file_path.parent.parent

# Добавляем корень проекта в начало списка путей поиска
sys.path.insert(0, str(project_root))

# Теперь импорт должен работать, так как Python "увидит" папку my_project/userforms
from userforms.main_single_window_userform import Ui_main_single_window
from PySide6.QtWidgets import QApplication, QMainWindow

class Main_single_window (QMainWindow, Ui_main_single_window,): 
    #         super(MyWindow, self).__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
    def __init__(self) -> None:
        """
        Конструктор класса MainWindow, в нем содержатся все поля и методы, которые нужны для работы окна при запуске приложения.
        """
        QMainWindow.__init__(self)
        self.setupUi(self)
           


if __name__ == "__main__":
    app = QApplication([])
    window = Main_single_window()
    window.show()
    app.exec()