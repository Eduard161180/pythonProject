def power_number(*numbers, power=3):
    return [num ** power for num in numbers]


print(power_number(1, 2, 3, 4, 5))

print("")
print("----------------------------------")


numbers = [1, 2, 4, 5, 7, 8, 10, 11]

# функция, которая проверяет числа
numbers = [1, 2, 4, 5, 7, 8, 10, 11]


# функция, которая проверяет числа
def filter_odd_num(in_num):
    if (in_num % 2) == 0:
        return True
    else:
        return False


# Применение filter() для удаления нечетных чисел
out_filter = filter(filter_odd_num, numbers)

print("Четные: ", list(out_filter))


def filter_odd_num(in_num):
    if (in_num % 2) > 0:
        return True
    else:
        return False


# Применение filter() для удаления четных чисел
out_filter = filter(filter_odd_num, numbers)

print("Нечетные: ", list(out_filter))


def filter_odd_num(in_num):
    for x in range(2, in_num):
        if in_num % x == 0:
            return False
        else:
            return True


# Применение filter() для определения простых чисел
out_filter = filter(filter_odd_num, numbers)

print("Простые: ", list(out_filter))


# -------------------------------

def ODD(x):
    if x % 2 == 0:
        return True
    else:
        return False


def print_filter_items(my_filter):
    for item in my_filter:
        print(item, end=' ')
    print()


# l1 = [1, 2, 3, 4, 5,6,7,8,9]
# fl = filter(ODD, l1)
# print_filter_items(fl)

def EVER(x):
    if x % 2 == 0:
        return False
    else:
        return True


def print_filter_items(my_filter):
    for item in my_filter:
        print(item, end=' ')
    print()


# l1 = [1, 2, 3, 4, 5,6,7,8,9]
# fl = filter(EVER, l1)
# print_filter_items(fl)


def PRIME(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
        else:
            return True


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
fl = filter(PRIME, l1)
print_filter_items(fl)