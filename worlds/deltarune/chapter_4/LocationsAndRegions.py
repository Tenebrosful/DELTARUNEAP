from BaseClasses import Location
from enum import StrEnum
from ..Locations import LocationIDs, LocationData, ConditionalLocationData, LocationGroups
from ..Regions import generic_create_regions, fusion_access_region
from typing import TYPE_CHECKING

if TYPE_CHECKING: from .. import DeltaruneWorld

class Ch4Locations(StrEnum):
  castle_town_lanino_elnina_challenge   = "CH4: Castle Town - Lanino&Elnina Challenge"
  castle_town_top_chef_gift             = "CH4: Castle Town - Top Chef Gift"
  castle_town_mike                      = "CH4: Castle Town - Mike"
  
  dark_sanctuary_jockington_prophecy_chest          = "CH4: Dark Sanctuary - Jockington Prophecy Chest"
  dark_sanctuary_chest_in_first_dark_area           = "CH4: Dark Sanctuary - Chest in First Dark Area"
  dark_sanctuary_worship_room_chest                 = "CH4: Dark Sanctuary - Worship Room Chest"
  dark_sanctuary_library_chest_1                    = "CH4: Dark Sanctuary - Library Chest 1"
  dark_sanctuary_lantern_puzzle_chest               = "CH4: Dark Sanctuary - Lantern Puzzle Chest"
  dark_sanctuary_library_chest_2                    = "CH4: Dark Sanctuary - Library Chest 2"
  dark_sanctuary_jackenstein_gift                   = "CH4: Dark Sanctuary - Jackenstein Gift"
  dark_sanctuary_climbing_tutorial_chest            = "CH4: Dark Sanctuary - Climbing Tutorial Chest"
  dark_sanctuary_cuptain_pillar_chest               = "CH4: Dark Sanctuary - Cuptain Pillar Chest"
  dark_sanctuary_sleeping_mizzle_chest              = "CH4: Dark Sanctuary - Sleeping Mizzle Chest"
  dark_sanctuary_hidden_climbing_chest              = "CH4: Dark Sanctuary - Hidden Climbing Chest"
  dark_sanctuary_sheetmusic                         = "CH4: Dark Sanctuary - SheetMusic"
  dark_sanctuary_hammer_of_justice_defeat_item_1    = "CH4: Dark Sanctuary - Hammer of Justice Defeat Item #1"
  dark_sanctuary_hammer_of_justice_defeat_item_2    = "CH4: Dark Sanctuary - Hammer of Justice Defeat Item #2"
  dark_sanctuary_fountain_sealed                    = "CH4: Dark Sanctuary - Fountain Sealed"
  dark_sanctuary_annoying_dog                       = "CH4: Dark Sanctuary - Annoying Dog...?"
  
  second_sanctuary_wall_climbing_chest              = "CH4: Second Sanctuary - Wall Climbing Chest"
  second_sanctuary_waterfall_chest                  = "CH4: Second Sanctuary - Waterfall Chest"
  second_sanctuary_destroyed_piano_block_chest      = "CH4: Second Sanctuary - Destroyed Piano Block Chest"
  second_sanctuary_man                              = "CH4: Second Sanctuary - Man"
  second_sanctuary_gallery_prophecy_chest           = "CH4: Second Sanctuary - Gallery Prophecy Chest"
  second_sanctuary_moss                             = "CH4: Second Sanctuary - Moss"
  second_sanctuary_fountain_sealed                  = "CH4: Second Sanctuary - Fountain Sealed"
  
  third_sanctuary_speed_climbing_chest              = "CH4: Third Sanctuary - Speed Climbing Chest"
  third_sanctuary_dark_area_chest                   = "CH4: Third Sanctuary - Dark Area Chest"
  third_sanctuary_titan_defeat                      = "CH4: Third Sanctuary - Titan Defeat"
  third_sanctuary_fountain_sealed                   = "CH4: Third Sanctuary - Fountain Sealed"
  
  old_man_shop_1 = "CH4: Old Man's Shop 1"
  old_man_shop_2 = "CH4: Old Man's Shop 2"
  old_man_shop_3 = "CH4: Old Man's Shop 3"
  old_man_shop_4 = "CH4: Old Man's Shop 4"
  
  # Recruits
  recruit_guei          = "CH4: Recruit Guei"
  recruit_balthizard    = "CH4: Recruit Balthizard"
  recruit_bibliox       = "CH4: Recruit Bibliox"
  recruit_mizzle        = "CH4: Recruit Mizzle"
  recruit_miss_mizzle   = "CH4: Recruit Miss Mizzle"
  recruit_wicabel       = "CH4: Recruit Wicabel"
  recruit_wingblade     = "CH4: Recruit Wingblade"
  recruit_organikk      = "CH4: Recruit Organikk"
  
  # Lost
  lost_guei             = "CH4: Lost Guei"
  lost_balthizard       = "CH4: Lost Balthizard"
  lost_bibliox          = "CH4: Lost Bibliox"
  lost_mizzle           = "CH4: Lost Mizzle"
  lost_miss_mizzle      = "CH4: Lost Miss Mizzle"
  lost_wicabel          = "CH4: Lost Wicabel"
  lost_wingblade        = "CH4: Lost Wingblade"
  lost_organikk         = "CH4: Lost Organikk"

