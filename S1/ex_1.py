# 1.Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
print("Таблица умножения от 2х2 до 9х10")
factor = 2
number = 2
while (number < 10):
    if (factor <= 10):
        print(f"{number}x{factor} = {number * factor}")
        factor +=1
    else:
        print(" ")
        factor = 2
        number += 1
        continue
