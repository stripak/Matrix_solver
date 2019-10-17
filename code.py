from sys import stdin
from copy import deepcopy


class Matrix:
    def __init__(self, list_of_lists):
        self.mat = deepcopy(list_of_lists)

    def __str__(self):
        string = ''
        for i in self.mat:
            for j in i:
                string = string + '%s\t' % j
            string = string[:- 1] + '\n'
        return string[:-1]

    def size(self):
        row = len(self.mat)
        column = len(self.mat[0])
        return row, column

    def __add__(self, other):
        if self.size() != other.size():
            raise MatrixError(self, other)
        else:
            add_new = []
            add_local = []
            sum_str = ''
            for i in range(len(self.mat)):
                for j in range(len(self.mat[i])):
                    add_local.append(self.mat[i][j] + other.mat[i][j])
                add_new.append(add_local)
                add_local = []
            return Matrix(add_new)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            it_new = []
            it_local = []
            for i in range(len(self.mat)):
                for j in range(len(self.mat[i])):
                    it_local.append(self.mat[i][j] * other)
                it_new.append(it_local)
                it_local = []
            return Matrix(it_new)
        elif isinstance(other, Matrix) and self.size()[1] == other.size()[0]:
            mul_new = []
            mul_local = []
            summ = 0
            for i in range(self.size()[0]):
                for j in range(other.size()[1]):
                    summ = 0
                    for k in range(self.size()[1]):
                        summ += self.mat[i][k] * other.mat[k][j]
                    mul_local.append(summ)
                mul_new.append(mul_local)
                mul_local = []
                summ = 0
            return Matrix(mul_new)
        else:
            raise MatrixError(self, other)

    __rmul__ = __mul__

    def transpose(self):
        new = []
        locaList = []
        size = self.size()
        for i in range(size[1]):
            for j in range(size[0]):
                locaList.append(self.mat[j][i])
            new.append(locaList)
            locaList = []
        self.mat = new
        new = Matrix(new)
        return new

    def transposed(self):
        return Matrix(list(map(list, zip(*self.mat))))


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


exec(stdin.read())
