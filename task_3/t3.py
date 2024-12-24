# Завдання 3 (не обов'язкове)

# Розробіть Python-скрипт для аналізу файлів логів. 
# Скрипт повинен вміти читати лог-файл, переданий як аргумент командного рядка,
# і виводити статистику за рівнями логування наприклад, INFO, ERROR, DEBUG.
# Також користувач може вказати рівень логування як другий аргумент командного рядка,
# щоб отримати всі записи цього рівня.

# Вимоги до завдання:

# 1. Скрипт повинен приймати шлях до файлу логів як аргумент командного рядка.
#    Скрипт повинен приймати не обов'язковий аргумент командного рядка, після аргументу шляху до файлу логів.
#    Він відповідає за виведення всіх записів певного рівня логування. 
#    І приймає значення відповідно до рівня логування файлу. 
#    Наприклад аргумент error виведе всі записи рівня ERROR з файлу логів.
# 2. Скрипт має зчитувати і аналізувати лог-файл, підраховуючи кількість записів
#    для кожного рівня логування (INFO, ERROR, DEBUG, WARNING).
# 3. Реалізуйте функцію parse_log_line(line: str) -> dict для парсингу рядків логу.
# 4. Реалізуйте функцію load_logs(file_path: str) -> list для завантаження логів з файлу.
# 5. Реалізуйте функцію filter_logs_by_level(logs: list, level: str) -> list для фільтрації логів за рівнем.
# 6. Реалізуйте функцію count_logs_by_level(logs: list) -> dict для підрахунку записів за рівнем логування.
# 7. Результати мають бути представлені у вигляді таблиці з кількістю записів для кожного рівня.
#    Для цього реалізуйте функцію display_log_counts(counts: dict),яка форматує та виводить результати. 
#    Вона приймає результати виконання функції count_logs_by_level.

import sys
import re
from typing import List, Dict

# Функція для парсингу рядків логу
def parse_log_line(line: str) -> Dict[str, str]:
    parts = line.split(" ", 3)
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "message": parts[3]
    }

# Функція для завантаження логів з файлу
def load_logs(file_path: str) -> List[Dict[str, str]]:
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                logs.append(parse_log_line(line.strip()))
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
        sys.exit(1)
    return logs

# Функція для фільтрації логів за рівнем
def filter_logs_by_level(logs: List[Dict[str, str]], level: str) -> List[Dict[str, str]]:
    return [log for log in logs if log["level"] == level.upper()]

# Функція для підрахунку записів за рівнем логування
def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    counts = {"INFO": 0, "ERROR": 0, "DEBUG": 0, "WARNING": 0}
    for log in logs:
        if log["level"] in counts:
            counts[log["level"]] += 1
    return counts

# Функція для виведення результатів підрахунку
def display_log_counts(counts: Dict[str, int]):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<15} | {count:<8}")

# Головна функція
def main():
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до файлу логів.")
        sys.exit(1)

    file_path = sys.argv[1]
    logs = load_logs(file_path)

    if len(sys.argv) == 3:
        level = sys.argv[2].upper()
        filtered_logs = filter_logs_by_level(logs, level)
        if filtered_logs:
            print(f"Деталі логів для рівня '{level}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print(f"Логів для рівня '{level}' не знайдено.")
    else:
        counts = count_logs_by_level(logs)
        display_log_counts(counts)

if __name__ == "__main__":
    main()
