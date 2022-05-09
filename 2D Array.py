

#2D array

array=[
    [23,23,33,44,45],
    [23,45,66,78,78],
    [65,78,89,33,67],
    [87,45,56,33,56],
    ]
print(array)

#print array first row
print(array[0])

#print second row 2 colu
print(array[1][1])

#second row two column Row and column print
for rows in array:
   for columns in rows:
      print(columns, end=" ")
   print() #one line blank break




# another program
rows,cols =(5,5)
array = [[0 for i in range(cols)] for j in range (rows)]
print(array)

#rows, cols
rows,cols = (5,5)
arr=[]
for i in range(rows):
    col=[]
    for j in range(cols):
        col.append(2)
    arr.append(col)
print(arr)

#