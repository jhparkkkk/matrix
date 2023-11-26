from linear_algebra.vector import Vector

class Matrix:
    def __init__(self, data: list[float]):
        try:
            assert len(data) != 0, "cannot init an empty vector"
            # TODO: cast all values in float ? 
            # self.data = [float(x) for x in data]
            self.data = data
            self.rows = len(data)
            self.cols = len(data[0])
        except AssertionError as e:
            print('error:', e)
    
    def __str__(self):
        display = ''
        i = 0
        for row in self.data:
            if i == 0:
                display += f"{str(row)}\n"
            else:
                display += f"{str(row)}\n"
            i += 1
        return display
    
    def __getitem__(self, index):
        """Get the value at the specified index in the vector.

        Args:
            index (int): The index to retrieve.

        Returns:
            float: The value at the specified index.

        Raises:
            IndexError: If the index is out of range.
        """
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            raise IndexError("Index out of range")

    def add(self, v: 'linear_algebra.matrix.Matrix'):
        if len(self.data) != len(v.data) or len(self.data[0]) != len(v.data[0]):
            raise ValueError(f"cannot add matrix shaped as ({len(self.data)},{len(self.data[0])}) and matrix shaped as ({len(v.data)},{len(v.data[0])})")
        self.data = [
            [a + b for a, b in zip(column, row)] for column, row in zip(self.data, v.data)
        ]
        return self
    
    def sub(self, v: 'linear_algebra.matrix.Matrix'):
        if len(self.data) != len(v.data) or len(self.data[0]) != len(v.data[0]):
            raise ValueError(f"cannot substract matrix shaped as ({len(self.data)},{len(self.data[0])}) and matrix shaped as ({len(v.data)},{len(v.data[0])})")
        self.data = [
            [a - b for a, b in zip(column, row)] for column, row in zip(self.data, v.data)
        ]
        return self

    def scl(self, a: float):
        self.data = [[a * b for b in row] for row in self.data]
        return self
    
    def lerp(self, other, scalar) -> 'linear_algebra.matrix.Matrix':
        res_data = [
            [
                (1 - scalar) * a + (scalar * b)
                for  a, b in zip(row_a, row_b)
                ]
                for row_a, row_b in zip(self.data, other.data)
                ]
        # TODO: to debug
        # for i in range(len(res_data)):
        #     for j in range(len(res_data[0])):
        #         print(f"iteration {i * len(res_data[0]) + j + 1}: i={i} j={j} a = {self.data[i][j]}, b = {other.data[i][j]}")
        return Matrix(res_data)
    def get_shape(self):
        """Returns shape of matrix

        Returns:
            int, int: row size, column size
        """
        return len(self.data), len(self.data[0])

    def is_square(self):
        return len(self.data) == len(self.data[0])
    
    def reshape(self):
        reshaped = [element for row in self.data for element in row]
        return reshaped
    
    def mul_vec(self, vec:'linear_algebra.vector.Vector') -> 'linear_algebra.vector.Vector':
        if self.cols != vec.get_size():
            raise ValueError("matrix must have as many columns as vector entries")
        return Vector([sum(row[i] * vec[i] for i in range(self.cols)) for row in self.data])
    
    def mul_mat(self, mat:'linear_algebra.matrix.Matrix') -> 'linear_algebra.matrix.Matrix':
        if self.cols != mat.rows:
            raise ValueError("invalid matrix")
        return Matrix([[sum(self.data[i][k] * mat.data[k][j] for k in range(self.cols)) for j in range(mat.cols)] for i in range(self.rows)])
    
    def trace(self) -> float | int:
        res = 0
        for i in range(self.rows):
            res += self.data[i][i]
        return res

    def transpose(self) -> 'linear_algebra.matrix.Matrix':
        return Matrix([[self.data[j][i] for j in range(len(self.data))] for i in range(len(self.data[0]))])

