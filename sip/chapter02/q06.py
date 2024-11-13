class DataManager():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def add_x(self,delta):
        self.x += delta
        return self.x
    def add_y(self,delta):
        self.y += delta
        return self.y
    def add_z(self,delta):
        self.z += delta
        return self.z
    
    def sum(self):
        return self.x + self.y + self.z
    


data_manager = DataManager(2, 3, 5)
print(data_manager.sum())  
data_manager.add_x(4)     
print(data_manager.sum()) 
data_manager.add_y(0)     
print(data_manager.sum())  
data_manager.add_z(-9)     
print(data_manager.sum())  