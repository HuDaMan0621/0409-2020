"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

Open the starter code (hero-starter-part1.py) for the hero game and rewrite it using objects.
Step 1
Make a Hero class to store the health and power of the hero, and make a Goblin class to store the health and power of the goblin. 
Use a hero object in place of the variables hero_health and hero_power and use a goblin object in place of the variables goblin_health 
and goblin_power all through out the app.

Step 2
Rewrite the code for the hero attacking the goblin and extract it into a method (call it attack) of the Hero class. 
Replace the existing code with a call to the attack method. Hint: attack should take in the goblin (enemy) as a parameter: hero.attack(goblin)

"""
from globin import Globin
from hero import Hero
# def main():
    # hero_health = 10
    # hero_power = 5
    # goblin_health = 6
    # goblin_power = 2

    while Globin.health > 0 and hero_health > 0:
        print("You have %d health and %d power." % (hero_health, hero_power))
        print("The goblin has %d health and %d power." % (goblin_health, goblin_power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            goblin_health -= hero_power
            print("You do %d damage to the goblin." % hero_power)
            if goblin_health <= 0:
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin_health > 0:
            # Goblin attacks hero
            hero_health -= goblin_power
            print("The goblin does %d damage to you." % goblin_power)
            if hero_health <= 0:
                print("You are dead.")

# main()
