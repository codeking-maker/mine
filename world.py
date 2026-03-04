# world.py

class World:
    def __init__(self):
        self.terrain = self.generate_terrain()
        self.environment = self.create_environment()

    def generate_terrain(self):
        # Placeholder for terrain generation logic
        terrain = "flat"
        return terrain

    def create_environment(self):
        # Placeholder for environment creation logic
        environment = "default"
        return environment

    def display_info(self):
        print(f"Terrain: {self.terrain}")
        print(f"Environment: {self.environment}")

# Example Usage
if __name__ == '__main__':
    world = World()
    world.display_info()