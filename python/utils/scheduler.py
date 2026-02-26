import schedule
import time

def job():
    print("Job executed!")

# Set the desired start time
start_time = "11:16"

# Schedule the job to run at the specified time
schedule.every().day.at(start_time).do(job)

while True:
    schedule.run_pending()
    time.sleep(1)


# pyinstaller --onefile scheduler.py  |  To create an executable program from your Python code