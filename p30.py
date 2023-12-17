# //30- Print all the factors of a number.50 -> 1  2  5  10  25 50
n = int(input("Enter a number: "))
list = []
for i in range(1,(n+1)):
    if( n % i == 0): list.append(i)
print(list)