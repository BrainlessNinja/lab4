def SqrGenerator(n):
    for i in range(n):
        yield i**2

x = int(input())
for i in SqrGenerator(x):
    print(i)