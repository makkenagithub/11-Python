t = (1,2,3,"true", [12,14,10])
print(t, type(t))
t1 = t[-1]
print(t1)

# tuple is an immutable data type
t[0] = 100  # it throws error. We cant change tuple values. This is diff b/w list and tuple
# TypeError: 'tuple' object does not support item assignment

print(t)

print(dir(t))
"""
count , index
"""

# to find index of a value in tuple, if we given non-existing value in the tuple as below, it throws error.
print(t.index("abc"))   # ValueError: tuple.index(x): x not in tuple

print(t.index("true")) # it gives 3 as index of "true"

t = (1,2,3,31,31,1,1,34,1,4,5,1,1,1,4)
# to count no. of 1's
print(t.count(1))


# unpacking concept - It works for list also
t = (1,2)
t1, t2 = t
print(t1, t2)    # o/p: 1 2
