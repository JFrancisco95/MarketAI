import os
import json
import time
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

History_File = 'data/task_history.json'
Logs_Dir= 'data/daily_logs'

def save_daily_log():
  if not os.path.exists(History_File):
    print("[Log]No history found.")
    return

  with open(History_File, 'r') as f:
    history = json.load(f)

  if not history:
      print("[Log]History is empty, nothing to save")
      return
  os.makedirs(Logs_Dir, exist_ok=True)
  log_filename = os.path.join(Logs_Dir, f"{datetime.now().strftime('%Y-%m-%d')}.json")

  with open(log_filename, 'w') as f:
    json.dump(history, f, indent=2)

    print(f"[Log]Daily log saved to {log_filename}")

def clear_history():
    with open(History_File, 'w') as f:
        f.write('[]')
    print("[Log]History cleared.")

def daily_job():
  print(f"\n[Scheduler] Running daily job at {datetime.now()}")
  save_daily_log()
  clear_history()
  print(f"[Scheduler] Daily job completed at {datetime.now()}")

def start_background_scheduler():
  scheduler = BackgroundScheduler()
  scheduler.add_job(daily_job, 'cron', hour=0, minute=0)  # Runs daily at midnight
  scheduler.start()
  print("[Scheduler] Background scheduler to run daily at 00:00.")

  try:
    while True:
      time.sleep(60)   # Keep the script running
  except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
    print("[Scheduler] Shutdown.")

if __name__ == "__main__":
  print("[Scheduler] Starting background scheduler...")
  start_background_scheduler()