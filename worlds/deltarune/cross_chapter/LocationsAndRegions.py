from enum import StrEnum
from typing import TYPE_CHECKING
from ..Regions import generic_create_regions
from ..chapter_1.LocationsAndRegions import Ch1Regions

if TYPE_CHECKING: from .. import DeltaruneWorld

class CrossChapterLocations(StrEnum):
  fuse = "fuse"

cross_chapter_locations: dict = {
  
}

cross_chapter_conditional_locations: dict = {
  
}


class CCRegions(StrEnum):
  menu      = "Menu"
  hub       = "Hub"
  new_game  = "New Game"
  
class CCEntrances(StrEnum):
  chapter1_entrance = "Chapter 1 Entrance"
  
cross_chapter_regions = [
  (CCRegions.menu.value, [CCRegions.new_game.value]),
  (CCRegions.hub.value, [
                              CCEntrances.chapter1_entrance,
                              # Ch2Regions.Ch2Entrances.chapter2_entrance,
                              # Ch3Regions.Ch3Entrances.chapter3_entrance,
                              # Ch4Regions.Ch4Entrances.chapter4_entrance,
                              # Ch5Regions.Ch5Entrances.chapter5_entrance,
                              # Ch6Regions.Ch6Entrances.chapter6_entrance,
                              # Ch7Regions.Ch7Entrances.chapter7_entrance,
                            ])
]

cross_chapter_mandatory_connections = [
  (CCRegions.new_game.value, CCRegions.hub.value),
  (CCEntrances.chapter1_entrance.value, Ch1Regions.chapter_1.value)
]

def create_regions(world: "DeltaruneWorld"):
  generic_create_regions(world,
                         cross_chapter_regions,
                         cross_chapter_locations,
                         cross_chapter_conditional_locations)