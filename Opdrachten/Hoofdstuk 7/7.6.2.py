def faculteit(x):
    if x == 1:
        return 1

    return faculteit(x-1) * x

for i in range(1,7):
    print(faculteit(i))