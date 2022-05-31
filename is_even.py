from token import NOTEQUAL


def is_even(n):
    if n % 3 == 1:
        return "False"
    else:
        return "True"
number = int (input("Please enter an integer: "))
print (is_even(number))
    