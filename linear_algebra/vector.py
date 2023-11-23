class Vector:

    def __init__(self, data: list[float]):
        """initialize a vector with the given data

        Args:
            data (list[float]): list of values for the vector
        """
        try:
            assert len(data) != 0, "cannot init an empty vector"
            # TODO: cast all values in float ? 
            # self.data = [float(x) for x in data]
            self.data = data
        except AssertionError as e:
            print('error:', e)

    def __str__(self):
        return str(self.data)

    def add(self, v: 'linear_algebra.vector.Vector'):
        """Adds another vector to this vector

        Args:
            v (linear_algebra.vector.Vector): the other vector to add 

        Raises:
            ValueError: if vectors dimensions don't match

        Returns:
            Vector: updated Vector
        """
        if len(self.data) != len(v.data):
           raise ValueError(f"cannot add vector of size {len(self.data)} and vector of size {len(v.data)}")
        self.data = [a + b for a, b in zip(self.data, v.data)]
        return self.data
    
    def sub(self, v: 'linear_algebra.vector.Vector'):
        """Substract this vector by another vector

        Args:
            v (linear_algebra.vector.Vector): the other vector to substract

        Raises:
            ValueError: if vectors dimensions don't match

        Returns:
            Vector: updated Vector
        """
        if len(self.data) != len(v.data):
           raise ValueError(f"cannot add vector of size {len(self.data)} and vector of size {len(v.data)}")
        self.data = [a - b for a, b in zip(self.data, v.data)]
        return self.data

    def scl(self, a: float):
        """Scales the vector by a scalar.

        Args:
            scalar (float): the scalar value.

        Returns:
            Vector: a new vector representing the scaled vector.
        """
        self.data = [a * b for b in self.data]
        return self.data
    
    def get_size(self):
        """Returns size of vector

        Returns:
            int: size of the vector
        """
        return len(self.data)

    def reshape(self, row, column):
        """reshape vector to a row * column matrix

        Args:
            row (int): number of rows of the desired matrix
            column (int): number of columns of the desired matrix

        Raises:
            ValueError: matrix dimension must match with vector size

        Returns:
            list[[]]: reshaped matrix
        """
        if row * column != len(self.data):
           raise ValueError(f"cannot reshape array of size {len(self.data)} into shape ({row},{column})")
        reshaped_matrix = []
        for i in range(row):
            row = self.data[i * column : (i + 1) * column]
            reshaped_matrix.append(row)
        return reshaped_matrix
