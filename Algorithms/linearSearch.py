def linearSearch(arr,key):
    n = len(arr)
    count=0
    for i in range(n):
        count+=1
        if(arr[i]==key):
            return i,count
    return -1,count

def main():
    arr = [3,6,2,7,4]
    key = int(input("Enter key :"))
    pos,count = linearSearch(arr,key)
    if(pos==-1):
        print("Not found in arr")
    else:
        print(f"{key} found in array at position {pos+1}")
    print(f"Number of compariosions are {count}")

if __name__ == "__main__":
    main()