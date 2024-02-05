class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


brian = Person("Brian Ngoya")
# print(brian.name)
brian.talk()

bob = Person("Bob Smith")
bob.talk()