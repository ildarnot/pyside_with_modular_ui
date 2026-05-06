#!/bin/bash
# Данный код запускает конвертирование из ui в py, дополнительно - он добавляет возможность ставить в DoubleSpinBox и "," , и "." 
# Запускать в терминале bash по команде (переходим в нужную директорию в bash): cd "C:\Users\NotfullinIF\Develop\single_window\pyside_with_modular_ui\userforms" 
# И следующая команда: "./convert_ui_to_py_with_replace.sh" 
# На данный момент в скрипте прописана конвертация файлов: main_single_window_test.ui, gearing_selector.ui, gears_strenght_calculator_userform.ui

# Путь к исходному ui-файлу и выходному py-файлу main_single_window_test
UI_FILE0="main_single_window_test.ui"
PY_FILE0="main_single_window_test.py"
# Генерация py-кода из ui-файла
pyside6-uic "$UI_FILE0" -o "$PY_FILE0"
# Добавляем строку после всех строк import
sed -i '/^import resources_rc/a \
\n\
class CustomDoubleSpinbox(QDoubleSpinBox):\n\    def validate(self, text: str, pos: int) -> tuple[int, str, int]:\n\        text = text.replace(".", ",")\n\        return super().validate(text, pos)\n\    def valueFromText(self, text: str) -> float:\n\        text = text.replace(",", ".")\n\        return float(text)\n\    \n\QDoubleSpinBox=CustomDoubleSpinbox # Ваш дополнительный код здесь!' "$PY_FILE0"
echo "1. Преобразование |Главное окно (одиночное)| main_single_window_test.ui успешно выполнено!"
