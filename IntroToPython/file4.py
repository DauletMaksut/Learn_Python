#Give notification of important lecture
x = 5
if x > 2:
	print('it is easy')
print('i will be printed')
#Got indentation error
#	print('Will i?')

# if, else if, else
if x > 5:
	print('more 5')
elif x == 4:
	print('it is 4')
else:
	print('This is my goal')
print('End of the process')

# try - except
blow = 'this is error'
try:
	blow = int(blow)
except:
	blow = -1
print('Must be', blow)

#Functions
def func():
	print('I am laerning, do not kill me')

func()

# Is it take only numbers in string
tmp = ' 123 lolk'
try:
	tmp = int(tmp)
except:
	tmp = -1
print('Is it worked', tmp)


# Type comparision
print(type(tmp))
tmp = 'this is string'
if type(tmp)is str:
	print('Really?')

# Function with argument/s not so different

#while loops
i = 10
while i > 0:
	print('Is', i)
	i-=1
print('it is easy')

#is space plays role in comparison
var1 = ' daulet '
var2 = 'daulet'
if var2 == var1:
	print('Space does not effect in double comparison')
else:
	print('Space effect in double comparison')

# for x in somethinf works as dolist in lisp












