# set Operations and Methods 
X = {1, 2,3, 4, 5}

Y = set([1,2,3,4,5])

# set operators
# 1. Union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
 
X = set1 | set2
print(X)

# 2.Intersection
Y = set1 & set2
print(Y)

# 3.difference
Z = set1 - set2
print(Z)

# 4. sysmmetric Difference
A = set1 ^ set2
print(A)


# Set methods
# 1. add
X = {1,2,3,4,5}
X.add(6)
print(X)

# 2. remove
X.remove(5)
print(X)
# 3. discard
X.discard(2)
print(X)
# 4. pop
X.pop()
print(X)
# 5. clear
X.clear()
print(X)
# 6. copy
X.copy()
print(X)
# 7. update
X.update({7,8,9})
print(X)

















