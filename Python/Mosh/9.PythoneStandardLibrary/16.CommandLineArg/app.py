import sys

print(sys.argv)

if len(sys.argv) == 1:
    print("USAGE: py3 App <pass>")

else:
    password = sys.argv[1]
    print(password)
