import random
from datetime import datetime

class SpeciesGenerator:
    def __init__(self):
        self.counters = {}
    
    def generate_rarity(self):
        options = ["common", "rare", "epic"]
        weights = [60, 30, 10]
        return random.choices(
            options,
            weights,
            k=1
        )[0]
    
    def generate_difficulty(self, rarity):

        if rarity == 'common':
            return random.choices(["easy", "medium"], [80, 20], k=1)[0]
        elif rarity == 'rare':
            return random.choices(["medium", "hard"], [70, 30], k=1)[0]
        elif rarity == 'epic':
            return "hard"

    def generate_active_time(self):
        options = ['day', 'night', 'day/night']
        weights = [50, 25, 25]

        return random.choices(options, weights=weights, k=1)[0]
    
    def generate_weight(self, rarity):

        if rarity == 'common':
            min_w = random.uniform(0.5, 3.5)
            max_w = random.uniform(min_w, 5.0)
        elif rarity == 'rare':
            min_w = random.uniform(3.5, 10.0)
            max_w = random.uniform(min_w, 15.0)
        else:
            min_w = random.uniform(10.0, 25.0)
            max_w = random.uniform(min_w, 50.0)

        return round(min_w, 2), round(max_w, 2)

    def get_shadow_size(self, min_weight, max_weight):
        avg_weight = (min_weight + max_weight) / 2

        if avg_weight < 3.5:
            return "small"
        elif avg_weight <= 10:
            return "medium"
        else:
            return "large"
    
    def get_shadow_speed(self, difficulty):

        if difficulty == 'easy':
            return 'slow'
        elif difficulty == 'medium':
            return 'medim'
        else:
            return 'fast'
        
    def calculate_price(self, min_weight, max_weight, rarity):

        avg_weight = (min_weight + max_weight) / 2
        
        if rarity == 'common':
            multiplier = 10
        elif rarity == 'rare':
            multiplier = 25
        elif rarity == 'epic':
            multiplier = 50

        variation = random.uniform(0.9, 1.1)

        price = avg_weight * multiplier * variation

        return int(round(price))

    def generate_season(self):
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

        choice = random.choices(
            ["all", "range", "single"],
            weights=[50, 30, 20],
            k=1
        )[0]

        if choice == "all":
            return "all"

        elif choice == "single":
            return random.choice(months)

        else:  
            start = random.randint(0, 11)
            max_length = 12 - start
            length = random.randint(1, max_length)
            end = start + length - 1

            return f"{months[start]}–{months[end]}"

    def generate_species_id(self, map_id, species_type):
        species_type = species_type.upper()

        if map_id not in self.counters:
            self.counters[map_id] = {
                "FISH": 0,
                "CREATURES": 0,
                "MONSTERS": 0
            }

        self.counters[map_id][species_type] += 1

        count = self.counters[map_id][species_type]

        return f"{map_id}_{species_type}_{count:03d}"
    

    def build_record(self, name, category, map_id):
        
        species_id = self.generate_species_id(map_id, species_type=category)
        current_time = datetime.now().isoformat()
        rarity = self.generate_rarity()
        difficulty = self.generate_difficulty(rarity)
        min_w, max_w = self.generate_weight(rarity)
        shadow_size = self.get_shadow_size(min_w, max_w)
        shadow_speed = self.get_shadow_speed(difficulty)
        active_time = self.generate_active_time()
        season = self.generate_season()
        base_price = self.calculate_price(min_w, max_w, rarity)

        return {
            "species_id":species_id,
            "species_name": name,
            "species_type": category,
            "map_id": map_id,
            "rarity": rarity,
            "min_weight": min_w,
            "max_weight": max_w,
            "shadow_size": shadow_size,
            "shadow_speed": shadow_speed,
            "active_time": active_time,
            "season": season,
            "difficulty": difficulty,
            "base_price": base_price,
            "created_at": current_time,
        }
    
    def build_species(self, map_data):
        result = []
        map_id = map_data["map_id"]
        
        for category in ["fish", 'creatures', 'monsters']:
            for name in map_data[category]:
                record = self.build_record(name, category, map_id)
                result.append(record)
        
        return result
    
    def process_all_maps(self, all_maps_data):
        final_data = []

        for map_data in all_maps_data:
            final_data.extend(self.build_species(map_data))

        return final_data    

