arr=list(map(int,input().split()))

print(len(arr))

for i in range(len(arr)):
    print(arr[i],end=" ")

print()
 #To remove elements by using index.
arr.pop(3)               
print(arr)        

 #To remove by using elements in input.
arr.remove(5)            
print(arr)

 #To insert element by using index.
arr.insert(0,2)          
print(arr)              

#To insert element at the end of the list.
arr.append(10)          
print(arr)

#To know the index of the element. 
arr.index(10)                
print(arr)

 #To arrange a elements Ascending order.
arr.sort()               
print(arr)

 #To arrange a elements in Descending order.
arr.sort(reverse=True)   
print(arr)

# Slicing
print(arr[0:6:2])        
print(arr[-1:-5:-3])    
