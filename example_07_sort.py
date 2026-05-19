# Datu kārtošana

import pandas as pd

students = pd.read_csv("data/students.csv")

sorted_data = students.sort_values(by="Atzime")

print(sorted_data)