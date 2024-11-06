class DataManager():   #３つの属性x,y,zを持つDataManagerクラスを定義する。
    def __init__(self,x,y,z): #オブジェクトの初期化
        self.x=x              #引数xを受け取り、オブジェクトの属性self.xに代入
        self.y=y
        self.z=z
    def add_x(self,delta): #引数deltaの値をそれぞれx,y,zに加算する
        self.x+=delta
    def add_y(self,delta):
        self.y+=delta
    def add_z(self,delta):
        self.z+=delta
    def sum(self,):         #x,y,zの現在の値の合計を計算し返す
        return self.x+self.y+self.z

data_manager = DataManager(2, 3, 5)#data_managerインスタンスを（）の値で初期化
print(data_manager.sum())  # => 10(sumメソッドでx,y,zの合計を計算)
data_manager.add_x(4)      # => data_manager.x の値が 2 から 6 に更新される
print(data_manager.sum())  # => 14（6+3+5）
data_manager.add_y(0)      # => data_manager.y の値が 3 から 3 に更新される
print(data_manager.sum())  # => 14
data_manager.add_z(-9)     # => data_manager.z の値が 5 から -4 に更新される
print(data_manager.sum())  # => 5(6+3-4)
#結果
#10
#14
#14
#5