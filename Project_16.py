def check_num(a, n):
    if a % n == 0:
        print(f"Число {n} является делителем числа {a}")
        print(f"Ответ: {a/n}""\n")
    else:
        print(f"Число {n} не является делителем числа {a}")
        print(f"Остаток: {a%n}""\n")


check_num(4, 2)
check_num(5, 2)
check_num(6, 2)
check_num(8, 3)
check_num(100, 50)
check_num(333, 3)
check_num(345, 4)

