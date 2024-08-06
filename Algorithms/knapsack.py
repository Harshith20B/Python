def show(w,p,n,m,v):
    i=n
    j=m
    #profit=v[n][m]
    while(i>0 and j>=0):
        if(v[i][j]!=v[i-1][j]):
            print(f"Item weight : {w[i]} Item Profit : {p[i]}")
            j=j-w[i]
        i=i-1
# n - Number of weights with different values
# m - weight of the bag

def knapsack(w,p,n,m):
    # n+1 - rows m+1 - columns
    v = [[0 for x in range(m+1)] for x in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if(i==0 or j==0):
                v[i][j]=0
            elif(w[i]>j):
                v[i][j]=v[i-1][j]
            else:
                v[i][j]=max(v[i-1][j],p[i]+v[i-1][j-w[i]])
    show(w,p,n,m,v)
    return v[n][m]

w=[0,2,1,3,2]   
p=[0,12,10,20,15]
n=4
m=5
res=knapsack(w,p,n,m)
print(f"optimal solution = {res}")
