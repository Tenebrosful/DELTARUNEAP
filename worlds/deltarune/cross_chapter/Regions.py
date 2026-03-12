from enum import StrEnum
from .. import DeltaruneWorld
from ..Regions import generic_create_regions

from .Locations import cross_chapter_locations, cross_chapter_conditional_locations

from chapter_1 import Ch1Regions

class CrossChapterRegions(StrEnum):
  menu      = "Menu"
  hud       = "Hud"
  new_game  = "New Game"
  
cross_chapter_regions = [
  (CrossChapterRegions.menu, [CrossChapterRegions.new_game]),
  (CrossChapterRegions.hud, [
                              Ch1Regions.Ch1Entrances.chapter1_entrance,
                              Ch2Regions.Ch2Entrances.chapter2_entrance,
                              Ch3Regions.Ch3Entrances.chapter3_entrance,
                              Ch4Regions.Ch4Entrances.chapter4_entrance,
                              # Ch5Regions.Ch5Entrances.chapter5_entrance,
                              # Ch6Regions.Ch6Entrances.chapter6_entrance,
                              # Ch7Regions.Ch7Entrances.chapter7_entrance,
                            ])
]

cross_chapter_mandatory_connections = [
  (CrossChapterRegions.new_game, CrossChapterRegions.hud)
]

def create_regions(world: DeltaruneWorld):
  generic_create_regions(world,
                         cross_chapter_regions,
                         cross_chapter_locations,
                         cross_chapter_conditional_locations,
                         cross_chapter_mandatory_connections)