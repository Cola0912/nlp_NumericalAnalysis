f = open('sample.txt', 'r', encoding='UTF-8')

data = f.read()
print(data)
print(data.count('の'))

f.close()