from generators.species_generator import SpeciesGenerator
from generators.player_generator import PlayerGenerator
from generators.equipment_generator import EquipmentGenerator
from utils.csv_generator import CSVGenerator
from data.data import *
# init
species_gen = SpeciesGenerator()
player_gen = PlayerGenerator()
equip_gen = EquipmentGenerator()
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