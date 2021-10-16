import requests
from bs4 import BeautifulSoup
import time
import telebot


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
    m.append(i.text.split())





n=1
while n!=40:
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
        m.append(i.text.split())
    print(f'Страница {n}')
    n+=1
    print(len(m))
    print(len(p))
    time.sleep(1)




f = open('file.txt',encoding='utf-8')
s = 0
mes = str()
num = 0
for i in f:
    if s!=len(m):
        b = str(m[s]) + str(p[s]) + '\n'
        if i.strip() == b.strip():
            print(f'OK {s}')
            s += 1
        elif str(m[s]) in i and str(p[s]) not in i:
            x = f'---Данние {i} изменились на {b}'
            print(x)
            s += 1
            if x not in mes:
                mes = mes + str(x)
                num+=1
                if num==10:
                    bot = telebot.TeleBot("1831028174:AAGuVKG-9nMZVTV9ghEutGZtmjAR3oxnjbA")
                    bot.send_message(1632649927, mes+str(time.asctime()))
                    num=0
                    mes=str()

        else:
            print(f'NOT OK {b}')
            s += 1
        time.sleep(0.1)



f = open('file.txt', 'w',encoding='utf-8')
f.close()

f = open('file.txt', 'a',encoding='utf-8')
for i in range(len(m)):
    f.write(str(m[i]) + str(p[i]) + '\n')
f.close()


print(mes)

bot = telebot.TeleBot("1831028174:AAGuVKG-9nMZVTV9ghEutGZtmjAR3oxnjbA")
bot.send_message(1632649927, mes+str(time.asctime()))




print('Программа завершена')



