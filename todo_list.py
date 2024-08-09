class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def clear_tasks(self):
        self.tasks.clear()

    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            status = "Completed" if task.completed else "Pending"
            task_str = f"|Task {i + 1}: {task.title:<25} | {task.description:<20} ({status})|"
            print(task_str)

    def edit_task_description(self, task_index, new_description):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].description = new_description
            print(f"Task '{task_index + 1}' description updated to '{new_description}'.")
        else:
            print("Invalid task number.")

    def set_task_priority(self, task_index, priority):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].set_priority(priority)
            print(f"Task '{self.tasks[task_index].description}' priority set to '{priority}'.")
        else:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Manager")
        print("1. Add a new task")
        print("2. List all tasks")
        print("3. Mark a task as completed")
        print("4. Remove a task")
        print("5. Edit a task description")
        print("6. Clear all tasks")
        print("7. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            title = input("Enter the task title: ")
            description = input("Enter the task description (optional): ")
            todo_list.add_task(title, description)
            print("Task added.")

        elif choice == '2':
            todo_list.list_tasks()

        elif choice == '3':
            todo_list.list_tasks()
            index = int(input("Enter the task number to mark as completed: "))
            todo_list.mark_task_completed(index)
            print("Task marked as completed.")

        elif choice == '4':
            todo_list.list_tasks()
            index = int(input("Enter the task number to remove: "))
            todo_list.remove_task(index)
            print("Task removed.")
        
        elif choice == '5':
            task_number = int(input("Enter the task number to edit: ")) - 1
            new_description = input("Enter the new task description: ")
            todo_list.edit_task_description(task_number, new_description)


        elif choice == '6':
            todo_list.clear_tasks()
            print("All tasks cleared.")

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()