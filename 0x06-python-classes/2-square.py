#!/usr/bin/python3
<<<<<<< HEAD
""" Creating a class square with specific attributes"""


class Square:
    """" Definition of the class Square """

    def __init__(self, size=0):
        """ Passing of arguments into the square.
         Args:
            size: size of the square'
        Raise:
            TypeError: if size is not an integer.
            ValueError: if type is less than zero.
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
=======
"""Creating a class square with specific attributes"""


class Square:
"""Definition of the class Square"""

def __init__(self, size=0):
	"""Passing of arguments into the square
	Args:
		size: size of the square'
	Raise:
		TypeError: if size is not an integer.
		ValueError: if type is less than zero.
	"""

	if not isinstance(size, int):
	    raise TypeError('size must be an integer')

	if size < 0:
	    raise ValueError('size must be >= 0')

	self.__size = size
>>>>>>> b061801388f9c7013063697738d174e1cd0195dd
