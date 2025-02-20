def fibonacci(n):
    sequence=[0,1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

n=int(input("How many fibonacci's numbers to generate: "))
sequence=fibonacci(n)
print(f"With an input of {n} it will create the following sequence: : {sequence}")
