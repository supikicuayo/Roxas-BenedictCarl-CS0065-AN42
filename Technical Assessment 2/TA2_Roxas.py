rooms = {
    "A": input("Enter the initial state of Room A (dirty/clean): ").lower(),
    "B": input("Enter the initial state of Room B (dirty/clean): ").lower()
}

def is_dirty(room):
    return rooms[room] == "dirty"

def clean_room(room):
    rooms[room] = "clean"

class VacuumAgent:
    def __init__(self):
        self.location = "A"

    def move(self):
        if self.location == "A":
            self.location = "B"
        else:
            self.location = "A"

    def perceive_and_act(self):
        if is_dirty(self.location):
            clean_room(self.location)
            return "Cleaned"
        else:
            self.move()
            return "Moved"

agent = VacuumAgent()
steps = int(input("Enter number of steps: "))

print("\nInitial Environment:")
print(rooms)
print("Initial Agent Location:", agent.location)

for step in range(steps):
    action = agent.perceive_and_act()
    print("\nStep", step + 1)
    print("Agent Location:", agent.location)
    print("Action:", action)
    print("Environment:", rooms)

print("\nFinal Environment:")
print(rooms)