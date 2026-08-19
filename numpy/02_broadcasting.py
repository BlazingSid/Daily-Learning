import numpy as np

marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [88, 92, 95]
])

bonus = np.array([5, 3, 2])

result = marks + bonus

print("Original:")
print(marks)

print("\nAfter broadcasting:")
print(result)