n= int(input("Enter a positive integer: "))

def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))

print("Fibonacci sequence:")
for i in range(n):
    print(fibo(i))