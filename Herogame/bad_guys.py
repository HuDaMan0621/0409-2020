from character import Character

#Bad_guys is a subclass of Character
#Bad_guys inherits from Character
#Character is the super clas of Bad_guys

class Bad_guys(Character):
    def receive_damage(self, how_much):
        self.health -= how_much
        if self.health <=0:
            self.health = 5

# class Bad_guys():

#     def __init__(self, bad_guys_name, secret_identity, power, health, bio):
#         self.bad_guys_name = bad_guys_name
#         self.secret_identity = secret_identity
#         self.power = power
#         self.health = health
#         self.bio = bio
#     def __repr__(self):
#         return f'{self.bad_guys_name}has power {self.power}'

#     def make_entrance(self):
#         return f'{self.bad_guys_name} has the power to {self.bio}'

#     def recharge(self):
#         self.health += 10
#         print(f'{self.bad_guys_name} increeeeeaaaased the health {self.health}')

#     def status(self):
#         if self.health < 50:
#             print(f'{self.bad_guys_name}has health {self.health} and needs to rest')
#         elif self.health > 150:
#             print(f'{self.bad_guys_name}has health {self.health} and can steal')
#         else:
#             print(f'{self.bad_guys_name}has health {self.health} and stop doing bad things')
 
#     def strike(self):
#         print(f'you called the strike function!{self.bad_guys_name}')
        

# im = Hero ('Iron Man', 'Tony Stark', 20, 100, 'calls for back up - multiple iron mans')
# su = Hero ('Super Man','Burce william', 5000, 100000, 'shoot laser beams')
    
    # def __init__(self, name, secret_identity, power, health, special_power):
    #     self.name = name
    #     self.secret_identity = secret_identity
    #     self.power = power
    #     self.health = health
    #     self.special_power = special_power

    # def __repr__(self):
    #     return f'{self.name} has power {self.power}'

    # def make_entrance(self):
    #     print(f'{self.name} has the {self.health}')

    # def intro(self):
    #     print(f'{self.name} special power is to {self.special_power}')


