from random import randint
import time
import matplotlib.pyplot as plt
def quickSort(arr,low,high):
    if(low<high):
        pivot = partition(arr,low,high)
        quickSort(arr,low,pivot-1)
        quickSort(arr,pivot+1,high)

def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if(arr[j]<=pivot):
            i+=1
            (arr[i],arr[j])=(arr[j],arr[i])
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
    
def main():
    x=[]
    y=[]
    for n in range(100,1001,100):
        a=[]
        x.append(n)
        for i in range(n):
            a.append(randint(1,n))
        start=time.time()
        quickSort(a,0,len(a)-1)
        end=time.time()
        gaptime=end-start
        y.append(gaptime)
        print("Sorted List")
        print(a)
    plt.plot(x, y, label='Merge Sort')
    plt.xlabel("Input Size")
    plt.ylabel("Time(ms)")
    plt.legend(loc='upper right')
    plt.show()

main()

        
