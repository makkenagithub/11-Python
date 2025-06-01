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
print(d.items())    # returs list of tuples

