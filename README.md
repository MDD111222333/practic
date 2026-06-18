# Система учёта заказов «Быстрая доставка»

## Как запустить
1. Установите зависимости (для тестов): `pip install -r requirements.txt`
2. GUI-режим: `python main_gui.py`
3. CLI-режим: 
   - Отчёт: `python main_cli.py report --period month`
   - Экспорт: `python main_cli.py export --file orders.json`
   - Импорт: `python main_cli.py import --file orders.json`
4. Тесты: `pytest`
