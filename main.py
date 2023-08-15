import sys
from pathlib import Path
from zipfile import ZipFile
import os
print(sys.argv[1])
print(Path(sys.argv[1]))
print(os.path.basename(Path(sys.argv[1])))
print(os.path.join("./", os.path.basename(Path(sys.argv[1]))))
input("Gotowy do akcji")
file_given = os.path.join("./", os.path.basename(Path(sys.argv[1]).rename(Path(sys.argv[1]).with_suffix('.zip'))))
file_name = file_given
# file_name = file_given.rename(file_given.with_suffix('.zip'))
# p = Path(file_given)
# print(file_given)
# print("converting to .zip")
# print(p)
# file_name = p.rename(p.with_suffix('.zip'))
# file_name = os.path.join("./", file_name)
input(file_name)
path = "./unpacked"
cnt = 1
while os.path.exists(path):
    if path[-3].isnumeric():
        path = path[:-3]
    if path[-2].isnumeric():
        path = path[:-2]
    if path[-1].isnumeric():
        path = path[:-1]
    path = path + str(cnt)
    cnt += 1
os.mkdir(path)

with ZipFile(file_name, 'r') as zip:
    print(zip.namelist())
    zip.extractall(path=path)
path = os.path.realpath(path)
os.startfile(path)
input()
