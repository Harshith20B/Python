import time
import matplotlib.pyplot as plt
from random import randint

def bubble(a,n):
    for i in range(n):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j],a[j+1] = a[j+1],a[j]

def selection(a,n):
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if a[j] < a[min_index]:
                min_index = j
        a[min_index],a[j] = a[j],a[min_index]

def main():
    x = []
    y = []
    z = []
    for n in range(1000,10000,1000):
        x.append(n)
        a=[]
        b=[]
        for i in range(n):
            a.append(randint(1,n))
            b = a[:]
        start = time.time()
        selection(a,n)
        end = time.time()
        st = time.time()
        bubble(b,n)
        ed = time.time()
        gap = end - start
        total = ed - st
        y.append(gap)
        z.append(total)
    plt.plot(x,y,label='Selection Sort')
    plt.plot(x,z,label='bubble Sort')
    plt.legend(loc='upper right')
    plt.show()

main()