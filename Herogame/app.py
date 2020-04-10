from hero import Hero
from bad_guys import Bad_guys
from character import Character

def main():

    while im.health > 0 and gk.health >0:
        print("What do you want to do?")
        print("1. Iron man attack Goblin King ")
        print("2. Goblin King attacks Iron Man")
        print("3. Exit")
        print("> ",)
        user_input = input()
        if user_input == "1": 
            # Iron man attacks Goblin King
            # health -= power
            print(f'Iron man power "{im.power}" and Iron Man health "{im.health}"')
            print(f'Iron man does "{im.power}" damage to the goblin." "{gk.health}"')
            current_health = gk.health - im.power
            print(f'goblin king now has "{current_health}"')
            gk.health = current_health
            
            if gk.health <= 0:
                print("The goblin king is dead.")
                break
        
        elif user_input == "2":
            print(f'Globin King power "{gk.power}" and Globin King health "{gk.health}"')
            print(f'Globin King does "{gk.power}" damage to Iron Man." "{im.health}"')
            current_health = gk.power - im.health
            print(f'Iron Man now has "{current_health}"')
            im.health = current_health
            
            if im.health <= 0:
                print("Iron man needs to recharge - iron man never dies")
                im.recharge()
                
        elif user_input == "3":
            print("Goodbye.")
            break
    else:
         print("Invalid input %r" % user_input)

    # if goblin_health > 0:
    #     # Goblin attacks hero
    #     hero_health -= goblin_power
    #     print("The goblin does %d damage to you." % goblin_power)
    #     if hero_health <= 0:
    #             print("You are dead.")
# while Globin.health > 0 and hero_health > 0:
#         print("You have %d health and %d power." % (hero_health, hero_power))
#         print("The goblin has %d health and %d power." % (goblin_health, goblin_power))
#         print()

#  def __init__(self, name, secret_identity, power, health, bio):
im = Hero ('Iron Man', 'Tony Stark', 20, 100, 'calls for back up - multiple iron mans')
su = Hero ('Super Man','Burce william', 5000, 100000, 'shoot laser beams')

gk = Bad_guys ('Globin King', 'King of the Globin', 15, 250, 'cast spells')
wl = Bad_guys ('Whiplash','super human', 200, 2500, 'throws fire ball with left hand')

# im.strike(gk)
# su.strike()
# gk.strike()
# wl.strike()