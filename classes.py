class Person:
    def getname():
        return name

    def getage():
        return age
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(name + ': Hi! My name is {0}. I am {1} years old.'.format(name, age))

    def say(s):
        print(getname() + ': ' + s)
bob = Person('Bob', 9)


