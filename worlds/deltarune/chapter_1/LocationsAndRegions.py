from BaseClasses import Location
from enum import StrEnum
from ..Locations import LocationIDs, LocationData
from ..Regions import generic_create_regions
from typing import TYPE_CHECKING

if TYPE_CHECKING: from . import DeltaruneWorld
  
class Ch1Locations(StrEnum):
  unknown_hidden_item = "CH1: ?????? - Hidden Item"
  
  castle_town_manual = "CH1: Castle Town - Manual"
  throw_away_manual  = "CH1: Throw Away Manual"
  
  field_warp_door                 = "CH1: Field - Warp Door"
  field_dark_candy_tree_1         = "CH1: Field - Dark Candy Tree 1"
  field_dark_candy_tree_2         = "CH1: Field - Dark Candy Tree 2"
  field_dark_candy_tree_3         = "CH1: Field - Dark Candy Tree 3"
  field_dark_candy_tree_4         = "CH1: Field - Dark Candy Tree 4"
  field_brokencake                = "CH1: Field - BrokenCake"
  field_return_top_cake           = "CH1: Field - Return Top Cake"
  field_maze_of_death_chest       = "CH1: Field - Maze of Death Chest"
  field_chest_before_great_board  = "CH1: Field - Chest Before Great Board"
  
  seam_seap_talk_about_strange_prisoner = "CH1: Seam's Seap - Talk About Strange Prisoner"
  seam_seap_1                           = "CH1: Seam's Seap 1"
  seam_seap_2                           = "CH1: Seam's Seap 2"
  seam_seap_3                           = "CH1: Seam's Seap 3"
  seam_seap_4                           = "CH1: Seam's Seap 4"
  
  forest_warp_door                  = "CH1: Forest - Warp Door"
  forest_scissor_dancers_chest      = "CH1: Forest - Scissor Dancers Chest"
  forest_hidden_chest_near_dancers  = "CH1: Forest - Hidden Chest Near Dancers"
  forest_coat_rack_chest            = "CH1: Forest - Coat Rack's Chest"
  forest_letter_block_chest         = "CH1: Forest - Letter Block Chest"
  forest_chest_near_worm            = "CH1: Forest - Chest Near Worm"
  forest_man                        = "CH1: Forest - Man"
  
  bake_sale_warp_door       = "CH1: Bake Sale - Warp Door"
  bake_sale_repair_top_cake = "CH1: Bake Sale - Repair Top Cake"
  bake_sale_repair_door_key = "CH1: Bake Sale - Repair Door Key"
  bake_sale_diamond_stand   = "CH1: Bake Sale - Diamond Stand"
  bake_sale_heart_stand     = "CH1: Bake Sale - Heart Stand"
  bake_sale_spade_stand     = "CH1: Bake Sale - Spade Stand"
  
  card_castle_warp_door     = "CH1: Card Castle - Warp Door"
  card_castle_ironshackle   = "CH1: Card Castle - IronShackle"
  card_castle_moss          = "CH1: Card Castle - Moss"
  card_castle_rudinn_gift   = "CH1: Card Castle - Rudinn Gift"
  card_castle_2f_chest      = "CH1: Card Castle - 2F Chest"
  card_castle_4f_chest      = "CH1: Card Castle - 4F Chest"
  card_castle_jevil_1       = "CH1: Card Castle - Jevil Defeat Item #1"
  card_castle_jevil_2       = "CH1: Card Castle - Jevil Defeat Item #2"
  card_castle_jevil_3       = "CH1: Card Castle - Jevil Defeat Item #3"
  
  fountain_sealed = "CH1: Card Kingdom - Fountain Sealed"
  
class Ch1Regions(StrEnum):  
  chapter_1       = "Chapter 1"
  light_world     = "CH1: Light World"
  castle_town     = "CH1: Castle Town"
  fields          = "CH1: Fields"
  forest          = "CH1: Forest"
  bake_sale       = "CH1: Bake Sale"
  card_castle     = "CH1: Card Castle"
  warp_hub        = "CH1: Warp Hub"
  
class Ch1Entrances(StrEnum):
  castle_town_entrance    = "CH1: Castle Town Entrance"
  fields_entrance         = "CH1: Fields Entrance"
  forest_entrance         = "CH1: Forest Entrance"
  bake_sale_entrance      = "CH1: Bake Sale Entrance"
  card_castle_entrance    = "CH1: Card Castle Entrance"
  light_world_entrance    = "CH1: Light World Entrance"
  
  # Warps
  fields_warp             = "CH1: Fields Warp"
  forest_warp             = "CH1: Forest Warp"
  bake_sale_warp          = "CH1: Bake Sale Warp"
  card_castle_warp        = "CH1: Card Castle Warp"
  
  # Warp Hubs
  fields_warp_hub         = "CH1: Fields Warp Hub"
  forest_warp_hub         = "CH1: Forest Warp Hub"
  bake_sale_warp_hub      = "CH1: Bake Sale Warp Hub"
  card_castle_warp_hub    = "CH1: Card Castle Warp Hub"
  
