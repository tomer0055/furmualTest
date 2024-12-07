import math
class dot:
    color = ""
    def __init__(self, x, y,relativePos):
        self.x =float(x)
        self.y = float(y)
        self.relativePos = relativePos
        if(self.relativePos=="left"):
            self.color = "red"
        elif(self.relativePos=="right"):
            self.color = "blue"
        else:
            self.color = "green"
    def __str__(self):
        return "Dot at x: " + str(self.x) + " y: " + str(self.y) + " color: " + self.color
    
    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)
    def distance_to(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

        