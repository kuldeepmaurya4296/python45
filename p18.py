print("Enter three numbers")
num1 = int(input())
num2 = int(input())
num3 = int(input())

if (num1 > num2 and num1 > num3): print(f"{num1} is Greatest number among them")
elif (num2 > num1 and num2 > num3): print(f"{num2} is Greatest number among them")
else: print(f"{num3} is greates among them")