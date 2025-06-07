import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

# NumPy
arr = np.array([1, 2, 3])
print("Array times 10:", arr * 10)

# Pandas
df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
print("DataFrame:\n", df)

# Matplotlib
plt.plot([1, 2, 3], [3, 2, 5])
plt.title("Sample Plot")
plt.show()

# Requests
r = requests.get("https://api.github.com")
print("GitHub API status:", r.status_code)
