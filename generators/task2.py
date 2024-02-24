def generator(n):
    for i in range(n+1):
        if i%2 == 0:
            yield i
            
x = int(input())
list1 = ', '.join(map(str, generator(x)))
print(list1)