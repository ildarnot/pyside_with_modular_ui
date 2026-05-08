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
from userforms.calculation_window_userform import Ui_Calculation_window
from PySide6.QtWidgets import QApplication, QMainWindow, QButtonGroup

class Calculation_window (QMainWindow, Ui_Calculation_window,): 
    def __init__(self) -> None:
        """
        Конструктор класса MainWindow, в нем содержатся все поля и методы, которые нужны для работы окна при запуске приложения.
        """
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.gearing_calculation_btn.clicked.connect(self.multi_division)

        # Создаём группу кнопок
        self.button_group = QButtonGroup()
        self.button_group.addButton(self.multi_button)
        self.button_group.addButton(self.divide_button)

        # Опционально: устанавливаем, что хотя бы одна кнопка всегда должна быть выбрана
        self.button_group.setExclusive(True)  # по умолчанию уже True, но можно указать явно

    def multi_division(self):
        '''
        Функция суммирования
        '''
        x=self.first_spinbox.value()
        y=self.second_spinbox.value()
        if self.multi_button.isChecked():
            z=x*y
        elif self.divide_button.isChecked():
            z=x/y
        self.multiplication_spinbox.setValue(z)


if __name__ == "__main__":
    app = QApplication([])
    window = Calculation_window()
    window.show()
    app.exec()

