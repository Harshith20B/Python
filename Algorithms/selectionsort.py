def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        minindex=i
        for j in range(i+1,n):
            if(arr[j]<arr[minindex]):
                minindex=j
        if(minindex!=i):
            arr[minindex],arr[i]=arr[i],arr[minindex]
        
def main():
    arr=[54,23,67,24,65,92,12]
    selection_sort(arr)
    for i in arr:
        print(i)

main()
