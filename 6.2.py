def addPrime(n):
    def checkPrime(n):
        for i in range(2,n//2+1):
            if n%i==0:
                return 0
        return 1
    
    s=0
    for i in range(2,n):
        if checkPrime(i):
            s=s+i
    return s

print("Sum is-->",addPrime(20))
print("Sum is-->",addPrime(30))
print("Sum is-->",addPrime(40))
print("Sum is-->",addPrime(50))



