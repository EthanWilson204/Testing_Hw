import unittest
from triangle import Triangle

class TriangleTest(unittest.TestCase):

    # test for a valid triangle
    def test_init_1(self):
        t = Triangle(3,4,5)
        assert t.s1 == 3
        assert t.s2 == 4
        assert t.s3 == 5
        
    # test for TypeError exception when creating and initializing a Triangle object
    def test_init_2(self):
        with self.assertRaises(TypeError):
            Triangle("3","4","5")


    # test for ValueError exception when creating and initializing a Triangle object: side(s) not positive
    def test_init_3(self):
        with self.assertRaises(ValueError):
            Triangle(-3,-4,-5)


    # test for ValueError exception when creating and initializing a Triangle object: invalid triagle
    def test_init_4(self):
        with self.assertRaises(ValueError):
            Triangle(20,2,2)
            
            
    # test for "Equilateral" type of triangle
    def test_type_1(self):
        t = Triangle(3,3,3)
        t_string = t.type()
        self.assertEqual(t_string, 'Equilateral')
        
        
    # test for "Isosceles" type of triangle
    def test_type_2(self):
        t = Triangle(5,5,6)
        t_string = t.type()
        self.assertEqual(t_string, 'Isosceles')


    # test for "Scalene" type of triangle
    def test_type_3(self):
        t = Triangle(3,4,5)
        t_string = t.type()
        self.assertEqual(t_string, 'Scalene')
    
    
    # test for checking if a triangle is equilateral
    def test_is_equilateral_1(self):
        t = Triangle(3,3,3)
        self.assertTrue(t.is_equilateral())


    # test for checking if a triangle is not equilateral
    def test_is_equilateral_2(self):
        t = Triangle(5,5,6)
        self.assertFalse(t.is_equilateral())


    # test for checking if a triangle is isosceles
    def test_is_isoceles_1(self):
        t = Triangle(5,5,6)
        self.assertTrue(t.is_isosceles())


    # test for checking if a triangle is not isosceles
    def test_is_isoceles_2(self):
        t = Triangle(3,4,5)
        self.assertFalse(t.is_isosceles())
        
        
    # test for checking if a triangle is scalene
    def test_is_scalene_1(self):
        t = Triangle(3,4,5)
        self.assertTrue(t.is_scalene())


    # test for checking if a triangle is not scalene
    def test_is_scalene_2(self):
        t = Triangle(3,3,3)
        self.assertFalse(t.is_scalene())


    # test if calling str() on a Triangle object returns expected string representation
    # of Triangle object (as list of sides)
    def test_str(self):
        t = Triangle(3,4,5)
        self.assertEqual(t.__str__(), f"[{t.s1},{t.s2},{t.s3}]")

    # test if two Triangle objects with same three sides returns True
    def test_eq_1(self):
        t1 = Triangle(3,4,5)
        t2 = Triangle(3,4,5)
        self.assertTrue(t1.__eq__(t2))

    # test if two Triangle objects with different sides returns False
    def test_eq_2(self):
        t1 = Triangle(3,4,5)
        t2 = Triangle(4,5,6)
        self.assertFalse(t1.__eq__(t2))

    # test if a Triangle object is equal to itself (i.e., returns True)
    def test_eq_3(self):
        pass

    # test if a Triangle object is not equal to an object that is not Triangle object (i.e., returns False)
    def test_eq_4(self):
        pass
