import os
import mytools

if not os.path.exists("data"):
    os.makedirs("data")

file_name = "data/workouts.json"


while True:
    print("\n--- МЕНЮ ---")
    print("1 - добавить тренировку")
    print("2 - показать все")
    print("3 - общее время")
    print("0 - выход")
    
    cmd = mytools.ask_text("Выбери действие: ")
    
    if cmd == "1":
        print("--- Новая тренировка ---")
        w_type = mytools.ask_text("Тип тренировки (бег, зал и т.д.): ")
        mins = mytools.ask_number("Сколько минут длилась? ")
        
        workout = {"type": w_type, "minutes": mins}
        
        old_data = mytools.load_json(file_name)
        old_data.append(workout)
        mytools.save_json(file_name, old_data)
        print("Тренировка сохранена")
        
    elif cmd == "2":
        print("--- Все тренировки ---")
        data = mytools.load_json(file_name)
        
        if len(data) == 0:
            print("Пока пусто.")
        else:
            for w in data:
                print(w["type"], "-", w["minutes"], "минут")
                
    elif cmd == "3":
        print("--- Общее время ---")
        data = mytools.load_json(file_name)
        total_time = 0
        
        for w in data:
            total_time = total_time + w["minutes"]
            
        print("Я потренировался в сумме на", total_time, "минут. (какой я молодец)")
        
    elif cmd == "0":
        print("Иду тренироваться")
        break
        
    else:
        print("Ошибка, нет такого пункта.")

