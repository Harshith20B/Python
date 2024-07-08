def mergeSort(arr,left,right):
    if(left<right):
        mid = (right+left)//2
        mergeSort(arr,left,mid)
        mergeSort(arr,mid+1,right)
        merge(arr,left,mid,right)

def merge(arr,left,mid,right):
    n1 = mid-left+1
    n2 = right-mid
    leftArr = [0]*n1
    rightArr = [0]*n2
    for i in range(n1):
        leftArr[i]=arr[left+i]
    for j in range(n2):
        rightArr[j]=arr[mid+1+j]
    i=0
    j=0
    k=left
    while (i<n1 and j<n2):
        if(leftArr[i]<=rightArr[j]):
            arr[k]=leftArr[i]
            i+=1
        else:
            arr[k]=rightArr[j]
            j+=1
        k+=1
    while(i<n1):
        arr[k]=leftArr[i]
        i+=1
        k+=1
    while(j<n2):
        arr[k]=rightArr[j]
        j+=1
        k+=1
    
def main():
    arr=[54,23,67,24,65,92,12]
    n=len(arr)
    mergeSort(arr,0,n-1)
    for i in arr:
        print(i)

main()