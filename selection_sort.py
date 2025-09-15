def sorting(arr):
    for i in range(len(arr)-1):
        pos=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[pos]:
                pos=j
        temp=arr[i]
        arr[i]=arr[pos]
        arr[pos]=temp
        print(arr)
    
    return arr


arr=list(map(int,input().split()))
print(sorting(arr))

