import json
import os
from datetime import date

def ask_number(prompt) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: пожалуйста, введите корректное число.")

def ask_text(prompt) -> str:
    """Спрашивает непустую строку, повторяет при ошибке."""
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("Ошибка: строка не может быть пустой. Попробуйте снова.")

def format_money(x) -> str:
    rounded_x = round(float(x), 2)
    formatted = f"{rounded_x:,.2f}" 
    formatted = formatted.replace(",", " ").replace(".", ",")
    return f"{formatted} ₽"

def today() -> str:
    return date.today().isoformat()

def load_json(path) -> list:
    if not os.path.exists(path):
        return []
    
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, IOError):
        return []

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
