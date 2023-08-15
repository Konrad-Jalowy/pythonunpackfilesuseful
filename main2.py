import sys
from pathlib import Path
import os
from zipfile import ZipFile

print(sys.argv[1])
print(Path(sys.argv[1]))
input("Gotowy do akcji")
withextension = sys.argv[1] + ".zip"
os.replace(Path(sys.argv[1]), withextension)
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

file_name = withextension
with ZipFile(file_name, 'r') as zip:
    print(zip.namelist())
    zip.printdir()
    zip.extractall(path=path)
path = os.path.realpath(path)
os.startfile(path)
