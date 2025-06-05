# for, for-else, while, while-else
# break, continue

l = [1,2,3, "false", "abd"]

for ele in l:
    if type(ele) == str:
        print(ele)


# find first string inside list and print
for ele in l:
    if type(ele) == str:
        print(ele)
        break

# find integers and add 10 to it
for ele in l:
    if type(ele) == int:
        print(ele + 10)
        continue
    if type(ele) == str:
        print(ele)
        break
else:
    print("exit from for loop when break statement does not executed")

# else block is always executed except when break statement hits

l = [1,2,3, "false", "abd"]
idx = 0
while idx < len(l):
    if type(l[idx]) == int:
        print(l[idx] + 10)
        idx = idx + 1
    elif type(l[idx]) == str:
        print(l[idx])
        break
    print("I am outside if block")
    idx += 1
else:
    print("exit from for loop when break statement does not executed")


d = {'k': 123, (1, 2, 3, 4): 123, (1, 2, 3, 4, 5): list(str(123))}
for k in d:
    print(k)    # prints only keys

for k, v in d.items():  # we have use d.items(), to get both key and values
    print(k, v)

# To show both index and value in a list / tuple we can use enumerate function
l = [1,2,3, "false", "abd"]
for i, v in enumerate(l):
    print(i, v)

l = (1,2,3, "false", "abd")
for i, v in enumerate(l):
    print(i, v)

# range() function
print(range(len(l)))
print(list(range(len(l))))

for i in range(len(l)):
    print(l[i])