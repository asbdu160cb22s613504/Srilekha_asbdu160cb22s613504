# Define the base class Player
class Player:
    def play(self):
        print("The player is playing cricket.")

# Derive the Batsman class from Player
class Batsman(Player):
    def play(self):
        print("The batsman is batting.")

# Derive the Bowler class from Player
class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")

# Create objects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

# Call the play() method for each object
batsman.play()
bowler.play()