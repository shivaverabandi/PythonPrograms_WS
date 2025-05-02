
# str1 = "mani" * 1100

# str2 = "mani" * 1100


# # print(str1 == str2) # --> True

# # print(str1 is str2) # --> false


# import sys
# str1 = sys.intern(str1)
# str2 = sys.intern(str2)

# # print(str1 is str2)


str1 = str("mani")


str2 = "maniabc"

str3 = str1 + "abc"

str5 = "mani" + "abc"
print(str3)
print(str2)

print(str5 is str2) # True

print(str3 == str2) # True

print(str3 is str2) # False

str4 = "a" + "b" + "c" + str2 + "d"

str6 = "a" + "b" + "c" + "maniabc"  + "d"

print(str4 is str6) # False

