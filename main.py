from datetime import datetime
from market_bias import get_market_bias
from task_manager import add_task, list_tasks, log_history, mark_done, load_tasks, save_tasks, view_history


def main():
  if not sys.stdin.isatty():
      print("This script should be run in an interactive terminal.")
      return
  while True:
    print("\nFinance Assistant Menu:")
    print("1. Get Market Bias")
    print("2. Add Task")
    print("3. List Tasks")
    print("4. Mark Task as Done")
    print("5. Remove Task")
    print("6. View History")
    print("7. Exit")
    choice = input("Enter your choice: ").strip()

    if choice == '1':
      print("\nGetting Market Bias...")
      print(get_market_bias())

    elif choice == '2':
      task = input("Enter the task: ")
      due = input("Enter due date (YYYY-MM-DD): ")
      add_task(task, due if due else None)
      print("Task added.")

    elif choice == '3':
      print("\nListing Tasks...")
      list_tasks()

    elif choice == '4':
      index = int(input("Enter the task index to mark as done: ")) - 1
      mark_done(index)

    elif choice == '5':
      tasks = load_tasks()
      if not tasks:
        print("No tasks found.")
        continue
      for i, t in enumerate(tasks):
        status = 'Done' if t['done'] else 'Pending'
        print(f"{i+1}. {t['task']} - {status}")
      try: 
        index = int(input("Enter the task index to remove: ")) - 1
      
      except ValueError:
        print("Invalid input. Please enter a number.")
      if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        save_tasks(tasks)
        log_history({
          'action': 'removed',
          'task': removed_task['task'],
          'timestamp': datetime.now().isoformat()
        })
        print(f"Task '{removed_task['task']}' removed.")
      else:
        print("Invalid task index.")
    elif choice == '6':
      view_history()

    elif choice == '7':
      print("Exiting...")
      break

    else:
      print("Invalid choice. Please try again.")


if __name__ == "__main__":
  main()
