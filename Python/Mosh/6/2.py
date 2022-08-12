try:
    with open('./app.txt') as file:
        pass
    x = int(input("Enter"))
    result = x / 10
except (ValueError, ZeroDivisionError):
    print("You did not enter valid age")
except FileNotFoundError as f:
    print(f)
    print(type(f))
else:
    print("Okay")
finally:
    # file.close()
    print("finally")
