from typing import TYPE_CHECKING

from ..chapter_1.LocationsAndRegions import Ch1Locations

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
            
        #   if current_chapter == 1: world.multiworld.get_location(Ch1Locations)

