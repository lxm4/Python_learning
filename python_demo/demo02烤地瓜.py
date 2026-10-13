class SweetPotato:
    def __init__(self):
        self.name = "sweet potato"
        self.state = "raw"
        self.cooked_time = 0
        self.condiments = []

    def cook(self, time):
        self.cooked_time += time
        if self.cooked_time < 5:
            self.state = "raw"
        elif 5 <= self.cooked_time < 10:
            self.state = "half-cooked"
        else:
            self.state = "cooked"

    def add_condiments(self, condiments):
        self.condiments = condiments

    def __str__(self):
        if self.condiments:
            return f"{self.name} is {self.state} and has {self.condiments}."
        else:
            return f"{self.name} is {self.state}."

sp1=SweetPotato()
sp1.cook(3)
sp1.add_condiments("salt")
sp1.cook(5)
sp1.cook(15)
sp1.add_condiments("butter")
print(sp1)