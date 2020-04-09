class Globin():
    
    def __init__(self, name, secret_identity, power, health, special_power):
        self.name = name
        self.secret_identity = secret_identity
        self.power = power
        self.health = health
        self.special_power = special_power

    def __repr__(self):
        return f'{self.name} has power {self.power}'

    def make_entrance(self):
        print(f'{self.name} has the {self.health}')

    def intro(self):
        print(f'{self.name} special power is to {self.special_power}')
gl = Globin ('Globin King', 'King of the Globin', 15, 250, 'cast spells')

print (gl)
