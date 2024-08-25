class Person:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        print("name is %s" %self.name)

    def get_age(self):
        print("age is %s" %self.age)

    def get_info(self):
        print("name is %s, age is %s" %(self.name, self.age))

    def birthday(self):
        self.age = self.age + 1
        print("HAPPY BIRTHDAY %s" %self.name)


Parsa = Person('Parsa', 13)

Parsa.get_name()
Parsa.get_age()
Parsa.get_info()
Parsa.birthday()
