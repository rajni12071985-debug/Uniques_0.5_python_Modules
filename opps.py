
 #four pillar of opps |

 #1. abstraction    Hiding the implementation detail of the class and showing the essential feature to the user.


class car :

    def __ init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):

        self.clutch = True
        self.acc = True
        print("Car Starting...")

car1 = car()
car1.start()        


            
 #2. Encapsulation
 #3. inheritance
 #4. polymorphism

# OPPS CONCEPT

# to map a real world scenarios, we started using object in code .

# 1. Procedural programming : in this we write code in sequence and execute it.
# 2. Object oriented programming : in this we create object and class to map real world scenarios.

# creating class  : class is a blueprint for creating object 

class car:
    name = "BMW"
    model = "X5"
    year = 2020

 # creating object : object is an instance of class
car1 = car()
print(car1.name)
print(car1.model)
print(car1.year)


  # constructer : All classes have a function called _init_() function 
  #               which is always execute when the class is being initiated.


class student:
    # default constructor
    section_name = "CSD"   #------------> class attributes
    def __init__(self): 
        
        print("Adding new student data successfully....")    
#                -----------------> self  parameter is used to refer to the current instance of the class. It is a convention to use self as the name of the first parameter in instance methods, but you can choose any name you like. The self parameter allows you to access the attributes and methods of the class within its own definition.
#                |-----------------> we can also use xyz , hello, etc instead of self but it is a convention to use self.

    def __init__(self, name, age,rollno):   # parameterized constructor
         # constructor
        self.name =name
        self.age= age 
        self.rollno = rollno
        print("uploading new student data successfully....") # constructer

s1 =student("pragati", 20, 101)  
print(s1.name)
print(s1.age)   
print(s1.rollno)  

s2 = student("harshita", 21, 102)
print(s2.name)
print(s2.age)
print(s2.rollno)

print(s1.section_name)
print(student.section_name)  # accessing class attribute using class name


#  obj attri > class attri
 

class fruit:
    name  ="mango"  # class attribute
    color = "yellow"  # class attribute

    def __init__(self, name , color):
        self.name  = name
        self.color = color

f1 = fruit("apple", "red")  
print(f1.name)  # accessing object attribute
print(f1.color) # accessing object attribute  



class house:
    def __init__(self , location):
        self.location = location

    def greet (self):
        print("welcome to " ,self.location) 

h1 = house("prayagraj") 

print(h1.greet())






class student :

    def __init__(self):
        print("Welcome student!")

    def __init__( self , name , marks) :
        self.name = name 
        self.marks = marks

    def percentage(self):
        sum = 0
        for i in self.marks:
            sum = sum +i
        print( " you get", (sum/300) *100 ,"percentage" )  

s1 = student ("pragati",[99,98,99])

s1.percentage()



# static method :  that dont use any self parameter 


class math:
    @staticmethod    # decorator
    def add(a, b):
        return a + b
    def mul(a,b):
        return a*b


addition = math.add(23,56)
print(addition)

multiplication = math.mul(4,6)
print(multiplication)






