from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)

# Object fernet
f = Fernet(key)

text = 'ສະບາຍດີເຈົ້າ ນີ້ແມ່ນຂໍ້ຄວາມຈາກເຫີຍ'

with open('homework.docx', 'rb') as file:
    docfile = file.read()

message = f.encrypt(docfile)
print('-------------Encrypt-------------')
# print(message.decode('utf-8'))
print(message.decode('utf-8'))

with open('hacker23.xxx', 'w') as file:
    file.write(message.decode('utf-8'))

print('---------------------------------')
