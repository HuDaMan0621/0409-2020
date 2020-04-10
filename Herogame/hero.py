from character import Character
class Hero(Character):
    def receive_damage(self, how_much):
        self.health -= how_much
        if self.health <=0:
            self.health = 5

  

# # hulk = Hero('Huuuulk', 'Dr Bruce Banner', 50, 500, 20)

# # thanos = Villain('Thanos', 'Thanos', 30, 5000, 5)

        # print('hello i am Iron man')
        # self.name = name
        # self.secret_identity = secret_identity
        # self.health = health
        # self.power = power

# def __repr__(self):
#     return f'{self.name} has the power of {self.power}'


# def make_entrance(self):
#     print (f'{self.name} crashes  through the wall')

# def go_to_the_spa(self):
#     self.health += 5
#     print(f'{self.name} increased their health by {self.health}')

# def status(self):
#     if self.health <50:
#         print(f'{self.name} has health {self.health} and looks terrible')
#     elif self.health >150:
#         print(f'{self.name} has health {self.health}and looks amazing!!!')

#     else:
#         print(f'{self.name} has health {self.health}and looks ok')