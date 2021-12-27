current_population = 312032486
secondInAYear = 31536000
year = eval(input("Enter number of years : "))
totalbirth= secondInAYear//7
totaldeath = secondInAYear//13
totalimmigrant = secondInAYear//45

population_in_year = (year*(totalbirth-totaldeath+totalimmigrant)+current_population)

print('The population in {} year is {}'.format(year,population_in_year))