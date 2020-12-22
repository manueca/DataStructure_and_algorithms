
  
class Parent: 
  
    # constructor of Parent class 
    def __init__(self): 
        # Initialization of the Strings 
        self.String1 ="Hello"
        self.String2 ="World"
  
    def Function2(self): 
        print("Function2 : ", self.String1) 
        return
  
# Child class is inheriting from Parent class 
class Child(Parent): 
  
    def Function1(self): 
        # calling Function2 Method in parent class  
        self.Function2() 
        print("Function1 : ", self.String2) 
        return   
  
### Instance of Parent class 
Object1 = Parent() 
  
### Instance of Child class 
Object2 = Child() 
  
# Calling Function1 using Child class instance 
Object2.Function1() 