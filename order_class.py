# Google Hash Code Qualification 2016

class Orders:
    def __init__(self, dest, done = False, prod, remaining):
        self.dest = dest
        self.done = done
        self.prod = prod
        self.remaining = remaining

    def receive(self, type, n):
        self.prod[type] = self.prod[type] - n
        self.remaining = self.remaining - n
        if self.remaining == 0: self.done =True

    def isCompleted(self):
        if self.done : return True
        else : return False