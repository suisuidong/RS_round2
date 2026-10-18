import numpy as np
class Matrix:
    def __init__(self,data):
        self.data=np.array(data)
        if self.data.ndim!=2:
            raise ValueError()
    def __add__(self, other):
        return Matrix(self.data+other.data)
    def __sub__(self, other):
        return Matrix(self.data-other.data)
    def __mul__(self, other):
        return Matrix(self.data @ other.data)
    def transpose(self):
        return Matrix(self.data.T)
    def __str__(self):
        return f"Matrix:\n{self.data}"
class SquareMatrix(Matrix):
    def __init__(self,data):
        super().__init__(data)
        if self.data.shape[0]!=self.data.shape[1]:
            raise ValueError()
    def trace(self):
        return np.trace(self.data)
    def is_symmetric(self):
        return np.allclose(self.data,self.data.T)








