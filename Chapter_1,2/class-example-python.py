class Man:
    def __init__(self,name):
        self.name = name
        print("Initialized.")
    def hello(self):
        print("Hello" + self.name + "!")
    def goodbye(self):
        print("Bye" + self.name + "!")

m = Man("Edited on Git")
m.hello()
m.goodbye()