class Ch4Regions(StrEnum):
  chapter_4                   = "Chapter 4"
  castle_town                 = "CH4: Castle Town"
  dark_sanctuary              = "CH4: Dark Sanctuary"
  dark_sanctuary_claimbclaws  = "CH4: Dark Sanctuary (ClaimbClaws Required)"
  second_sanctuary            = "CH4: Second Sanctuary"
  third_sanctuary             = "CH4: Third Sanctuary"
  titan_fight                 = "CH4: Titan Fight"
  light_world                 = "CH4: Light World"

class Ch4Entrances(StrEnum):
  castle_town_entrance                = "CH4: Castle Town Entrance"
  fusion_access_entrance              = "CH4: Fusion access Entrance"
  dark_sanctuary_entrance             = "CH4: Dark Sanctuary Entrance"
  dark_sanctuary_claimbclaws_entrance = "CH4: Dark Sanctuary (ClaimbClaws Required) Entrance"
  second_sanctuary_entrance           = "CH4: Second Sanctuary Entrance"
  third_sanctuary_entrance            = "CH4: Third Sanctuary Entrance"
  titan_fight_entrance                = "CH4: Titan Fight Entrance"
  light_world_entrance                = "CH4: Light World Entrance"

chapter4_end_region = Ch4Regions.light_world.value

