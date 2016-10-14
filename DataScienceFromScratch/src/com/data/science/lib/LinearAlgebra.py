from com.data.science import reduce, math

def vectorAddition(v, w):
    """Add two vectors"""
    return [(v_i + w_i) for v_i, w_i in zip(v, w)]

def vectorSubtraction(v, w):
    """Subtract two vectors"""
    return [(v_i - w_i) for v_i, w_i in zip(v, w)]

def vectorsSum(vectors):
    """sums all corresponding elements"""
    return reduce(vectorAddition, vectors);

def scalarMultiply(c, v):
    """Scalar multiply vector"""
    return [(c * v_i) for v_i in v]

def vectorMean(vectors):
    """compute the vector whose ith element is the mean of the ith elements of the input vectors"""
    n = len(vectors)
    return scalarMultiply(1/n, vectorsSum(vectors))

def vectorDot(v, w = None):
    """Dot two vectors"""
    if (w == None):
        return sum([(v_i * v_i) for v_i in v])
    else:
        return sum([(v_i * w_i) for v_i, w_i in zip(v, w)])

def magnitude(v):
    """magnitude a vector"""
    return math.sqrt(vectorDot(v, v))

def distance(v, w):
    """distance between 2 vectors"""
    return math.sqrt(vectorDot(vectorSubtraction(v, w)))

#
# functions for working with matrices
#

def shape(A):
    numRows = len(A);
    numColumns = len(A[0]) if A else 0;
    return numRows, numColumns;

def getRow(A, i):
    return A[i] # A[i] is already the ith row

def getColumn(A, j):
    return [A_i[j] # jth element of row A_i
            for A_i in A] # for each row A_i
    
def makeMatrix(num_rows, num_cols, entry_fn):
    """returns a num_rows x num_cols matrix whose (i,j)th entry is entry_fn(i, j)"""
    return [[entry_fn(i, j) for j in range(num_cols)]for i in range(num_rows)];

def diagonal(i, j):
    return 1 if i == j else 0; 


    
    