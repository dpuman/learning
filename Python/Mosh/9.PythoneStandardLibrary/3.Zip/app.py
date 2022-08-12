from pathlib import Path

from zipfile import ZipFile

# with ZipFile("file.Zip", "w") as File:
#     for path in Path("ecommerce").rglob("*.*"):
#         File.write(path)

with ZipFile("./file.Zip") as File:
    print(File.namelist())
    info = File.getinfo("ecommerce/Shopping/sales.py")
    print(info.file_size)
    print(info.compress_size)
    File.extractall("extract")
