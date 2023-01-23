def print_number_info(num):
    if (num % 2) == 0:
        print("Enter number is even")
    else:
        print("Enter number is odd")


def print_squere_num(num):
    print("Squre of the num is", num ** 2)


def process_number(num, callback_fn):
    callback_fn(num)


entered_num = int(input('Enter any number'))

process_number(entered_num, print_number_info)
process_number(entered_num, print_squere_num)
