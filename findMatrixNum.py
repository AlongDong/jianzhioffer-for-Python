class FindMtrixnumber:

    def __init__(self,matrix,rows,columns):
        self.matrix=matrix
        self.rows=rows
        self.columns=columns

    def matrix_search(self,num):
        #首先判断矩阵是否空
        row=0
        column=self.columns
        if self.matrix:
            while (row<self.rows and column>=0):
                if self.matrix[row][column]>num:
                    column=column-1
                elif self.matrix[row][column]<num:
                    row=row+1
                else:
                    return True
            else:
                return False

matrix=[[1,2,8,9],
        [2,4,9,2],
        [4,7,10,13],
        6,8,11,15]
a=FindMtrixnumber(matrix,3,3)
b=a.matrix_search(9)
print(b)