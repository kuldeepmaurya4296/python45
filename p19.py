# 19- Accept a year and check if it a leap year or not (google to find out what's a leap year)
# divide by 4; divide by 400 but not divide by 100

year = int(input("Enter year: "))
if((year % 4 == 0 and year % 100 !=0 )or year % 400 == 0): print(f"{year} is a Leap year")
else: print(f"{year} is Not leap year")
