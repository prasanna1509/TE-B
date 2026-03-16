n = 5

for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()

n = 5

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

print("  *****  ")
print(" *     * ")
print("*  * *  *")
print("*       *")
print("*  ---  *")
print(" *     * ")
print("  *****  ")

print("         /\\_/\\ ")
print("         ( o o )")
print("          = ^ = ")
print("THE CAT WILL PROVIDE FACTORIAL")

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

num = 5
print(f"Factorial of {num} is {factorial(num)}")
