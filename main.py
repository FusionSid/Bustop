from flask import Flask
from flask import render_template, request, url_for, redirect, jsonify
import sqlite3
import random

# Flask
app = Flask("Bustop")


# UI Stuff
@app.route('/')
def home():
    return render_template('index.html')

# Insert Page

@app.route('/insert/', methods=['POST', 'GET'])
def insert():
    conn = sqlite3.connect('Bustop.db')
    c = conn.cursor()
    if request.method == "POST":
        letter = request.form['letter']
        cat = request.form['cat']
        thing = request.form['thing']
        def insert(table, column, thing):
            with conn:
                c.execute("INSERT INTO {} ({}) VALUES (:thing)".format(table, column), {'thing':thing})
        insert(letter, cat, thing)
        son = ("{} has been succesfuly inserted into the database".format(thing))
        return render_template('insert.html', result=son)
    else:
        return render_template('insert.html')

# Search Specific Page

@app.route('/search/', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        letter = request.form['letter']
        cat = request.form['cat']

        conn = sqlite3.connect('Bustop.db')
        c = conn.cursor()
        
        def get_thing(letter, thing):
            c.execute("SELECT {} FROM {}".format(thing, letter))
            ans = c.fetchall()
            for item in ans:
                if item == (None,):
                    ans.remove(item)
            for item in ans:
                if item == (None,):
                    ans.remove(item)
            try:
                for item in ans:
                    if item == null or [null] or 'null':
                        ans.remove(item)
            except:
                print("f")
            
            return ans

        ans = get_thing(letter, cat)
        return jsonify(ans)
    else:
        return render_template('search.html')

# Letter Page

@app.route('/bustop/', methods=['GET', 'POST'])
def bustop():
    if request.method == "POST":
        cats = ['name', "food", 'place', 'color', 'movie', 'animal']
        conn = sqlite3.connect("Bustop.db")
        c = conn.cursor()
        letter = request.form['letter']

        def get_all_from_db(letter):
            ans = []
            for item in cats:
                c.execute("SELECT {} FROM {}".format(item, letter))
                res = c.fetchall()
                ans.append(item)
                ans.append(res)
            a = ans
            ans = []
            for item in a:
                i1 = item
                for item in i1:
                    try:
                        if item[0][0].lower == letter.lower():
                            print(':)')
                    except:
                        print('f')
                    else:
                        ans.append(item[0])
            print(ans)
            for x in ans:
                print ("".join(x)+"")
            return ans

        ans = get_all_from_db(letter)
        print(ans)
        return render_template('bustop.html', ans=ans)

    else:
        return render_template('bustop.html')

# API:

# Get all
@app.route('/api/letter=<letter>/')
def apisearchall(letter):
    l = letter

    conn = sqlite3.connect('Bustop.db')
    c = conn.cursor()

    def get_all(letter):
        c.execute("SELECT * FROM {}".format(letter))
        ans = c.fetchall()     
        return ans

    ans = get_all(l)
    return jsonify(ans)
    

# Find specific things
@app.route('/api/<letter>/<thing>/')
def apisearch(letter, thing):

    l = letter
    t = thing

    conn = sqlite3.connect('Bustop.db')
    c = conn.cursor()
    
    def get_thing(letter, thing):
        c.execute("SELECT {} FROM {}".format(thing, letter))
        ans = c.fetchall()
        for item in ans:
            if item == (None,):
                ans.remove(item)
        for item in ans:
            if item == (None,):
                ans.remove(item)
        try:
            for item in ans:
                if item == null or [null] or 'null':
                    ans.remove(item)
        except:
            print("f")
        
        return ans

    ans = get_thing(l, t)
    return jsonify(ans)


# Run
app.run(host='0.0.0.0', port=8080)

