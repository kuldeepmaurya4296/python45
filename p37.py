n = int(input("Enter a number: "))
temp = n;
n2 = 0
while n > 0:
    r = n%10;
    n2 = (n2*10)+r;
    n//=10;
print("Palindrome number" if temp==n2 else "Not Palindrome number")