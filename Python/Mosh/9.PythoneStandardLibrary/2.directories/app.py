from pathlib import Path

path = Path('ecommerce')
# path.mkdir()
print(path.exists())

# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("Newname")

# directions = path.iterdir()
print(path)

# for p in path.iterdir():
#     print(p)

# paths = [p for p in path.iterdir()]
# print(paths)

# paths = [p for p in path.iterdir() if p.is_dir()]
# print(paths)
# pyfiles = [p for p in path.glob("*.py")]
pyfiles = [p for p in path.rglob("*.py")]
print(pyfiles)
