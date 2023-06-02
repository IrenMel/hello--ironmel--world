class Character:
    name = 'some_name'
    power = 0
    energy = 100
    hands = 2
    backpack = []

    def eat(self,food):
        if self.energy < 100:
            self.energy += food
        else:
            print('Not hungry')
    def do_exercise(self, hours):
        if self.energy > 0:
            self.energy -= hours * 2
            self.power += hours * 2
        else:
            print('Too tired')
    def change_alias(self, new_alias):
        print(self)
        self.alias = new_alias

peter = Character()
bruce = Character()

peter.backpack.append('web-shooter') #дадим питеру веб-шутер(оружие)

