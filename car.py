class Car:
    def __init__(self,model,colour,registration,make):
        self.model=model
        self.colour=colour
        self.registration=registration
        self.make=make
    def speed(self):
        return f"Iam a {self.model} with{self.colour} colour and a registration of{self.registration} hence having a maake of {self.make} "
    def accellaration(self):
        return f"I bought a {self.model} car with a{self.colour} colour and a registration  number of{self.registration} hence having a maake of {self.make} "
    


