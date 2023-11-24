class Matrix:
    def __init__(self, data: list[float]):
        try:
            assert len(data) != 0, "cannot init an empty vector"
            # TODO: cast all values in float ? 
            # self.data = [float(x) for x in data]
            self.data = data
        except AssertionError as e:
            print('error:', e)
    
    def __str__(self):
        display = ''
        i = 0
        for row in self.data:
            if i == 0:
                display += f"{str(row)}\n"
            else:
                display += f"      {str(row)}\n"
            i += 1
        return display

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
            int, int: column size, row size
        """
        return len(self.data), len(self.data[0])

    def is_square(self):
        return len(self.data) == len(self.data[0])
    
    def reshape(self):
        reshaped = [element for row in self.data for element in row]
        return reshaped

