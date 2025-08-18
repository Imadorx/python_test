class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}  
    def add_animal(self, animal_type, count=1):
        
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    def get_info(self):
        
        title = f"{self.name}'s Farm\n"
        if not self.animals:
            return title + "\nNo animals yet.\n\nE-I-E-I-O!"

        longest = max(len(a) for a in self.animals.keys())
        lines = []
        for animal, count in self.animals.items():
            lines.append(f"{animal.capitalize():<{longest}} : {count}")

        body = "\n".join(lines)
        return f"{title}\n{body}\n\nE-I-E-I-O!"

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        if not self.animals:
            return f"{self.name}'s farm has no animals yet."

        def pluralize(name, n):
            if n <= 1:
                return name
            if name.lower() == "sheep":
                return "sheep"   
            return name + "s"

        kinds = self.get_animal_types()
        parts = [pluralize(k, self.animals[k]) for k in kinds]

        if len(parts) == 1:
            animals_str = parts[0]
        elif len(parts) == 2:
            animals_str = f"{parts[0]} and {parts[1]}"
        else:
            animals_str = ", ".join(parts[:-1]) + f" and {parts[-1]}"

        return f"{self.name}'s farm has {animals_str}."

macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')      
macdonald.add_animal('sheep')      
macdonald.add_animal('goat', 12)

print(macdonald.get_info())

print(macdonald.get_animal_types())  
print(macdonald.get_short_info())    
