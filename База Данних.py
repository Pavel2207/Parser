import sqlite3
from random import randint
b=sqlite3.connect('server.db')

dd=b.cursor()

#создаем таблицу
dd.execute('''CREATE TABLE IF NOT EXISTS users (
                login TEXT,
                password TEXT,
                cash BIGINT
                 )''')
# подтверждаем действие
b.commit()

# просим пользователя ввести данние

def reg():
    user_login = input('Login:')
    user_password = input('Password:')
    # проверяем наличие данних в базе
    dd.execute(f'SELECT login FROM users WHERE login="{user_login}"')

    if dd.fetchone() is None: # если таких данних нет

        dd.execute(f'INSERT INTO users VALUES (?,?,?)', (user_login,user_password,0))

        b.commit()  # подтверждаем действие
        print('Зарегистрировано !')

    else:
        print('Такая запись уже имеется !')

        # выводим данние таблицы
        for i in dd.execute('SELECT * FROM users'):
            print(i)

def casino():
    user_login = input('Login:')
    user_password = input('Password:')

    x=randint(1,2)

    for i in dd.execute(f'SELECT cash FROM users WHERE login="{user_login}"'):
        profit=i[0]

    dd.execute(f'SELECT login FROM users WHERE login="{user_login}"')
    if dd.fetchone() is None:
        print('Такой записи нет ! Зарегистрируйтесь.')
        reg()
    else:
        if x==1:
            dd.execute(f'UPDATE users SET cash="{1000+profit}" WHERE login="{user_login}"')
            b.commit()
            print('Ви виграли 1000 !')
            for i in dd.execute(f'SELECT login,cash FROM users WHERE login="{user_login}" '):
                print(i)
        if x==2:
            print('Ви ничего не виграли . Ви будете удалени из казино.')
            dd.execute(f'DELETE FROM users WHERE login="{user_login}"')
            b.commit()

casino()