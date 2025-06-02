import random

class Board:
    def __init__(self, size=100):
        self.size = size
        self.snakes = {}  # {head: tail}
        self.ladders = {} # {start: end}

    def add_snake(self, head, tail):
        self.snakes[head] = tail

    def add_ladder(self, start, end):
        self.ladders[start] = end

    def get_new_position(self, pos):
        if pos in self.snakes:
            print(f"Oops! Bitten by a snake at {pos}, moving to {self.snakes[pos]}")
            return self.snakes[pos]
        if pos in self.ladders:
            print(f"Yay! Climbed a ladder at {pos}, moving to {self.ladders[pos]}")
            return self.ladders[pos]
        return pos


class Dice:
    @staticmethod
    def roll():
        return random.randint(1, 6)


class Player:
    def __init__(self, name):
        self.name = name
        self.position = 1  # Starting position

    def move(self, steps, board):
        new_position = self.position + steps
        if new_position > board.size:
            print(f"{self.name} rolled {steps}, but can't move beyond {board.size}")
            return  # Stay at the same position
        self.position = board.get_new_position(new_position)
        print(f"{self.name} moved to {self.position}")


class GameController:
    def __init__(self, players, board):
        self.players = players
        self.board = board
        self.dice = Dice()

    def play_turn(self, player):
        print(f"\n{player.name}'s turn:")
        roll = self.dice.roll()
        print(f"{player.name} rolled a {roll}")
        player.move(roll, self.board)
        if player.position == self.board.size:
            print(f"\n🏆 {player.name} wins! 🏆\n")
            return True
        return False

    def start_game(self):
        print("🎲 Snakes and Ladders Game Started! 🎲\n")
        while True:
            for player in self.players:
                if self.play_turn(player):
                    return

# Example Usage
board = Board()
board.add_snake(99, 10)
board.add_snake(95, 25)
board.add_ladder(5, 30)
board.add_ladder(40, 90)

players = [Player("Alice"), Player("Bob")]
game = GameController(players, board)
game.start_game()
