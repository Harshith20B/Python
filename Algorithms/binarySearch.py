def binarySearch(arr,key):
    n = len(arr)
    low=0
    count=0
    high=n-1
    while(low<=high):
        count+=1
        mid = (low+high)//2
        if(key<arr[mid]):
            high=mid-1
        elif(key>arr[mid]):
            low=mid+1
        else:
            return mid,count
    return -1,count

def main():
    arr = [2,3,4,5,9]
    key = int(input("Enter key :"))
    pos,count = binarySearch(arr,key)
    if(pos==-1):
        print("Not found in arr")
    else:
        print(f"{key} found in array at position {pos+1}")
    print(f"Number of comparisions are {count}")

if __name__ == "__main__":
    main()