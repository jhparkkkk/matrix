from linear_algebra.vector import Vector


class Matrix:
    def __init__(self, data: list[float]):
        try:
            assert len(data) != 0, "cannot init an empty matrix"
            self.data = data
            self.rows = len(data)
            self.cols = len(data[0])
        except AssertionError as e:
            print("error:", e)

    def __str__(self):
        display = ""
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

    def __setitem__(self, index1: int, index2: int):
        """Set the value at the specified index in the vector.
        Args:
        index (int): The index at which to set the value.
        value (float): The new value to set.

        Raises:
            IndexError: If the index is out of range.
        """
        if 0 <= index1 < len(self.data):
            self.data[index1] = self.data[index2]
        else:
            raise IndexError("Index out of range")

    def add(self, v: "linear_algebra.matrix.Matrix"):
        """
        Adds the elements of another matrix to this matrix.

        Parameters:
        - v (Matrix): The matrix to be added.

        Raises:
        - ValueError: If the matrices have different shapes.

        Returns:
        - Matrix: The resulting matrix after addition.
        """
        if len(self.data) != len(v.data) or len(self.data[0]) != len(v.data[0]):
            raise ValueError(
                f"cannot add matrix shaped as ({len(self.data)},{len(self.data[0])}) and matrix shaped as ({len(v.data)},{len(v.data[0])})"
            )
        self.data = [
            [a + b for a, b in zip(column, row)]
            for column, row in zip(self.data, v.data)
        ]
        return self

    def sub(self, v: "linear_algebra.matrix.Matrix"):
        if len(self.data) != len(v.data) or len(self.data[0]) != len(v.data[0]):
            raise ValueError(
                f"cannot substract matrix shaped as ({len(self.data)},{len(self.data[0])}) and matrix shaped as ({len(v.data)},{len(v.data[0])})"
            )
        self.data = [
            [a - b for a, b in zip(column, row)]
            for column, row in zip(self.data, v.data)
        ]
        return self

    def scl(self, a: float):
        self.data = [[a * b for b in row] for row in self.data]
        return self

    def lerp(self, other, scalar) -> "linear_algebra.matrix.Matrix":
        """
        Performs linear interpolation (LERP) between two matrices.

        Args:
            other (Matrix): The matrix to interpolate towards.
            scalar (float): The interpolation parameter. Should be in the range [0, 1].

        Returns:
            Matrix: The result of the linear interpolation.

        Raises:
            ValueError: If the dimensions of the matrices do not match.
        """
        res_data = [
            [(1 - scalar) * a + (scalar * b) for a, b in zip(row_a, row_b)]
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

    def mul_vec(
        self, vec: "linear_algebra.vector.Vector"
    ) -> "linear_algebra.vector.Vector":
        if self.cols != vec.get_size():
            raise ValueError("matrix must have as many columns as vector entries")
        return Vector(
            [sum(row[i] * vec[i] for i in range(self.cols)) for row in self.data]
        )

    def mul_mat(
        self, mat: "linear_algebra.matrix.Matrix"
    ) -> "linear_algebra.matrix.Matrix":
        if self.cols != mat.rows:
            raise ValueError("invalid matrix")
        return Matrix(
            [
                [
                    sum(self.data[i][k] * mat.data[k][j] for k in range(self.cols))
                    for j in range(mat.cols)
                ]
                for i in range(self.rows)
            ]
        )

    def trace(self) -> float | int:
        res = 0
        for i in range(self.rows):
            res += self.data[i][i]
        return res

    def transpose(self) -> "linear_algebra.matrix.Matrix":
        return Matrix(
            [
                [self.data[j][i] for j in range(len(self.data))]
                for i in range(len(self.data[0]))
            ]
        )

    def row_echelon(self) -> "linear_algebra.matrix.Matrix":
        def first_nonzero_row(matrix):
            res = next(((i, row) for i, row in enumerate(matrix) if any(row)), None)
            if res == None:
                raise ValueError("Matrix is already reduced")
            return res

        def first_nonzero_term(row):
            res = next((i for i, element in enumerate(row) if element != 0), None)
            return res

        def row_swap(mat, row1, row2):
            print("row_swap", type(mat))
            if row1 < 0 or row1 >= len(mat) or row2 < 0 or row2 >= len(mat):
                raise IndexError("Row indices are out of range.")
            mat[row1], mat[row2] = mat[row2], mat[row1]
            return mat

        def row_scale(row, scalar):
            scaled_row = [row[i] * scalar for i in range(len(row))]
            return scaled_row

        def row_sub(mat, row1, row2):
            mat[row2] = [mat[row2][i] - row1[i] for i in range(len(mat[0]))]

        try:
            mat = self.data
            i = first_nonzero_row(mat)[0]
            j = first_nonzero_term(mat[i])
            for r in range(self.rows):
                if j == None and r <= self.rows - 1:
                    continue
                mat[r] = row_scale(mat[r], 1 / mat[i][j])
                for sub_r in range(self.rows):
                    if sub_r != r:
                        tmp = row_scale(mat[r], mat[sub_r][j])
                        row_sub(mat, tmp, sub_r)
                i = i + 1
                if i < self.rows:
                    j = first_nonzero_term(mat[i])
            return Matrix(mat)
        except ValueError as error:
            print(error)
            return self

    def determinant(self) -> float:
        def solve_two(mat) -> float:
            return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]

        def solve_three(mat) -> float:
            sub_a = [[mat[1][1], mat[1][2]], [mat[2][1], mat[2][2]]]
            sub_b = [[mat[1][0], mat[1][2]], [mat[2][0], mat[2][2]]]
            sub_c = [[mat[1][0], mat[1][1]], [mat[2][0], mat[2][1]]]
            a = mat[0][0] * solve_two(sub_a)
            b = mat[0][1] * solve_two(sub_b)
            c = mat[0][2] * solve_two(sub_c)
            return a - b + c

        def solve_four(mat):
            det = 0
            for col in range(4):
                sub_matrix = []
                for sub_row in range(1, 4):
                    row = []
                    for sub_col in range(4):
                        if sub_col != col:
                            row.append(mat[sub_row][sub_col])
                    sub_matrix.append(row)
                sign = (-1) ** col
                det += sign * mat[0][col] * solve_three(sub_matrix)
            return det

        try:
            if self.is_square() == False:
                raise TypeError("Matrix is not square")
            solve_dict = {2: solve_two, 3: solve_three, 4: solve_four}
            mat = self.data
            determinant = solve_dict[len(mat)](mat)
            return determinant
        except TypeError as error:
            print(error)

    def inverse(self) -> "linear_algebra.matrix.Matrix":
        """calculate inverse of a given matrix using adjoint method

        Returns:
            linear_algebra.matrix.Matrix: inverse of the given matrix
        """

        def solve_minor(mat) -> float:
            return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]

        def create_sub_matrix(mat, i, j) -> list:
            sub_matrix = []

            for col in range(0, len(mat)):
                sub_row = []
                for row in range(0, len(mat[0])):
                    if col != i and row != j:
                        sub_row.append(mat[col][row])
                if sub_row:
                    sub_matrix.append(sub_row)
            return sub_matrix

        def create_cofactor_matrix(mat):
            cofactor_matrix = [[0] * self.rows for _ in range(self.cols)]
            for row in range(self.rows):
                for col in range(self.cols):
                    sub_m = create_sub_matrix(mat, row, col)
                    cofactor_matrix[row][col] = (
                        (-1) ** ((row + 1) + (col + 1))
                    ) * solve_minor(sub_m)
            return cofactor_matrix

        mat = self.data
        determinant = self.determinant()
        cofactor_matrix = create_cofactor_matrix(mat)
        adjoint_matrix = Matrix(
            [
                [cofactor_matrix[j][i] for j in range(len(cofactor_matrix))]
                for i in range(len(cofactor_matrix[0]))
            ]
        )
        inverse_matrix = [[b / determinant for b in row] for row in adjoint_matrix]
        return inverse_matrix

    def rank(self) -> int:
        rref = self.row_echelon()
        rank = sum(1 for row in rref if sum(row) != 0)
        return rank
