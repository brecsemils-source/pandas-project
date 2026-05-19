# Saglabāšana CSV failā

import pandas as pd


data = {
    "Vards": ["Anna", "Juris"]
}

frame = pd.DataFrame(data)

frame.to_csv("output.csv", index=False)

print("Fails saglabāts")