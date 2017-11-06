from random import random


class Cell:
    def __init__(self):
        self.__alive = False

    def is_alive(self):
        return self.__alive

    def make_alive(self):
        self.__alive = True

    def kill(self):
        self.__alive = False


class World:
    def __init__(self, real_size):
        self.__real_size = real_size
        self.__cells = [[Cell() for _ in range(self.__real_size)] for _ in range(self.__real_size)]
        self.__seed(0.1)

    def __seed(self, chance):
        for x in range(self.__real_size):
            for y in range(self.__real_size):
                if random() <= chance:
                    self.__cell(x, y).make_alive()

    def __cell(self, x, y):
        def make_real(val, real_size):
            if val >= 0:
                return val % real_size
            else:
                return real_size - abs(val) % real_size

        x = make_real(x, self.__real_size)
        y = make_real(y, self.__real_size)

        return self.__cells[x][y]

    def __neighbours(self, x, y):
        result = []
        for xx in range(x - 1, x + 2):
            for yy in range(y - 1, y + 2):
                if xx != x or yy != y:
                    result.append(self.__cell(xx, yy))
        return result

    def next(self):
        for x in range(self.__real_size):
            for y in range(self.__real_size):
                cur_cell = self.__cell(x, y)
                alive_neighbours_num = len([n for n in self.__neighbours(x, y) if n.is_alive()])
                if cur_cell.is_alive():
                    if alive_neighbours_num not in (2, 3):
                        cur_cell.kill()
                else:
                    if alive_neighbours_num == 3:
                        cur_cell.make_alive()

    def __str__(self):
        result = ''
        for x in range(self.__real_size):
            result += '\n'
            for y in range(self.__real_size):
                cur_cell = self.__cell(x, y)
                result += 'O\t' if cur_cell.is_alive() else '.\t'
        return result


def main():
    world = World(50)
    print(world)

    while True:
        input("Press Enter to continue...")
        world.next()
        print(world)


if __name__ == "__main__":
    main()