chapter4_locations = {
  Ch4Locations.castle_town_lanino_elnina_challenge.value: LocationData(LocationIDs.ch4_castle_town_lanino_elnina_challenge.value, Ch4Regions.castle_town, LocationGroups.chapter4.value),
  Ch4Locations.castle_town_top_chef_gift.value:           LocationData(LocationIDs.ch4_castle_town_top_chef_gift.value,           Ch4Regions.castle_town, LocationGroups.chapter4.value),
  # Ch4Locations.castle_town_mike.value:                    LocationData(LocationIDs.ch4_castle_town_mike.value,                    Ch4Regions.castle_town, LocationGroups.chapter4.value),
  
  Ch4Locations.dark_sanctuary_jockington_prophecy_chest.value:  LocationData(LocationIDs.ch4_dark_sanctuary_jockington_prophecy_chest.value,  Ch4Regions.dark_sanctuary, LocationGroups.chapter4.value),
  Ch4Locations.dark_sanctuary_chest_in_first_dark_area.value:   LocationData(LocationIDs.ch4_dark_sanctuary_chest_in_first_dark_area.value,   Ch4Regions.dark_sanctuary, LocationGroups.chapter4.value),
  Ch4Locations.dark_sanctuary_library_chest_1.value:            LocationData(LocationIDs.ch4_dark_sanctuary_library_chest_1.value,            Ch4Regions.dark_sanctuary, LocationGroups.chapter4.value),
  Ch4Locations.dark_sanctuary_worship_room_chest.value:         LocationData(LocationIDs.ch4_dark_sanctuary_worship_room_chest.value,         Ch4Regions.dark_sanctuary, LocationGroups.chapter4.value),
  Ch4Locations.dark_sanctuary_lantern_puzzle_chest.value:       LocationData(LocationIDs.ch4_dark_sanctuary_lantern_puzzle_chest.value,       Ch4Regions.dark_sanctuary, LocationGroups.chapter4.value),
  Ch4Locations.dark_sanctuary_library_chest_2.value:            LocationData(LocationIDs.ch4_dark_sanctuary_library_chest_2.value,            Ch4Regions.dark_sanctuary, LocationGroups.chapter4.value),
  
  Ch4Locations.old_man_shop_1.value:                            LocationData(LocationIDs.ch4_old_man_shop_1.value,                            Ch4Regions.dark_sanctuary, LocationGroups.chapter4.value),
  Ch4Locations.old_man_shop_2.value:                            LocationData(LocationIDs.ch4_old_man_shop_2.value,                            Ch4Regions.dark_sanctuary, LocationGroups.chapter4.value),
  Ch4Locations.old_man_shop_3.value:                            LocationData(LocationIDs.ch4_old_man_shop_3.value,                            Ch4Regions.dark_sanctuary, LocationGroups.chapter4.value),
  Ch4Locations.old_man_shop_4.value:                            LocationData(LocationIDs.ch4_old_man_shop_4.value,                            Ch4Regions.dark_sanctuary, LocationGroups.chapter4.value),
  
  Ch4Locations.dark_sanctuary_jackenstein_gift.value:           LocationData(LocationIDs.ch4_dark_sanctuary_jackenstein_gift.value,           Ch4Regions.dark_sanctuary_claimbclaws, LocationGroups.chapter4.value),
  Ch4Locations.dark_sanctuary_climbing_tutorial_chest.value:    LocationData(LocationIDs.ch4_dark_santuary_climbing_tutorial_chest.value,     Ch4Regions.dark_sanctuary_claimbclaws, LocationGroups.chapter4.value),
  Ch4Locations.dark_sanctuary_cuptain_pillar_chest.value:       LocationData(LocationIDs.ch4_dark_sanctuary_cuptain_pillar_chest.value,       Ch4Regions.dark_sanctuary_claimbclaws, LocationGroups.chapter4.value),
  Ch4Locations.dark_sanctuary_sleeping_mizzle_chest.value:      LocationData(LocationIDs.ch4_dark_sanctuary_sleeping_mizzle_chest.value,      Ch4Regions.dark_sanctuary_claimbclaws, LocationGroups.chapter4.value),
  Ch4Locations.dark_sanctuary_hidden_climbing_chest.value:      LocationData(LocationIDs.ch4_dark_sanctuary_hidden_climbing_chest.value,      Ch4Regions.dark_sanctuary_claimbclaws, LocationGroups.chapter4.value),
  Ch4Locations.dark_sanctuary_sheetmusic.value:                 LocationData(LocationIDs.ch4_dark_sanctuary_sheetmusic.value,                 Ch4Regions.dark_sanctuary_claimbclaws, LocationGroups.chapter4.value),
  Ch4Locations.dark_sanctuary_hammer_of_justice_defeat_item_1.value:  LocationData(LocationIDs.ch4_dark_sanctuary_hammer_of_justice_defeat_item_1.value,  Ch4Regions.dark_sanctuary_claimbclaws, LocationGroups.chapter4.value),
  Ch4Locations.dark_sanctuary_hammer_of_justice_defeat_item_2.value:  LocationData(LocationIDs.ch4_dark_sanctuary_hammer_of_justice_defeat_item_2.value,  Ch4Regions.dark_sanctuary_claimbclaws, LocationGroups.chapter4.value),
  
  Ch4Locations.dark_sanctuary_fountain_sealed.value:                  LocationData(LocationIDs.ch4_dark_sanctuary_fountain_seal.value,                     Ch4Regions.second_sanctuary, LocationGroups.chapter4.value),
  Ch4Locations.second_sanctuary_waterfall_chest.value:                LocationData(LocationIDs.ch4_second_sanctuary_waterfall_chest.value,                Ch4Regions.second_sanctuary, LocationGroups.chapter4.value),
  Ch4Locations.second_sanctuary_man.value:                            LocationData(LocationIDs.ch4_second_sanctuary_man.value,                            Ch4Regions.second_sanctuary, LocationGroups.chapter4.value),
  Ch4Locations.second_sanctuary_moss.value:                           LocationData(LocationIDs.ch4_second_sanctuary_moss.value,                           Ch4Regions.second_sanctuary, LocationGroups.chapter4.value),
  Ch4Locations.second_sanctuary_gallery_prophecy_chest.value:         LocationData(LocationIDs.ch4_second_sanctuary_gallery_prohecy_chest.value,          Ch4Regions.second_sanctuary, LocationGroups.chapter4.value),
  Ch4Locations.second_sanctuary_fountain_sealed.value:                LocationData(LocationIDs.ch4_second_sanctuary_fountain_seal.value,                  Ch4Regions.second_sanctuary, LocationGroups.chapter4.value),
  Ch4Locations.second_sanctuary_destroyed_piano_block_chest.value:    LocationData(LocationIDs.ch4_second_sanctuary_destroyed_piano_block_chest.value,    Ch4Regions.second_sanctuary, LocationGroups.chapter4.value),

  Ch4Locations.dark_sanctuary_annoying_dog.value:                     LocationData(LocationIDs.ch4_dark_sanctuary_annoying_dog.value,                     Ch4Regions.third_sanctuary, LocationGroups.chapter4.value),
  Ch4Locations.third_sanctuary_speed_climbing_chest.value:            LocationData(LocationIDs.ch4_third_sanctuary_speed_climbing_chest.value,            Ch4Regions.third_sanctuary, LocationGroups.chapter4.value),
  Ch4Locations.third_sanctuary_dark_area_chest.value:                 LocationData(LocationIDs.ch4_third_sanctuary_dark_area_chest.value,                 Ch4Regions.third_sanctuary, LocationGroups.chapter4.value),

  Ch4Locations.third_sanctuary_titan_defeat.value:                    LocationData(LocationIDs.ch4_third_sanctuary_titan_defeat.value,                    Ch4Regions.titan_fight, LocationGroups.chapter4.value),
  Ch4Locations.third_sanctuary_fountain_sealed.value:                 LocationData(LocationIDs.ch4_third_sanctuary_fountain_seal.value,                    Ch4Regions.titan_fight, LocationGroups.chapter4.value),
  
  Ch4Locations.second_sanctuary_man.value: LocationData(LocationIDs.ch4_second_sanctuary_man.value, Ch4Regions.second_sanctuary, LocationGroups.chapter4.value),
}

