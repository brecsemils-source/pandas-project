# Funkcijas pielietošana kolonnai

import pandas as pd


data = {
    "Punkti": [5, 7, 9]
}

frame = pd.DataFrame(data)

frame["Dubults"] = frame["Punkti"].apply(lambda x: x * 2)

print(frame)