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

bot = telebot.TeleBot("1831028174:AAGuVKG-9nMZVTV9ghEutGZtmjAR3oxnjbA")

def send(mes):
    bot.send_message(1632649927, mes + str(time.asctime()))
    print(mes)
    input('Для закрытия програмы нажмите "Enter"')


b=requests.get("https://www.ceneo.pl/Telewizory",headers=headers)
soup=BeautifulSoup(b.content,'html.parser')

spisok = ['LG 70UP77003LB',
'LG OLED65C11LB',
'LG OLED55C11LB',
'LG 48C12LA',
'LG 48C11LB',
'LG 55NANO883PB',
'LG 55NANO863PA-2',
'LG 55NANO863PA-1',
'LG OLED55C12LA',
'SAMSUNG QE43LS03AAUXXH',
'LG 55nano813PA',
'LG 55NANO883PB',
'LG 55NANO863NA',
'LG 65UP77003LB',
'LG 43UP81003la',
'LG 43NANO753PA',
'SAMSUNG QE55Q80A',
'LG 55NANO863PA',
'LG 55NANO903NA',
'LG OLED55GX3LA']

p=[]
for j in spisok:
    data=soup.find_all('a',title=j)
    for i in data:
        p.append(i.text.split())
print('Страница 0')

n=1
while n!=51:
    b = requests.get("https://www.ceneo.pl/Telewizory;0020-30-0-0-{}.htm".format(n),headers=headers)
    soup = BeautifulSoup(b.content, 'html.parser')
    for j in spisok:
        data = soup.find_all('a', title=j)
        for i in data:
            p.append(i.text.split())

    time.sleep(0.1)
    print(f'Страница {n}')
    n+=1

k=p[1::4]



if k!=[]:
    f = open('paket.txt', encoding='utf-8')
    s = 0
    mes = str()
    num = 0
    num_mes=0
    for i in f:
        if s != len(k):
            b = str(spisok[s]) + str(k[s]) + '\n'
            if str(spisok[s]) in i and str(k[s]) not in i:
                x = f'---Данние {i} изменились на {b}'
                print(x)
                s += 1
                if x not in mes:
                    mes = mes + str(x)
                    num += 1
                    if num == 10:
                        bot.send_message(1632649927, mes + str(time.asctime()))
                        num = 0
                        mes = str()
                        num_mes=num_mes+1
            time.sleep(0.1)
    f.close()


    f = open('paket.txt', 'w', encoding='utf-8')
    f.close()

    f = open('paket.txt', 'a', encoding='utf-8')
    for i in range(len(k)):
        f.write(str(spisok[i]) + str(k[i]) + '\n')
    f.close()

    if num_mes==0 and mes==str():
        mes=('Изменений нет.')
        send(mes)
    else:
        send(mes)

else:
    mes=('Запустите парсер через 2 часа.')
    send(mes)