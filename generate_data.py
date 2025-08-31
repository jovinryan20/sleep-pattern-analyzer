import csv
import random
from datetime import date, timedelta

today = date.today()

with open("logs.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["user", "date", "sleep_start", "sleep_end"])  # hours in 0-23
    for user in range(1, 6):            # 5 users
        for d in range(7):             # last 7 days
            day = today - timedelta(days=d)
            # bedtime around late night: choose 22..26 then mod 24 to allow after-midnight values
            bed = random.randint(22, 26) % 24
            wake = random.randint(6, 9)   # wake between 6 and 9
            writer.writerow([user, day.isoformat(), bed, wake])

print("Wrote logs.csv (sample phone sleep logs).")
