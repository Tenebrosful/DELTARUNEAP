from BaseClasses import MultiWorld, Region, Entrance
from typing import TYPE_CHECKING
from .Locations import LocationData, ConditionalLocationData, DeltaruneLocation

if TYPE_CHECKING: from . import DeltaruneWorld

fusion_access_region = "Fusion access"
fusion_access_entrance = "Fusion access Entrance"

def link_deltarune_areas(world: MultiWorld, player: int, connections: list[tuple[str, str]]):
    for (exit, region) in connections:
        world.get_entrance(exit, player).connect(world.get_region(region, player))

def DeltaruneRegion(world: "DeltaruneWorld", region_name: str, exits: list[str], locations: dict[str, LocationData | ConditionalLocationData]) -> Region:
    region = Region(region_name, world.player, world.multiworld)
    
    for location_name, location_data in locations.items():
        region.locations += [DeltaruneLocation(world.player, location_name, location_data.id, region)]
            
    for exit in exits:
        region.exits += [Entrance(world.player, exit, region)]
        
    return region

def generic_create_regions(world: "DeltaruneWorld", regions: list, locations: dict[str, LocationData], conditional_locations: dict[str, ConditionalLocationData]):
    for (region_name, exits) in regions:       
        locations_in_region: dict[str, LocationData | ConditionalLocationData] = {}
        
        locations_in_region.update([location for location in locations.items() 
                                if location[1].region == region_name])
        
        locations_in_region.update([location for location in conditional_locations.items()
                                if location[1].region == region_name and location[1].should_be_included(world)])
        
        world.multiworld.regions += [DeltaruneRegion(world, region_name, exits, locations_in_region)]