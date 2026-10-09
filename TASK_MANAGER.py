import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    port=3310,
    user="root",
    password="harleydavid",
    database="task_manager"
)
cursor=db.cursor()
def add_task():
    title=input("ENTER TASK")
    sql="INSERT INTO task(title) values (%s) "
    cursor.execute(sql,(title,))
    db.commit()
def view_task():
    cursor.execute("select * from task")
    tasks=cursor.fetchall()
    if not tasks:
        print( "tasks not FOUND")
        return 
    count=0
    pending_task=[]
    print("--------------------------")
    print(" VIEW Y🧐UR TASKS")
    print("--------------------------")
    for task in tasks:
        status="✔" if task[2] else "❌ "
       
        print(task[0],task[1],status)
        print("----------------------------")
        
        if not task[2]:
            count+=1
            pending_task.append(task[1])
    print(f"Pending tasks ={count}")
    print(f"TASKS ARE{pending_task}")


def completed():
    task_id=int(input("ENTER TASK ID"))
    sql="update task set completed=TRUE where id = %s"
    cursor.execute(sql,(task_id,))
    db.commit()
    print("😀 TASK COMPLETED!")

def delete_task():
    task_id=int(input("enter id"))
    sql="delete from task where id=%s"
    cursor.execute(sql,(task_id,))
    print("🫡Task delete!")
while True:
    print("====TASK MANAGER ======")
    print("1 Add task")
    print("2 View tasks")
    print("3 Completed tasks")
    print("4 Delete task ")
    print("5 Exit")
    choose=input("CHOOSE 🤔  :")
    if choose== "1":
        add_task()
    elif choose=="2":
        view_task()
    elif choose=="3":
        completed()
    elif choose=="4":
        delete_task()
    elif choose=="5":
        print("  🥺 GOOD BYE")
        break
    else:
        print("🤬 INVALID  CHOICE")


    