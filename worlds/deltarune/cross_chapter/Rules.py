from typing import TYPE_CHECKING

from ..chapter_1.Items import Ch1Items
from ..chapter_1.LocationsAndRegions import Ch1Locations
from ..chapter_2.Items import Ch2Items
from ..chapter_2.LocationsAndRegions import Ch2Locations
from ..chapter_3.Items import Ch3Items
from ..chapter_3.LocationsAndRegions import Ch3Locations
from ..chapter_4.Items import Ch4Items
from ..chapter_4.LocationsAndRegions import Ch4Locations

if TYPE_CHECKING: from .. import DeltaruneWorld

def set_rules(world: "DeltaruneWorld"):
    player = world.player
    multiworld = world.multiworld
  
    if world.is_chapters_in_order():
        playable_chapters = world.get_playable_chapters()
        
        for current_chapter in playable_chapters:
            next_chapter = world.get_next_in_order_chapter(current_chapter)
            if next_chapter == -1: break
            
            print(get_location(world, current_chapter))
            print(world.create_item(get_unlock_item(world, next_chapter)))
            get_location(world, current_chapter).place_locked_item(world.create_item(get_unlock_item(world, next_chapter)))

def get_location(world: "DeltaruneWorld", chapter: int):
    if chapter == 1: return world.multiworld.get_location(Ch1Locations.fountain_sealed, world.player)
    if chapter == 2: return world.multiworld.get_location(Ch2Locations.fountain_sealed, world.player)
    if chapter == 3: return world.multiworld.get_location(Ch3Locations.fountain_sealed, world.player)
    if chapter == 4: return world.multiworld.get_location(Ch4Locations.third_sanctuary_fountain_sealed, world.player)
    
def get_unlock_item(world: "DeltaruneWorld", chapter: int):
    if chapter == 1: return Ch1Items.chapter_1_unlock
    if chapter == 2: return Ch2Items.chapter_2_unlock
    if chapter == 3: return Ch3Items.chapter_3_unlock
    if chapter == 4: return Ch4Items.chapter_4_unlock