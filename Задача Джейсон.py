import json

f=open(r'C:\Users\777\Downloads\group_people.json')
l=(json.load(f))
n=0
for i in l:
    num=i['id_group']
    year=i['people']
    year.append(num)
    for j in year:
        try:
            if j['gender']=='Female' and j['year']>=1977:
                n=n+1
        except:
            print(j,n)
            n=0

f.close()