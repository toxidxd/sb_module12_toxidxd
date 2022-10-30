import random

print('Задача 9. Недоделка')

# Вы пришли на работу в контору по разработке игр,
# целевая аудитория которых - дети и их родители.
# 
# У прошлого программиста было задание
# сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них.
# 
# Однако программист, на место которого вы пришл
# и, перед увольнением не успел сделать эту задачу и оставил только небольшой шаблон проекта.
# 
# Используя этот шаблон,
# реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
# 
# Правила игры «Камень, ножницы, бумага»:
# программа запрашивает у пользователя строку
# и выводит победил он или проиграл.
# 
# Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
# 
# Правила игры “Угадай число”:
# программа запрашивает у пользователя число до тех пор, пока он его не отгадает.


def rock_scissors_paper():
    pc_choice = random.randint(1, 3)  # 1 - rock  2 - scissors  3 - paper
    # есть и более аккуратный вариант со списками и random.choise, но мы его еще не проходили
    if pc_choice == 1:
        pc_choice = 'камень'
    elif pc_choice == 2:
        pc_choice = 'ножницы'
    elif pc_choice == 3:
        pc_choice = 'бумагу'

    user_choice = input("Камень, ножницы, бумага? ---> ")
    print(f"Компьютер выбрал {pc_choice}")

    if user_choice == 'камень':
        if pc_choice == 'бумагу':
            print('Вы проиграли =(')
        elif pc_choice == 'ножницы':
            print('Вы выиграли =)')
        else:
            print("Победила дружба!")

    if user_choice == 'ножницы':
        if pc_choice == 'камень':
            print('Вы проиграли =(')
        elif pc_choice == 'бумагу':
            print('Вы выиграли =)')
        else:
            print("Победила дружба!")

    if user_choice == 'бумага':
        if pc_choice == 'ножницы':
            print('Вы проиграли =(')
        elif pc_choice == 'камень':
            print('Вы выиграли =)')
        else:
            print("Победила дружба!")


def guess_the_number():
    taken_number = random.randint(1, 10)
    trying = 0

    while True:
        trying += 1
        number = int(input("Введите число от 1 до 10: "))

        if number > taken_number:
            print("Число больше, чем нужно. Попробуйте ещё раз!")
        elif number < taken_number:
            print("Число меньше, чем нужно. Попробуйте ещё раз!")
        elif number == taken_number:
            print(f"Вы угадали! Число попыток: {trying}")
            break


def main_menu():
    game_choice = int(input("Выберите игру:\n1 - Камень, ножницы, бумага\n2 - Угадай число\n---> "))
    if game_choice == 1:
        rock_scissors_paper()
    elif game_choice == 2:
        guess_the_number()
    else:
        print("Неверные ввод!")


main_menu()
