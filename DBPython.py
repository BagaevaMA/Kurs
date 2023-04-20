import psycopg2

def create_db(conn):
    with conn.cursor() as cur:
        cur.execute("""
        DROP TABLE phone_number;
        DROP TABLE clients;
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS clients(
            client_id SERIAL PRIMARY KEY,
            firstname_client VARCHAR(40) NOT NULL,
            lastname_client VARCHAR(40) NOT NULL,
            email VARCHAR(40) UNIQUE CHECK(email !='' and email like '%@%')
            );
        """)
        conn.commit()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS phone_number(
            number_id SERIAL PRIMARY KEY,
            number numeric NOT NULL,
            client_id INTEGER NOT NULL REFERENCES clients(client_id)
        );
        """)
        conn.commit()


def add_client(conn):
    firstname = input('Введите имя: ')
    lastname = input('Введите фамилию: ')
    mail= input('Введите email: ')
    DATA=(firstname, lastname, mail)
    with conn.cursor() as cur:
        cur.execute("SELECT email FROM clients WHERE email =%s",(mail,))
        if cur.fetchone() is None:
            cur.execute("INSERT INTO clients (firstname_client,lastname_client,email) VALUES (%s,%s,%s) returning client_id", DATA)
            print ('Вы успешно зарегистрировались!')
            return(cur.fetchone())
        else:
            print('Пользователь с таким электронным адресом уже существует!')


def add_phone(conn,client_id):
    phone = input('Введите номер телефона: ')
    with conn.cursor() as cur:
        cur.execute("SELECT number FROM phone_number WHERE number =%s", (phone,))
        if cur.fetchone() is None:
            cur.execute("INSERT INTO phone_number(number, client_id) VALUES(%s,%s)", (phone,client_id))
            conn.commit()
            print('Телефон успешно сохранен')
        else:
            print('Пользователь с таким телефоном уже есть в базе данных')
    return

def change_client(conn,client_id):
    new_firstname = input('Введите новое имя: ')
    new_lastname = input('Введите новую фамилию: ')
    with conn.cursor() as cur:
        cur.execute("UPDATE clients SET firstname_client=%s, lastname_client=%s WHERE client_id=%s;", (new_firstname,new_lastname,client_id))
        conn.commit()
        print('Данные успешно изменены')
    return

def del_phone(conn):
    number_del=input('Введите номер, который хотите удалить')
    with conn.cursor() as cur:
        cur.execute("SELECT number FROM phone_number WHERE number =%s", (number_del,))
        if cur.fetchone() is None:
            print('Такого номера нет в базе данных')
        else:
            cur.execute("DELETE FROM phone_number WHERE number=%s", (number_del,))
            conn.commit()
            print('Номер успешно удален')
        return

def del_client(conn):
    cl_id=input('Введите id клиента, который будет удален')
    with conn.cursor() as cur:
        cur.execute("DELETE FROM clients WHERE client_id=%s", (cl_id))
        print('Запись о клиенте удалена')
        return
def get_client(conn, firstname: str = None, lastname: str = None, mail: str = None) -> int:
    with conn.cursor() as cur:
        cur.execute("SELECT client_id FROM clients WHERE firstname_client=%s or lastname_client=%s or email=%s ", (firstname,lastname, mail))
        return cur.fetchone()[0]

my_database = input('Введите название базы данных')
my_user = input('Введите имя пользователя')
my_password=input('Введите пароль')

with psycopg2.connect(database=my_database, user=my_user, password=my_password) as conn:
    create_db(conn)
    client_id = add_client(conn)
    add_phone(conn,client_id)
    change_client(conn,client_id)
    del_phone(conn)
    del_client(conn)
    mary_id = get_client(conn, 'Мария')
    print('Мария', mary_id)


conn.close()
