class Man:
    def __init__(self,name):
        self.name = name
        print("Initialized.")
    def hello(self):
        print("Hello" + self.name + "!")
    def goodbye(self):
        print("Bye" + self.name + "!")

m = Man("Working on anaconda")
m.hello()
m.goodbye()
