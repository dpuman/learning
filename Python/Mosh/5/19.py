num = {11, 11, 2, 3, 4, 5}
num2 = {6, 11, 2, 7, 8, 9}
num2 = set(num2)

print(num)
# UNION
print(num | num2)
# IN BOTH
print(num & num2)
# Diffenent
print(num-num2)
# Unique from both
print(num ^ num2)
