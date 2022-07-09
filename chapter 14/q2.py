def main():
    entry = input('Enter the numbers (seprated by one space) : ').strip()
    nums = [int(item) for item in entry.split()]
    max = 0
    maximumNums = []
    count = {}
    for i in nums:
        if i in count:
            count[i] +=1
        else:
            count[i] = 1
        if count[i] == max:
            maximumNums.append(i)
        elif count[i]>max:
            max = count[i]
            if len(maximumNums):
                maximumNums.clear()
            maximumNums.append(i)

    print('Entry with most occurrence ' + ('are' if len(maximumNums)>1 else 'is ')+ ': ')
    for j in maximumNums:
        print(f'{j} : {count[j]}')
main()
