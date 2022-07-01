import os
import random
import time
import shutil

path = r'C:\Users\Hery\Desktop\My Projects\Python-Web-Hacking-and-Security\Test-Trojan'


file = os.path.join(path,'homework.docx')

file_name = 'homework2.docx'
for i in range(3,10):
    copyfile = os.path.join(path,file_name)
    shutil.copyfile(file,copyfile)
    file_name = 'homework{}.docx'.format(i)
    time.sleep(3)