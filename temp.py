class Ashish:
    a = 10
    def __init__(self):
        self.ash = 20
        self.__secret = 10

    def __ashish__(self):
        print("works")
    def __setattr__(self,name,value):
        print(name,value)
        self.__dict__[name] = value
