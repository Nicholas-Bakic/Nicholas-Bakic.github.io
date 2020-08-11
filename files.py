##import random
##
##def registration_check(username):
##    found = False
##    file = open("db.txt", "r")
##    # code that allows us to check if file is empty
##    if os.stat("db.txt").st_size == 0:
##        found = False
##        for line in file.readlines():
##            login_info = line.split()
##            if username == login_info[0]:
##                found = True
##                found = False
##    file.close()
##    return found
##
##def writing_database(username, password):
##    file = open("db.txt", "a")
##    line = username + " " + password
##    file.write(line)
##    file.close()
##
##def add_password(username):
##    password = input("Please enter a password.")
##    writing_database(username, password)
##    print("you can now log in.")
##
##def add_password_with_random(username):
##    # tweak username, so that random num is in there
##    username = username + str(random.randint(1,100))
##    password = input("Please enter a password.")
##    writing_database(username, password)
##    print("you can now log in.")
##
##def register():
##    firstname = input("What is your first name?")
##    surname = input("What is your surname")
##    username = surname + "_" + firstname[0:1]
##    if registration_check(username):
##        add_password_with_random(username)
##        add_password(username)
##
##def login():
##    username = input("enter your username")
##    password = input("enter your password")
##    login_check(username, password)
##
##def login_check(username, password):
##    file = open("db.txt", "r")
##    for line in file.readlines():
##        login_info = line.split()
##        if username == login_info[0] and password == login_info[1]:
##            print("you have successfully logged in.")
##            login()
##       
##action = input("Would you like to register, log in or quit?")
##
##if action == "register":
##    register()
##else:
##    login()
##
##print("Thank you for using the program")


import random # imports everything from the "random" library.

def writing_database(username, password):
    file = open("db.txt", "a") # opens text file
    line = "\n" + username + " " + password 
    file.write(line) # adds username and password
    file.close() # closes file

def add_password(username):
    password = input("Please enter a password.") # user creates password
    writing_database(username, password) # calls writing_database function
    print("you can now log in.")

def add_password_with_random(username):
    # tweak username, so that random num is in there
    username = username + str(random.randint(1,100))
    password = input("Please enter a password.")
    writing_database(username, password)
    print("you can now log in.")

def register():
    firstname = input("What is your first name?")
    surname = input("What is your surname")
    username = surname + "_" + firstname[0:1] # creates username format
    add_password(username) # calls add_password function

def login():
    username = input("enter your username")
    password = input("enter your password") # user enters credentials.
    login_check(username, password) # calls login_check function

def login_check(username, password):
    file = open("db.txt", "r")  # opens text file
    for line in file.readlines(): # reads what is in the text file
        login_info = line.split() # splits line in text file
        if username == login_info[0] and password == login_info[1]: # if the password and username is found
            print("you have successfully logged in.")
            #login()
       
def quiz():
    username = input("enter your username")
    password = input("enter your password")
    file = open("db.txt", "r") # opens text file in read mode.
    for line in file.readlines():
        login_info = line.split()
        if username == login_info[0] and password == login_info[1]: # checks if username and password are in text file.         
            ask_again = "yes" # making the variable assigned to "yes".

            while ask_again == "yes": # starts program
                name=input("What is your name?") # asks name
                print ("Alright",name,"lets get into the questions.")
                score=0 # score assigned to 0 at the start.

                for question_num in range(1, 21): # will print 20 questions.
                    operators = ['+', '-', '*', "/"] # set of operations.
                    random1=random.randint(1,10) # generates random number from 1-10
                    random2=random.randint(1,10) # generates random number from 1-10
                    operation = random.choice(operators) # random operation from list
                    if random1 <= random2:
                        maths = eval(str(random2) + operation + str(random1))
                        print ("The question is",random2,operation,random1)
                    else:
                        maths = eval(str(random1) + operation + str(random2)) # question generated.
                        print ("The question is",random1,operation,random2)
                    
                    d=int(input ("What is your answer:"))
                    if d==maths: # checks if the answer is correct.

                        print ("Correct")
                        score=score+1 # if the answer is correct, print correct and +1 score.
                    else:
                        print ("Incorrect. The actual answer is",maths)# if wrong, score +0.
                        print("Test complete, you got a score of",score) # outputs user's score.

                ask_again = str(input("Do you want to take the quiz again?"))
            else:
                print("Login unsuccessful or you didn't want to take the quiz again")

