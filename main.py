import sqlite3
from wsgiref.validate import InputWrapper
from userdb import Userdb
import userdb
auth = False
admin_auth = False
adminuser = "admin"

def adminsection():
    print("What would you like to do?")
    selection = str(input("Add a new user. user "))
    


conn = sqlite3.connect('users.db')

curs = conn.cursor()

#curs.execute("""CREATE TABLE users  (
#        username text,
#        password text
#        )""")

#curs.execute("INSERT INTO users VALUES ('Ash', 'technoxmonty')")
#curs.execute("INSERT INTO users VALUES ('Fire2430', 'Magid')")
#curs.execute("INSERT INTO users VALUES ('admin', 'admin')")

#usr_1 = Userdb('Hannah', 'Ashton')
#usr_2 = Userdb('Bently', 'Pinkbentlyclub')

#curs.execute("INSERT INTO users VALUES (?,?)", (usr_2.username, usr_2.password))A

#curs.execute("SELECT * FROM users WHERE username='Ash'")
#curs.execute("SELECT * FROM users WHERE username='Fire2430'")
#print(curs.fetchone())
adminsec = str(input("Would you like to enter admin mode? Y/N "))
username1 = input("please input your username. ")
curs.execute("SELECT * FROM users WHERE username=?", (username1,))
record = curs.fetchall()
for row in record:
    password = row[1]
    userpass = str(input("Please enter your password. "))
    if adminsec == "Y":
        curs.execute("SELECT * FROM users WHERE username=?", (adminuser,))
        record = curs.fetchall()
        if userpass == row[1]:
            print("yes")
    elif password == userpass:
        print("Well Done")
        auth = True
        player1 = row[0]
    else:
        print("Password is incorrect.")

username1 = input("please input your username.")
curs.execute("SELECT * FROM users WHERE username=?", (username1,))
record = curs.fetchall()
for row in record:
    password = row[1]
    userpass = str(input("Please enter your password. "))
    if password == userpass:
        print("Well Done")
        auth1 = True
        player2 = row[0]
    else:
        print("Password is incorrect.")
        
    

conn.commit()

conn.close

if auth == True and auth1 == True:
    print("Auth Passed")
    print ("The players are", player1, "and", player2)
