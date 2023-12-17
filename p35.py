n = int(input("Enter a number: "))
list = [];
while n > 0:
    list.append(n%10);
    n//=10;
print(list)
sum1 = 0;
for i in list:
    sum1 += i;
print(sum1)