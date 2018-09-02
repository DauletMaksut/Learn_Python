#Related to tuples in python as it was said that it is important lecture
d = [
	('daulet', 12),
	('aktan', 4),
	('akmaral', 20)
	]

print(sorted(d))

for key, value in d:
	print('Name:', key, '  Age:', value)


print('if i store')

d = sorted(d)
for key, value in d:
	print('Name:', key, '  Age:', value)

print('Sort by value')


tmp = list()
for key, value in d:
	tmp.append((value, key))

print(sorted(tmp))
print(sorted(tmp, reverse = True))

print( sorted( [ (v, k ) for k ,v in d], reverse=True))
