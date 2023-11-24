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
            if all(isinstance(x, (float, int)) for x in data):
                self.data = data
            else:
                raise ValueError("All elements in vector must be float or int")
        except AssertionError as e:
            print('error:', e)

    def __str__(self):
        return str(self.data)
    
    def __setitem__(self, index: int, value: float):
        """Set the value at the specified index in the vector.

        Args:
            index (int): The index at which to set the value.
            value (float): The new value to set.

        Raises:
            IndexError: If the index is out of range.
        """
        if 0 <= index < len(self.data):
            self.data[index] = value
        else:
            raise IndexError("Index out of range")
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

    def ft_sqrt(self, value: float):
        """calculate square root of value by calculating value power 0.5
        Args:
            value (float): value to operate on
        Returns:
        float: result
        """
        return value ** (0.5)

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
        return self
    
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
        return self

    def scl(self, a: float):
        """Scales the vector by a scalar.

        Args:
            scalar (float): the scalar value.

        Returns:
            Vector: a new vector representing the scaled vector.
        """
        self.data = [a * b for b in self.data]
        return self
    
    def lerp(self, other, scalar) -> 'linear_algebra.vector.Vector':
        return Vector([round((1 - scalar) * a + scalar * b, 2) for a, b in zip(self.data, other.data)])
    
    def dot(self, v: 'linear_algebra.vector.Vector') -> 'linear_algebra.vector.Vector':
        if len(self.data) != len(v.data):
            raise ValueError(f"cannot operate dot product if vector size don't match")
        res = 0
        for a, b in zip(self.data, v.data):
            res += a*b 
        return res

    def norm_1(self) -> float:
        res = 0.
        for x in self.data:
            res += abs(x)
        return res
    
    def norm(self) -> float:
        res = 0.0
        for x in self.data:
            res += pow(x, 2)
        return self.ft_sqrt(res)

    def norm_inf(self) -> float:
        res = [abs(ele) for ele in self.data]
        return max(res)    
        