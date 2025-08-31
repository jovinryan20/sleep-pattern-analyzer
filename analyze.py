# analyze.py
import pandas as pd

df = pd.read_csv("logs.csv")

# Ensure integer hours
df["sleep_start"] = df["sleep_start"].astype(int)
df["sleep_end"] = df["sleep_end"].astype(int)

# Duration handling across midnight: use modulo 24
df["duration"] = (df["sleep_end"] - df["sleep_start"]) % 24

# Average sleep per user
summary = df.groupby("user")["duration"].mean().reset_index()
summary["avg_sleep"] = summary["duration"].round(2)

# Simple classification
def classify(hours):
    if 7 <= hours <= 9:
        return "Good"
    elif 6 <= hours < 7:
        return "Okay"
    else:
        return "Poor"

summary["sleep_health"] = summary["avg_sleep"].apply(classify)
summary = summary[["user", "avg_sleep", "sleep_health"]]

print(summary)
summary.to_csv("user_sleep_summary.csv", index=False)
print("Wrote user_sleep_summary.csv")
