a = 5


def my_fn():
    def inner_fn():
        global b
        b = 1
        print(a + b + 2, 'inside the function')
    inner_fn()


my_fn()

print(a + b)
