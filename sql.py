import sqlite3

with sqlite3.connect("blog.db") as connection:

    c=connection.cursor()

    c.execute("""
                 create table posts(title text, post text)""")

    c.execute('insert into posts values("Good","I\'m good.")')
    c.execute('INSERT INTO posts VALUES("Well","I\'m well.")')
    c.execute('INSERT   INTO    posts   VALUES("Excellent","I\'m excellent.")')
    c.execute('INSERT   INTO    posts   VALUES("Okay","I\'m okay.")')
    