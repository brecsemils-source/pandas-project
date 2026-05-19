# Grafiku veidošana

import pandas as pd
import matplotlib.pyplot as plt


data = {
    "Mēnesis": ["Jan", "Feb", "Mar"],
    "Pārdošana": [100, 150, 200]
}

frame = pd.DataFrame(data)

frame.plot(x="Mēnesis", y="Pārdošana")

plt.show()