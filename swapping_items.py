fruits = ["apples", "oranges", "grapes", "strawberries"]
first = fruits[0]
last = fruits[3]
fruits[0] = last
fruits[-1] = first
print(f"Updated fruit list: {fruits}")