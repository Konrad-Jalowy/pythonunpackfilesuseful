from zipfile import ZipFile
import os

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
file_name = 'zipfolder'
with ZipFile(file_name, 'r') as zip:
    print(zip.namelist())
    zip.printdir()
    zip.extractall(path=path)
path = os.path.realpath(path)
os.startfile(path)


