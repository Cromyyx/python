import random

class Rabbit:
    def __init__(self, gender, age=0):
        self.gender = gender
        self.age = age
        self.pregnant = False

    def age_one_month(self):
        self.age += 1

    def is_mature(self):
        if self.gender == 'female':
            return self.age >= 5
        else:
            return self.age >= 9

class Simulation:
    def __init__(self, initial_females=3):
        self.month = 0
        self.rabbits = [Rabbit('female') for _ in range(initial_females)]

    def simulate_month(self):
        new_rabbits = []
        for rabbit in self.rabbits:
            rabbit.age_one_month()
            if rabbit.gender == 'female' and rabbit.is_mature() and not rabbit.pregnant:
                rabbit.pregnant = True
            elif rabbit.pregnant:
                rabbit.pregnant = False
                for _ in range(6):  # average 6 offspring
                    gender = random.choice(['male', 'female'])
                    new_rabbits.append(Rabbit(gender))
        self.rabbits.extend(new_rabbits)
        self.month += 1

    def run_simulation(self, months):
        for _ in range(months):
            self.simulate_month()
        self.print_results()

    def print_results(self):
        males = sum(1 for rabbit in self.rabbits if rabbit.gender == 'male')
        females = sum(1 for rabbit in self.rabbits if rabbit.gender == 'female')
        print(f"Nach {self.month} Monaten gibt es {len(self.rabbits)} Kaninchen: {males} Männchen und {females} Weibchen.")

# Simulation starten
simulation = Simulation()
simulation.run_simulation(12)  # Simulation für 12 Monate
