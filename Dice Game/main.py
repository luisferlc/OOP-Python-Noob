import random
from xml.sax.handler import property_encoding


class Die():

    def __init__(self, value=None):
        self._value = value

    @property
    def value(self):
        return self._value

    def roll(self):
        new_value = random.randint(1,6)
        self._value = new_value
        return new_value


class Player():

    def __init__(self, die, is_computer=False):
        self._die = die
        self._is_computer = is_computer
        self._counter = 5

    @property
    def die(self):
        return self._die

    @property
    def is_computer(self):
        return self._is_computer

    @property
    def counter(self):
        return self._counter

    def increment_counter(self):
        self._counter += 1

    def decrement_counter(self):
        self._counter -= 1

    def roll_die(self):
        return self._die.roll()


class DiceGame:

    def __init__(self, player, computer):
        self._player = player
        self._computer = computer

    def play(self):
        print("==================================")
        print("==== Welcome to roll the dice ====")
        print("==================================")
        print("\n")
        while True: #creates an infinite loop that will run forever until it is explicitly stopped
            self.play_round()
            game_over = self.check_game_over()
            if game_over:
                break

    def play_round(self):
        ### Main functionality
        # 1. Welcome to round message
        self.welcome_round_message()

        # 2. roll the dice
        player_value = self._player.roll_die()
        computer_value = self._computer.roll_die()

        # 3. show values of the dice
        self.show_value_dice(player_value, computer_value)

        # 4. determine winner
        if player_value > computer_value:
            print("You won the round!!")
            self.update_counters(winner=self._player, loser=self._computer)
        elif computer_value > player_value:
            print("You lose this one, try next rounds!")
            self.update_counters(winner=self._computer, loser=self._player)
        else:
            print("This is a tie!")

        # 5. show counters
        self.show_counters()

    ##Supportive functions
    def welcome_round_message(self):
        print("-----------------------------------")
        print("------------ New Round ------------")
        input("Press any key to roll the dice:")

    def show_value_dice(self, player_value, computer_value):
        print(f"\nPlayer value: {player_value}")
        print(f"Computer value: {computer_value}")

    def update_counters(self, winner, loser):
        winner.decrement_counter()
        loser.increment_counter()

    def show_counters(self):
        print(f"\nPlayer counter: {self._player.counter}")
        print(f"Computer counter: {self._computer.counter}")

    def check_game_over(self):
        if self._player.counter == 0:
            self.show_game_over(self._player)
            return True
        elif self._computer.counter == 0:
            self.show_game_over(self._computer)
            return True
        else:
            return False

    def show_game_over(self, winner):
        if winner.is_computer:
            print("-----------------------")
            print("---G A M E - O V E R---")
            print("-----------------------")
            print("The computer wins, try next time.")
            print("-----------------------")
        else:
            print("------------------------")
            print("-- P L A Y E R - W I N !")
            print("------------------------")
            print("Congratulations, arriba la humanidad")
            print("-----------------------")


player_die = Die()
computer_die = Die()

player_one = Player(player_die, False)
computer_one = Player(player_die, True)

first_game = DiceGame(player_one, computer_one)

first_game.play()





#my_die = Die()
#luison = Player(my_die, False)

#print(luison.die)
#print(luison.is_computer)
#print(luison.counter)

#print("Initial die:",my_die.value)
#my_die.roll() #meetodo directo deel dado
#print("first roll:",my_die.value)

#luison.roll_die() #metodo heredado para el player
#print("Second roll:", my_die.value)
#print("second also:", luison.die.value)