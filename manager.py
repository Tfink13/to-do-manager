import time
import datetime
import item
from textwrap import dedent

class Manager(object):

    def showItems(self):
        # variable to hold all the content inside of the todos.txt
        readItems = open("todos.txt", "r")# read mode
        # creating an if tatement so that you can choose what you want to do
        # setting the contents inside the variable readitems to the message
        message = readItems.read()
        print(message)
        readItems.close()

    def CreateNewTask(self, amount):
        for amount in range(20):
            now = datetime.datetime.now().strftime("%Y-%m-%d%H:%M:%S")
            of = open("todos.txt","a+")#append mode
            # creating an if statement so that you can choose what you want to do
            task = input("Create A New Task: ")
            of.write("\n" + now + " " + task + str(False))
            of.close()

    def markComplete(self):
        # I wanted to print the list so you are able to see what is int he list. Neither True or False means it was not completed
        printTask = open("todos.txt", "r")
        message = printTask.read()
        print(message)
        printTask.close()

        # Creating variable to hold the contents in the file
        editTask = open("todos.txt").read()
        taskCompleted = input("Want to mark anything as completed?")
        # new variable to hold the new contents
        markTask = editTask.replace(taskCompleted, taskCompleted + " " + str(True))
        # opening the file to so i can write in the new tasks
        newMarkedTask = open("todos.txt", "w")
        # writing the replaced data to the new instance of the file
        newMarkedTask.write(markTask)
        # always close open
        newMarkedTask.close()


        printTask = open("todos.txt", "r")
        message = printTask.read()
        print(message)
        printTask.close()



    def run(self):
        print('What is your name?')
        name = input('> ')
        print(f'{name}, Welcome to your todo manager!')
        while True:
            choice = input('> ')
            if choice == 'add' or choice == 'a':
                print('How many entries?')
                amount = input('> ')
                if amount >= '20':
                    print('You may not have that many entries.')
                else:
                    self.CreateNewTask(amount)
            elif choice == 'list' or choice == 'l':
                self.showItems()
            elif choice == 'mark' or choice == 'm':
                self.markComplete()
            elif choice == 'quit' or choice == 'q':
                exit(0)
            elif choice == 'help':
                print(dedent('''
                            You may use "add" to update your list with  another task; "list" to show your complete  list; "mark" will ask what task you have completed; "quit" will exit program.'''))
            else:
                print('You can use "help" to see a list of commands')