chapter1_locations = {
  Ch1Locations.unknown_hidden_item:                   LocationData(LocationIDs.ch1_unknown_hidden_item.value,                    Ch1Regions.castle_town),
  
  Ch1Locations.castle_town_manual:                    LocationData(LocationIDs.ch1_castle_town_manual.value,                     Ch1Regions.castle_town),
  Ch1Locations.throw_away_manual:                     LocationData(LocationIDs.ch1_throw_away_manual.value,                      Ch1Regions.castle_town),
  
  Ch1Locations.field_dark_candy_tree_1:               LocationData(LocationIDs.ch1_field_dark_candy_tree_1.value,                Ch1Regions.fields),
  Ch1Locations.field_dark_candy_tree_2:               LocationData(LocationIDs.ch1_field_dark_candy_tree_2.value,                Ch1Regions.fields),
  Ch1Locations.field_dark_candy_tree_3:               LocationData(LocationIDs.ch1_field_dark_candy_tree_3.value,                Ch1Regions.fields),
  Ch1Locations.field_dark_candy_tree_4:               LocationData(LocationIDs.ch1_field_dark_candy_tree_4.value,                Ch1Regions.fields),
  Ch1Locations.field_brokencake:                      LocationData(LocationIDs.ch1_field_brokencake.value,                       Ch1Regions.fields),
  Ch1Locations.field_return_top_cake:                 LocationData(LocationIDs.ch1_field_return_top_cake.value,                  Ch1Regions.fields),
  Ch1Locations.field_maze_of_death_chest:             LocationData(LocationIDs.ch1_field_maze_of_death_chest.value,              Ch1Regions.fields),
  Ch1Locations.field_chest_before_great_board:        LocationData(LocationIDs.ch1_field_chest_before_great_board.value,         Ch1Regions.fields),
  
  Ch1Locations.seam_seap_talk_about_strange_prisoner: LocationData(LocationIDs.ch1_seam_seap_talk_about_strange_prisoner.value,  Ch1Regions.fields),
  Ch1Locations.seam_seap_1:                           LocationData(LocationIDs.ch1_seam_seap_1.value,                            Ch1Regions.fields),
  Ch1Locations.seam_seap_2:                           LocationData(LocationIDs.ch1_seam_seap_2.value,                            Ch1Regions.fields),
  Ch1Locations.seam_seap_3:                           LocationData(LocationIDs.ch1_seam_seap_3.value,                            Ch1Regions.fields),
  Ch1Locations.seam_seap_4:                           LocationData(LocationIDs.ch1_seam_seap_4.value,                            Ch1Regions.fields),
  
  Ch1Locations.forest_warp_door:                      LocationData(LocationIDs.ch1_forest_warp_door.value,                       Ch1Regions.forest),
  Ch1Locations.forest_coat_rack_chest:                LocationData(LocationIDs.ch1_forest_coat_rack_chest.value,                 Ch1Regions.forest),
  Ch1Locations.forest_letter_block_chest:             LocationData(LocationIDs.ch1_forest_letter_block_chest.value,              Ch1Regions.forest),
  
  Ch1Locations.bake_sale_warp_door:                   LocationData(LocationIDs.ch1_bake_sale_warp_door.value,                    Ch1Regions.bake_sale),
  Ch1Locations.bake_sale_repair_door_key:             LocationData(LocationIDs.ch1_bake_repair_door_key.value,                   Ch1Regions.bake_sale),
  Ch1Locations.bake_sale_repair_top_cake:             LocationData(LocationIDs.ch1_bake_repair_top_cake.value,                   Ch1Regions.bake_sale),
  Ch1Locations.bake_sale_diamond_stand:               LocationData(LocationIDs.ch1_bake_diamond_stand.value,                     Ch1Regions.bake_sale),
  Ch1Locations.bake_sale_heart_stand:                 LocationData(LocationIDs.ch1_bake_heart_stand.value,                       Ch1Regions.bake_sale),
  Ch1Locations.bake_sale_spade_stand:                 LocationData(LocationIDs.ch1_bake_spade_stand.value,                       Ch1Regions.bake_sale),
  Ch1Locations.forest_scissor_dancers_chest:          LocationData(LocationIDs.ch1_forest_scissor_dancers_chest.value,           Ch1Regions.bake_sale),
  Ch1Locations.forest_hidden_chest_near_dancers:      LocationData(LocationIDs.ch1_forest_hidden_chest_near_dancers.value,       Ch1Regions.bake_sale),
  Ch1Locations.forest_chest_near_worm:                LocationData(LocationIDs.ch1_forest_chest_near_worm.value,                 Ch1Regions.bake_sale),
  Ch1Locations.forest_man:                            LocationData(LocationIDs.ch1_forest_man.value,                             Ch1Regions.bake_sale),
  
  Ch1Locations.card_castle_warp_door:                 LocationData(LocationIDs.ch1_card_castle_warp_door.value,                  Ch1Regions.card_castle),
  Ch1Locations.card_castle_ironshackle:               LocationData(LocationIDs.ch1_card_castle_ironshackle.value,                Ch1Regions.card_castle),
  Ch1Locations.card_castle_moss:                      LocationData(LocationIDs.ch1_card_castle_moss.value,                       Ch1Regions.card_castle),
  Ch1Locations.card_castle_rudinn_gift:               LocationData(LocationIDs.ch1_card_castle_rudinn_gift.value,                Ch1Regions.card_castle),
  Ch1Locations.card_castle_2f_chest:                  LocationData(LocationIDs.ch1_card_castle_2f_chest.value,                   Ch1Regions.card_castle),
  Ch1Locations.card_castle_4f_chest:                  LocationData(LocationIDs.ch1_card_castle_4f_chest.value,                   Ch1Regions.card_castle),
  Ch1Locations.card_castle_jevil_1:                   LocationData(LocationIDs.ch1_card_castle_jevil_1.value,                    Ch1Regions.card_castle),
  Ch1Locations.card_castle_jevil_2:                   LocationData(LocationIDs.ch1_card_castle_jevil_2.value,                    Ch1Regions.card_castle),
  Ch1Locations.card_castle_jevil_3:                   LocationData(LocationIDs.ch1_card_castle_jevil_3.value,                    Ch1Regions.card_castle),
  
  Ch1Locations.fountain_sealed:                       LocationData(LocationIDs.ch1_fountain_sealed.value,                        Ch1Regions.light_world),
}

