"""Module for all Models"""
class Model:
    """The Model to store Data"""

    def __init__(self):
        self.__grid = []

    def set_dimensions(self, dimensions):
        """Set the Dimesions of the grid"""
        self.__grid = []
        for number in range(dimensions[0]):
            self.__grid.append([])
            for number in range(dimensions[1]):
                self.__grid[-1].append(0)

    def get_dimensions(self):
        """Get"""
        return self.__grid

    dimensions = property(get_dimensions, set_dimensions)
