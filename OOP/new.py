class Character:
    def __init__(self, name, health, attack, blood):
        self.name = name
        self.health = health
        self.attack = attack
        self.blood = blood

    def attack_enemy(self):
        print(f"{self.name} attacks {self.name} for {self.attack} {self.blood} damage!")

warrior = Character("Warrior", 100, 20, "physical")
mage = Character("Mage", 80, 25, "arcane")

warrior.attack_enemy()  # Output: Warrior attacks Mage for 20 physical damage!
mage.attack_enemy()  # Output: Mage attacks Warrior for 25 arcane damage!

