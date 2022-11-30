import collections

sample = open('sample.txt','r',encoding='UTF-8')
letter = sample.read()
all = len(letter)

out = [[0 for j in range(3)] for i in range(26)]
txtcount = collections.Counter(letter)
i=0
code = 0x61

while i < 26:
	out[i][0]=str(chr(code))
	out[i][1]=txtcount[chr(code)]
	out[i][2]=str(txtcount[chr(code)]/all*100) + "%"
	code +=1
	i +=1

out.sort(key=lambda x:x[1])
out = reversed(out)
print("word Counter:", end="")
print(all)
print(*out,sep='\n')


sample.close()