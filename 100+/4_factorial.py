n = int(input())
if n < 0:
    print("Factorial of -ve no. is not possible")
elif n == 0:
    print("1")
else:
    i = 1
    while n > 1:
        i = n*i
        n -= 1
    print(i)