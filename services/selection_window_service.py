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
from userforms.selection_window_userform import Ui_selection_window
from PySide6.QtWidgets import QApplication, QMainWindow

class Selection_window (QMainWindow, Ui_selection_window,): 
    def __init__(self) -> None:
        """
        Конструктор класса MainWindow, в нем содержатся все поля и методы, которые нужны для работы окна при запуске приложения.
        """
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.gearing_selection_btn.clicked.connect(self.summ)

    def summ(self):
        '''
        Функция суммирования
        '''
        x=self.first_spinbox.value()
        y=self.second_spinbox.value()
        z=x+y
        self.third_spinbox.setValue(z)
        

if __name__ == "__main__":
    app = QApplication([])
    window = Selection_window()
    window.show()
    app.exec()

