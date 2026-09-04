import numpy as np
import pandas as pd
import matplotlib 
from pathlib import Path

win_path = Path(r"numpy\numpy_revision\output.csv")

read = pd.read_csv(win_path)

df = pd.DataFrame(read)

print(df.head)
#random_elements = df.iloc[5, 7]
#print(random_elements)

#print(df.dtypes)




