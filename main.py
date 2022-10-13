import sqlite3
from userdb import Userdb
conn = sqlite3.connect('users.db')

curs = conn.cursor()

#curs.execute("""CREATE TABLE users  (
#        username text,
#        password text
#        )""")

#curs.execute("INSERT INTO users VALUES ('Ash', 'technoxmonty')")
#curs.execute("INSERT INTO users VALUES ('Fire2430', 'Magid')")

#usr_1 = Userdb('Hannah', 'Ashton')
#usr_2 = Userdb('Bently', 'Pinkbentlyclub')

#curs.execute("INSERT INTO users VALUES (?,?)", (usr_2.username, usr_2.password))

#curs.execute("SELECT * FROM users WHERE username='Ash'")
#curs.execute("SELECT * FROM users WHERE username='Fire2430'")
#print(curs.fetchone())

username1 = input("please input your username.")
curs.execute("SELECT * FROM users WHERE username=?", (username1,))
print(curs.fetchone())

conn.commit()

conn.close