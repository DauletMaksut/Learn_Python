print ('Hello to my world')
getthat = input('Do you want to try?')
print (getthat)
print (type(getthat))
print('Count how many words you wrote')
name = input('Enter the name of file::: ')
file = open(name, 'r')
totalWordCount = 0
count = dict()
for line in file:
	words = line.split()
	for word in words:
		totalWordCount+=1
		count[word] = count.get(word,0) + 1
print(totalWordCount)
status = input('Do yon want to know pattern of word y/n?')
if status == 'y':
	print(count)
