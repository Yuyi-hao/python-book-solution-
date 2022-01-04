salesAmount = 1.01
commission = 0
while commission < 5000:
    if salesAmount > 10000:
        commission = 5000 * 1.08 + 5000 * 1.1 + (salesAmount - 10000) * 1.12

    elif salesAmount >= 5001:
        commission = 5000 * 1.08 + (salesAmount - 5000) * 1.10

    else:
        commission = salesAmount * 1.08
        salesAmount += 1.01
print(salesAmount)