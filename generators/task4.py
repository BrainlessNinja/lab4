def square(a, b):
    for i in range(a, b+1):
        yield i**2
        
a = int(input())
b = int(input())
print(f"Series of square numbers in range({a}, {b}):" )

for i in square(a, b):
    print(i)