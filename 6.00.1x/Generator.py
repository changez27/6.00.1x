def genPrimes():
    num = 2
    while True:
        flag = 0
        for i in range(2,(int(num ** 0.5))+1):
            if num % i == 0:
                flag = 1
                break
        if flag == 0:
            yield num
        num += 1
        
foo = genPrimes()
print(foo.__next__())