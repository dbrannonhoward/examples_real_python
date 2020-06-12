"""
vals = [expression for value in collection if condition]

vals = []
for value in collection:
    if condition:
        vals.append(expression)
"""

print([x * x for x in range(10) if not x % 2])
