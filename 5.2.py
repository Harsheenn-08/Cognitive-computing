n=int(input("Enter the number"))
s=0
for i in range(1,n):
    if i%7==0 and i%9==0 :
        s=s+i
print("Sum is -->",s)
    