#daily_log

import datetime

entry = input("what did you do today...")
today = datetime.date.today()

with open("daily_log.txt", "a") as f:
    f.write(f"{today}: {entry}\n")

print("log saved.")