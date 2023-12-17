a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
ans = 1
for i in range(1,(a+1)):
    ans*=b
print(ans)
