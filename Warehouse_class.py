# Google Hash Code 2016 Qualification


class Warehouse:
    def __init__(self, coord, products):
        self.coord = coord
        self.products = products
        self.drones = []

    def give(self, drone_type, drone_n):
        if self.products[drone_type] - drone_n >= 0:
            self.products[drone_type] -= drone_n
        else:
            needed = drone_n - self.products[drone_type]
            self.products[drone_type] = 0
            print "You need more ", needed

    def take(self, drone_type, drone_n):
        self.products[drone_type] += drone_n
