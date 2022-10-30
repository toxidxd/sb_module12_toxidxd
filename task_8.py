print('Задача 8. НОД')
# Напишите функцию, вычисляющую наибольший общий делитель двух чисел


def gcd_finder(small_num, large_num):
    print('gcd_finder')
    if large_num % small_num != 0:
        remains = large_num % small_num
        new_large_num = small_num
        remains = gcd_finder(remains, new_large_num)
    else:
        remains = small_num

    return remains


f_num = int(input("Введите первое число: "))
s_num = int(input("Введите второе число: "))
gcd = 0

if f_num <= 0 or s_num <= 0:
    print("Числа должны быть положительными!")
else:
    max_num = int((f_num + s_num) / 2 + abs(f_num - s_num) / 2)
    min_num = int((f_num + s_num) / 2 - abs(f_num - s_num) / 2)

    if max_num % min_num == 0:
        gcd = min_num
    else:
        gcd = gcd_finder(min_num, max_num)

    print(f"НОД равен {gcd}")
