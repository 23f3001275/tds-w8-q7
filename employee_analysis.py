"""
Employee Performance Visualization
Author: 23f3001275@ds.study.iitm.ac.in

This script:
- Loads employee dataset
- Counts number of Finance employees
- Prints frequency
- Creates histogram of department distribution
- Saves output as HTML
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# 1. Generate a sample dataset (100 employees, 15 finance)
# -----------------------------
import random

departments = (
    ["Finance"] * 15 +
    ["Engineering"] * 30 +
    ["HR"] * 20 +
    ["Marketing"] * 20 +
    ["Sales"] * 15
)

random.shuffle(departments)

data = {
    "Employee_ID": range(1, 101),
    "Department": departments
}

df = pd.DataFrame(data)


# -----------------------------
# 2. Count Finance department frequency
# -----------------------------
finance_count = (df["Department"] == "Finance").sum()
print("Finance Department Count:", finance_count)

# -----------------------------
# 3. Create histogram visualization
# -----------------------------
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Department", palette="viridis")
plt.title("Employee Count by Department")
plt.xlabel("Department")
plt.ylabel("Frequency")
plt.tight_layout()

# save plot separately
plt.savefig("department_hist.png")

# -----------------------------
# 4. Save everything to an HTML file
# -----------------------------
html_content = f"""
<html>
<head>
<title>Employee Performance Analysis</title>
</head>
<body>
<h1>Employee Performance Analysis</h1>
<p><b>Email:</b> 23f3001275@ds.study.iitm.ac.in</p>
<p><b>Finance Department Count:</b> {finance_count}</p>

<h2>Histogram of Departments</h2>
<img src="department_hist.png" width="600">

</body>
</html>
"""

with open("employee_analysis.html", "w") as f:
    f.write(html_content)

print("HTML file created: employee_analysis.html")
