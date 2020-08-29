def primes():
    yield 2
    a = 2
    a += 1
    while True:
        
        b = 0
        for i in range(1, a + 1, 2):
            if a % i == 0:
                b += 1
                # print(i, b)
                if b == 3:
                    break
        if b == 2:
            yield a
        a += 2
        
x = primes()
print (next(x))
print (next(x))
print (next(x))
print (next(x))
print (next(x))
print (next(x))