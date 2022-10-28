#!/usr/bin/env python

import sys
import getpass
from cryptography.fernet import Fernet
from passlib.hash import sha256_crypt

password = sha256_crypt.encrypt("password")
password2 = sha256_crypt.encrypt("password")

print(password)
print(password2)

print(sha256_crypt.verify("password", password))

sys.exit('aaaaaaaaaaa')




password = ''
try:
    password = getpass.getpass(prompt='password needed for encrypted file:')
except Exception as error:
    print('ERROR', error)

f = Fernet(password)

original_file = open('etc/credentials.yml', 'rb')
original_file_content = original_file.read()
original_file.close()

encrypted_file_content = f.encrypt(original_file_content)

encrypted_file = open('etc/credentials.yml.enc', 'wb')
encrypted_file.write(encrypted_file_content)
encrypted_file.close()

sys.exit('aaaaaaaaaaa')
