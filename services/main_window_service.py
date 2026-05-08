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

# Импортируем преобразованный виджет
from services.selection_window_service import Selection_window
from services.calculation_window_service import Calculation_window
from services.added_calculation_window_service import Added_calculation_window

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

        self.home_pg_btn.clicked.connect(
            lambda: self.stackedWidget_2.setCurrentIndex(0)
        )
        self.gearing_selection_btn.clicked.connect(
            lambda: self.stackedWidget_2.setCurrentIndex(1)
        )
        self.gearing_calculation_btn.clicked.connect(
            lambda: self.stackedWidget_2.setCurrentIndex(2)
        )
        self.gear_calculation_btn.clicked.connect(
            lambda: self.stackedWidget_2.setCurrentIndex(3)
        )

        self.gearing_selection_btn_2.clicked.connect(
            lambda: self.stackedWidget_2.setCurrentIndex(1)
        )
        self.gearing_calculation_btn_2.clicked.connect(
            lambda: self.stackedWidget_2.setCurrentIndex(2)
        )
        self.gear_calculation_btn_2.clicked.connect(
            lambda: self.stackedWidget_2.setCurrentIndex(3)
        )

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ Настройка импорта ui с другого самостоятельного окна ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓      
        # Создаём экземпляр Selection_window (с UI и логикой)
        self.selection_widget = Selection_window()
        # Берём его центральный виджет для встраивания в stackedWidget
        selection_central_widget = self.selection_widget.centralWidget()
        # Добавляем в stackedWidget на страницу с индексом 1
        self.stackedWidget_2.insertWidget(1, selection_central_widget)
# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ Настройка импорта ui с другого самостоятельного окна ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑


# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ Настройка импорта ui с другого самостоятельного окна calculation_window ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓      
        # Создаём экземпляр Selection_window (с UI и логикой)
        self.calculation_widget = Calculation_window()
        # Берём его центральный виджет для встраивания в stackedWidget
        calculation_central_widget = self.calculation_widget.centralWidget()
        # Добавляем в stackedWidget на страницу с индексом 1
        self.stackedWidget_2.insertWidget(2, calculation_central_widget)
# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ Настройка импорта ui с другого самостоятельного окна calculation_window ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ Настройка импорта ui с другого самостоятельного окна calculation_window ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓      
        # Создаём экземпляр Selection_window (с UI и логикой)
        self.added_calculation_widget = Added_calculation_window()
        # Берём его центральный виджет для встраивания в stackedWidget
        added_calculation_central_widget = self.added_calculation_widget.centralWidget()
        # Добавляем в stackedWidget на страницу с индексом 1
        self.stackedWidget_2.insertWidget(3, added_calculation_central_widget)
# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ Настройка импорта ui с другого самостоятельного окна calculation_window ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑


if __name__ == "__main__":
    app = QApplication([])
    window = Main_single_window()
    window.show()
    app.exec()
