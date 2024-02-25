# Class that models a triangle given the lengths of its sides
class Triangle(object):

    # Initializes a Triangle object given three sides
    def __init__(self, s1, s2, s3):
        if not (isinstance(s1,(int,float)) and isinstance(s2,(int,float)) and isinstance(s3,(int,float))):
            raise TypeError("Inappropriate argument type")
        if not (s1 > 0 and s2 > 0 and s3 > 0):
            raise ValueError("Sides of triangle must be positive")
        if not ((s1 < s2 + s3) and (s2 < s1 + s3) and (s3 < s1 + s2)):
            raise ValueError("Given sides don't make a valid triangle")
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    # Return type of triangle as "Equilateral", "Isosceles", or "Scalene"
    def type(self):
        if self.is_equilateral():
            return "Equilateral"
        elif self.is_isosceles():
            return "Isosceles"
        else:
            return "Scalene"

    # Return True if triangle is equilateral, False otherwise
    def is_equilateral(self):
        return self.s1 == self.s2 and self.s2 == self.s3

    # Return True if triangle is isosceles, False otherwise
    def is_isosceles(self):
        return not(self.is_equilateral() or self.is_scalene())

    # Return True if triangle is scalene, False otherwise
    def is_scalene(self):
        return self.s1 != self.s2 and self.s1 != self.s3 and self.s2 != self.s3

    # Return string representation of triangle object as a list of three sides
    def __str__(self):
        return f"[{self.s1},{self.s2},{self.s3}]"

    # Return True if this Triangle object is value equal to the other object, False otherwise
    def __eq__(self, other):
        if not isinstance(other,Triangle):
            return False
        if self is other:
            return True
        return self.s1 == other.s1 and self.s2 == other.s2 and self.s3 == other.s3
