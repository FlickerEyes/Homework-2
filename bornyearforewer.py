answer = ""
while not answer.isdigit():
    answer = input("Какой год рождения А.С. Пушкина? - ")

answer = int(answer)

while answer != "1799":
    answer = input("Какой год рождения А.С. Пушкина? - ")
print ("Все верно!")
