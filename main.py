import sqlite3
import string
from tkinter import Y
from wsgiref.validate import InputWrapper
from userdb import Userdb
import userdb
from time import sleep
from random import randint, random
auth = False
admin_auth = False
adminuser = "admin"
roundnum = 0

conn = sqlite3.connect('users.db')
curs = conn.cursor()

# curs.execute("""CREATE TABLE users  (
#        username text,
#        password text
#        )""")

#curs.execute("INSERT INT1O users VALUES ('Ash', 'technoxmonty')")
#curs.execute("INSERT INTO users VALUES ('Fire2430', 'Magid')")
#curs.execute("INSERT INTO users VALUES ('admin', 'admin')")

#usr_1 = Userdb('Hannah', 'Ashton')
#usr_2 = Userdb('Bently', 'Pinkbentlyclub')

# curs.execute("INSERT INTO users VALUES (?,?)", (usr_2.username, usr_2.password))A

#curs.execute("SELECT * FROM users WHERE username='Ash'")
#curs.execute("SELECT * FROM users WHERE username='Fire2430'")
# print(curs.fetchone())


def game(player1, player2, roundnum):
    player1total = 0
    player2total = 0
    print("Hello", player1, "and", player2, "Are you ready to play the game?")
    sleep(1.7)
    print("Too late. You don't get a choice.")
    sleep(1.5)
    roundnum = roundnum+1
    print("Round", roundnum)
    sleep(1.2)
    player1roll1 = randint(1, 6)
    player2roll1 = randint(1, 6)
    print(player1, "rolled a", player1roll1)
    sleep(1.3)
    print(player2, "rolled a", player2roll1)
    sleep(1.3)
    player1total = player1roll1 + player1total
    player2total = player2roll1 + player2total
    roundnum = roundnum+1
    print("Time to go again!!")
    sleep(1.1)
    print("Are you ready for round", roundnum,)
    sleep(1.2)
    player1roll2 = randint(1, 6)
    player2roll2 = randint(1, 6)
    print(player1, "rolled a", player1roll2)
    sleep(1.3)
    print(player2, "rolled a", player2roll2)
    sleep(1.3)
    player1total = player1roll2 + player1total
    player2total = player2roll2 + player2total
    roundnum = roundnum+1
    print(player1, "has", player1total, "points")
    sleep(1.2)
    print(player2, "has", player2total, "points")
    print("Time to go again!!")
    sleep(1.1)
    print("Are you ready for round", roundnum,)
    sleep(1.2)
    player1roll3 = randint(1, 6)
    player2roll3 = randint(1, 6)
    print(player1, "rolled a", player1roll3)
    sleep(1.3)
    print(player2, "rolled a", player2roll3)
    sleep(1.3)
    player1total = player1roll3 + player1total
    player2total = player2roll3 + player2total
    roundnum = roundnum+1
    print(player1, "has", player1total, "points")
    sleep(1.2)
    print(player2, "has", player2total, "points")
    print("Time to go again!!")
    sleep(1.1)
    print("Are you ready for round", roundnum,)
    sleep(1.2)
    player1roll4 = randint(1, 6)
    player2roll4 = randint(1, 6)
    print(player1, "rolled a", player1roll3)
    sleep(1.3)
    print(player2, "rolled a", player2roll3)
    sleep(1.3)
    player1total = player1roll4 + player1total
    player2total = player2roll4 + player2total
    roundnum = roundnum+1
    print(player1, "has", player1total, "points")
    sleep(1.2)
    print(player2, "has", player2total, "points")
    print("Time to go again!!")
    sleep(1.1)
    print("Are you ready for round", roundnum,)
    sleep(1.2)
    player1roll5 = randint(1, 6)
    player2roll5 = randint(1, 6)
    print(player1, "rolled a", player1roll5)
    sleep(1.3)
    print(player2, "rolled a", player2roll5)
    sleep(1.3)
    player1total = player1roll5 + player1total
    player2total = player2roll5 + player2total
    roundnum = roundnum+1
    print(player1, "has", player1total, "points")
    sleep(1.2)
    print(player2, "has", player2total, "points")


def adminsection():
    print("What would you like to do?")
    selection = str(input(
        "Add A new user (user), Checks Passwords (pass), Change Password (forgotpass)"))
    if selection == "user":
        user1 = str(input("What would you like the username to be?"))
        sleep(0.5)
        print("What would you like the password to be.")
        sleep(0.1)
        pass1 = str(
            input("Must have atleast 8 Characters, One uppercase and One specail Charater."))
        temp = pass1.lower()
        if len(pass1) <= 8:
            print("The password is too small.")
            adminsection()
        elif pass1 == temp:
            print("Your password does not have any Uppercase characters.")
            adminsection()
        elif pass1.isalnum() == True:
            print("Your password does not have a speaical character.")
            adminsection()
        else:
            curs.execute("INSERT INTO users VALUES(?,?)", (user1, pass1))
    elif selection == "pass":
        print("What is the username of the account you want the password checked?")
        sleep(0.5)
        user2 = str(input("Please enter the username. "))
        curs.execute("SELECT * FROM users WHERE username=?", (user2,))
        records1 = curs.fetchall()
        for row in records1:
            sleep(0.5)
            print("The password is")
            sleep(0.2)
            print(row[1])
    elif selection == "forgotpass":

        sleep(0.2)
        user3 = str(
            input("Please enter the username of the account you want to change."))
        curs.execute("SELECT * FROM users WHERE username=?", (user3,))
        records2 = curs.fetchall()
        curs.execute("SELECT * FROM users WHERE username=?", (adminuser,))
        admin = curs.fetchall()
        for row in records2:
            sleep(0.2)
            pass3 = str(input(
                "Please enter your old password or if you dont have it please enter the admin password."))
            if pass3 == row[1]:
                newpass = str(input("Please enter your new password."))
                curs.execute("INSERT INTO users VALUES (?,?)",
                             (user3, newpass))
        for row in admin:
            if pass3 == row[1]:
                newpass = str(input("Please enter your new password."))
                curs.execute("DELETE FROM users WHERE username=?", (user3,))
                curs.execute("INSERT INTO users VALUES (?,?)",
                             (user3, newpass))
    else:
        print("You made an invalid input.")
        adminsection()


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
            adminsection()
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
    print("The players are", player1, "and", player2)
    scoreboard = str(input("Would you like to see the score board? (Y/N) "))
    if scoreboard == "Y":
        print("Not here yet. :(")
    else:
        game(player1, player2, roundnum)

else:
    print("Authentication failed.")
