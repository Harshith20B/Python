def Floyd(arr):
    n=len(arr)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                arr[i][j] = min(arr[i][j],(arr[i][k] + arr[k][j]))

def main():
    arr = [[0,999,3,999],
           [2,0,999,999],
           [999,7,0,1],
           [6,999,999,0]]
    print("Adjacency matric")
    for row in arr:
        print(row)
    print("All pairs shortest path")
    Floyd(arr)
    for row in arr:
        print(row)
main()
    
