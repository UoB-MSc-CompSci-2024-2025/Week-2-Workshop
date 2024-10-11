def first_function(num1, num2, num3):
    print(num1, num2, num3)

def second_function(*args):
    first_function(*args)

second_function(1, 2, 3)