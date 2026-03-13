from BaseClasses import MultiWorld, Region, Entrance
from typing import TYPE_CHECKING
from .Locations import LocationData, ConditionalLocationData, DeltaruneLocation

if TYPE_CHECKING:
    from . import DeltaruneWorld


def link_deltarune_areas(world: MultiWorld, player: int, connections: list[tuple[str, str]]):
    for (exit, region) in connections:
        print(f"Connecting {region} to {exit}")
        world.get_entrance(exit, player).connect(world.get_region(region, player))

def DeltaruneRegion(world: "DeltaruneWorld", region_name: str, exits: list[str], locations: dict[str, LocationData | ConditionalLocationData]) -> Region:
    region = Region(region_name, world.player, world.multiworld)
    
    for location_name, location_data in locations.items():
        region.locations += [DeltaruneLocation(world.player, location_name, location_data.id, region)]
            
    for exit in exits:
        region.exits += [Entrance(world.player, exit, region)]
        
    print(region)
        
    return region

def generic_create_regions(world: "DeltaruneWorld", regions: list, locations: dict[str, LocationData], conditional_locations: dict[str, ConditionalLocationData]):
    locations_in_region: dict[str, LocationData | ConditionalLocationData] = {}
    
    for (region_name, exits) in regions:       
        locations_in_region.update([location for location in locations.items() 
                                if location[1].region == region_name])
        
        locations_in_region.update([location for location in conditional_locations.items()
                                if location[1].region == region_name and location[1].should_be_included(world)])
        
        world.multiworld.regions += [DeltaruneRegion(world, region_name, exits, locations_in_region)]

# (Region name, list of exits)
deltarune_regions = [
    ("Menu", ["New Game"]),
    ("Hub", ["Chapter 1 Entrance", "Chapter 2 Entrance", "Chapter 3 Entrance", "Chapter 4 Entrance"]),
    ("Chapter 1", ["CH1: Castle Town Entrance"]),
    ("CH1: Castle Town", ["CH1: Fields Entrance"]),
    ("CH1: Fields", ["CH1: Forest Entrance", "CH1: Fields Warp"]),
    ("CH1: Forest", ["CH1: Bake Sale Entrance", "CH1: Forest Warp"]),
    ("CH1: Bake Sale", ["CH1: Card Castle Entrance", "CH1: Bake Sale Warp"]),
    ("CH1: Card Castle", ["CH1: Castle Warp", "CH1: Light World Entrance"]),
    ("CH1: Warp Hub", ["CH1: Fields Warp Hub", "CH1: Forest Warp Hub", "CH1: Bake Sale Warp Hub", "CH1: Castle Warp Hub"]),
    ("CH1: Light World", []),
    ("Chapter 2", ["CH2: Castle Town Entrance"]),
    ("CH2: Castle Town", ["CH2: Cyber Field Entrance"]),
    ("CH2: Cyber Field", ["CH2: Cyber City Entrance"]),
    ("CH2: Cyber City", ["CH2: Mansion Entrance"]),
    ("CH2: Mansion", ["CH2: Post-Chapter Castle Town Entrance"]),
    ("CH2: Post-Chapter Castle Town", []),
    ("Chapter 3", ["CH3: Couch Cliffs Entrance"]),
    ("CH3: Couch Cliffs", ["CH3: Board 1 Entrance"]),
    ("CH3: Board 1", ["CH3: Green Room Entrance"]),
    ("CH3: Green Room", ["CH3: Board 2 Entrance"]),
    ("CH3: Board 2", ["CH3: TV World Entrance"]),
    ("CH3: TV World", ["CH3: Goulden Sam Entrance"]),
    ("CH3: Goulden Sam", ["CH3: Cold Place Entrance"]),
    ("CH3: Cold Place", []),
    # ("CH3: Warp Hub", ["CH3: TV World Entrance Warp Hub","CH3: Goulden Sam Warp Hub"]),
    ("Chapter 4", ["CH4: Castle Town Entrance"]),
    ("CH4: Castle Town", ["CH4: Dark Sanctuary Entrance"]),
    ("CH4: Dark Sanctuary", ["CH4: Dark Sanctuary (Claimb Required) Entrance"]),
    ("CH4: Dark Sanctuary (Claimb Required)", ["CH4: Second Sanctuary Entrance"]),
    ("CH4: Second Sanctuary", ["CH4: Third Sanctuary Entrance"]),
    ("CH4: Third Sanctuary", ["CH4: Titan Fight Entrance"]),
    ("CH4: Titan Fight", ["CH4: Light World Entrance"]),
    ("CH4: Light World", []),
]

