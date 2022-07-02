from cryptography.fernet import Fernet

# Object fernet
f = Fernet(b'VHbxhdtPkEYZnBxFiiqMUB5-FjVXhyJ16tMaK8hHpcc=')

text = 'gAAAAABiv8cF1VthoK-lS1tsZIvzFqdmrFzTaDzJfbvumr-Qww-PYAcMEovmc4v2PEa61MoQT1rEkCjKxXrYrtjmLFWGQV-FungHxIwjVcT8-A_Ii0ATvIOzA0WN5GEqqxwiQu1Op6sI6JM64OlpjaARi7AhPxFVs8Ru5SeY02YTZ1FdzgkS-ZSDeGefNDGuIa_hKmDU5-tAqJo3gOded9y8-BEbpE1Olg=='

text_convert = text.encode('utf-8')
print(text_convert)

text_decrypt = f.decrypt(text_convert)
print(text_decrypt.decode('utf-8'))