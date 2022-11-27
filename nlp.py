f = open('sample.txt', 'r', encoding='UTF-8')

data = f.read()
print(data,'\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
print('の	',data.count('の'))
print('ののの	',data.count('ののの'))
print('!	',data.count('!'))
print('2	',data.count('2'))
print('sc	',data.count('sc'))
print('&	',data.count('&'))


f.close()