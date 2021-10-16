f=open(r'C:\Users\777\Downloads\numbers.txt')
d,s=[],[]
for i in f:
    i=str(i)
    if len(i)==4:
        d.append(i)
    if len(i)==3:
        s.append(int(i))
print(len(d))
print(sum(s))
f.close()