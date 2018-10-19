class User:
    firstName = None
    def __init__(self):
        pass
    def printFirstName(self):
        print(self.firstName)
class Programmer(User):
    lastName = None
    def _init_(self):
        pass
    def printLastName(self):
        print(self.lastName)

programmer1 = Programmer()
programmer1.firstName = "Arief"
programmer1.lastName = "Wicaksono" 
programmer1.printFirstName()
programmer1.printLastName() 
