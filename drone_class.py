#Google Hash Code Qualification 2016

class Drones:
    def __init__(self, coord = [0, 0], prod, weight, busy = False):
        self.coord = coord
        self.prod = prod
        self.weight = weight
        self.busy = busy

    def isBusy(self):
        if self.busy : return True
        else : return False

    def isWhere(self):
        return self.coord

    def hasProductType(self, type):
        if self.prod[type] != 0: return True
        else: return False

    def give(self, prod_weight, n):
        if self.prod >= n:
            self.prod = self.prod - n
            self.weight = self.weight - (n * prod_weight)
            print "Unloading done!"
        else:
            print "Drone does not have that much product"

    def take(self, n, prod_weight, max_weight):
        new_weight = prod_weight * n
        if max_weight >= new_weight + self.weight:
            self.weight += new_weight
            self.prod += n
            print "Loading done!"
        else :
            print "The drone cannot take so much weight!"

    def deliver(self):
        self.prod = 0
        self.weight = 0
        print "Delivery done!"