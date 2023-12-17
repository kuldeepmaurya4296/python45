# 29- Print the sum of all even & odd numbers in a range seperately.

a = int(input("Enter a number: "))
oddSum = 0
evenSum = 0;

for i in range(a):
    if(i%2==0): evenSum+=i;
    else: oddSum +=i;
print(f"Sum of all even {evenSum} and odd {oddSum} in range {a}")