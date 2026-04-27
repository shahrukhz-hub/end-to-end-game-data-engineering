class EquipmentGenerator: 
    def __init__(self):
        self.rod_counter = 0
        self.bait_counter = 0

    def generate_rod_id(self):
        self.rod_counter += 1
        return f"R{self.rod_counter:03d}"
    
    def generate_bait_id(self):
        self.bait_counter += 1
        return f"B{self.bait_counter:03d}"

    def generate_rods(self, rod_data):

        rods = []
        rod_capability = []
        
        for rod in rod_data:
            rod_id = self.generate_rod_id()

            rod_record = {
                "rod_id": rod_id,
                "rod_name": rod["rod_name"],
                "rod_description": rod["rod_description"],
                "buying_cost": rod["buying_cost"],
                "currency":rod["currency"],
                "durability": rod["durability"],
                "level_requirement": str(rod["level_requirement"])
            }

            rods.append(rod_record)

            for capability in rod["rod_useful_for"]:
                rod_capability.append({
                    "rod_id": rod_id,
                    "capability": capability
                })
       
        return rods, rod_capability

    
    def generate_baits(self, bait_data):
        baits = []
        bait_capability = []

        for bait in bait_data:
            bait_id = self.generate_bait_id()

            bait_record = {
                "bait_id": bait_id,
                "bait_name": bait["bait_name"],
                "bait_description": bait["bait_description"],
                "buying_cost": bait["buying_cost"],
                "currency": bait["currency"],
                "quantity": bait["quantity"],
                "level_requirement":str(bait["level_requirement"])
            }

            baits.append(bait_record)

            for capability in bait["bait_useful_for"]:
                bait_capability.append({
                    "bait_id": bait_id,
                    "capability": capability
                })

        return baits, bait_capability
    