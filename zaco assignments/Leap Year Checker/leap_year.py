year = int(input('Enter the year: '))

if (year % 100 == 0 and year % 400 == 0):
    print("Entered Year {} is Leap year ".format(year))

elif (year % 4 == 0):
    print("Entered Year {} is a leap year".format(year))

else:
    print("Entered year {} is NOT leap year".format(year))
