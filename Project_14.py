class Numb:
    def __init__(self,num1):
        print('Первое число')
        self.num1 = num1

    def __lt__(self, other):
        return self.num1 < other.num1


num1 = Numb(200)
num2 = Numb(3)

if num1 > num2:
    print('OK')
    print('__lt__ is run')

if num1.__lt__(num2):
    print('__lt__')