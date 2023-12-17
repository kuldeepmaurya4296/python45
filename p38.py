n = int(input("Enter a number: "))
temp = n;
sum = 0
while n>0:
    r = n%10;
    fact = 1;
    for i in range(1,(r+1)):
        fact *= i;
    sum+=fact;
    n//=10;
print("Strong number"if sum==temp else "Not a strong number")