chapter4_conditional_locations = {
  # Recruits
  Ch4Locations.recruit_guei.value:         ConditionalLocationData(LocationIDs.ch4_recruit_guei.value,        Ch4Regions.dark_sanctuary,              lambda world: world.is_all_recruits(), LocationGroups.chapter4.value),
  Ch4Locations.recruit_balthizard.value:   ConditionalLocationData(LocationIDs.ch4_recruit_balthizard.value,  Ch4Regions.dark_sanctuary,              lambda world: world.is_all_recruits(), LocationGroups.chapter4.value),
  Ch4Locations.recruit_bibliox.value:      ConditionalLocationData(LocationIDs.ch4_recruit_bibliox.value,     Ch4Regions.dark_sanctuary,              lambda world: world.is_all_recruits(), LocationGroups.chapter4.value),
  Ch4Locations.recruit_mizzle.value:       ConditionalLocationData(LocationIDs.ch4_recruit_mizzle.value,      Ch4Regions.dark_sanctuary,              lambda world: world.is_all_recruits(), LocationGroups.chapter4.value),
  Ch4Locations.recruit_miss_mizzle.value:  ConditionalLocationData(LocationIDs.ch4_recruit_miss_mizzle.value, Ch4Regions.dark_sanctuary_claimbclaws,  lambda world: world.is_all_recruits(), LocationGroups.chapter4.value),
  Ch4Locations.recruit_wicabel.value:      ConditionalLocationData(LocationIDs.ch4_recruit_wicabel.value,        Ch4Regions.second_sanctuary,            lambda world: world.is_all_recruits(), LocationGroups.chapter4.value),
  Ch4Locations.recruit_wingblade.value:    ConditionalLocationData(LocationIDs.ch4_recruit_winglade.value,        Ch4Regions.second_sanctuary,            lambda world: world.is_all_recruits(), LocationGroups.chapter4.value),
  Ch4Locations.recruit_organikk.value:     ConditionalLocationData(LocationIDs.ch4_recruit_organikk.value,        Ch4Regions.second_sanctuary,            lambda world: world.is_all_recruits(), LocationGroups.chapter4.value),
  
  # Losts
  Ch4Locations.lost_guei.value:         ConditionalLocationData(LocationIDs.ch4_lost_guei.value,        Ch4Regions.dark_sanctuary,              lambda world: world.is_weird_route(), LocationGroups.chapter4.value),
  Ch4Locations.lost_balthizard.value:   ConditionalLocationData(LocationIDs.ch4_lost_balthizard.value,  Ch4Regions.dark_sanctuary,              lambda world: world.is_weird_route(), LocationGroups.chapter4.value),
  Ch4Locations.lost_bibliox.value:      ConditionalLocationData(LocationIDs.ch4_lost_bibliox.value,     Ch4Regions.dark_sanctuary,              lambda world: world.is_weird_route(), LocationGroups.chapter4.value),
  Ch4Locations.lost_mizzle.value:       ConditionalLocationData(LocationIDs.ch4_lost_mizzle.value,      Ch4Regions.dark_sanctuary,              lambda world: world.is_weird_route(), LocationGroups.chapter4.value),
  Ch4Locations.lost_miss_mizzle.value:  ConditionalLocationData(LocationIDs.ch4_lost_miss_mizzle.value, Ch4Regions.dark_sanctuary_claimbclaws,  lambda world: world.is_weird_route(), LocationGroups.chapter4.value),
  Ch4Locations.lost_wicabel.value:      ConditionalLocationData(LocationIDs.ch4_lost_wicabel.value,        Ch4Regions.second_sanctuary,            lambda world: world.is_weird_route(), LocationGroups.chapter4.value),
  Ch4Locations.lost_wingblade.value:    ConditionalLocationData(LocationIDs.ch4_lost_winglade.value,        Ch4Regions.second_sanctuary,            lambda world: world.is_weird_route(), LocationGroups.chapter4.value),
  Ch4Locations.lost_organikk.value:     ConditionalLocationData(LocationIDs.ch4_lost_organikk.value,        Ch4Regions.second_sanctuary,            lambda world: world.is_weird_route(), LocationGroups.chapter4.value),
}

