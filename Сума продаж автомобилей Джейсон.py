import json

f=open(r"C:\Users\777\Downloads\manager_sales.json")
m=(json.load(f))
sum=0
for i in m:
    name=i['manager']
    p=i['cars']
    p.append(name)
    for j in p:
        try:
            sum+=j['price']
            print(sum)
        except:
            print(j['first_name'],j['last_name'])
            sum=0

f.close()