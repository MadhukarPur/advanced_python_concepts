# Numpy Introduction
'''
    Introduction: 
        Numpy is an open-source library used to handle multi-dimensional data with ease. 
        It has a data structure called ndarray, which is the reason behind NumPy's efficiency.

    Reasons why NumPy is preferred over Python lists.
        1. Faster Execution
            Operations that require a lot of effort and time can be done easily in less time. It has been found that just switching 
            from Python lists to NumPy arrays can provide up to a 100x performance improvement.

            The reason why NumPy is so fast is because it is created using high-performance languages like C and C++.

        2. Used with Various Libraries
            NumPy is heavily used with various libraries like Pandas, SciPy, scikit-learn, etc.

        3. Broad Application Domain
            NumPy is used in high-level applications like Quantum Computing, Signal Processing, Bioinformatics, Machine Learning, and many more.

        4. Arrays are Homogeneous
            NumPy arrays are homogeneous, meaning they can only store elements of the same data type, enabling efficient storage and computation.

'''

# Array Creation
'''
    To create an array from scratch, we can use functions like
        np.zeros() and np.ones()
        np.arange() and np.linspace()
        np.random.rand() and np.random.randint()

    import numpy as np
    arr1 = np.array([1,2,3,4,5])
    
    # create an array with 5 elements filled with zeros
    array1 = np.zeros(5)
    arr3 = np.ones(5)

    # elements between 10 and 40 with stepsize 4
    array1 = np.arange(10, 50 , 4)
    
    # generate 4 elements between 10 and 40 
    array2 = np.linspace(10, 50 , 4)
    
    # array of length 5 with random integer values ranging from 1 to 100
    rand_array = np.random.randint(1, 100, size=5)
    
    # generate an array of 4 random numbers between 0 and 1
    array1 = np.random.rand(4)

    # create an empty with total capacity of 5
    empty_array = np.empty(5)

    # create 2x2 array all filled with the value 5
    numpy_array = np.full((2, 2), 5)

    # reshape a 1D array into a 2D array with 2 rows and 4 columns
    result = np.reshape(array1, (2, 4))
    
    # reshape the 1D array to a 3D array
    result = np.reshape(array1, (2, 2, 2))

    # flatten the array
    flattened_array = array1.flatten()

    # flatten the array
    array2 = np.ravel(array1)

    # flatten() is an ndarray object method whereas ravel() is a library-level function.
    # ravel() works with a list of arrays, but flatten() doesn't.

    # create a 2D matrix
    matrix1 = np.matrix([[1, 2], [3, 4]])

    # Difference Between 2D Array and Matrix in NumPy
    # NumPy matrices has special operators * (multiplication) and ** (power), which behaves like they do in 
    # linear algebra. For example, the * operator performs matrix multiplication in matrices, and 
    # element-wise multiplication in arrays.

    # attempt to calculate the dot product
    result = np.dot(matrix1, matrix2)

    # get transpose of matrix1
    result = np.transpose(matrix1)

    # create a 2x2 identity matrix using eye()
    matrix1 = np.eye(2)
    
    # create a 3x3 identity matrix using identity()
    matrix2 = np.identity(3)
'''
# Array indexing
'''
    Array Indexing - Starts from 0
    Negative Indexing - starts from -1 from the end
    
    Boolean Indexing:
        # select only the even numbers from the array
        even_numbers = numbers[numbers % 2 == 0]

        # change all even numbers to 0 
        numbers[numbers % 2 == 0] = 0
    
    Fancy Indexing:
        # select elements at index 1, 2, 5, 7
        elements = numbers[[1, 2, 5, 7]]
'''

#  Array Attributes
'''
    Attributes	    Description
    ----------      -----------
    ndim	        specifies the number of dimensions of an array (for 1D array, it is 1)
    shape	        returns the size of the array in each dimension (for 1d array, it is the length of the array)
    size	        specifies total number of elements in the array
    dtype	        specifies the data type of elements of the array (float, int, or complex)
    itemsize	    represents the size in bytes of each element of the array
    nbytes	        represents total size in bytes of the array (nbytes = itemsize * size)
'''

#  Mathmetical OPerations:
'''
    Element-wise Operation	    Operator	Function
    ----------------------      --------    --------
    Addition	                +	        add()
    Subtraction	                -	        subtract()
    Multiplication	            *	        multiply()
    Division	                /	        divide()
    Exponentiation	            **	        power()
'''

# Comparison Operators
'''
    Operators	                Functions           Descriptions
    ---------                   ---------           ------------
    < (less than)	            less()             returns True if element of the first array is less than the second one
    <= (less than or equal to)	less_equal()       returns True if element of the first array is less than or equal to the second one
    > (greater than)	        greater()          returns True if element of the first array is greater than the second one
    >= (greater than or equal to) greater_equal()  returns True if element of the first array is greater than or equal to the second one
    == (equal to)	            equal()            returns True if the element of the first array is equal to the second one
    != (not equal to)	        not_equal()        returns True if the element of the first array is not equal to the second one
'''

#  Logical Operations
'''
    Operators	        Descriptions
    ---------           ------------
    logical_and	        Computes the element-wise truth value of x1 AND x2
    logical_or	        Computes the element-wise truth value of x1 OR x2
    logical_not	        Computes the element-wise truth value of NOT x
'''

#  Statistical Functions
'''
    Functions	    Descriptions
    ---------       ------------
    median()	    returns the median of an array
    mean()	        returns the mean of an array
    std()	        returns the standard deviation of an array
    percentile()	returns the nth percentile of elements in an array
    min()	        returns the minimum element of an array
    max()	        returns the maximum element of an array
'''

# Advanced Numpy Concepts
'''
    # Array Filtering
    filtered_arr = array1[array1 < 0]

    # np.where()
    # The np.where() function creates a new array based on the condition array1 > 0.
    # If the condition is true, it selects the corresponding element from array1, otherwise, it selects 0.
    print(np.where(array1>0,array1,0))

    # np.any() function checks whether any element in an array satisfies a given condition.
    # It returns True if at least one element in the array meets the condition.
    print(np.any(arr > 3)) # True

    # np.all() to check whether all elements in an array satisfy a given condition.
    # It returns True if all elements in the array meet the condition.
    # check if all element in each row is greater than 5
    result_row = np.all(array1 > 5, axis=1)
    
    # check if all element in each column is negative
    result_column = np.any(array1 < 0, axis=0)

    # Stack operation is used to join a sequence of arrays into a new matrix along a new axis.
    result = np.stack((array1, array2), axis = 0)
    result = np.stack((array1, array2), axis = 1)

    # calculate the sum along columns (axis 1)
    sum_coumns = np.sum(array1, axis=1)

    # calculate the average along columns (axis 1)
    mean_coumns = np.mean(array1, axis=1)

    # NumPy ufunc(universal functions) are functions that operate on N-d arrays element by element. 
    # These functions support broadcasting and typecasting features of nd arrays.
'''