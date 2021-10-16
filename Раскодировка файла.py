import json

j=open(r'C:\Users\777\Downloads\Alphabet.json')
t=open(r'C:\Users\777\Downloads\Abracadabra.txt',encoding='utf-8')
js=json.load(j)
tx=t.read()
n=0
g=[]
for i in tx:
    g.append(js.get(i,i))
s=''.join(g)
print(s)




j.close()
t.close()