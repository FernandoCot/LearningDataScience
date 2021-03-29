import pandas as pd
from numpy.random import randn

# In the line below I need to pass the following params: data, row names, column names.
x = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['First', 'Second', 'Third', 'Fourth'])

print(x)
