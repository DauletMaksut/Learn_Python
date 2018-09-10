import re
import socket
#unicode and string is the same thing in python 3

#Just trained
x = "there should be aby text 23 give some numbers 42 213 8827312"
y = re.findall('[0-9]+', x)
print (y)

print(~8)
num = [0] * 2
num[0] = 2
num[1] = 3
print(num)

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
mysock.close()
#mysock.send(message.edcode())
#mysock.recv
#
t = True
f = False
n = None
print(ord('\n'))
print(t)
print(f)
print(n)

print(ord(' '))
