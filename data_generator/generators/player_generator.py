import random
from datetime import datetime, timedelta, timezone

class PlayerGenerator:
    
    def __init__(self):
        self.player_counter = 0

    def generate_player_id(self):
        self.player_counter += 1
        return f"P{self.player_counter:04d}"
    
    def generate_joined_date(self):
        days_ago = random.randint(1, 90)
        return (datetime.now(timezone.utc) - timedelta(days=days_ago)).date().isoformat()
    
    def generate_country(self):
        countries = [
            "United States", "Canada", "Brazil", "Argentina", "United Kingdom", "France", "Germany", "Italy",
            "Spain", "Japan", "China", "India", "Australia", "South Africa", "Mexico", "Russia",
            "South Korea", "Vietnam", "Thailand", "Egypt", "Nigeria", "Kenya", "Turkey", "Saudi Arabia",
            "Indonesia", "Netherlands", "Sweden", "Norway", "Finland", "Denmark", "Poland", "Greece",
            "Portugal", "Switzerland", "Austria", "Belgium", "Ireland", "New Zealand", "Chile", "Colombia"
        ]
        return random.choice(countries)
    
    def generate_level(self):
        return random.randint(1, 10)
    
    def generate_players(self, names):
        players = []

        for name in names:
            players.append({
                "player_id": self.generate_player_id(),
                "first_name": name["first_name"],
                "last_name": name["last_name"],
                "joined_data": self.generate_joined_date(),
                "level":self.generate_level(),
                "country": self.generate_country(),
                "created_at": datetime.now(timezone.utc).isoformat()
            })

        return players