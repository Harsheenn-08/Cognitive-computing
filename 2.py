scores = (45,89.5,76,45.4,89,92,58,45)
highest = max(scores)
print("highest",highest)
highest_index=scores.index(highest)
print("highest index",highest_index)

lowest = min(scores)
print("lowest",lowest)
print("count",scores.count(lowest))

print(list(scores[::-1]))

a=int(input("Enter the no ."))
if(a in scores):
    pos= scores.index(a)
    print("First occurence of",a,"is-->",pos)
else:
    print("Not present")