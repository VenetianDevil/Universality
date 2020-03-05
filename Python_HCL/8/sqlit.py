#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
import sqlite3

# 1
conn = sqlite3.connect('example.db')
c = conn.cursor()

# 2
c.execute('''CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real)''')

# 3, 4
c.execute("INSERT INTO employees VALUES(1, 'Janusz', 4700)")
conn.commit()

# 5
try:
    c.execute("INSERT INTO employees VALUES(1, 'Janusz', 4700)")
except sqlite3.Error as e:
    print('blad plecenia INSERT: ', e.args[0])

# 6
c.execute("INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(2, 'Grzegorz', 7500, 'IT', 'programmer', '2019-03-09')")
conn.commit()

# 7
c.execute("SELECT * from employees")

# 8
c.execute("UPDATE employees SET name='Grazyna' where id=1")
conn.commit()
c.execute("SELECT * from employees")

# 9
c.execute("DROP TABLE employees")
conn.commit()

conn.close()