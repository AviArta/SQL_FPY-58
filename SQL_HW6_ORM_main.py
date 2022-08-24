import sqlalchemy
import json
from pprint import pprint
from sqlalchemy.orm import sessionmaker

from SQL_HW6_ORM_models import create_tables, Publisher, Book, Shop, Stock, Sale

def config_read():
    filename = 'pas.config'
    contents = open(filename).read()
    config = eval(contents)
    sybd = config['sybd']
    user = config['user']
    password = config['password']
    bd = config['bd']
    return sybd, user, password, bd

sybd, user, password, bd = config_read()

DSN = f"{sybd}://{user}:{password}@localhost:5432/{bd}"
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Заполнение БД тестовыми данными. Чтение json-файла, создание соотведствующих экземляров моделей и сохранение в БД.
with open('data_hw6.json', encoding = 'utf-8') as file:
    data = json.load(file)
    # pprint(data)

for element in data:
    if element['model'] == 'publisher':
        publisher = Publisher(id=element['pk'], name=element['fields']['name'])
        session.add(publisher)

    elif element['model'] == 'book':
        book = Book(id=element['pk'], title=element['fields']['title'], id_publisher=element['fields']['id_publisher'])
        session.add(book)

    elif element['model'] == 'shop':
        shop = Shop(id=element['pk'], name=element['fields']['name'])
        session.add(shop)

    elif element['model'] == 'stock':
        stock = Stock(id=element['pk'], id_book=element['fields']['id_book'], id_shop=element['fields']['id_shop'],
                      count=element['fields']['count'])
        session.add(stock)

    elif element['model'] == 'sale':
        sale = Sale(id=element['pk'], price=element['fields']['price'], date_sale=element['fields']['date_sale'],
                    id_stock=element['fields']['id_stock'], count=element['fields']['count'])
        session.add(sale)

    session.commit()

# Запрос выборки магазинов, продающих целевого издателя (на выбор: по названию или идентификатору издательства).
print('Введите имя или идентификатор издателя: ')
n = input()
# подзапрос не потребовался (оставила себе для примера).
# subq = session.query(Publisher).filter(Publisher.id == n or Publisher.name == n).subquery()
shops = []
for c in session.query(Shop).join(Stock, Shop.id == Stock.id_shop).\
        join(Book, Stock.id_book == Book.id).join(Publisher, Book.id_publisher == Publisher.id).\
        filter(Publisher.name == n or Publisher.id == int(n)).all():
    shops.append(c.name)
print(f'Книги издательства {n} можно приобрести в магазине/ах: ')
print(*shops, sep=', ')

session.close()