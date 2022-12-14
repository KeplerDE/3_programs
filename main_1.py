import pyAesCrypt        # шифрование, дешифрование

# password = input("Введите пароль для шифрования: ")
# # password = "please-use-a-long-and-random-password"
# #encrypt
# pyAesCrypt.encryptFile("data.txt", "data.txt.aes", password)

# decrypt
pyAesCrypt.decryptFile("data.txt.aes", "dataout.txt", password)
