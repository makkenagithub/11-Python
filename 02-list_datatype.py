l = [1, 2, 3, 4, "suresh", True, False, ["suresh", 4, 5, 6, False, [7, 8], "abc"]]
print(l)
print(l, type(l))

l1 = l[3]
print( l1 )
l2 = l[7][0]
print( l2 )
print( l[-1][0] )

print( len(l) )

print( l[len(l) - 1] )


print( dir(l) )

"""
'append', 'clear', 'copy', 'count', 'extend', 'index', 
'insert', 'pop', 'remove', 'reverse', 'sort'
"""

l = ["suresh", 4, 5, 6, False, "abc"]

# append an element at end of the list
l.append(True)
print( l )
l.append( [10, 20, 30] )
l.insert(0, "abc")

l = [1,2,3]
l.extend([10,20,30])
print(l)        # o/p: [1,2,3,10,20,30]

l = [2,6,1,3]
l.sort()        # sort is inplace operation. It changes l value. Means it effetcs original list
print(l)

# we sorted function
l1 = sorted(l)  # sorted returns a new list. This does not effect original list
print(l1)

# list is a mutable data type. Means we can change its values even after declaring its values
l = [1,2,3,4,5]
l[2] = 500
print(l)

