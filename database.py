import sqlite3
import random

conn = sqlite3.connect('Bustop.db')

c = conn.cursor()

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def create_table(name:str):
    with conn:
        c.execute("""CREATE TABLE IF NOT EXISTS {} (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT, 
            place TEXT, 
            animal TEXT,
            food TEXT, 
            color TEXT, 
            movie TEXT)""".format(name))

def insert(table, column, thing):
    with conn:
        c.execute("INSERT INTO {} ({}) VALUES (:thing)".format(table, column), {'thing':thing})

def get_thing(letter, thing, amount = 'all'):
    c.execute("SELECT {} FROM {}".format(thing, letter))
    ans = c.fetchall()
    for item in ans:
        if item == (None,):
            ans.remove(item)
    for item in ans:
        if item == (None,):
            ans.remove(item)
    if amount == 'random' or 'r':
        ans = random.choice(ans)
        return ans
    else:
        return ans

#insert('a', 'name', 'Andrew')
#print(get_thing('a', 'name', 'r'))

conn.close()