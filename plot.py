# plot.py
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("user_sleep_summary.csv")

plt.figure(figsize=(6,4))
plt.bar(df["user"].astype(str), df["avg_sleep"])
plt.axhline(7, linestyle="--", linewidth=1, label="Healthy min (7h)")
plt.axhline(9, linestyle="--", linewidth=1, label="Healthy max (9h)")
plt.xlabel("User")
plt.ylabel("Average sleep (hours)")
plt.title("Average sleep per user (sample)")
plt.legend()
plt.tight_layout()
plt.savefig("sleep_plot.png")
print("Saved sleep_plot.png")
plt.show()
