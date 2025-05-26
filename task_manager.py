import json
import os
from datetime import datetime


TASKS_FILE = 'data/tasks.json' 

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as f: 
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def add_task(task, due=None):
  tasks = load_tasks()
  tasks.append({
    'task': task,
    'due': due,
    'done': False,})
  save_tasks(tasks)

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
    print(f"Task {index+1} marked as done.")
  else:
    print("Invalid task index.")