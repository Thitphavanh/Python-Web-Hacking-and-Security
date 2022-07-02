from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)

# Object fernet
f = Fernet(key)

text = 'ສະບາຍດີເຈົ້າ ນີ້ແມ່ນຂໍ້ຄວາມຈາກເຫີຍ'
message = f.encrypt(text.encode('utf-8'))

print('-------------Encrypt-------------')
print(message.decode('utf-8'))
print('---------------------------------')
