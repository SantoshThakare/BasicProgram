

my_set1 = [1,3,5,9]
a= set(my_set1)
print(my_set1)
print(type(a))


my_set2 = [4,5,6,9]
b= set(my_set2)
print(my_set2)
print(type(b))

print("Union :", a | b)


print("Intersection :", a & b)


print("Difference :", a - b)

print("Symmetric difference :", a ^ b)