import matplotlib.colors
import seaborn as sns
from cycler import cycler
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import pandas as pd  # Assuming you need pandas for DataFrame operations

# Sample data for demonstration (remove or replace this with your actual data loading code)
df = pd.DataFrame({
    "Annual Mean": np.random.randn(50).cumsum(),
    "Lowess Smoothing": np.random.randn(50).cumsum()
})
df.index = pd.date_range(start="1950", periods=50, freq="Y")

# Configuration settings
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '--'
mpl.rcParams["figure.figsize"] = (10, 6)
mpl.rcParams["font.size"] = 14
mpl.rcParams["axes.grid"] = True
mpl.rcParams["axes.grid.axis"] = "y"
mpl.rcParams['axes.spines.bottom'] = True
mpl.rcParams['axes.spines.left'] = False
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False
mpl.rcParams['axes.linewidth'] = 0.5
mpl.rcParams['ytick.major.width'] = 0
mpl.rcParams['ytick.major.size'] = 0

# Sample plot (remove this if you already have your data and plotting code)
data = np.random.randn(50)
plt.plot(data)

# Your actual plotting code
fig, ax = plt.subplots()

df["Annual Mean"].plot(ax=ax, c="black", marker="s")
df["Lowess Smoothing"].plot(ax=ax, c="red")

x = df.index.tolist()
y = df["Annual Mean"].tolist()

# Define the 95% confidence interval
ci = np.mean(y) + 1.96 * np.std(y) / np.sqrt(len(y))
plt.fill_between(x, y - ci, y + ci, color="gray", alpha=0.25, label="LSAT+SST Uncertainty")

ax.axhline(y=0, linestyle="--", color="black")
plt.legend(loc="upper left")
plt.ylabel("Temperature anomaly w.r.t. 1951-80 mean (°C)")
plt.title("Global surface air temperature change estimates based on land and ocean data")
plt.savefig("C:\\Users\\SBS\\Desktop\\graph.png", dpi=300)

plt.show()
