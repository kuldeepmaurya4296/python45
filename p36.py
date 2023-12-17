n = int(input("Enter a number: "))
n2 = 0
while n>0:
    t=n%10;
    n2 = (n2*10)+t
    n//=10
print(n2)