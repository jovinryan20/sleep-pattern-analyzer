# Sleep Pattern Analyzer 🛌

This is a simple beginner data science project where I try to understand sleep patterns using fake data.  
The idea is: phone logs can tell when people sleep and wake up, so I created a small dataset myself and analyzed it.

---

## Project Structure

sleep-analyzer/
│
├── data/
│ └── logs.csv # generated fake data
│
├── generate_data.py # script to create fake sleep data
├── analyze.py # script to analyze sleep duration
├── plot.py # script to visualize results
│
└── README.md

---

## 🚀 How to Run

1. Clone the repo or download the folder.
2. Open a terminal inside the folder.
3. Run these steps:

### Step 1: Generate fake data

python 

generate_data.py
This will create a file called logs.csv inside the data/ folder.

### Step 2: Analyze the data

python analyze.py
This will read logs.csv, calculate average sleep for each user, and save the results in user_sleep_summary.csv.

### Step 3: Visualize the results

python plot.py
This will show a bar chart of average sleep hours per user with healthy ranges marked.

### 📊 Example Output

logs.csv → daily sleep logs for a few fake users

user_sleep_summary.csv → each user’s average sleep and health status

Bar chart → compares user sleep with healthy range (7–9 hours)

Here’s an example of the sleep pattern visualization:

![Sleep Pattern Plot](outputs/sleep_plot.png)

### 🌱 What I Learned

- How to generate a dataset myself

- Basics of pandas for data analysis

- How to use matplotlib for simple plots

- How to organize a Python project

### 🔮 Future Improvements

- Make the dataset larger and more realistic

- Add clustering (group users by sleep type)

- Create an interactive dashboard

👨‍💻 This is just a beginner-friendly project I made to practice Data Science concepts.

### Created by Jovin Ryan Samuel ✨
