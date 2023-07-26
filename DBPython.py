import psycopg2

my_database = input('Введите название базы данных')
my_user = input('Введите имя пользователя')
my_password=input('Введите пароль')

with psycopg2.connect(database='my_database', user="my_user", password='my_password') as conn:
    with conn.cursor() as cur:
        def create_db(cursor):
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


        create_db(conn)

        def add_client(cursor, firstname, lastname, mail):
            cur.execute("SELECT email FROM clients WHERE email =%s",(mail,))
            DATA = (firstname, lastname, mail)
            if cur.fetchone() is None:
                cur.execute("INSERT INTO clients (firstname_client,lastname_client,email) VALUES (%s,%s,%s) returning client_id", DATA)
                print ('Вы успешно зарегистрировались!')
                return (cur.fetchone())
            else:
                print('Пользователь с таким электронным адресом уже существует!')

        add_client(conn, 'Надежда', 'Гасанова', 'nad@mail.ru')
        add_client(conn, 'Евгения', 'Носова', 'evg@mail.ru')
        add_client(conn, 'Карина', 'Громова', 'grom@mail.ru')

        def add_phone(cursor,client_id,phone: int):
            cur.execute("SELECT number FROM phone_number WHERE number =%s", (phone,))
            if cur.fetchone() is None:
                cur.execute("INSERT INTO phone_number(number, client_id) VALUES(%s,%s)", (phone,client_id))
                conn.commit()
                print('Телефон успешно сохранен')
            else:
                print('Пользователь с таким телефоном уже есть в базе данных')
            return

        add_phone(conn, 1 ,7654321)
        add_phone(conn, 2 ,1234567)
        add_phone(conn, 3,32564)
        def change_client(cursor,client_id, new_firstname: str = None, new_lastname: str = None, new_mail: str = None, phone:int=None):
            if new_firstname is not None:
                cur.execute("UPDATE clients SET firstname_client=%s WHERE client_id=%s;", (new_firstname, client_id))
            if new_lastname is not None:
                cur.execute("UPDATE clients SET lastname_client=%s WHERE client_id=%s;", (new_lastname,  client_id))
            if new_mail is not None:
                cur.execute(
                        "UPDATE clients SET email=%s WHERE client_id=%s;",
                        (new_mail, client_id))
            if phone is not None:
                cur.execute("UPDATE phone_number SET number=%s WHERE client_id=%s", (phone, client_id))
            conn.commit()
            print('Данные успешно изменены')
            return

        change_client(conn, 2, 'Евгений', 'Суворов', 'suv@mail.ru', '0987654')

        def del_phone(cursor, number_del):
            cur.execute("SELECT number FROM phone_number WHERE number =%s", (number_del,))
            if cur.fetchone() is None:
                print('Такого номера нет в базе данных')
            else:
                cur.execute("DELETE FROM phone_number WHERE number=%s", (number_del,))
                conn.commit()
                print('Номер успешно удален')
            return

        del_phone(conn, 7654321)
        def del_client(cursor, cl_id):
            cur.execute("DELETE FROM clients WHERE client_id=%s", cl_id)
            print('Запись о клиенте удалена')
            return

        del_client(conn,'1')

        def get_client(cursor, firstname: str = None, lastname: str = None, mail: str = None, phone: int = None):
            DATA_1 = (firstname, lastname, mail, phone)
            cur.execute("SELECT c.client_id, c.firstname_client, c.lastname_client, c.email, p.number FROM clients AS c LEFT JOIN phone_number AS p ON c.client_id = p.client_id WHERE c.firstname_client= %s and c.lastname_client=%s and c.email=%s and p.number=%s", DATA_1)
            return cur.fetchone()

        get_id = get_client(conn,'Евгений', 'Суворов', 'suv@mail.ru', '0987654')
        print(get_id)


conn.close()
