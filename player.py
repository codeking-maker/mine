class Player:
    def __init__(self, name, position=(0, 0, 0)):
        self.name = name
        self.position = position

    def move(self, direction):
        if direction == "up":
            self.position = (self.position[0], self.position[1], self.position[2] + 1)
        elif direction == "down":
            self.position = (self.position[0], self.position[1], self.position[2] - 1)
        elif direction == "left":
            self.position = (self.position[0] - 1, self.position[1], self.position[2])
        elif direction == "right":
            self.position = (self.position[0] + 1, self.position[1], self.position[2])
        print(f"{self.name} moved {direction}. New position: {self.position}")

    def interact(self, object):
        print(f"{self.name} interacts with {object}")

# Example usage
if __name__ == '__main__':
    player = Player("Hero")
    player.move("up")
    player.interact("a treasure chest")