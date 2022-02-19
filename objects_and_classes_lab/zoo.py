class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        self.__animals += 1  # Zoo.__animals += 1

        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

    def get_info(self, species):
        animals_name = None
        res = None
        if species == "mammal":
            animals_name = self.mammals
            res = "Mammals"
        elif species == "fish":
            animals_name = self.fishes
            res = "Fishes"
        elif species == "bird":
            animals_name = self.birds
            res = "Birds"
        animals_data = ", ".join(animals_name)
        return f"""{res} in {self.name}: {animals_data}
Total animals: {self.__animals}"""


zoo_name = input()
n = int(input())
zoo = Zoo(zoo_name)

for i in range(n):
    args = input().split()
    zoo.add_animal(args[0], args[1])

species_type = input()
res = zoo.get_info(species_type)
print(res)
