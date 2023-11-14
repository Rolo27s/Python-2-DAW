numbers = list(range(1, 6))
calls = 0

for i in range(6, 24, 6):
    result = list(map(lambda n, i = i: n * i, numbers))
    calls += len(numbers)
    print(result)

print(calls)
