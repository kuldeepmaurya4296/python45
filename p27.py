# 27- Sum up to n terms.
n = int(input("Enter a number: "));
sum = 0;
for i in range(n):
    sum+=i
print(f"Sum = {sum+n}")