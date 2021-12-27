minutes = int(input("Enter the number of minutes : "))
days = minutes/1440
years = days//365
finalDays = days%365

print('{} minutes is approximately {:.0f} years and {:.0f} days'.format(minutes,years,finalDays))