# -*- coding: utf-8 -*-
import sqlite3

def initiate_db():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL  
    ) 
    ''')

    cursor.execute("SELECT * FROM Products")
    if cursor.fetchone() is None:
        for i in range(4):
            cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                           ('Продукт' + str(i + 1), 'Описание ' + str(i + 1), 100 * (i + 1)))


    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    connection.close()
    # for product in products:
    #     print(f'Название:{product[1]}|Описание:{product[2]}|Цена:{product[3]}')
    # for i in range(len(products)):
    #     print(f'Название:{products[i][1]}|Описание:{products[i][2]}|Цена:{products[i][3]}')
    return products


if __name__ == '__main__':
    initiate_db()
    get_all_products()

