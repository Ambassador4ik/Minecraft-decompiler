from shutil import copy
import decompiler
import os.path
import time

path = input()
filenames = next(os.walk(path), (None, None, []))[2]
filecount = len(filenames)

for i in range(filecount):
    ext = os.path.splitext(filenames[i])
    extension = ext[1]
    if extension != '.java':
        filenames[i] = '0'

try:
    os.mkdir(path + '\output')
except FileExistsError:
    pass

for i in range(filecount):
    if filenames[i] != '0':
        directory = path + '\output\\' + filenames[i]
        copy((path + '\\' + filenames[i]), (path + '\output'))
        try:
            decompiler.decompile(directory)
        except UnicodeDecodeError:
            print('Failed do read class file')
            pass

print('Time elapsed:', time.perf_counter())
