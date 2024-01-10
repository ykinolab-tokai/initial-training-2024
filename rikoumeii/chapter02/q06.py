class DataManager:
    def _init_(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def add_x(self,delta):
        x += delta
    
    def add_y(self,delta):
        y += delta

    def add_z(self,delta):
        z += delta

    def sum(self):
        return self.x + self.y + self.z
