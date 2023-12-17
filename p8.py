#//8- Accept the parameters and calculate the Compound Interest &
    # // print it on STDOUT (Use Math class methods)

p = float(input("Enter the amount: "))
r = float(input("Enter the Rate: "))
n = float(input("Enter the Number of year: "))
x = float(input("Enter the number of period in a year: "))
nt = x*n;
A = p*(1+r/100)**nt;
print(f"Ammount is {A} and intrest is {A-p}")