class Beer:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        
    def drinkable(self):
        
        if self.name == "keystone":
            print("Don't drink")
            
        if self.name == "guiness":
            print("Sure have a sip")
            
        else:
            print('DRINK UP')
            
        
        
b = Beer('budlight', '12oz')
newbeer = Beer("guiness", '12oz')
newbeer.drinkable()
b.drinkable()






# print(b.name)
# print(b.size)

    
