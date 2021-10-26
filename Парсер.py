import requests
from bs4 import BeautifulSoup
from ast import literal_eval


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.0; rv:14.0) Gecko/20100101 Firefox/14.0.1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language':'ru-ru,ru;q=0.8,en-us;q=0.5,en;q=0.3',
    'Accept-Encoding':'gzip, deflate',
    'Connection':'keep-alive',
    'DNT':'1'
}

f=requests.get('https://hotline.ua/av/televizory/',headers=headers)
s=BeautifulSoup(f.content,'html.parser')


p=[]
flag=0
price=s.find_all('div',class_='text-sm')
for i in price:
    p.append(i.text.split())
    flag+=1
if flag!=25:
    for i in range(flag):
        p.pop()
    pri = s.find_all('div', class_='item-price stick-bottom')
    for i in pri:
        p.append(i.text.split())


m=[]
mark = s.find_all('p', class_='h4')
for i in mark[1:26]:
    m.append(i.text.strip())


n=1
while n!=50:
    f = requests.get('https://hotline.ua/av/televizory/?p='+str(n), headers=headers)
    s = BeautifulSoup(f.content, 'html.parser')

    price = s.find_all('div', class_='text-sm')

    flag=0
    for i in price:
        p.append(i.text.split())
        flag+=1
    if flag != 25:
        for i in range(flag):
            p.pop()
        price = s.find_all('div', class_='item-price stick-bottom')
        for i in price:
            p.append(i.text.split())


    mark = s.find_all('p', class_='h4')
    for i in mark[1:26]:
        m.append(i.text.strip())
    print(f'Страница {n}')
    n+=1
    print(len(m))
    print(len(p))







message=str()
f=open("file.txt",encoding='utf-8') # открываем файл со значениями
for i in f:
    i=literal_eval(i) # строку преобразовываем в словарь
    for j in range(len(m)):
        temp_data={m[j]:p[j]}
        if i.keys()==temp_data.keys(): # сравниваем ключи
            if str(i.values()).strip()==str(temp_data.values()).strip():  # сравниваем значения
                print('Цена не изменилась')
            else:
                print(f'---Цена {i} изменилась на {temp_data}')
                data=str(f'---Цена {i} изменилась на {temp_data}')
                if data not in message:
                    message=message+str(f'---Цена {i} изменилась на {temp_data}'+str('\n'))

        else:
            print('Ключи не совпадают')
f.close()


f=open('file.txt','w',encoding='utf-8')
f.close()

f = open("file.txt", "a", encoding="utf-8")
x = 0
for i in range(len(m)):
        f.write(str({m[x]:p[x]}) +'\n')
        x += 1
f.close()

print(message)
