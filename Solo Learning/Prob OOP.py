class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
        self.tuples = (coor1, coor2)
        # print(type(self.tuples))
    def check(self):
        return self.tuples

    def distance(self):
        dist = (self.coor1 * self.coor2) / 2
        return f'The distance is {dist}'

    def slope(self):
        slp = self.coor1 / self.coor2
        return f'The slope is {slp}'


li = Line(8, 10)
print(li.check())
print(li.distance())
print(li.slope())





