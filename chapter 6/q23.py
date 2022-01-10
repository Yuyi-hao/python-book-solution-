def converMillis(millis):
    second = millis//1000
    minute = second//60
    rsecond = second%60
    hour = minute//60
    rminute = minute%60
    time = f'{hour} : {rminute} : {rsecond}'
    return time 

def main():
    millis = int(input("Enter milliseconds : "))
    print(converMillis(millis))

main()