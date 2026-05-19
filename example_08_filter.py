# Datu filtrēšana

import pandas as pd

students = pd.read_csv("data/students.csv")

filtered = students[students["Atzime"] > 7]

print(filtered)