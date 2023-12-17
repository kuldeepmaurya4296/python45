#    6- Accept two numbers from user and swap their values
print("Enter two numbers")

n1 = int(input())
n2 = int(input())
print(f"----before swapping----\n{n1} is a and {n2} is b")
temp  = n1;
n1 = n2;
n2 = temp;
print(f"----After swapping----\n{n1} is a and {n2} is b")
