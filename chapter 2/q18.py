import time 

gmt = eval(input("Enter the time zone offset to GMT (e.g. +5) : "))

# converting gmt to hours 

# getting hours from gmt 
gmthours = int(gmt)
gmtminute = ((gmt*100)%100)/60

agmt = gmthours+gmtminute

# converting gmt hours to second
gmtsecond = agmt*3600
currentTime = time.time()
actualSecond = currentTime + gmtsecond
# get second 
second = int(actualSecond)
#get minute 
minute = second//60
#get remaining second 
rsecond = second%60 
#get hours 
hours = minute//60
#current hour 
currentHours = hours%24
# get remaining minutes 
rminute = minute%60 

print("{}:{}:{} GMT".format(currentHours,rminute,rsecond))