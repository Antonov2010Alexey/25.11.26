# app_v2.py
kol = 0

while True:
    print("\nУчёт книг v2")
    print("1 — Выдать книгу")
    print("2 — Показать количество выданных книг")
    print("3 — Сбросить счётчик")
    print("4 — Вернуть книгу")
    print("0 — Выход")

    kom = input("Введите команду: ")

    if kom == "1":
        kol += 1
        print("Книга выдана")
    elif kom == "2":
        print("Выдано книг:", kol)
    elif kom == "3":
        kol = 0
        print("Счётчик сброшен до 0")
    elif kom == "4":
        if kol > 0:
            kol -= 1
            print("Книга возвращена")
        else:
            print("Нет выданных книг")
    elif kom == "0":
        print("Выход из программы")
        break
    else:
        print("Команда не найдена, вводить можно только цифры от 0 до 3")
