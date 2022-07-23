#!/usr/bin/python3
""" we define a square class with one attribute
size which is peculiar to different square object.
size is always an integer greater than or equal to 0
Attribute:
    size; size tells the size of the sides of the square
Method:
    area; calculates the are of the square
    my_print; print the square as a grid of hashes
"""


class Square:
    """This class initializes an attribute size on each instance
    using the init function, condition to set size
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """ This is the method used to get class attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """This is the method used to set the class attribute size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Area calculate the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """  This method prints the square object as hashes
        0 size means no square (empty)"""
        if self.__size != 0:
            for line in range(self.__size):
                print("#" * self.__size)
        else:
            print("")
