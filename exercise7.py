def exercise(*args, **kwargs):
    for argument in args:
        print(argument)
    for key, value in kwargs.items():
        print(f"key = {key}, value = {value}")

exercise(5, 10, stud_nbr="12345", mod_code="SWW1")