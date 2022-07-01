import os
import random
import time
import shutil

path = r'C:\Users\Hery\Desktop\My Projects\Python-Web-Hacking-and-Security\Test-Trojan'

folder_list = os.listdir(path)

print(folder_list)

result_folder = []
result_file = []


for fd in folder_list:
    check = fd.split('.')
    if len(check) > 1:
        # print('File:', fd)
        result_file.append(fd)
    else:
        # print('Folder:', fd)
        result_folder.append(fd)

print('FD:', result_folder)
print('FL:', result_file)


# initialize
file_dict = {}

for f in result_file:
    select = random.choice(result_folder)
    folder_path = os.path.join(path, select)
    file_path = os.path.join(folder_path, f)
    current = os.path.join(path, f)
    # print(current, '------>', file_path)
    file_dict[f] = {'current': current, 'next': file_path}

for fk, fv in file_dict.items():
    current = fv['current']
    next_path = fv['next']
