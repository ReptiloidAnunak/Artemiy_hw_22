# Вам не кажется, что CubeVolumeCalculator 
# чаще дергает методы класса Cube? Исправьте так, 
# чтобы избавиться от лишних обращений к классу Cube


class Cube:

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_z(self):
        return self._z

    def cube_volume(self):
        self.get_z() * self.get_y() * self.get_z()


class CubeVolumeCalculator:

    @staticmethod
    def calc_cube_volume(cube: Cube):
        return cube.cube_volume()
