import time 
n1 = int(time.time()) % 25 + 65
n2 = int(time.time()) % 25 + 97

print("upper case {} lower case  {}".format(chr(n1),chr(n2)))