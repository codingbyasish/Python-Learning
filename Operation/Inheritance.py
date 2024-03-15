# Single Inheritance
# Multi Level

class GF:
    
    def __init__(self):
        print("Automatically Called when Object is created")
    
    
    name = "Asish"
    def home(self):
        self.name2 = "Asish"
        print("5BHK")

class Father(GF):
    def home2(self):
        print("GOA")

class Son(Father):
   def home3(self):
       print("Bangalore")

asish = Son()
asish.home()
asish.home2()
asish.home3()

mmd = Father()
mmd.home()
mmd.home2()


gkd = GF()
gkd.home()
