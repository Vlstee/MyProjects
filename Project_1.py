def my_fun(a, b):
    a = (a + 4)
    b = (b / 2)
    c = a + b
    return c


num_one = 3
num_two = 2

res = my_fun(num_one, num_two)
print(res)
print(num_one)
print(num_two)

cow = id(num_one)
print(cow)
riw = (num_one == 3)
print(riw)

ciw = id(num_two)
print(ciw)
cir = (num_two == 2)
print(cir)
