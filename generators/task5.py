def generator(n):
    for i in range(n, -1, -1):
        yield i
        
x = int(input())
list1 = list(generator(x))
print(*list1)