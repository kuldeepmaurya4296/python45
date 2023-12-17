# 26- Take a number as input and print its table
    #    5 * 1 = 5
    #    5 * 2 = 10 ... up to 10 terms
    
a = int(input("Enter your number: "))
i = 1;
for i in range(11,20):
    print(f"{a} * {i+1} = {(i+1)*a}")