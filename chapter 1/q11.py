current_population = 312032486
secondInAYear = 31536000
year = 5
totalbirth= secondInAYear//7
totaldeath = secondInAYear//13
totalimmigrant = secondInAYear//45

population_in_year = year*(totalbirth-totaldeath+totalimmigrant)+current_population

print(population_in_year)

