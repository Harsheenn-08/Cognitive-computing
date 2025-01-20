def addOdd(n):
    s=0
    for i in range(2,n):
        if i%2 != 0:
            s=s+i
    return s
        
print("Sum is -->",addOdd(20))
print("Sum is -->",addOdd(30))
print("Sum is -->",addOdd(40))
print("Sum is -->",addOdd(50))