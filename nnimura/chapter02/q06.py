class DataManager:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def add_x(self,delta):
        self.x = self.x + delta
    def add_y(self,delta):
        self.y =self.y + delta
    def add_z(self,delta):
        self.z = self.z + delta
    def sum(self):
        return self.x + self.y + self.z
