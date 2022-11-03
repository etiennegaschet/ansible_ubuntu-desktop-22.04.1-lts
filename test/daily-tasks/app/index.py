#!/usr/bin/env python

import sys
from lib import config 

print('')
print('# ########################')
print('# daily-tasks')
print('# ########################')
print('')

CONFIG = {}

value = input("password for encrypted config:\n")

# print(f'You entered {value}')

f = Fernet(value)

with open('grades.csv', 'rb') as original_file:
    original = original_file.read()

encrypted = f.encrypt(original)

with open ('enc_grades.csv', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)



sys.exit('aaaaaaaaaaa')


















sYamlConfigFile = 'etc/config.yml'
CONFIG = config.load(CONFIG, sYamlConfigFile)

print('  -> ok')

print('# ########################')
print(CONFIG['tasks'])
print('# ########################')

sys.exit('OK')


print('- loading ' + sYamlTasksFile + '...')

with open(sYamlTasksFile, "r") as stream:
    try:
        sYamlTasks = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
        sys.exit('Error when tryin to parse tasks config file: ' + sYamlTasksFile)

nbTasks = len(sYamlTasks['tasks']);
print(f'  -> {nbTasks} task(s) to treat.')

print('')

print('Hello, world!')