chapter1_conditional_locations: dict = {
  
}

chapter1_end_region = Ch1Regions.light_world
  
chapter1_regions = [
  (Ch1Regions.chapter_1,       [Ch1Entrances.castle_town_entrance]),
  (Ch1Regions.castle_town,     [Ch1Entrances.fields_entrance]),
  (Ch1Regions.fields,          [Ch1Entrances.forest_entrance, Ch1Entrances.fields_warp]),
  (Ch1Regions.forest,          [Ch1Entrances.bake_sale_entrance, Ch1Entrances.forest_warp]),
  (Ch1Regions.bake_sale,       [Ch1Entrances.card_castle_entrance, Ch1Entrances.bake_sale_warp]),
  (Ch1Regions.card_castle,     [Ch1Entrances.light_world_entrance, Ch1Entrances.card_castle_warp]),
  (Ch1Regions.warp_hub,        [Ch1Entrances.fields_warp_hub, Ch1Entrances.forest_warp_hub, Ch1Entrances.bake_sale_warp_hub, Ch1Entrances.card_castle_warp_hub]),
  (Ch1Regions.light_world,     []),
]

chapter1_mandatory_connections = [
  (Ch1Entrances.castle_town_entrance, Ch1Regions.castle_town),
  (Ch1Entrances.fields_entrance,      Ch1Regions.fields),
  (Ch1Entrances.forest_entrance,      Ch1Regions.forest),
  (Ch1Entrances.bake_sale_entrance,   Ch1Regions.bake_sale),
  (Ch1Entrances.card_castle_entrance, Ch1Regions.card_castle),
  (Ch1Entrances.light_world_entrance, Ch1Regions.light_world),
  (Ch1Entrances.fields_warp,          Ch1Regions.warp_hub),
  (Ch1Entrances.forest_warp,          Ch1Regions.warp_hub),
  (Ch1Entrances.bake_sale_warp,       Ch1Regions.warp_hub),
  (Ch1Entrances.card_castle_warp,     Ch1Regions.warp_hub),
]

def create_regions(world: "DeltaruneWorld"):
  generic_create_regions(world, chapter1_regions, chapter1_locations, chapter1_conditional_locations)