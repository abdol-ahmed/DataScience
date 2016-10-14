import unittest

from com.data.science.lib import LinearAlgebra as linearAlgebra

class TestLinearAlgebra(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestLinearAlgebra, self).__init__(*args, **kwargs)
    
    def setUp(self):
        self.v = [1, 2]
        self.w = [2,1]
        self.vectors = [[1,2],[2,1],[1,2],[2,1],[1,2],[2,1]]
        
        self.A = [[1, 2, 3], # A has 2 rows and 3 columns
                  [4, 5, 6]]
        self.B = [[1, 2], # B has 3 rows and 2 columns
                  [3, 4],
                  [5, 6]]
        
        super(TestLinearAlgebra, self).setUp()
    
    def test_vectorAddition(self):
        result = [3,3]
        self.assertEqual(result, linearAlgebra.vectorAddition(self.v, self.w));
        
    def test_vectorSubtraction(self):
        result = [-1,1]
        self.assertEqual(result, linearAlgebra.vectorSubtraction(self.v, self.w));
        
    def test_vectorsSum(self):
        result = [9,9]
        self.assertEqual(result, linearAlgebra.vectorsSum(self.vectors));
    
    def test_scalarMultiply(self):
        result = [2,4]
        self.assertEqual(result, linearAlgebra.scalarMultiply(2, self.v))
        
    def test_vectorMean(self):
        result = [1.5,1.5]
        self.assertEqual(result, linearAlgebra.vectorMean(self.vectors))
    
    def test_vectorDot(self):
        result = 4
        self.assertEqual(result, linearAlgebra.vectorDot(self.v, self.w))
    
    def test_magnitude(self):
        result = 2.2360680
        self.assertAlmostEqual(result, linearAlgebra.magnitude(self.v))
    
    def test_distance(self):
        result = 1.4142136
        self.assertAlmostEqual(result, linearAlgebra.distance(self.v,self.w))
        
    #
    # functions for working with matrices
    #

    def test_shape(self):
        resultNumOfRows = 2;
        resultNumOfCols = 3;
        numRows, numColumns =linearAlgebra.shape(self.A)
        self.assertEqual(resultNumOfRows, numRows)
        self.assertEqual(resultNumOfCols, numColumns)
    
    def test_getRow(self):
        result = [1, 2, 3];
        self.assertEqual(result, linearAlgebra.getRow(self.A, 0))
    
    def test_getColumn(self):
        result = [3,6];
        self.assertEqual(result, linearAlgebra.getColumn(self.A, 2))
        
    def test_makeMatrix(self):
        result = [[1,0,0],
                  [0,1,0],
                  [0,0,1]];
        self.assertEqual(result, linearAlgebra.makeMatrix(3,3, linearAlgebra.diagonal))
        
if __name__ == '__main__':
    unittest.main()
