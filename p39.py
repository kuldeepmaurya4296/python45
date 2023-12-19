import math;

n = int(input("Enter a number: "))
t= n;
squre_n = math.pow(n,2);
ans = 0
ans2 = 0;
while n>0:
    r = squre_n%10;
    ans = (10*ans)+r;
    n//=10;
    squre_n//=10;
print(ans)
while ans>0:
    r= ans%10;
    ans2 = (10*ans2)+r;
    ans//=10;
print(ans2);
print(t);
print(ans2==t);
    