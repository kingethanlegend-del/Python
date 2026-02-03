tasks = []
def show_menu():
    print("\n--- To-Do List Menu ---")
    print("\n 1. Add a task")
    print("\n 2. View task")
    print("\n 3. Remove a task")
    print("\n 4. Exit")

while True:
    show_menu()
    choice = int(input("Choose an option between 1 to 4: "))
    if choice == 1 :
        task = input("Enter a task to add :")
        tasks.append(task)
        print(f"Task{task} added ")

    elif choice == 2:
        if not tasks :
            print("No tasks found , your to do list is empty")
        else :
            print("\nYour tasks:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}.{task}")
                
    elif choice == 3:
        if not tasks :
            print("Your to do list is empty , no task to delete")
        else :
            task = input("Enter which task you want to delete")
            if task in tasks:
                tasks.remove(task)
                print(f" Task '{task}' removed!")
            else : 
                print("Task not found")
    
    elif choice == 4:
        print("Exiting the to do list")
        break
    else :
        print("Invalid choice")

        
