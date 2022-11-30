import re

sample = open('sample.txt','r',encoding='UTF-8') #サンプルテキスト読み込み
letter = sample.read()

ans = re.sub(r"[^a-zA-Z]", " ", letter) #置換処理
print(ans)
out = open('output.txt', mode='w') #ファイル出力
out.write(ans)
out.close()
