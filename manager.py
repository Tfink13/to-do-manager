import time
import datetime
import item


class Manager(object):
    def showItems():

        # variable to hold all the content inside of the todos.txt
        readItems = open("todos.txt", "r")# read mode
        # creating an if statement so that you can choose what you want to do
            # setting the contents inside the variable readitems to the message
        message = readItems.read()
        print(message)
        readItems.close()

    def CreateNewTask():
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print('If you want to create a new item type add')
        choice = input('> ')

        of = open("todos.txt","a+")#append mode
        # creating an if statement so that you can choose what you want to do
        task = input("Create A New Task: ")
        of.write("\n" + now + " " + task)
        of.close()


    def markComplete():
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
