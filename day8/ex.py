class Father:
    def __init__(self):
        self.money=1000
        print("Father Class ")
    def show(self):
        print("Show Method")


class Son(Father):
    def __init__(self):
        self.money=1500
        self.car='BMW'
        print("son class Constructor")

    def disp(self):
        print("son class")

s=Son()
print(s.money)