# (Entrance, region pointed to)
mandatory_connections = [
    ("New Game", "Hub"),
    ("Chapter 1 Entrance", "Chapter 1"),
    ("Chapter 2 Entrance", "Chapter 2"),
    ("Chapter 3 Entrance", "Chapter 3"),
    ("Chapter 4 Entrance", "Chapter 4"),
    ("CH1: Castle Town Entrance", "CH1: Castle Town"),
    ("CH1: Fields Entrance", "CH1: Fields"),
    ("CH1: Forest Entrance", "CH1: Forest"),
    ("CH1: Bake Sale Entrance", "CH1: Bake Sale"),
    ("CH1: Card Castle Entrance", "CH1: Card Castle"),
    ("CH1: Light World Entrance", "CH1: Light World"),
    ("CH1: Castle Warp", "CH1: Warp Hub"),
    ("CH1: Fields Warp", "CH1: Warp Hub"),
    ("CH1: Forest Warp", "CH1: Warp Hub"),
    ("CH1: Bake Sale Warp", "CH1: Warp Hub"),
    ("CH1: Castle Warp Hub", "CH1: Card Castle"),
    ("CH1: Fields Warp Hub", "CH1: Fields"),
    ("CH1: Forest Warp Hub", "CH1: Fields"),
    ("CH1: Bake Sale Warp Hub", "CH1: Bake Sale"),
    ("CH2: Castle Town Entrance", "CH2: Castle Town"),
    ("CH2: Cyber Field Entrance", "CH2: Cyber Field"),
    ("CH2: Cyber City Entrance", "CH2: Cyber City"),
    ("CH2: Mansion Entrance", "CH2: Mansion"),
    ("CH2: Post-Chapter Castle Town Entrance", "CH2: Post-Chapter Castle Town"),
    ("CH3: Couch Cliffs Entrance", "CH3: Couch Cliffs"),
    ("CH3: Board 1 Entrance", "CH3: Board 1"),
    ("CH3: Green Room Entrance", "CH3: Green Room"),
    ("CH3: Board 2 Entrance", "CH3: Board 2"),
    ("CH3: TV World Entrance", "CH3: TV World"),
    ("CH3: Goulden Sam Entrance", "CH3: Goulden Sam"),
    ("CH3: Cold Place Entrance", "CH3: Cold Place"),
    #("CH3: TV World Entrance Warp", "CH3: Warp Hub"),
    #("CH3: Goulden Sam Warp", "CH3: Warp Hub"),
    #("CH3: TV World Entrance Warp Hub", "CH3: TV World"),
    # ("CH3: Goulden Sam Warp Hub", "CH3: Goulden Sam"),
    ("CH4: Castle Town Entrance", "CH4: Castle Town"),
    ("CH4: Dark Sanctuary (Claimb Required) Entrance", "CH4: Dark Sanctuary (Claimb Required)"),
    ("CH4: Dark Sanctuary Entrance", "CH4: Dark Sanctuary"),
    ("CH4: Second Sanctuary Entrance", "CH4: Second Sanctuary"),
    ("CH4: Third Sanctuary Entrance", "CH4: Third Sanctuary"),
    ("CH4: Titan Fight Entrance", "CH4: Titan Fight"),
    ("CH4: Light World Entrance", "CH4: Light World"),
]