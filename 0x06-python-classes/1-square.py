#!/usr/bin/python3
""" Creating a class called Square that has some attributes """


class Square:
    """ Creation of the class """

    def __init__(self, size):
        """ Definition of the init method which contains a private instant
        called size which represents the size of the square"""

        self.__size = size
