import psycopg2

class Client:
    def __init__(self, first_name, last_name, email=None, phone_number=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

# Функция удаления всех предыдущих таблиц
    def drop_db(conn):
        try:
            cur.execute("""
                    DROP TABLE client_emails;
                    DROP TABLE client_phones;
                    DROP TABLE client_names;
                                    """)
            return 'Удаление всех предыдущих таблиц успешно.'
        except psycopg2.errors.UndefinedTable:
            return 'В базе данных не было таблиц.'

# Функция создания БД:
    def create_db(conn):
        print(Client.drop_db(conn))
        cur.execute("""
                CREATE TABLE IF NOT EXISTS client_names(
                id_client SERIAL PRIMARY KEY,
                first_name VARCHAR (10) not null,
                last_name VARCHAR (10) not null
                );
                """)

        cur.execute("""
                CREATE TABLE IF NOT EXISTS client_emails(
                id_email SERIAL PRIMARY KEY,
                email VARCHAR (20) not null,
                id_client integer not null references client_names(id_client)
                );
                """)

        cur.execute("""
                CREATE TABLE IF NOT EXISTS client_phones(
                id_phone SERIAL PRIMARY KEY,
                phone_number VARCHAR (13) UNIQUE,
                id_client integer not null references client_names(id_client)
                );
                """)

        return 'База данных создана.'

    # Функция, позволяющая добавить нового клиента
    def add_client(conn, first_name: str, last_name: str):
        values = ({'first_name': first_name, 'last_name': last_name})
        cur.execute("""
            INSERT INTO client_names(first_name, last_name)
            VALUES (%(first_name)s, %(last_name)s)
            RETURNING id_client, first_name, last_name;
            """, values)
        return f'Клиент "{first_name} {last_name}" добавлен в базу данных.'

    # Функция, позволяющая добавить почту для существующего клиента
    def add_email(conn, email: str, id_client):
        values = ({'email': email, 'id_client': id_client})
        cur.execute("""
            INSERT INTO client_emails(email, id_client)
            VALUES (%(email)s, %(id_client)s)
            RETURNING id_client, email;
            """, values)
        return f'Для клиента номер {id_client} добавлен адрес электронной почты "{email}".'

    # Функция, позволяющая добавить телефон для существующего клиента
    def add_phone(conn, phone_number: str, id_client):
        values = ({'phone_number': phone_number, 'id_client': id_client})
        cur.execute("""
            INSERT INTO client_phones(phone_number, id_client)
            VALUES (%(phone_number)s, %(id_client)s)
            RETURNING id_client, phone_number;
            """, values)
        (cur.fetchone())
        return f'Для клиента номер {id_client} добавлен номер телефона "{phone_number}".'

    # Функция, позволяющая изменить данные о клиенте
    def change_client(conn, id_client, first_name=None, last_name=None, email=None, phone_number=None):
        values = ({'id_client': id_client, 'first_name': first_name, 'last_name': last_name,
                   'email': email, 'phone_number': phone_number})
        for key, value in values.items():
            if value != None and key == 'first_name':
                cur.execute("""
                    UPDATE client_names
                    SET first_name = %(first_name)s
                    WHERE id_client = %(id_client)s
                    RETURNING id_client, first_name, last_name;
                """, values)
                return f'Имя клиента номер {id_client} изменено на "{first_name}".'
            elif value != None and key == 'last_name':
                cur.execute("""
                    UPDATE client_names
                    SET last_name = %(last_name)s
                    WHERE id_client = %(id_client)s
                    RETURNING id_client, first_name, last_name;
                """, values)
                return f'Фамилия клиента номер {id_client} изменена на "{last_name}".'
            elif value != None and key == 'email':
                cur.execute("""
                    UPDATE client_emails
                    SET email = %(email)s
                    WHERE id_client = %(id_client)s
                    RETURNING id_client, email;
                """, values)
                return f'Адрес электронной почты клиента номер {id_client} изменён на "{email}".'
            elif value != None and key == 'phone_number':
                cur.execute("""
                    UPDATE client_phones
                    SET phone_number = %(phone_number)s
                    WHERE id_client = %(id_client)s
                    RETURNING id_client, phone_number;
                """, values)
                return f'Номер телефона клиента номер {id_client} изменён на "{phone_number}".'

    # Функция, позволяющая удалить телефон для существующего клиента
    def delete_phone(conn, id_client, phone_number):
        values = ({'id_client': id_client, 'phone_number': phone_number})
        cur.execute("""
            DELETE from client_phones
            WHERE id_client = %(id_client)s;
                    """, values)
        return f'Номер телефона клиента {id_client} удалён.'

    # Функция, позволяющая удалить существующего клиента
    def delete_client(conn, id_client):
        values = ({'id_client': id_client})
        cur.execute("""
            DELETE from client_phones
            WHERE id_client = %(id_client)s;
            """, values)
        cur.execute("""
            DELETE from client_emails
            WHERE id_client = %(id_client)s;
                """, values)
        cur.execute("""
            DELETE from client_names
            WHERE id_client = %(id_client)s;
                """, values)
        return f'Клиент под номером {id_client} удалён.'

    # Функция, позволяющая найти клиента по его данным (имени, фамилии, email-у или телефону)
    def find_client(conn, first_name=None, last_name=None, email=None, phone_number=None):
        values = ({'first_name': first_name, 'last_name': last_name, 'email': email, 'phone_number': phone_number})
        for key, value in values.items():

            if value != None and key == 'first_name':
                cur.execute("""
                    SELECT id_client from client_names
                    WHERE first_name = %(first_name)s
                    """, values)
                return f'Имя "{first_name}" принадлежит клиенту номер {cur.fetchone()[0]}.'

            if value != None and key == 'last_name':
                cur.execute("""
                    SELECT id_client from client_names
                    WHERE last_name = %(last_name)s
                    """, values)
                return f'Имя "{last_name}" принадлежит клиенту номер {cur.fetchone()[0]}.'

            if value != None and key == 'email':
                cur.execute("""
                    SELECT id_client from client_emails
                    WHERE email = %(email)s
                    """, values)
                return f'Адрес электронной почты "{email}" принадлежит клиенту номер {cur.fetchone()[0]}.'

            if value != None and key == 'phone_number':
                cur.execute("""
                    SELECT id_client from client_phones
                    WHERE phone_number = %(phone_number)s
                    """, values)
                return f'Номер телефона "{phone_number}" принадлежит клиенту номер {cur.fetchone()[0]}.'

    def join_database(conn):
        cur.execute("""
            SELECT cn.id_client, first_name, last_name, email, phone_number from client_names cn
            JOIN client_emails ce ON cn.id_client = ce.id_client
            JOIN client_phones cp ON ce.id_client = cp.id_client
            """)
        return cur.fetchall()[0]

def config_read():
    filename = 'pas.config'
    contents = open(filename).read()
    config = eval(contents)
    password = config['password']
    return password

password = config_read()

conn = psycopg2.connect(database='sql_hw5', user='postgres', password=password)
with conn.cursor() as cur:
    print(Client.create_db(conn))
    print(Client.add_client(conn, 'Анна', 'Кувшинова'))
    print(Client.add_client(conn, 'Людмила', 'Сидорина'))
    print(Client.add_client(conn, 'Ирина', 'Анютина'))
    print(Client.add_email(conn, 'akuvshinova@mail.ru', '1'))
    print(Client.add_email(conn, 'lsidorina@yandex.ru', '2'))
    print(Client.add_email(conn, 'ianyutina@mail.ru', '3'))
    print(Client.add_phone(conn, '89030100001', '1'))
    print(Client.add_phone(conn, '89260200002', '2'))
    print(Client.add_phone(conn, '89260300003', '3'))

    print(Client.change_client(conn, id_client='1', first_name='Алиса'))
    print(Client.change_client(conn, id_client='3', last_name='Посадская'))
    print(Client.change_client(conn, id_client='1', email='abuzlova@mail.ru'))
    print(Client.change_client(conn, id_client='2', phone_number='89264440002'))

    print(Client.delete_phone(conn, id_client='2', phone_number='89264440002'))
    print(Client.delete_client(conn, id_client='2'))

    print(Client.find_client(conn, first_name='Алиса'))
    print(Client.find_client(conn, last_name='Кувшинова'))
    print(Client.find_client(conn, email='abuzlova@mail.ru'))
    print(Client.find_client(conn, phone_number='89260300003'))

    print(Client.join_database(conn))
conn.commit()