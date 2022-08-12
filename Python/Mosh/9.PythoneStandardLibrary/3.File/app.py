from pathlib import Path
from time import ctime
import shutil
path = Path("3.File\\ecommerce\\__init__.py")
# path.exists()
# path.rename("New")
# path.unlink()

# print(path.stat())
# print(ctime(path.stat().st_ctime))
# print(path.read_bytes())
# print(path.read_text())

source = Path("3.File\\ecommerce\\__init__.py")
print(Path())
target = Path()/"__init__.py"

print(target.exists())

# target.write_text(source.read_text())

shutil.copy(source, target)
