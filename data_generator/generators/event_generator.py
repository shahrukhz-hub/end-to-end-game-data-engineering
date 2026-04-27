import random
from datetime import datetime, timezone, timedelta

class EventGenerator:
    def __init__(self):
        self.event_counter = 0

    def generate_event_id(self):
        self.event_counter += 1
        return f"E{self.event_counter:05d}"

    def generate_event_time(self, base_date):
        seconds = random.randint(0, 86400)
        return (base_date + timedelta(seconds)).isoformat()
    
    def get_species_capability(self, species):
        return f"{species["rarity"]}_{species["species_type"]}"
    
    def get_valid_ids(self, species_cap, mapping, id_key):
        base_type = species_cap.split("_")[-1]

        return [
            m[id_key]
            for m in mapping
            if m["capability"] == species_cap or m["capability"] == base_type
        ]
    
    def pick_rod(self, species_cap, rods, rod_capability):
        valid_ids = self.get_valid_ids(species_cap, rod_capability, "rod_id")
        valid_rods = [r for r in rods if r["rod_id"] in valid_ids]

        if valid_rods and random.random() < 0.8:
            return random.choice(valid_rods)
        
        return random.choice(rods)


    def pick_bait(self, species_cap, baits, bait_capability):
        valid_ids = self.get_valid_ids(species_cap, bait_capability, "bait_id")
        valid_baits = [b for b in baits if b["bait_id"] in valid_ids]

        if not valid_baits or random.random() < 0.3:
            return None
        
        return random.choice(valid_baits)
    

    def generate_events(self, players, species_data, rods, rod_capability, baits, bait_capability, num_events, base_date):

        species = random.choice(species_data)
        player = random.choice(players)

        species_cap = self.get_species_capability(species)

        rod = self.pick_rod(species_cap, rods, rod_capability)
        bait = self.pick_bait(species_cap, baits, bait_capability)

        events = []

        success = True
        if rod is None:
            success = False

        for _ in range(num_events):
            events.append({
                "event_id": self.generate_event_id(),
                "player_id": player["player_id"],
                "species_id": species["species_id"],
                "map_id": species["map_id"],
                "rod_id": rod["rod_id"] if rod else None,
                "bait_id": bait["bait_id"] if bait else None,
                "event_type": "catch",
                "event_time": self.generate_event_time(base_date),
                "weight": species["min_weight"],
                "price": species["base_price"],
                "success_flag": success,
                "created_at": datetime.now(timezone.utc).isoformat()
            })
        
        return events
    
    