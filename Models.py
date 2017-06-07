class Grid():
    def __init__(self):
        self.__grid = []
        self.dimensions = [5,5]

    def set_dimensions(self, dimensions):
        self.__grid = []
        for number in range(dimensions[0]):
            self.__grid.append([])
            for number in range(dimensions[1]):
                self.__grid[-1].append(0)

    def get_dimensions(self):
        return [len(self.__grid), len(self.__grid[0])]

    dimensions = property(get_dimensions, set_dimensions)