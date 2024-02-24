def divisible(n):
    for i in range(n+1):
        if i%3==0 and i%4==0:
            yield i

n = int(input())
list1 = list(divisible(n))
print(f"List of divisivles by 3 and 4{list1}")