chapter4_regions = [
  (Ch4Regions.chapter_4.value,                  [Ch4Entrances.castle_town_entrance.value, Ch4Entrances.fusion_access_entrance]),
  (Ch4Regions.castle_town.value,                [Ch4Entrances.dark_sanctuary_entrance.value]),
  (Ch4Regions.dark_sanctuary.value,             [Ch4Entrances.dark_sanctuary_claimbclaws_entrance.value]),
  (Ch4Regions.dark_sanctuary_claimbclaws.value, [Ch4Entrances.second_sanctuary_entrance.value]),
  (Ch4Regions.second_sanctuary.value,           [Ch4Entrances.third_sanctuary_entrance.value]),
  (Ch4Regions.third_sanctuary.value,            [Ch4Entrances.titan_fight_entrance.value]),
  (Ch4Regions.titan_fight.value,                [Ch4Entrances.light_world_entrance.value]),
  (Ch4Regions.light_world.value,                []),
]

chapter4_mandatory_connections = [
  (Ch4Entrances.castle_town_entrance.value,                 Ch4Regions.castle_town.value),
  (Ch4Entrances.fusion_access_entrance.value,               fusion_access_region),
  (Ch4Entrances.dark_sanctuary_entrance.value,              Ch4Regions.dark_sanctuary.value),
  (Ch4Entrances.dark_sanctuary_claimbclaws_entrance.value,  Ch4Regions.dark_sanctuary_claimbclaws.value),
  (Ch4Entrances.second_sanctuary_entrance.value,            Ch4Regions.second_sanctuary.value),
  (Ch4Entrances.third_sanctuary_entrance.value,             Ch4Regions.third_sanctuary.value),
  (Ch4Entrances.titan_fight_entrance.value,                 Ch4Regions.titan_fight.value),
  (Ch4Entrances.light_world_entrance.value,                 Ch4Regions.light_world.value),
]

def create_regions(world: "DeltaruneWorld"):
  generic_create_regions(world, chapter4_regions, chapter4_locations, chapter4_conditional_locations)