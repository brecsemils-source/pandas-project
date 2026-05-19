# Tukšo vērtību dzēšana

import pandas as pd


data = {
    "Punkti": [10, None, 7]
}

frame = pd.DataFrame(data)

clean = frame.dropna()

print(clean)