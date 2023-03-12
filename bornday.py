answer = int(input("Какой год рождения А.С. Пушкина? - "))
if answer < 1799:
    print("неверно")
elif answer > 1799:
    print("Неверный год рождения")
else:
    day = (input("Напишите точную дату - "))
    if day == "06.06.1799":
        print("Верно")
    else:
        print("Неверный день рождения")

