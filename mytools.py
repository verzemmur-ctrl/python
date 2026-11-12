import json
import os
from datetime import date


def load_json(path):
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        return []
    if not isinstance(data, list):
        return []
    return data


def save_json(path, data):
    folder = os.path.dirname(path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def ask_number(prompt):
    while True:
        raw = input(prompt).strip().replace(",", ".")
        try:
            return float(raw)
        except ValueError:
            print("Это не число. Попробуйте ещё раз.")


def ask_text(prompt):
    while True:
        raw = input(prompt).strip()
        if raw:
            return raw
        print("Пустой ввод. Попробуйте ещё раз.")


def format_money(x):
    return f"{x:,.2f} ₽".replace(",", " ")


def today():
    return date.today().isoformat()


if __name__ == "__main__":
    test_path = "test_mytools.json"

    save_json(test_path, [{"a": 1}, {"b": 2}])
    loaded = load_json(test_path)
    assert loaded == [{"a": 1}, {"b": 2}], "save/load не совпадают"
    print("load_json / save_json: OK")

    assert load_json("no_such_file.json") == [], "нет файла -> должен быть []"
    print("load_json (нет файла): OK")

    assert format_money(1234.5) == "1 234.50 ₽", format_money(1234.5)
    print("format_money: OK")

    print("today:", today())
    print("Все проверки пройдены.")
