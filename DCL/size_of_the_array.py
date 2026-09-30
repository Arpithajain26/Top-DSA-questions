def size_of_array(arr):
    i=0
    j=len(arr)-1
    while i<j:
        i+=1
        j-=1
    if i==j:
        return "odd"
    else:
        return "even"
print(size_of_array([1,2,3,4,5,6]))
print(size_of_array([1,2,3]))