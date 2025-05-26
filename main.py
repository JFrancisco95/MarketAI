from market_bias import get_market_bias
from task_manager import add_task, list_tasks, mark_done

def main():
  while True:
    print("\nFinance Assistant Menu:")
    print("1. Get Market Bias")
    print("2. Add Task")
    print("3. List Tasks")
    print("4. Mark Task as Done")
    print("5. Exit")
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
      index=int(input("Enter the task index to mark as done: ")) - 1
      mark_done(index)

    elif choice == '5':
      print("Exiting...")
      break

    else: 
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()