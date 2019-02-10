import time
import datetime
import item
import dedent


class Manager(object):
    def showItems(self):
        # variable to hold all the content inside of the todos.txt
        readItems = open("todos.txt", "r")# read mode
        # creating an if statement so that you can choose what you want to do
            # setting the contents inside the variable readitems to the message
        message = readItems.read()
        print(message)
        readItems.close()

    def CreateNewTask(self):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        choice = input('> ')
        
        of = open("todos.txt","a+")#append mode
        # creating an if statement so that you can choose what you want to do
        task = input("Create A New Task: ")
        of.write("\n" + now + " " + task)
        of.close()


    def markComplete(self):
        # Creating variable to hold the contents in the file
        editTask = open("todos.txt").read()
        taskCompleted = input("Have you finished any tasks?")
        # new variable to hold the new contents
        markTask = editTask.replace(taskCompleted, taskCompleted + " " + str(True))
        # opening the file to so i can write in the new tasks
        newMarkedTask = open("todos.txt", "w+")
        # writing the replaced data to the new instance of the file
        newMarkedTask.write(markTask)
        # always close open
        newMarkedTask.close()

        printTask = open("todos.txt", "r")
        message = printTask.read()
        print(message)
        printTask.close()

    def runner(object):
        print('What is your name?')
        name = input('> ')
        while True:
            print(f'{name}, Welcome to your todo manager!')
            choice = input('> ')
            if choice == 'add' or choice == 'a':
                self.CreateNewTask()
            elif choice == 'list' or choice == 'l':
                self.showItems()
            elif choice == 'mark' or choice == 'm':
                self.markComplete()
            elif choice == 'quit' or choice == 'q':
                exit(0)
            elif choice == 'help':
                print(dedent('''
                            You may use "add" to update your list with  another task; "list" to show your complete  list; "mark" will ask what task you have    completed; "quit" will exit program.''')










# class Manager(Item):
#
#     def add_item(text):
#         newitem = Item.lists.append(text)
#
#
#     def completed(self):
#         if list[1] + 2 == False:
#             Print("Have you done this today?")
#             choice = input('> ')
#             if choice == 'yes':
#                 list[1] = True
#
#             if choice == 'no':
#                 list[1] == False
#
# add = Manager()
# add.add_tem('Hello')
