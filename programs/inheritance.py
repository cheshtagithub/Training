#            ​ Inheritance:

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def greet(self):
        return f"Hello, my name is {self.firstname} {self.lastname}."

class Information(Person):
    def __init__(self, fname, lname, age, profession):
        super().__init__(fname, lname)
        self.age = age
        self.profession = profession
        
    def info(self):
        return f"I am {self.age} years old and work as a {self.profession}."

p = Information("Shruti", "Mittal", 30 ,"chef")
print(f"{p.greet()} {p.info()}")

'''
Output:
Hello, my name is Shruti Mittal. I am 30 years old and work as a chef.
'''
