a={34,56,78,90}
b={78,45,90,23}
print("union of a and b",a|b)
print("intersection of a and b",a&b)
print("difference of a and b",a-b)
print("difference of b and a",b-a)

is_a_subset_of_b= a.issubset(b)
is_b_superset_of_a= a.issuperset(b)
print("Are scores of team a a subset of team b?", is_a_subset_of_b)
print("Are scores of team b a superset of team a?", is_b_superset_of_a)

x=int(input("Enter a score to remove from set "))
if x in a:
    a.remove(x)
    print("Removed and updated set is -->",a)
else:
    print("Not found")