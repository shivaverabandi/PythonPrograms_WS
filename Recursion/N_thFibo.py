# def nth_fibNum(n):
#     n1 = 0
#     n2 = 1
#     ans = 0
#     for i in range(n):
#         ans = n1 + n2
#         n1 = n2
#         n2 = ans

#     return ans


def fibo(n):
    if(n==1):
        return 1
    elif(n==0):
        return 0 
    
    ans = fibo(n-1) + fibo(n-2)
    return ans


n = int(input())

result = fibo(n)

print(result)