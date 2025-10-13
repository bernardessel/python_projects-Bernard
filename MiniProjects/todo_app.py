"""
Simple To-Do List (Beginner-friendly)

This is a small command-line application that lets you:
 - add tasks
 - list tasks
 - mark tasks as completed
 - delete tasks

The code is written with clear comments and simple input checks so a beginner
can read and understand how it works.
"""

# In-memory list to store tasks. Each task is a dictionary with keys:
# - 'text': the task description (string)
# - 'done': completion flag (bool)
tasks = []


def add_task():
    """Prompt the user to enter a new task and add it to the list."""
    text = input("Enter a new task (or leave empty to cancel): ").strip()
    if text == "":
        print("No task added.\n")
        return
    tasks.append({"text": text, "done": False})
    print(f"Added: {text}\n")


def view_tasks():
    """Print all tasks with their number and status."""
    if not tasks:
        print("No tasks yet. Add one from the menu.\n")
        return

    print("\nYour Tasks:")
    for i, t in enumerate(tasks, start=1):
        status = "[x]" if t["done"] else "[ ]"
        print(f"{i}. {status} {t['text']}")
    print()


def choose_task(prompt):
    """Ask the user to pick a task number. Return the index (0-based) or None.

    This helper keeps input handling in one place and returns None when the
    user cancels or enters invalid input.
    """
    if not tasks:
        print("No tasks to choose from.\n")
        return None

    try:
        choice = input(prompt).strip()
        if choice == "":
            print("Cancelled.\n")
            return None
        num = int(choice)
        if 1 <= num <= len(tasks):
            return num - 1
        print("Number out of range.\n")
    except ValueError:
        print("Please enter a valid number.\n")
    return None


def mark_completed():
    """Mark a selected task as completed."""
    view_tasks()
    idx = choose_task("Enter task number to mark completed (or press Enter to cancel): ")
    if idx is None:
        return
    tasks[idx]["done"] = True
    print(f"Marked completed: {tasks[idx]['text']}\n")


def delete_task():
    """Delete a selected task from the list."""
    view_tasks()
    idx = choose_task("Enter task number to delete (or press Enter to cancel): ")
    if idx is None:
        return
    removed = tasks.pop(idx)
    print(f"Deleted: {removed['text']}\n")


def main():
    """Main loop that shows the menu and reacts to user choices."""
    while True:
        print("=== SIMPLE TO-DO LIST ===")
        print("1) Add task")
        print("2) View tasks")
        print("3) Mark task completed")
        print("4) Delete task")
        print("5) Exit")

        choice = input("Choose (1-5): ").strip()
        print()
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Please choose a number between 1 and 5.\n")


if __name__ == "__main__":
    main()
