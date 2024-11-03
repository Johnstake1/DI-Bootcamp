import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('operations.csv',parse_dates=[0])

import matplotlib.pyplot as plt

# QUALITATIVE VARIABLE
# Pie chart
data["categ"].value_counts(normalize=True).plot(kind='pie')
# This line ensures that the pie chart is circular, not elliptical
plt.axis('equal') 
plt.show() # Displays the graph

# Bar graph
data["categ"].value_counts(normalize=True).plot(kind='bar')
plt.show()

# QUANTITATIVE VARIABLE
# Vertical line graph
data["quart_month"].value_counts(normalize=True).plot(kind='bar',width=0.1)
plt.show()

# Histogram
data["amount"].hist(normed=True)
plt.show()
# Prettier Histogram
data[data.amount.abs() < 100]["amount"].hist(density=True,bins=20)
plt.show()
