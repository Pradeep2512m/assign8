import math


class Point(object):
    """Class to handle point in a 2 dimensions space"""

    def __init__(self, x, y):
        """
        :param x: the value on the X-axis
        :type x: float
        :param y: the value on the Y-axis
        :type y: float
        """
        self.x = x
        self.y = y


    def show(self):
        """
        :return: the coordinate of this point
        :rtype: a tuple of 2 elements (float, float)
        """
        return self.x, self.y


    def move(self, x, y):
        """
        :param x: the value to move on the X-axis
        :type x: float
        :param y: the value to move on the Y-axis
        :type y: float
        """
        self.x += x
        self.y += y




