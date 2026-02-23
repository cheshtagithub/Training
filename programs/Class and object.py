'''           ​ Making a class Person and object:
Q1: Inside the editor, complete the following steps:
1. Create a class called Person
2. Add an __init__ method that takes name and age as parameters
3. Add a method called greet that prints "Hello, my name is " followed by the name and “I am _____ years old.” where blank is replaced by age.
Code:'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print("Hello my name is " + self.name +", I am " + self.age +" years old.")

name = input("Enter the name:")
age = input("Enter the age: ")
s1 = Person(name, age)
s1.greet()

'''
Output:
Enter the name:Anjali
Enter the age: 22
Hello my name is Anjali, I am 22 years old.

Q2:Inside the editor, complete the following steps:
1. Create a class called Dog
2. Add an __init__ method that takes self, name, and age as parameters and assigns them as properties
3. Add a method called bark that prints the dog's name followed by " says Woof!"
4. Create an object d1 of the Dog class with name "Buddy" and age 3
5. Print the age of d1
6. Call the bark method on d1

Code:'''

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print(self.name + " says Woof!")
        
d1 =Dog("Buddy", 3)
print(d1.age)
d1.bark()

'''
Output:
3
Buddy says Woof!
'''
