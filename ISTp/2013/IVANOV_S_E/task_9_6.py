# Задача 9. Вариант 6.
# Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен его отгадать. Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток узнать, есть ли какая-либо буква в слове, причем программа может отвечать только "Да" и "Нет". Вслед за тем игрок должен попробовать отгадать слово.

# Ivanov S. E.
# 23.09.2016


import random


WORDS = ("питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник")

correct = random.choice(WORDS)

print("Загаданное слово состоит из ", len(correct), " букв.")

for try_count in range(0, 5):
    char = ""
    while not char and len(char) != 1:
        char = input("Введите букву: ")
    if char and char in correct:
        print("Эта буква есть в слове")
    else:
        print("Такой буквы в слове нет")
    print()
else:
    if input("Введите слово: ") == correct:
        print("Правильный ответ!!!")
    else:
        print("Вы проиграли!\nПравильное слово: ", correct)

input("\nНажмите Enter для выхода.")