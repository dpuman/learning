from timeit import timeit
code1 = '''
def display(age):
    if age < 0:
        raise ValueError("Error")
    else:
        pass


try:
    display(-1)
except ValueError as e:
    print(e)
'''
code2 = '''
def display(age):
    if age < 0:
        return None
    else:
        pass


res=display(-1)
# print(res)
'''

print("first", timeit(code1, number=10000))
print("second", timeit(code2, number=10000))
