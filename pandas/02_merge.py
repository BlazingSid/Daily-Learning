import pandas as pd

students = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Shahid", "Raj", "Alex"]
})

marks = pd.DataFrame({
    "id": [1, 2, 3],
    "marks": [92, 85, 88]
})

result = pd.merge(students, marks, on="id")

print(result)