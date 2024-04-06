import random
spisok = ["Камень", "Ножницы", "Бумага"]
print("""Выберите фигуру: 
1 - Камень 
2 - Бумага 
3 - Ножницы 
Ваш выбор:""")
user = int(input())
pc = random.choice(spisok)
if user in [1, 2, 3]:
    if (user == 1 and pc == "Ножницы") or (user == 2 and pc == "Камень") or (user == 3 and pc == "Бумага"):
        print("Вы победили!")
    elif (user == 1 and pc == "Камень") or (user == 2 and pc == "Бумага") or (user == 3 and pc == "Ножницы"):
        print("Ничья!")
    else:
        print("Вы проиграли!")
    print("Ваш соперник выбрал:")
    print(pc)
else:
    print("Не катайтесь лицом по клаве, а выберите цифру от 1 до 3")
