from asyncio.windows_events import NULL
from typing import Sized


def is_Sorted(row):
    prevElement=row[0]
    for i in row:
        if i<prevElement:
            return False
        prevElement=i

    return True


def change_SymetricElements(matrix,size):
    temp=NULL
    maxSize=size
    for i in range(size):
        temp=matrix[0][i]
        k = matrix[maxSize-1][size-1]
        matrix[0][i]=matrix[maxSize-1][size-1]
        matrix[maxSize-1][size-1]=temp
        maxSize -= 1
    return matrix

def print_Matrix(matrix,size):
     for i in range(size):
        for j in range(size):
            print(matrix[i][j], ' ', end='')
        print('\n')
     return

def generate_Matrix(size):
    row = []
    matrix=[]
    for i in range(size):
        for j in range(size):
          row.append(int(input()))
        matrix.append(row)
        row = []
    return matrix

def sort_ByDesc(matrix,size):
    row=[]
    index=0
    for i in range(size):
        for j in range(size):
           if i==j:
               row.append(matrix[i][j])

    row.sort()
    for i in range(size):
        for j in range(size):
           if i==j:
               matrix[i][j]=row[index]
               index+=1

    return matrix

def reverese_Matrix(matrix,size):
    row = []
    arr=[]
    for i in range(size):
            if i % 2== 0:
                row.append(matrix[i])
                arr.append(row[i-1][::-1])
            else:
                arr.append(matrix[i])
    return arr

def main():   
    print('Pleaze Input Size Of Matrix')

    size=(int(input()))
    print('Now Pleaz input ',size*size,' elements')
    isSorted = True
    matrix = generate_Matrix(size)

    print("You Got Matrix Successfuly))")
    print_Matrix(matrix,size)
    
    for i in range(size):
        currentRow=matrix[i]
        if is_Sorted(currentRow)==False:
            isSorted=False
            break

    if isSorted==True:
        print("////---------------Sorting Array Symetric Elements-----------------\\\\")
        matrix =change_SymetricElements(matrix,size)
        print_Matrix(matrix,size)
    else:
        print("////---------------Sorting Array Central Elements----------------------\\\\")
        matrix= sort_ByDesc(matrix,size)
        print_Matrix(matrix,size)
    
    print("Reversed Matrix\n\n")
    print_Matrix(reverese_Matrix(matrix,size),size)

    return "Completed!!!"
   
print(main())
