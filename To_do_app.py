def task():
    tasks = []# Empty list
    print("---Welcome to the task management app---")
    total_task = int(input("Enter how many task you want to add = "))#5
    for i in range(1,total_task+1):
        task_name = input(f"Enter task-{i} = ")
        tasks.append(task_name)
    print(f"Today Tasks Are:\n{tasks}")

    while True:
        operation = int(input("Enter:\n1-Add\n2-Update\n3-Delete\n4-view\n5-Exit/Stop/"))
        if operation == 1: # for Add task
            add = input("Enter task you want to add = ")
            tasks.append(add)
            print(f"Task {add} has been successfuly added...")
        elif operation == 2: # for Update task
            update_val = input("Enter the task name you want to update= ")
            if update_val in tasks:
                up = input("Enter new task= ")
                ind = tasks.index(update_val)
                tasks[ind] = up
                print(f"Updated task {update_val} to {up}")

        elif operation == 3: # for Delete task
            del_val = input("Which task you want to delete= ") 
            if del_val in tasks: 
                ind = tasks.index(del_val)
                del tasks[ind] #delete method
                print(f"Task {del_val} has been deleted...")

        elif operation == 4: # view total tasks
            print(f"Total tasks = {tasks}")
            
        elif operation == 5:
            print("Closing the programm...►")
            break
        else:
            print("Invailid Input.....Please enter right input")
task()    