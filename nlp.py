f = open('sample.txt', 'r', encoding='UTF-8')
pool = open('pool.txt', 'r', encoding='UTF-8')
path_w = 'output.txt'

data = f.read()
print(data,'\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
out = []
list1 = list(data)
print(list1)
list1.sort(key=len)

print('の	',data.count('の'))
out += str(data.count('の'))
print('ののの	',data.count('ののの'))
out += str(data.count('ののの'))
print('!	',data.count('!'))
print('2	',data.count('2'))
print('sc	',data.count('sc'))
print('&	',data.count('&'))

with open(path_w, mode='w') as f:
	f.write(data)
	f.write('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~5~\n')

	f.write('の	')
	f.writelines(out)
	f.write('\nののの	')
	f.writelines(out)
	


f.close()