action = input("Would you like to register, login, quit, or quiz?")

if action == "register": # if they type "register"
    register() # call register function
elif action == "login": # if they type "login"
    login() # call login function
elif action == "quiz": # if they type "quiz"
    quiz() # call quiz function
else: # if neither of these results were inputted by the user, stop the program
    print("Thank you for using the program, you didn't log in")

import random
import os

def registration_check(username):
    found = False
    file = open("db.txt", "r")
    # code that allows us to check if file is empty
    if os.stat("db.txt").st_size == 0:
        found = False
        for line in file.readlines():
            login_info = line.split()
            if username == login_info[0]:
                found = True
                found = False
    file.close()
    return found

def writing_database(username, password):
    file = open("db.txt", "a")
    line = "\n" + username + " " + password
    file.write(line)
    file.close()

def add_password(username):
    password = input("Please enter a password.")
    writing_database(username, password)
    print("you can now log in.")

def add_password_with_random(username):
    # tweak username, so that random num is in there
    username = username + str(random.randint(1,100))
    password = input("Please enter a password.")
    writing_database(username, password)
    print("you can now log in.")

def register():
    firstname = input("What is your first name?")
    surname = input("What is your surname")
    username = surname + "_" + firstname[0:1]
    print("a")
    #if registration_check(username):
    #add_password_with_random(username)
    add_password(username)

def login():
    username = input("enter your username")
    password = input("enter your password")
    login_check(username, password)

def login_check(username, password):
    file = open("db.txt", "r")
    for line in file.readlines():
        login_info = line.split()
        if username == login_info[0] and password == login_info[1]:
            print("you have successfully logged in.")
            #login()
       
def dice():
    username = input("enter your username")
    password = input("enter your password")
    file = open("db.txt", "r")
    for line in file.readlines():
        login_info = line.split()
        if username == login_info[0] and password == login_info[1]:           
            ask_again = "yes" # making the variable assigned to "yes".

            while ask_again == "yes": # starts program
                print("Round 1")

                for round in range(5):
                    fscore = 0
                    sscore = 0
                    dice0 = random.randint(1,6)
                    dice1 = random.randint(1,6)
                    dice2 = random.randint(1,6)
                    dice4 = random.randint(1,6)
                    dice9 = random.randint(1,6)
                    dice5 = random.randint(1,6)                       
                    print("Player 1 rolls", dice1)
                    print("2nd roll is", dice2)
                    dice3 = dice1 + dice2
                    if dice1 == dice2:
                        print("3rd roll was", dice0)
                        fscore = dice1 + dice2 + dice0
                    else:
                        fscore = fscore

                    if dice3%2 == 0 and dice1 != dice2:
                        dice3 = dice3 + 10
                        fscore = fscore + dice3
                    else:
                        dice3 = dice3 - 5   
                        fscore = fscore + dice3

                    if fscore <= 0:
                        fscore = 0
                    else:
                        fscore = fscore
                       
                    print("Player 1 score is now", fscore)
                    input("Press Enter to continue...")
                    print("player 2 rolls", dice4)
                    print("and rolls", dice5)
                    dice6 = dice4 + dice5
                
                    if dice4 == dice5:
                        print("3rd roll was", dice9)
                        dice6 = dice6 + dice9
                        sscore = dice4 + dice5 + dice9
                    else:
                        dice6 == dice6

                    if dice6%2 == 0 and dice4 != dice5:
                        dice6 = dice6 + 10
                        sscore = sscore + dice6
                    else:
                        dice6 = dice6 - 5
                        sscore = sscore + dice6
                        if sscore <= 0:
                            sscore = 0
                        else:
                            sscore = sscore
                    if sscore <= 0:
                        sscore = 0
                    else:
                        sscore = sscore
                            
                    print("Player 2 score is now", sscore)
                    input("Press Enter to continue...")
                
                
                ask_again = str(input("Do you want to play dice again?"))
            else:
                print("Login unsuccessful or you didn't want to play dice")

action = input("Would you like to register, login, quit, or dice?")

if action == "register":
    register()
elif action == "login":
    login()
elif action == "dice":
    dice()
else:
    print("Thank you for using the program, you didn't log in")









