import json

# Function to load tasks from a file
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

# Function to save tasks to a file
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# Function to display the To-Do List
def display_tasks(tasks):
    if tasks:
        print("To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("Your To-Do List is empty!")

# Function to add a task
def add_task(tasks, task):
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

# Function to mark a task as completed
def complete_task(tasks, index):
    if 1 <= index <= len(tasks):
        completed_task = tasks.pop(index - 1)
        print(f"Task '{completed_task}' marked as completed!")
    else:
        print("Invalid task index!")

# Main function
def main():
    tasks = load_tasks()
    
    while True:
        print("\nMenu:")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            task = input("Enter task: ")
            add_task(tasks, task)
            save_tasks(tasks)
        elif choice == "3":
            index = int(input("Enter index of task to mark as completed: "))
            complete_task(tasks, index)
            save_tasks(tasks)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
