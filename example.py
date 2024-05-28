print("Fibonacci")
limit = int(input("Entrada "))
a, b = 0, 1
while a < limit:
    print(a)
    sum = a + b
    a = b
    b = sum

