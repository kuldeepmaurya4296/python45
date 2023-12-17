# 32- Check if the number is Prime or not.

n = int(input("Enter a number: "))
isPrime = True
for i in range(2,n):
    if(n%i==0):
        isPrime = False
        break
print("Prime number" if isPrime  else "Not prime number")