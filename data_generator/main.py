from datetime import datetime, timedelta
import os

from generators.species_generator import SpeciesGenerator
from generators.player_generator import PlayerGenerator
from generators.equipment_generator import EquipmentGenerator
from generators.event_generator import EventGenerator
from utils.csv_generator import CSVGenerator
from data.data import *
# init
species_gen = SpeciesGenerator()
player_gen = PlayerGenerator()
equip_gen = EquipmentGenerator()
event_gen = EventGenerator()
writer = CSVGenerator()

# generate
species = species_gen.process_all_maps(all_maps_data)
players = player_gen.generate_players(names)
rods, rod_cap = equip_gen.generate_rods(rod_data)
baits, bait_cap = equip_gen.generate_baits(bait_data)

# write
writer.write(species, "data_generator/output/species/species.csv")
writer.write(players, "data_generator/output/players/players.csv")
writer.write(rods, "data_generator/output/equipments/rods.csv")
writer.write(rod_cap, "data_generator/output/equipments/rod_capability.csv")
writer.write(baits, "data_generator/output/equipments/baits.csv")
writer.write(bait_cap, "data_generator/output/equipments/bait_capability.csv")
writer.write(maps_data, "data_generator/output/maps/maps.csv")

start_date = datetime(2026, 4, 1)
num_days = 5
events_per_day = 100

base_output_path = 'data_generator/output/events'

for i in range(num_days):

    current_date = start_date + timedelta(days=i)

    events = event_gen.generate_events(players, species, rods, rod_cap, baits, bait_cap, events_per_day, current_date)

    folder_path = os.path.join(base_output_path, f"date={current_date.date()}")

    file_path = os.path.join(folder_path, "events.csv")

    writer.write(events, file_path)

    print(f"Generated {len(events)} events for {current_date.date()}")