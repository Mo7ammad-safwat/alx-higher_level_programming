#!/usr/bin/python3
def uppercase(s):
    for char in s:
        uppercase_char = chr(ord(char) - ord('a') + ord('A'))
        print(uppercase_char, end='')
    else:
        print(char, end='')
