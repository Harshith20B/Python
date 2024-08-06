def Floyd(arr):
    n=len(arr)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                arr[i][j] = min(arr[i][j],(arr[i][k] + arr[k][j]))

def main():
    # matrix = [[0,999,3,999],
    #        [2,0,999,999],
    #        [999,7,0,1],
    #        [6,999,999,0]]
    n = int(input("Enter the number of vertices"))
    matrix = []
    print("Enter matrix values row wise")
    for i in range(n):
        a=[]
        for j in range(n):
            a.append(int(input()))
        matrix.append(a)
    print("Adjacency matric")
    for row in matrix:
        print(row)
    print("All pairs shortest path")
    Floyd(matrix)
    for row in matrix:
        print(row)
main()
    
