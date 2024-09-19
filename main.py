task_number = 1  # Global variable to store the task number
import datetime

print("******* Task-Tracker *******\n")
def add():
    
    now = datetime.datetime.now()

    global task_number

    print("—"*10 +" Add your task here " + "—"*10 +"\n")
    while True:
        print("Or press 1 to go BACK!! ")
        task = input("Enter a task: ")
        formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")


        if task == "1":
            menu()
        else:
            file_path = "list_of_task.txt"
            with open(file_path, "a") as file:
                file.write(f"{task_number}. {task} [Date: {formatted_date}]\n")
                print("—"*10)
                print("Added tasks!")
                print(f"{task_number}. {task} [Date: {formatted_date}]  ")
                print("—"*10)
                task_number += 1 
                
def view():
    print("—"*10 +" View your task here " + "—"*10 +"\n")
    while True:
        file_path = "list_of_task.txt"
        with open(file_path, "r") as file:
            print("—"*50)
            print(" "*25 + file.read())
            print("—"*50)

        re = input("Enter 1 to exist")
        if re == '1':
            menu()
            break
        elif re >= '2':
            print("sorry otheer number wont work except for 1")

        else: 
            print("Please enter correct number! ")


def menu():

    print("What would you like to do: \n")

    while True:   #yesle chai menu list ture na hunnu jel samma infinite time show garcha
        print("1. Add Task        2. View Task\n")
        print("3. Modify Task     4. Delete Task\n")
        print("            5. EXIT \n")

        try:            
            pick = int(input("enter your choice: "))
            if pick == 1:
                add()
            elif pick == 2:
                view()
                break
            else:
                print("PLEASE ENTER CORRECT NUMBER")

        except ValueError:
            print("Please enter number not Letters or symbols.")

menu()