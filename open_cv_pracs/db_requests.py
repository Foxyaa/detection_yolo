import sqlite3

db = sqlite3.connect('plastic_detect.db')
cur = db.cursor()
cur.execute('PRAGMA foreign_keys = ON')
cur.execute('''
    CREATE TABLE plastic_types (
        it_type INTEGER PRIMARY KEY AUTOINCREMENT,
        name text UNIQUE
    )''')
cur.execute('''
    CREATE TABLE visibility (
        id_visibility INTEGER PRIMARY KEY AUTOINCREMENT,
        name text UNIQUE
    )''')
cur.execute('''
    CREATE TABLE color_plastic (
        id_color INTEGER PRIMARY KEY AUTOINCREMENT,
        name text UNIQUE
    )''')
cur.execute('''
    CREATE TABLE devices (
        id_device INTEGER PRIMARY KEY AUTOINCREMENT,
        name text UNIQUE
    )''')
cur.execute('''
    CREATE TABLE images (
        id_img INTEGER PRIMARY KEY AUTOINCREMENT,
        timedate DATETIME DEFAULT (datetime('now')),
        id_device INTEGER,
        file_name text UNIQUE,
        FOREIGN KEY(id_device) REFERENCES devices(id_device)
    )''')
cur.execute('''
    CREATE TABLE plastic (
        id_plastic INTEGER PRIMARY KEY,
        color INTEGER,
        visibility INTEGER,
        type INTEGER,
        FOREIGN KEY(color) REFERENCES color_plastic(id_color),
        FOREIGN KEY(visibility) REFERENCES visibility(id_visibility),
        FOREIGN KEY(type) REFERENCES plastic_types(id_type),
        FOREIGN KEY(id_plastic) REFERENCES images(id_img)
    )''')
db.commit()
data_types = [('PE-C2',), ('PE-HD',), ('PE-LD',), ('PE-LLD',), ('PE-MD',), ('PE-UHMW',), ('PE-VLD',), ('PET',), ('PP',), ('PVC-C',), ('PVC-U',)]
data_visibility = [('прозрачный',), ('полупрозрачный',), ('непрозрачный',)]
data_color = [('синий',), ('зеленый',), ('коричневый',)]
cur.executemany('INSERT INTO plastic_types(name) VALUES (?)', data_types)
db.commit()
cur.executemany('INSERT INTO visibility(name) VALUES (?)', data_visibility)
db.commit()
cur.executemany('INSERT INTO color_plastic(name) VALUES (?)', data_color)
db.commit()
cur.execute('INSERT INTO devices(name) VALUES (?)', ('веб-камера',))
db.commit()
#Вывод данных из таблицы plastic_types
cur.execute('SELECT * FROM plastic_types')
plastic_types_data = cur.fetchall()
print("Данные из таблицы plastic_types:")
for row in plastic_types_data:
    print(row)

# Вывод данных из таблицы visibility
cur.execute('SELECT * FROM visibility')
visibility_data = cur.fetchall()
print("Данные из таблицы visibility:")
for row in visibility_data:
    print(row)

# Вывод данных из таблицы color_plastic
cur.execute('SELECT * FROM color_plastic')
color_plastic_data = cur.fetchall()
print("Данные из таблицы color_plastic:")
for row in color_plastic_data:
    print(row)

# Вывод данных из таблицы devices
cur.execute('SELECT * FROM devices')
devices_data = cur.fetchall()
print("Данные из таблицы devices:")
for row in devices_data:
    print(row)
db.close()