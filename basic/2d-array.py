row=int(input("enter no of row"));
column= int(input("enter no of column"))

martix = [[int(input()) for x in range(row)] for y in range(column)];

for x in range(row):
    for y in range(column):
        print(martix[x][y], end="")
