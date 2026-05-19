# Tabulu apvienošana

import pandas as pd

left = pd.DataFrame({
    "ID": [1, 2],
    "Vards": ["Anna", "Juris"]
})

right = pd.DataFrame({
    "ID": [1, 2],
    "Atzime": [9, 7]
})

merged = pd.merge(left, right, on="ID")

print(merged)