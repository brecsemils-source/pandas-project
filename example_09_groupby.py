# Grupēšana

import pandas as pd

students = pd.read_csv("data/students.csv")

result = students.groupby("Kurss").mean()

print(result)