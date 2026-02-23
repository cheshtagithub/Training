'''            ​ Class methods:
1. __str__() method:
Without __str__():'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
p1 = Person("Emily", 36)
print(p1)
'''
Output:
<__main__.Person object at 0x7cfcf3f91be0>

With __str__():'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name}({self.age})"
p1 = Person("Emily", 36)
print(p1)
'''
Output:
Emily(36)

2. delete method:'''

class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello!")

p1 = Person("Emil")
p1.greet() 

del Person.greet

p1.greet() 

'''
Output:
Hello!
ERROR!
Traceback (most recent call last):
  File "<main.py>", line 13, in <module>
AttributeError: 'Person' object has no attribute 'greet'
'''
