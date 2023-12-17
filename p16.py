# Print after how many years the user will be eligible
name = input("Enter your name: ");
age = int(input("Enter your age: "))
if(age >= 18): print(f"Hello! {name} you are a valid voter.")
else: print(f"Sorry! {name} your are a valid voter after {18-age} years.")