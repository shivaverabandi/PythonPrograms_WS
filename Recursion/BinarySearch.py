
def binarySearch(list,target):
    start = 0
    end = len(list) - 1

    while(start <= end):
        mid = ( start + end ) // 2
        if(list[mid] == target):
            return mid
        elif(list[mid]<target):
            start = mid + 1
        else:
            end = mid - 1
    return -1



list = [2,3,4,5,7,9,13,16,20,27,30]
target = 4
index  = binarySearch(list,target)

if(index == -1):
    print("element Not found")
else:
    print("element is found at: ", index, "th index")
