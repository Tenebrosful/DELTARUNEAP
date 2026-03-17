from typing import TYPE_CHECKING

from ..chapter_1.Items import Ch1Items
from ..chapter_1.LocationsAndRegions import Ch1Locations
from ..chapter_2.Items import Ch2Items
from ..chapter_2.LocationsAndRegions import Ch2Locations

if TYPE_CHECKING:
    from .. import DeltaruneWorld

def set_rules(world: "DeltaruneWorld"):
    player = world.player
    multiworld = world.multiworld
  
    if world.is_chapters_in_order():
        playable_chapters = world.get_playable_chapters()
      
        for current_chapter in playable_chapters:
            next_chapter = world.get_next_in_order_chapter(current_chapter)
            if next_chapter == -1: break
            
            get_location(world, current_chapter).place_locked_item(world.create_item(get_unlock_item(next_chapter), player))

def get_location(world: "DeltaruneWorld", chapter: int):
    if chapter == 1: return world.multiworld.get_location(Ch1Locations.fountain_sealed, world.player)
    if chapter == 2: return world.multiworld.get_location(Ch2Locations.fountain_sealed, world.player)
    
def get_unlock_item(world: "DeltaruneWorld", chapter: int):
    if chapter == 1: return Ch1Items.chapter_1_unlock
    if chapter == 2: return Ch2Items.chapter_2_unlock