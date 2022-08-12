def display(age):
    if age < 0:
        raise ValueError("Error")
    else:
        pass


try:
    display(-1)
except ValueError as e:
    print(e)
