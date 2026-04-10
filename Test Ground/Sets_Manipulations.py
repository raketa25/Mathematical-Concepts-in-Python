A = {1 ,2, 3, 4, 5, 6}
B = set(['A', 'B', 'C', 'D', 'E'])

# Union of A and B
C = A.union(B)
print(f"The union of A and B is: {C}")

#Intersection of A and B
D = A.intersection(B)
print(f"The intersection of A and B is: {D}")

# Difference of A and B
E = A.difference(B)
print(f"The difference of A and B is: {E}")

# Inclusion of A in B
F = A.issubset(B)
print(f"Is A a subset of B? {F}")

# Inclusion check

G = {1, 2}.issubset(A)
print(f"Is {{1, 2}} a subset of A? {G}")

# Equality check
print(A == B)
print({1, 2, 3, 4, 5, 6} == A)

# A Use case of List Comprehension to create a list of even numbers from 0 to 11
F = [x for x in range(0, 12) if x % 2 == 0]
print(f"The list of even numbers from 0 to 11 is: {F}")






