class Character():
    def __init__(self, name, secret_identity, power, health, bio):
        print('how many prints = to how many characters - Should print 4 times because we have 4 characters')
        self.name = name
        self.secret_identity = secret_identity
        self.power = power
        self.health = health
        self.bio = bio

#this is the representation function 
    def __repr__(self):
        return f'{self.name}has power {self.power}'

    def make_entrance(self):
        return f'{self.name} has the power to {self.bio}'

    def recharge(self):
        self.health += 100
        print(f'{self.name} increeeeeaaaased the health {self.health}')

    def status(self):
        if self.health < 50:
            print(f'{self.name}has health {self.health} and needs to recharge')
        elif self.health > 150:
            print(f'{self.name}has health {self.health} and can perform normal duties')
        else:
            print(f'{self.name}has health {self.health} and feeling great')

    def strike(self,target):
        # print(f'you called the strike function!{self.name}')
        print(f'{self.name} is striking {target.name}')
        # target.health -= self.power
        target.receive_damage(self.power)

    def receive_damage(self, how_many_points):
        print(f'{self.name} receives {how_many_points} damage')
        self.health -= how_many_points