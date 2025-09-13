arr=list(map(int,input().split()))

print(len(arr))

for i in range(len(arr)):
    print(arr[i],end=" ")

print()
arr.pop(3)                #To remove elements by using index.
print(arr)        

arr.remove(5)             #To remove by using elements in input.
print(arr)

arr.insert(0,2)           #To insert element by using index.
print(arr)              

arr.append(10)            #To insert element at the end of the list.
print(arr)

arr.index(10)             #To know the index of the element.
print(arr)

arr.sort()                #To arrange a elements assending order.
print(arr)

arr.sort(reverse=True)    #To arrange a elements in desending order.
print(arr)

print(arr[0:6:2])         #sliceing.

print(arr[-1:-5:-3])      #slicing.