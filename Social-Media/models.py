import sqlite3 as sql
from os import path

#allows server to interact with database, finds database file
ROOT = path.dirname(path.relpath(__file__))

def create_post(name, content):
    #establish a connection to db using db file
    con = sql.connect(path.join(ROOT, 'database.db'))
    #cursor that finds info we need in db
    cur = con.cursor()
    #execute raw sql syntax into db
    cur.execute('insert into posts (name, content) values(?, ?)', (name, content))
    #commit entry into db
    con.commit()
    #close connection to db
    con.close()

def get_posts():
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('select * from posts')
    #retrieve all records from the result set as a list of tuples. Each tuple represents a single record
    posts = cur.fetchall()
    return posts