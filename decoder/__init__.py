import re

text = '''Hello there'''

for word in text.split():
    for c in list(word):
        if (c == ' '):
            print('   ',end='')
        else:
            print(chr(ord(c) + int('4e00',16)), end='')