
import os

f = open("category.txt",'r')

lines = ''
while True:
    line = f.readline()
    lines += line
    lines += '\n'
    if not line: break
    print(line)
print(lines)
f.close
