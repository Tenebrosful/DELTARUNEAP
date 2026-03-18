from enum import StrEnum
from typing import TYPE_CHECKING
from ..Locations import ConditionalLocationData, LocationIDs
from ..Regions import generic_create_regions, fusion_access_region, fusion_access_entrance
from ..chapter_1.LocationsAndRegions import Ch1Regions
from ..chapter_2.LocationsAndRegions import Ch2Regions
from ..chapter_3.LocationsAndRegions import Ch3Regions

if TYPE_CHECKING: from .. import DeltaruneWorld

class CCLocations(StrEnum):
  castle_town_twin_ribbon_fusion  = "Castle Town - Twin Ribbon Fusion"
  castle_town_tensionbow_fusion   = "Castle Town - TensionBow Fusion"
  castle_town_ddburger_fusion     = "Castle Town - DD-Burger Fusion"
  castle_town_silver_card_fusion  = "Castle Town - Silver Card Fusion"
  castle_town_spike_band_fusion   = "Castle Town - Spike Band Fusion"

class CCRegions(StrEnum):
  menu      = "Menu"
  hub       = "Hub"
  new_game  = "New Game"

class CCEntrances(StrEnum):
  chapter_1_entrance = "Chapter 1 Entrance"
  chapter_2_entrance = "Chapter 2 Entrance"
  chapter_3_entrance = "Chapter 3 Entrance"

cross_chapter_locations: dict = {
  
}

cross_chapter_conditional_locations: dict = {
  CCLocations.castle_town_ddburger_fusion.value:      ConditionalLocationData(LocationIDs.cc_castle_town_dd_burger_fusion.value,    fusion_access_region, lambda world: world.can_access_fusion()),
  CCLocations.castle_town_silver_card_fusion.value:   ConditionalLocationData(LocationIDs.cc_castle_town_silver_card_fusion.value,  fusion_access_region, lambda world: world.can_access_fusion()),
  # Require Pink Ribbon that can be found in chapter 2 and 3 and White Ribbon that can be found in chapter 1 and 3 and starting armor for chapter 2
  CCLocations.castle_town_twin_ribbon_fusion.value:   ConditionalLocationData(LocationIDs.cc_castle_town_twin_ribbon_fusion.value,  fusion_access_region, lambda world: world.can_access_fusion() and world.has_at_least_one_chapter_included([2, 3]) and world.has_at_least_one_chapter_included([1, 2, 3])),
  # Require IronShackle that is exclusive to chapter 1 and Glow Wrist to chapter 2 (shop) and chapter 4 (starting armor like chapter 3 but chapter 3 can't fuse)
  CCLocations.castle_town_spike_band_fusion.value:    ConditionalLocationData(LocationIDs.ch2_castle_town_spike_band_fusion.value,  fusion_access_region, lambda world: world.can_access_fusion() and world.include_chapter(1) and world.has_at_least_one_chapter_included([2, 4])),
  # Require B.ShotBowtie that is exclusive to chapter 2 and can't be obtained on weird route
  CCLocations.castle_town_tensionbow_fusion.value:    ConditionalLocationData(LocationIDs.cc_castle_town_tension_bow_fusion.value,  fusion_access_region, lambda world: world.can_access_fusion() and world.include_chapter(2) and not world.is_weird_route()),
}

def get_cross_chapter_regions(world: "DeltaruneWorld"):
  regions = [(CCRegions.menu.value, [CCRegions.new_game.value])]
  
  chapter_entraces = []
  
  if world.include_chapter(1): chapter_entraces.append(CCEntrances.chapter_1_entrance.value)
  if world.include_chapter(2): chapter_entraces.append(CCEntrances.chapter_2_entrance.value)
  if world.include_chapter(3): chapter_entraces.append(CCEntrances.chapter_3_entrance.value)
  
  regions.append((CCRegions.hub.value, chapter_entraces))
  
  if world.can_access_fusion(): regions.append((fusion_access_region, []))
  
  return regions
  

def get_cross_chapter_mandatory_connection(world: "DeltaruneWorld"):
  connections = [(CCRegions.new_game.value, CCRegions.hub.value)]
  
  if world.include_chapter(1): connections.append((CCEntrances.chapter_1_entrance.value, Ch1Regions.chapter_1.value))
  if world.include_chapter(2): connections.append((CCEntrances.chapter_2_entrance.value, Ch2Regions.chapter_2.value))
  if world.include_chapter(3): connections.append((CCEntrances.chapter_3_entrance.value, Ch3Regions.chapter_3.value))
  
  if world.can_access_fusion(): connections.append((fusion_access_entrance, fusion_access_region))
  
  return connections

def create_regions(world: "DeltaruneWorld"):
  generic_create_regions(world,
                         get_cross_chapter_regions(world),
                         cross_chapter_locations,
                         cross_chapter_conditional_locations)