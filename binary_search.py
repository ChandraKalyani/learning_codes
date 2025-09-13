#By using while loop
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
    print("found", pos)
else:
    print("Not found")



#By using for loop
pos=-1
def search(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            globals() ['pos']=i
            return True
        else:
            return False
    
arr=list(map(int,input().split()))
key=int(input())
if search(arr,key):
    print("found", pos)
else:
    print("Not found")