# syntax --> []

# a = [1,2,3,4,5]

# b = [1,2,3,4,5]

# print(a == b)

# print(a is b)

# c = b

# print(c is b)

# c[2] = 34

# print(b[2])

# why list ? 
""""
list is linear data structure

heterogenous --> storing diffrent types. (mixed)


"""

li = [1,2,3,4,"manideep"]



a = li[-2] # length - 2 --> 5 - 2 = 3 which is li[3] is 4 

print(a)

"""
tuple is like immutable list

"""
tp1 = (1,2,3,4,5,5)

tp2 = (1,2,3,4,5)

print(tp1)
print(tp1 is tp2)

print(tp1[3])

# tp1[3] = 4

print(tp1)


li2 = [1,2,3,4,"manideep"]

li2 = tp1

print(li2)


# set 

hashSet = [1,2,3,3,4,4,2,1]

print(hashSet)

for i in range(hashSet.__len__()):
    a = hashSet.pop()
    print(a)


print(hashSet)

list = [1,2,3,4]


tp = (list,2,3,4,5)

tp[0][2] = 34

print(tp)