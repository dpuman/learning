
from pathlib import Path

# Path("c:\\Program File\\Microsoft")
# Path(r"c:\Program File\Microsoft")
# Path()
# Path()/Path(r"ecommerce\__init__.py")
# Path()/"ecommerce"/"__init.py"

# Path.home()
path = Path(r"ecommerce\__init__.py")
path.exists()
path.is_file()
path.is_dir()
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)

# path = path.with_name("file.txt")
# print(path)

print(path.absolute())
path = path.with_suffix(".txt")
print(path)
