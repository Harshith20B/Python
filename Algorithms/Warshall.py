def warshall(arr):
    n=len(arr)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                arr[i][j] = arr[i][j] or (arr[i][k] and arr[k][j])

def main():
    arr = [[0,1,0,0],
           [0,0,0,1],
           [0,0,0,0],
           [1,0,1,0]]
    print("Adjacency matric")
    for row in arr:
        print(row)
    print("Transitive Matrix")
    warshall(arr)
    for row in arr:
        print(row)
main()
    
