#Working with files
#Find it easy, move to list

#list is very similar to lisp list

#looking for dict similar to Map in Java but have syntacsis difference
exm = dict()
exm['daulet'] = 20
exm['Daulet'] = 20
print(exm)
exm['daulet'] = exm['daulet'] +20
print(exm)

exm1 = dict()
exm1 = {
	'no': 20,
	'yes': 12
}
print(exm1)

print('I am doing this again whaaaa')
text = input('Enter text please: ')
words = text.split()
print('Program counted:', len(words), 'words')

pattern = dict()
for word in words:
	pattern[word] = pattern.get(word, 0) + 1

print('And you word pattern is:')
print(pattern)