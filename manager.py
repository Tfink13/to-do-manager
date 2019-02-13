import time
import datetime
import item
from textwrap import dedent

class Manager(object):

    def showItems(self):
        # variable to hold all the content inside of the todos.txt
        readItems = open("todos.txt", "r")# read mode
        # setting the contents inside the variable readitems to the message
        message = readItems.read()
        print(message)
        readItems.close()

    def CreateNewTask(self):
        print('Enter as many entries as you like.')
        print('Type "q" to escape')
        # for some reason this is really weird

        while True:
            task = input("Create A New Task: ")
            now = datetime.datetime.now().strftime("%Y-%m-%d%H:%M:%S")
            of = open("todos.txt","a+")#append mode
            # creating an if statement so that you can choose what  you want to do
            of.write("\n" + now + " " + task)
                #unfortunately you have to put your name in again -_-
            if task == 'q':
                self.run()
            else:
                of.close()


    def markComplete(self):
        # I wanted to print the list so you are able to see what is int he list. Neither True or False means it was not completed
        printTask = open("todos.txt", "r")
        message = printTask.read()
        print(message)


        # Creating variable to hold the contents in the file
        editTask = open("todos.txt").read()
        taskCompleted = input("Want to mark anything as completed? ")
        # if taskCompleted == editTask:
        #     markTask = editTask.replace(taskCompleted, taskCompleted + " " + str(True))
        # else:
        #     print('You dont have that task in your list')
        # new variable to hold the new contents
        markTask = editTask.replace(taskCompleted, taskCompleted + " " + str(True))
        # opening the file to so i can write in the new tasks
        newMarkedTask = open("todos.txt", "w")
        # writing the replaced data to the new instance of the file
        newMarkedTask.write(markTask)
        # always close open
        newMarkedTask.close()


        print(message)
        printTask.close()

    def delete(self):
        printTask = open("todos.txt", "r")
        message = printTask.read()
        print(message)
        print('Would you like to delete your to-do list?')
        choice = input ('> ')

        if choice == 'yes' or choice == 'y':
            print('Are you sure?')
            nchoice = input('> ')
            if choice == 'yes':
                f = open('todos.txt', 'r+')
                f.truncate(0)
            else:
                print('You have returned to login')
                self.run()

        elif choice == 'no' or choice == 'n':
            print('No harm done!')
            print('You have returned to login')
            self.run()

        else:
            print('Not a command')
        printTask.close()


    def run(self):
        print('What is your name?')
        name = input('> ')
        print(f'{name}, Welcome to your todo manager!')
        # The while true was a great idea for making my program, acctually able to be "inside" of it Thanks Zach!.
        while True:
            # the choice is the command you will choose
            choice = input('> ')
            if choice == 'add' or choice == 'a':
                self.CreateNewTask()
            elif choice == 'list' or choice == 'l':
                print(f"{name}'s Todo List")
                self.showItems()
            elif choice == 'mark' or choice == 'm':
                self.markComplete()
            elif choice == 'quit' or choice == 'q':
                exit(0)
            elif choice == 'help':
                print(dedent('''
                            "add" to update your list
                            "list" to show your list
                            "mark" will mark a completed task
                            "quit" will exit program.
                            "delete" to delete your entire list'''))
            elif choice == 'delete':
                self.delete()

            else:
                print('You can use "help" to see a list of commands')
