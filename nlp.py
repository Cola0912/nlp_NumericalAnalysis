f = open('sample.txt', 'r', encoding='UTF-8')

date = f.read()
print(date)
print(date.count('の'))

f.close()