# Tukšo vērtību aizvietošana

import pandas as pd


data = {
    "Punkti": [10, None, 7]
}

frame = pd.DataFrame(data)

filled = frame.fillna(0)

print(filled)