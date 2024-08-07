from random import randint
import time
import matplotlib.pyplot as plt

def sum_of_elements(arr):
    total_sum = 0
    for element in arr:
        total_sum += element
    return total_sum

def print_even_elements(matrix):
    for row in matrix:
        for element in row:
            if element % 2 == 0:
                print(element, end=" ")
        print()

def main():
    n = int(input("Enter the number of rows in the matrix: "))
    m = int(input("Enter the number of columns in the matrix: "))
    matrix = []
    print("Enter matrix elements row by row:")
    for i in range(n):
        a=[]
        for j in range(m):
            a.append(int(input()))
        matrix.append(a)
    
    print("Even elements in the matrix:")
    print_even_elements(matrix)

if __name__ == "__main__":
    main()

def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

# def main():
#     decimal_number = int(input("Enter a decimal number: "))
#     print(f"Binary equivalent: {decimal_to_binary(decimal_number)}")


