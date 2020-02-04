import pandas as pd
from numpy.random import randn

# In the line below I need to pass: data, rows name, columns name.
x = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['First', 'Second', 'Third', 'Fourth'])

print(x)