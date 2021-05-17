import sqlite3
def select():
    conn = sqlite3.connect('hesam.db')
    cur = conn.cursor()
    cur.execute('select * from pintrest')
    t1 = cur.fetchall()
    conn.close()
    return t1

print (select())