def computeCommission(salesAmount):
    commission = 0
    if salesAmount > 10000:
        commission = (5000 * 0.08) + (5000 * 0.1) + (salesAmount - 10000) * 0.12
    elif salesAmount > 5000:
        commission = 5000 * 0.08 + (salesAmount - 5000) * 0.1
    else:
        commission = salesAmount * 0.08

    return commission

def main():
    salesAmount = 10000 
    print("Sales Amount \t Commission")
    while salesAmount < 100001:
        print('{} \t\t {}'.format(salesAmount,computeCommission(salesAmount)))
        salesAmount += 5000
main()

