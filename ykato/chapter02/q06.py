class DataManager:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add_x(self, delta):
        self.x += delta

    def add_y(self, delta):
        self.y += delta

    def add_z(self, delta):
        self.z += delta

    def sum(self):
        return self.x + self.y + self.z

data_manager = DataManager(2, 3, 5)
print(data_manager.sum()) # => 10

data_manager.add_x(4)     # => data_manager.xの値が2から6に更新される
print(data_manager.sum()) # => 14

data_manager.add_y(0)     # => data_manager.yの値が3から3に更新される
print(data_manager.sum()) # => 14

data_manager.add_z(-9)    # => data_manager.zの値が5から-4に更新される
print(data_manager.sum()) # => 5
