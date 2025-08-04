TO_DO_LIST =[]
print("\tTO DO LIST MENU ")
print("1. ADD TASK.")
print("2. MARK AS TASK COMPLETED.")
print("3. VIEW TASK.")
print("4. DELETE TASK.")
print("5. EXIT.")





def add_task():
    task = input("Enter the task to be added : ")
    TO_DO_LIST.append({"Title":task,"completed":False})
    print("Task added.")
def view_task():
    if not TO_DO_LIST:
        print("No Task Completed.")
    else:
        print("\nYour Tasks:")
        for  i,task in enumerate(TO_DO_LIST):
            status = "completed" if task['completed'] else "Not completed"
            print(f"{i + 1}. {task['Title']} [{status}]")
def mark_completed():
     view_task()
     task_no=int(input("Enter task number to mark as completed : "))
     if 1<= task_no <= len(TO_DO_LIST):
         TO_DO_LIST[task_no-1]['completed']=True
         print("Task marked as completed.")
     else:
         print("Invalid task number.")
def delete_task():
     view_task()
     task_no=int(input("Enter the task number to delete : "))
     if 1 <=task_no <=len(TO_DO_LIST):
         removed=TO_DO_LIST.pop(task_no-1)
         print(f"Deleted task: {removed['Title']}")
     else:
         print("Invalid task number.")
     

while True:
    ch=int(input("Enter your choise : "))
    if ch==1:
        add_task()
    elif ch==2:
         mark_completed()
    elif ch==3:
         view_task()
    elif ch==4:
         delete_task()   
    elif ch==5:
         print("Exit")
         break
    else:
         print("Invalid choice.Try again.")
