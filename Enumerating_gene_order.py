import itertools
n=6
numbers = range(1, n+1)
permutations = list (itertools.permutations(numbers))
print (len(permutations))
for perm in permutations:
    print(*perm)
