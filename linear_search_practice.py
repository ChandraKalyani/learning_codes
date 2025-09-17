# Linear Search Practice

# Find the index of a given element in an array.
pos=-1
def search(arr,key):
    i=0
    while i<len(arr):
        if arr[i]==key:
            globals() ['pos']=i
            return True
        i+=1
    else:
        return False
arr=list(map(int,input().split()))
key=int(input())
if search(arr,key):
    print("Found at in didex at: ",pos)
else:
    print("Not found")



# Count how many times a given element appears in an array.

def search1(arr,key):
    count=0
    i=0
    while i<len(arr):
        if arr[i]==key:
            count+=1
        i+=1
    return count
arr=list(map(int,input().split()))
key=int(input())
print(search1(arr,key))
# Find the first occurrence and last occurrence of an element.
def search2(arr):
    first=arr[0]
    last=arr[(len(arr)-1)]
    for i in range(len(arr)):
        if arr[i]==first:
            print("first is: ",arr[i])
        if arr[i]==last:
            print("last is: ",arr[i])

arr=list(map(int,input().split()))
search2(arr)

# Find the maximum and minimum element in an array using linear search.
def search3(arr):
    max=arr[0]
    min=arr[0]
    i=0
    while i<len(arr):
        if arr[i]>max:
            max=arr[i]
        else:
            if arr[i]<min:
                min=arr[i]
        i+=1
    print("max is: ",max)
    print("min is: ",min)
arr=list(map(int,input().split()))
search3(arr)

# Check if an array is a palindrome using linear search.
s="chandu"
rev=""
for i in range(len(s)-1,-1,-1):
    rev=rev+s[i]
if s==rev:
    print("yes")
else:
    print("No")
