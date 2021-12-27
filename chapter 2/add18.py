gmt = 5.3
gmt = 7

# converting gmt to hours 

# getting hours from gmt 
gmthours = int(gmt)
gmtminute = ((gmt*100)%100)/60

print(gmthours,gmtminute)