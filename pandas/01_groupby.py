import pandas as pd

data = {
    "name": ["A", "B", "C", "D", "E"],
    "department": ["AI", "AI", "CS", "CS", "AI"],
    "marks": [85, 92, 78, 88, 95]
}

df = pd.DataFrame(data)

result = df.groupby("department")["marks"].agg(
    ["mean", "max", "min"]
)

print(result)