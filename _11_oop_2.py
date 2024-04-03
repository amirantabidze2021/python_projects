# აბსტრაქცია = ენკაფსულაცია + მონაცემთა დამალვა
#Encapsulation - oop-ის ერთ-ერთი მექანიზმი 
#data hiding

'''
მონაცემები:
1. საჯარო ტიპის - Public 
2. დაცული - protected 
3. პრივატული - private

'''
'''

# Encapsulation
class animal:
    def __init__(self):
        self.pub = "I am pubic type data "  # საჯარო ტიპის
        self._prot = " I am protected type data" # _ " ერთი ქვედა ტირე  = დაცული ტიპი"
        self.__priv = "I am private "  # __ private type

a = animal()

print(a.pub)
print(a._prot)
print(a.__priv) #AttributeError: 'animal' object has no attribute '__priv
'''

'''

# Single Inheritance
class Animal:
    def __init__(self, name, age):
        self.name= name
        self.age = age

    def family(self):
        return f"Animal class include {self.name} animal and his age is {self.age}"
    
class Zoo(Animal):
    def __init__(self,name, age,color):
        super().__init__(self,color) #იგივე ჩანაწერია Animal.__init__(self,color)
        self.name= name
        self.age = age 
        self.color = color 
    def family(self):
        return f"Animal class include {self.name} animal and his age is {self.age}, color is {self.color}"
    
#animal_1  = Animal("Zebra", 20) 
#print(animal_1.family())
#animal_1 = Zoo("Zebra",20,"blue")
#print(animal_1.family())
#print(issubclass(Zoo,Animal))              #issubclass(class1,class2)-->True or False
'''
'''
# multilevel inheritance

class shape:
    def __init__(self, color):
        self.color  = color 

    def name(self):
        return f"I am Shape and my color is {self.color}"
    
class Quadrangle(shape):
    def __init__(self, a,b,c,d, color):
        super().__init__(color)
        self.a = a 
        self.b = b 
        self.c = c 
        self.d = d 

    def name(self):
        return f"I am Shape, and my size is {self.a},{self.b},{self.c},{self.d} and my color is {self.color}"
    
class Rectangle(Quadrangle):
    def __init__(self, a, b, color):
        shape.__init__(self,color)
        self.a = a 
        self.b = b 
    def name(self):
        return f"I am Shape, and my size is {self.a},{self.b} and my color is {self.color}"
fig1 = shape("red")
#print(fig1.name())

fig2 = Quadrangle(4,2,3,5,"blue")
#print(fig2.name())

fig3 = Rectangle(7,1,"green")
print(fig3.name())
'''

#Polymorphism -პოლიმორფიზმი -მრავალფორმიანობა

'''
class Cat:
    def eat(self):
        print("Cat drinks milk")
    def walk(self):
        print("cat walks 3 km/h speed")

class Dog:
    def eat(self):
        print("Dogs eats a bone ")
    def walk(self):
        print("Dogs walks 100 km/h speed ")
dog1 = Dog()
cat1 = Cat()
print(isinstance(dog1,Cat))                    #isinstance(obj,class)-->True or False
#cat1.eat()

#dog1.eat()
'''

print()
def name():
    print("Hello")

