# Write an if statement to determine whether a variable holding a year
# is a leap year.

year = int(input('Enter a year: '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, 'is leap year')
        else:
            print(year, 'is not leap year')
    else:
        print(year, 'is leap year')
else:
    print(year, 'is not leap year')



