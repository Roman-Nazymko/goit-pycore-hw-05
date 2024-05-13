from decimal import Decimal
import re
from typing import Callable

def generator_numbers(text: str):
    # Використання регулярного виразу для знаходження всіх дійсних чисел у тексті
    pattern = r"\b\d+\.\d+\b"
    return re.findall(pattern, text)


def sum_profit(text: str, func: Callable):
    # Отримати числа з тексту
    numbers = func(text)
    
    # Перетворити список рядків у список Decimal
    numbers = map(Decimal, numbers)

    # Обчислення загальної суми чисел
    total = sum(numbers)
    return total

# Приклад використання
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")