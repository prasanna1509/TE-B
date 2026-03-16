 m = 5

 for i in range(m):
    for j in range(m):
        print("*", end="")
    print()


n = 5

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
