def mul(*numbers):
    num = 1
    for i in numbers:
        num *= i
    return num


def display(**students):
    print(students)


display(name="dipu", roll=1075, sec="A")

print(mul(1, 2, 3, 4, 5,))
