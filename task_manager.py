import json
import os
from datetime import datetime

History_File = 'data/task_history.json'
TASKS_FILE = 'data/tasks.json'

def log_history(entry):
  if not os.path.exists(History_File):
    history = []
  else:
    with open(History_File, 'r') as f:
      history = json.load(f)
    history.append(entry)
    with open(History_File, 'w') as f:
      json.dump(history, f, indent=2)

def load_tasks():
  if not os.path.exists(TASKS_FILE):
    return []
  with open(TASKS_FILE, 'r') as f:
    return json.load(f)

def save_tasks(tasks):
  with open(TASKS_FILE, 'w') as f:
   json.dump(tasks, f, indent=2)

def add_task(task, due=None):
  if not task.strip():
    print("Task cannot be empty.")
    return
  tasks = load_tasks()
  tasks.append({
  'task': task,
  'due': due,
  'done': False,
  })
  save_tasks(tasks)

def remove_task(task):
  tasks = load_tasks()
  removed = None
  filtered = []
  for t in tasks:
    if t['task'] == task and removed is None:
      removed = t
    else:
      filtered.append(t)
  if removed:
    log_history({
      'action': 'removed',
      'task': removed['task'],
      'was_done': removed['done'],
      'timestamp': datetime.now().isoformat()
    })
    save_tasks(filtered)
    print(f"Task '{task}' removed.")
  else:
    print(f"Task '{task}' not found.")
  return filtered

def list_tasks():
  tasks = load_tasks()
  if not tasks:
    print("No tasks found.")
    return
  for i, t in enumerate(tasks):
    status = 'Done' if t['done'] else 'Pending'
    due = f"Due: {t['due']}" if t['due'] else ''
    print(f"{i+1}. {t['task']} - {status} {due}")

def mark_done(index):  
  tasks = load_tasks()  
  if 0 <= index < len(tasks):
    tasks[index]['done'] = True
    save_tasks(tasks)
    log_history({
      'action': 'mark_done',
      'task': tasks[index]['task'],
      'timestamp': datetime.now().isoformat()
    })
    print(f"Task {index+1} marked as done.")
  else:
    print("Invalid task index.")

def view_history():
  if not os.path.exists(History_File):
    print("No history found.")
    return  

  with open(History_File, 'r') as f:
    history = json.load(f)

  if not history:
    print("History is empty.")
    return

  for entry in history:
    line = f"{entry['timestamp']} - {entry['action']} - {entry['task']}"
    if entry['action'] == 'removed' and 'was_done' in entry:
      status = 'Done' if entry['was_done'] else 'Pending'
      line += f" ({status})"
    print(line)