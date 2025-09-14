pos=-1
def search(arr,key):
    l=0
    u=len(arr)-1
    while l<=u:
        mid=(l+u)//2
        if arr[mid]==key:
            globals() ['pos']=mid
            return True
        else:
            if arr[mid]<key:
                l=mid+1
            else:
                u=mid-1

arr=list(map(int,input().split()))
key=int(input())
if search(arr,key):
    print("Found at index: ",pos)
else:
    print("not found")




#by using foor loop
pos=-1
def search(arr,key):
    l=0
    u=len(arr)-1
    for i in range(l,u):
        mid=(l+u)//2
        if arr[mid]==key:
            globals() ['pos']=mid
            return True
        else:
            if arr[mid]<key:
                l=mid+1
            else:
                u=mid-1
    return False
arr=list(map(int,input().split()))
key=int(input())
if search(arr,key):
    print("Found at index: ",pos)
else:
    print("not found")