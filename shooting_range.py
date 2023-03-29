def check_numbers(total, number):
    if 73 <= total <= 87 and 1 <= number <= 8:
        if count_87(total, number):
            return True
    return False


def count_87(total, number):
    total = total - (7 + 8) - 9 * number
    if total < 0:
        return False

    len_total = 8 - number
    count_8 = 1

    if number == 8:
        return count_8

    if total / len_total >= 7:
        for _ in range(len_total):
            check = total / len_total

            if check >= 8:
                count_8 += 1
                total -= 8
            else:
                total -= 7
            len_total -= 1
        return count_8

    return False


sum_numbers = int(input('Введите сумму очков: '))
number_9 = int(input('Кол-во попаданий в 9: '))

if check_numbers(sum_numbers, number_9):
    number_8 = count_87(sum_numbers, number_9)
    len_numbers = 10 - number_9

    for num in range(1, len_numbers):
        if num <= number_8:
            print(f'{"9 " * number_9}{"8 " * num}{"7 " * (len_numbers - num)}')

else:
    print('Некорректно указаны значения.')
