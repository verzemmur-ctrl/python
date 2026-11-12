import os
import mytools

path = os.environ.get("EXPENSES_PATH", "data/expenses.json")

while True:
    print("\n--- МЕНЮ ---")
    print("1 - добавить расход")
    print("2 - показать все")
    print("3 - сумма по категории")
    print("0 - выход")
    
    choice = mytools.ask_text("Выбери цифру: ")
    
    if choice == "1":
        print("Добавляем новый расход...")
        amount = mytools.ask_number("Сколько потратил? ")
        category = mytools.ask_text("На что потратил (категория)? ")
        date = mytools.today()
        
        new_expense = {"amount": amount, "category": category, "date": date}
        
        data = mytools.load_json(path)
        
        data.append(new_expense)
        
        mytools.save_json(path, data)
        print("Успешно сохранилось.")
        
    elif choice == "2":
        print("\nВсе мои расходы:")
        data = mytools.load_json(path)
        
        if len(data) == 0:
            print("Пока пусто, ничего не потрачено.")
        else:
            
            for item in data:
                money = mytools.format_money(item["amount"])
                print(item["date"], "|", item["category"], "|", money)
                
    elif choice == "3":
        print("\nСчитаем по категории...")
        data = mytools.load_json(path)
        
        if len(data) == 0:
            print("Нет данных для подсчета.")
        else:
            cat_to_find = mytools.ask_text("Какую категорию посчитать? ")
            total = 0
            for item in data:
                if item["category"] == cat_to_find:
                    total = total + item["amount"]
            
            print("Итого по категории:", mytools.format_money(total))
            
    elif choice == "0":
        print("Закрываю калькулятор.")
        break
    else:
        print("Нет такой цифры в меню. Попробуй еще раз.")
