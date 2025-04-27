"""
--> Key words in Exception Handling 
1. try --> risky code
2. except --> catch appropriate exception
3. finally --> closing resources
4. raise --> raise exception explicitly.

"""

a = int(input())
b = int(input())

print("Before Division..")
try:
    print("Try to divide")
    c = a/b
    print(c)
    #Excption
    print("Successful")
except Exception as e:
    print("Not able to divide with zero")


print("after division..")


