# Задача 4. Вариант 6.
# Напишите программу, которая выводит имя, под которым скрывается София Шиколоне. Дополнительно необходимо вывести область интересов указанной личности, место рождения, годы рождения и смерти (если человек умер), вычислить возраст на данный момент (или момент смерти). Для хранения всех необходимых данных требуется использовать переменные. После вывода информации программа должна дожидаться пока пользователь нажмет Enter для выхода.

# Ivanov S. E.
# 19.09.2016


NAME = "София Шиколоне"
PSEUDONYM = "Софи Лорен"
BIRTH_PLACE = "Рим, Королевтсво Италия"
BIRTH_DATA = "20 сентября 1934"
AGE = "81"
AREA_OF_INTEREST = "актриса, певица"

print("{} более известна, как {}".format(NAME, PSEUDONYM))
print("Место рождения: {}".format(BIRTH_PLACE))
print("Год рождения: {}".format(BIRTH_DATA))
print("Возраст: {}".format(AGE))
print("Область интересов: {}".format(AREA_OF_INTEREST))

input("\nНажмите Enter для выхода.")