n = int(input("Enter 1- Addition \n2- Substraction \n3 - Multiplication \n4- Division \n"))
a = int(input("Enter your first number: "))
b = int(input("Enter your Second number: "))
if(n==1): print(a+b);
elif(n==2): print(a-b);
elif(n==3): print(a*b);
elif(n==4): print(a/b);
else: print("Wrong Input")