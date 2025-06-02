# dictionary is key value pair based
d = {'k': 12}
print(d['k'])   #o/p: 12

d = {'k': 12, 'k': 123}
print(d['k'])   #o/p: 123
# so better not use duplicate keys in python

d = {'k': 12, [1,2,3]: 123}
print(d[[1,2,3]])       # o/p: TypeError: unhashable type: 'list'

d = {'k': 12, (1,2,3): 123}
print(d[(1,2,3)])       # o/p: 123
# so key should always be of immutable data type. Key should not be mutable datat type

d = {'k': 12, (1,2,3): 123, (1,2,3,4): list(str(123))}
print(k[(1,2,3,4)])     o/p: ['1', '2', '3']
# we use list(str(123)) regularly. It returns a list. String converted to list of individual characters.


print(dir(d))
"""
clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
"""
print(d.keys())
print(d.values())
print(d.items())    # returs list of tuples  # [('k', 123), ((1, 2, 3, 4), 123), ((1, 2, 3, 4, 5), ['1', '2', '3'])]

# dictionary is a mutable data type.
d['k'] = 456
print(d)




# set
s = {'a', 'b', 'c', 'a'}
print(s)    # o/p; {'b', 'a', 'c'}
# set does not allow dupkicate values. Set does not follow order of values given in set
# set is immutable data type. We cant change the values of set once we define it.

s[0] = 'abc'    # TypeError: set does not support item assignment

print(dir(s))
"""
'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 
'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 
'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'
"""

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)  #o/p: True
print("banssanaa" in thisset)  #o/p: False
print("banana" not in thisset)  #o/p: False

# in or not in  operator can be used for list, set, tuples etc
