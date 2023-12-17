import math;

print("Enter three sides of triangle: ")
a = float(input())
b = float(input())
c = float(input())
s = (a+b+c)/2;
area = float(math.sqrt(s*(s-a)*(s-b)*(s-c)));
print(f"The area of the given triangle is {area}")