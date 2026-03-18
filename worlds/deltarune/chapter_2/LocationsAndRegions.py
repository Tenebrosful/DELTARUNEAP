from BaseClasses import Location
from enum import StrEnum
from ..Locations import LocationIDs, LocationData, ConditionalLocationData
from ..Regions import generic_create_regions, fusion_access_entrance
from typing import TYPE_CHECKING

if TYPE_CHECKING: from .. import DeltaruneWorld

class Ch2Locations(StrEnum):
  castle_town_jigsaw_joe_challenge = "CH2: Castle Town - Jigsaw Joe Challenge"
  castle_town_graze_challenge_1 = "CH2: Castle Town - Graze Challenge 1"
  castle_town_clover_rematch_challenge = "CH2: Castle Town - Clover Rematch Challenge"
  castle_town_top_chef_gift = "CH2: Castle Town - Top Chef Gift"
  castle_town_tasque_manager_says_challenge = "CH2: Castle Town - Tasque Manager Says Challenge"
  castle_town_ch2_all_stars_challenge = "CH2: Castle Town - Ch2 All Stars Challenge"
  
  
  cyber_field_first_chest = "CH2: Cyber Field - First Chest"
  cyber_field_nubert_chest = "CH2: Cyber Field - Nubert's Chest"
  cyber_field_tasque_maze_checkmark = "CH2: Cyber Field - Tasque Maze Checkmark"
  cyber_field_teacup_ride_checkmark = "CH2: Cyber Field - Teacup Ride Checkmark"
  cyber_field_giasfelfebrehber = "CH2: Cyber Field - Giasfelfebrehber Checkmark"
  cyber_field_chest_near_music_shop = "CH2: Cyber Field - Chest Near Music Shop"
  cyber_field_virovirokun_puzzle_chest = "CH2: Cyber Field - Virovirokun Puzzle Chest"
  cyber_field_teacup_puzzle_chest = "CH2: Cyber Field - Teacup Puzzle Chest"
  
  music_shop_1 = "CH2: Music Shop 1"
  music_shop_2 = "CH2: Music Shop 2"
  music_shop_3 = "CH2: Music Shop 3"
  music_shop_4 = "CH2: Music Shop 4"
  
  trash_zone_trash_can = "CH2: Trash Zone - Trash Can"
  
  cyber_city_trash_can_1 = "CH2: Cyber City - Trash Can #1"
  cyber_city_trash_can_2 = "CH2: Cyber City - Trash Can #2"
  cyber_city_queen_poster_chest = "CH2: Cyber City - Queen Poster Chest"
  cyber_city_chest_guarded_by_virovirokun = "CH2: Cyber City - Chest Guarded By Virovirokun"
  cyber_city_purchase_mannequin = "CH2: Cyber City - Purchase Mannequin"
  cyber_city_annoying_dog = "CH2: Cyber City - Annoying Dog...?"
  cyber_city_man = "CH2: Cyber City - Man"
  cyber_city_moss = "CH2: Cyber City - Moss"
  cyber_city_purchase_kris_tea = "CH2: Cyber City - Purchase Kris Tea"
  cyber_city_purchase_noelle_tea = "CH2: Cyber City - Purchase Noelle Tea"
  cyber_city_purchase_susie_tea = "CH2: Cyber City - Purchase Susie Tea"
  cyber_city_purchase_ralsei_tea = "CH2: Cyber City - Purchase Ralsei Tea"
  cyber_city_cheese_maze_chest = "CH2: Cyber City - Cheese Maze Chest"
  cyber_city_trash_can_3 = "CH2: Cyber City - Trash Can #3"
  cyber_city_trash_can_4 = "CH2: Cyber City - Trash Can #4"
  cyber_city_trash_can_5 = "CH2: Cyber City - Trash Can #5"
  
  mansion_painting_chest = "CH2: Mansion - Painting Chest"
  mansion_sculpture_room_chest = "CH2: Mansion - Sculpture Room Chest"
  mansion_platter_chest = "CH2: Mansion - Platter Chest"
  mansion_tunnel_of_love_chest = "CH2: Mansion - Tunnel of Love Chest"
  mansion_basement_chest = "CH2: Mansion - Basement Chest"
  mansion_basement_mechanism = "CH2: Mansion - Basement Mechanism"
  mansion_spamton_neo_defeat_item_1 = "CH2: Mansion - Spamton NEO Defeat Item #1"
  mansion_spamton_neo_defeat_item_2 = "CH2: Mansion - Spamton NEO Defeat Item #2"
  mansion_spamton_neo_defeat_item_3 = "CH2: Mansion - Spamton NEO Defeat Item #3"
  
  swatch_cafe_1 = "CH2: Swatch's Cafe 1"
  swatch_cafe_2 = "CH2: Swatch's Cafe 2"
  swatch_cafe_3 = "CH2: Swatch's Cafe 3"
  swatch_cafe_4 = "CH2: Swatch's Cafe 4"
  
  spamton_shop_1 = "CH2: Spamton's Shop 1"
  spamton_shop_2 = "CH2: Spamton's Shop 2"
  spamton_shop_3 = "CH2: Spamton's Shop 3"
  spamton_shop_4 = "CH2: Spamton's Shop 4"
  
  fountain_sealed = "CH2: Mansion - Fontain Sealed"
  
  # Warps
  cyber_field_warp_door = "CH2: Cyber Field - Warp Door"
  trash_zone_warp_door = "CH2: Trash Zone - Warp Door"
  mansion_warp_door = "CH2: Mansion - Warp Door"
  
  # Recruits
  recruit_werewire = "CH2: Recruit Werewire"
  recruit_tasque = "CH2: Recruit Tasque"
  recruit_virovirokun = "CH2: Recruit Virovirokun"
  recruit_poppup = "CH2: Recruit Poppup"
  recruit_ambyu_lance = "CH2: Recruit Ambyu-lance"
  recruit_maus = "CH2: Recruit Maus"
  recruit_swatchling = "CH2: Recruit Swatchling"
  recruit_tasque_manager = "CH2: Recruit Tasque Manager"
  recruit_mauswheel = "CH2: Recruit Mauswheel"
  recruit_werewerewire = "CH2: Recruit Werewerewire"
  
  # Weird route
  cyber_city_purchase_freezering = """CH2: Cyber City - "Purchase" FreezeRing"""
  cyber_city_purchase_thornring = "CH2: Cyber City - Purchase ThornRing"
  
  lost_werewire = "CH2: Lost Werewire"
  lost_tasque = "CH2: Lost Tasque"
  lost_virovirokun = "CH2: Lost Virovirokun"
  lost_poppup = "CH2: Lost Poppup"
  lost_ambyulance = "CH2: Lost Ambyu-lance"
  lost_maus = "CH2: Lost Maus"
  lost_swatchlings = "CH2: Lost Swatchlings"
  lost_tasque_manager = "CH2: Lost Tasque Manager"
  lost_mauswheel = "CH2: Lost Mauswheel"
  lost_werewerewire = "CH2: Lost Werewerewire"
  
class Ch2Regions(StrEnum):
  chapter_2 = "Chapter 2"
  castle_town = "CH2: Castle Town"
  cyber_field = "CH2: Cyber Field"
  cyber_city = "CH2: Cyber City"
  mansion = "CH2: Mansion"
  post_chapter_castle_town = "CH2: Post-Chapter Castle Town"
  
class Ch2Entrances(StrEnum):
  castle_town_entrance = "CH2: Castle Town Entrance"
  cyber_field_entrance = "CH2: Cyber Field Entrance"
  cyber_city_entrance = "CH2: Cyber City Entrance"
  mansion_entrance = "CH2: Mansion Entrance"
  post_chapter_castle_town_entrance = "CH2: Post-Chapter Castle Town Entrance"
  
chapter2_end_region = Ch2Regions.post_chapter_castle_town.value
  
chapter2_locations = {
  Ch2Locations.castle_town_jigsaw_joe_challenge.value:      LocationData(LocationIDs.ch2_castle_town_jigsaw_joe_challenge.value,      Ch2Regions.castle_town.value),
  Ch2Locations.castle_town_graze_challenge_1.value:         LocationData(LocationIDs.ch2_castle_town_graze_challenge_1.value,         Ch2Regions.castle_town.value),
  Ch2Locations.castle_town_clover_rematch_challenge.value:  LocationData(LocationIDs.ch2_castle_town_clover_rematch_challenge.value,  Ch2Regions.castle_town.value),
  Ch2Locations.castle_town_top_chef_gift.value:             LocationData(LocationIDs.ch2_castle_town_top_chef_gift.value,             Ch2Regions.castle_town.value),
  
  Ch2Locations.cyber_field_first_chest.value:               LocationData(LocationIDs.ch2_cyber_field_first_chest.value,               Ch2Regions.cyber_field.value),
  Ch2Locations.cyber_field_nubert_chest.value:              LocationData(LocationIDs.ch2_cyber_field_nubert_chest.value,              Ch2Regions.cyber_field.value),
  Ch2Locations.cyber_field_tasque_maze_checkmark.value:     LocationData(LocationIDs.ch2_cyber_field_tasque_maze_checkmark.value,     Ch2Regions.cyber_field.value),
  Ch2Locations.cyber_field_teacup_ride_checkmark.value:     LocationData(LocationIDs.ch2_cyber_field_teacup_ride_checkmark.value,     Ch2Regions.cyber_field.value),
  Ch2Locations.cyber_field_giasfelfebrehber.value:          LocationData(LocationIDs.ch2_cyber_field_giasfelfebrehber_checkmark.value,Ch2Regions.cyber_field.value),
  Ch2Locations.cyber_field_chest_near_music_shop.value:     LocationData(LocationIDs.ch2_cyber_field_chest_near_music_shop.value,     Ch2Regions.cyber_field.value),
  Ch2Locations.cyber_field_virovirokun_puzzle_chest.value:  LocationData(LocationIDs.ch2_cyber_field_virovirokun_puzzle_chest.value,  Ch2Regions.cyber_field.value),
  Ch2Locations.cyber_field_teacup_puzzle_chest.value:       LocationData(LocationIDs.ch2_cyber_field_teacup_puzzle_chest.value,       Ch2Regions.cyber_field.value),
  
  Ch2Locations.music_shop_1.value:                          LocationData(LocationIDs.ch2_music_shop_1.value,                          Ch2Regions.cyber_field.value),
  Ch2Locations.music_shop_2.value:                          LocationData(LocationIDs.ch2_music_shop_2.value,                          Ch2Regions.cyber_field.value),
  Ch2Locations.music_shop_3.value:                          LocationData(LocationIDs.ch2_music_shop_3.value,                          Ch2Regions.cyber_field.value),
  Ch2Locations.music_shop_4.value:                          LocationData(LocationIDs.ch2_music_shop_4.value,                          Ch2Regions.cyber_field.value),
  
  Ch2Locations.trash_zone_trash_can.value:                  LocationData(LocationIDs.ch2_trash_zone_trash_can.value,                  Ch2Regions.cyber_city.value),
  
  Ch2Locations.cyber_city_trash_can_1.value:                  LocationData(LocationIDs.ch2_cyber_city_trash_can_1.value,                  Ch2Regions.cyber_city.value),
  Ch2Locations.cyber_city_trash_can_2.value:                  LocationData(LocationIDs.ch2_cyber_city_trash_can_2.value,                  Ch2Regions.cyber_city.value),
  Ch2Locations.cyber_city_queen_poster_chest.value:           LocationData(LocationIDs.ch2_cyber_city_queen_poster_chest.value,           Ch2Regions.cyber_city.value),
  Ch2Locations.cyber_city_chest_guarded_by_virovirokun.value: LocationData(LocationIDs.ch2_cyber_city_chest_guarded_by_virovirokun.value, Ch2Regions.cyber_city.value),
  Ch2Locations.cyber_city_cheese_maze_chest.value:          LocationData(LocationIDs.ch2_cyber_city_cheese_maze_chest.value,          Ch2Regions.cyber_city.value),
  Ch2Locations.cyber_city_trash_can_3.value:                LocationData(LocationIDs.ch2_cyber_city_trash_can_3.value,                Ch2Regions.cyber_city.value),
  Ch2Locations.cyber_city_trash_can_4.value:                LocationData(LocationIDs.ch2_cyber_city_trash_can_4.value,                Ch2Regions.cyber_city.value),
  Ch2Locations.cyber_city_trash_can_5.value:                LocationData(LocationIDs.ch2_cyber_city_trash_can_5.value,                Ch2Regions.cyber_city.value),
  
  Ch2Locations.mansion_spamton_neo_defeat_item_1.value:     LocationData(LocationIDs.ch2_mansion_spamton_neo_defeat_item_1.value,     Ch2Regions.mansion.value),
  Ch2Locations.mansion_spamton_neo_defeat_item_2.value:     LocationData(LocationIDs.ch2_mansion_spamton_neo_defeat_item_2.value,     Ch2Regions.mansion.value),
  Ch2Locations.mansion_spamton_neo_defeat_item_3.value:     LocationData(LocationIDs.ch2_mansion_spamton_neo_defeat_item_3.value,     Ch2Regions.mansion.value),
  
  Ch2Locations.fountain_sealed.value:                       LocationData(LocationIDs.ch2_fountain_sealed.value,                       Ch2Regions.post_chapter_castle_town),
  
  Ch2Locations.cyber_field_warp_door.value:                 LocationData(LocationIDs.ch2_cyber_field_warp_door.value,                 Ch2Regions.cyber_field.value),
  Ch2Locations.trash_zone_warp_door.value:                  LocationData(LocationIDs.ch2_trash_zone_warp_door.value,                  Ch2Regions.cyber_city.value),
  Ch2Locations.mansion_warp_door.value:                     LocationData(LocationIDs.ch2_mansion_warp_door.value,                     Ch2Regions.mansion.value),
}

chapter2_conditional_locations = {
  # All Recruits
  Ch2Locations.recruit_werewire.value:                ConditionalLocationData(LocationIDs.ch2_recruit_werewire.value,               Ch2Regions.cyber_field.value, lambda world: world.is_all_recruits()),
  Ch2Locations.recruit_tasque.value:                  ConditionalLocationData(LocationIDs.ch2_recruit_tasque.value,                 Ch2Regions.cyber_field.value, lambda world: world.is_all_recruits()),
  Ch2Locations.recruit_virovirokun.value:             ConditionalLocationData(LocationIDs.ch2_recruit_virovirokun.value,            Ch2Regions.cyber_field.value, lambda world: world.is_all_recruits()),
  Ch2Locations.recruit_poppup.value:                  ConditionalLocationData(LocationIDs.ch2_recruit_poppup.value,                 Ch2Regions.cyber_city.value,  lambda world: world.is_all_recruits()),
  Ch2Locations.recruit_ambyu_lance.value:             ConditionalLocationData(LocationIDs.ch2_recruit_ambyu_lance.value,            Ch2Regions.cyber_city.value,  lambda world: world.is_all_recruits()),
  Ch2Locations.cyber_city_purchase_mannequin.value:   ConditionalLocationData(LocationIDs.ch2_cyber_city_purchase_mannequin.value,  Ch2Regions.cyber_city.value,  lambda world: world.is_all_recruits()),
  Ch2Locations.cyber_city_annoying_dog.value:         ConditionalLocationData(LocationIDs.ch2_cyber_city_annoying_dog.value,        Ch2Regions.cyber_city.value,  lambda world: world.is_all_recruits()),
  Ch2Locations.cyber_city_man.value:                  ConditionalLocationData(LocationIDs.ch2_cyber_city_man.value,                 Ch2Regions.cyber_city.value,  lambda world: world.is_all_recruits()),
  Ch2Locations.cyber_city_moss.value:                 ConditionalLocationData(LocationIDs.ch2_cyber_city_moss.value,                Ch2Regions.cyber_city.value,  lambda world: world.is_all_recruits()),
  Ch2Locations.cyber_city_purchase_kris_tea.value:    ConditionalLocationData(LocationIDs.ch2_cyber_city_purchase_kris_tea.value,   Ch2Regions.cyber_city.value,  lambda world: world.is_all_recruits()),
  Ch2Locations.cyber_city_purchase_noelle_tea.value:  ConditionalLocationData(LocationIDs.ch2_cyber_city_purchase_noelle_tea.value, Ch2Regions.cyber_city.value,  lambda world: world.is_all_recruits()),
  Ch2Locations.cyber_city_purchase_susie_tea.value:   ConditionalLocationData(LocationIDs.ch2_cyber_city_purchase_susie_tea.value,  Ch2Regions.cyber_city.value,  lambda world: world.is_all_recruits()),
  Ch2Locations.cyber_city_purchase_ralsei_tea.value:  ConditionalLocationData(LocationIDs.ch2_cyber_city_purchase_ralsei_tea.value, Ch2Regions.cyber_city.value,  lambda world: world.is_all_recruits()),
  Ch2Locations.recruit_maus.value:                    ConditionalLocationData(LocationIDs.ch2_recruit_maus.value,                   Ch2Regions.cyber_city.value,  lambda world: world.is_all_recruits()),
  Ch2Locations.mansion_painting_chest.value:          ConditionalLocationData(LocationIDs.ch2_mansion_painting_chest.value,         Ch2Regions.mansion.value,     lambda world: world.is_all_recruits()),
  Ch2Locations.mansion_sculpture_room_chest.value:    ConditionalLocationData(LocationIDs.ch2_mansion_sculpture_room_chest.value,   Ch2Regions.mansion.value,     lambda world: world.is_all_recruits()),
  Ch2Locations.mansion_platter_chest.value:           ConditionalLocationData(LocationIDs.ch2_mansion_platter_chest.value,          Ch2Regions.mansion.value,     lambda world: world.is_all_recruits()),
  Ch2Locations.mansion_tunnel_of_love_chest.value:    ConditionalLocationData(LocationIDs.ch2_mansion_tunnel_of_love_chest.value,   Ch2Regions.mansion.value,     lambda world: world.is_all_recruits()),
  Ch2Locations.mansion_basement_chest.value:          ConditionalLocationData(LocationIDs.ch2_mansion_basement_chest.value,         Ch2Regions.mansion.value,     lambda world: world.is_all_recruits()),
  Ch2Locations.mansion_basement_mechanism.value:      ConditionalLocationData(LocationIDs.ch2_mansion_basement_mechanism.value,     Ch2Regions.mansion.value,     lambda world: world.is_all_recruits()),
  # Can't lost swatchlings during weird route, only during all routes with a save reload
  Ch2Locations.recruit_swatchling.value:              ConditionalLocationData(LocationIDs.ch2_recruit_swatchling.value,             Ch2Regions.mansion.value,     lambda world: world.is_all_recruits()),
  Ch2Locations.recruit_tasque_manager.value:          ConditionalLocationData(LocationIDs.ch2_recruit_tasque_manager.value,         Ch2Regions.mansion.value,     lambda world: world.is_all_recruits()),
  Ch2Locations.recruit_mauswheel.value:               ConditionalLocationData(LocationIDs.ch2_recruit_mauswheel.value,              Ch2Regions.mansion.value,     lambda world: world.is_all_recruits()),
  Ch2Locations.swatch_cafe_1.value:                   ConditionalLocationData(LocationIDs.ch2_swatchs_cafe_1.value,                 Ch2Regions.mansion.value,     lambda world: world.is_all_recruits()),
  Ch2Locations.swatch_cafe_2.value:                   ConditionalLocationData(LocationIDs.ch2_swatchs_cafe_2.value,                 Ch2Regions.mansion.value,     lambda world: world.is_all_recruits()),
  Ch2Locations.swatch_cafe_3.value:                   ConditionalLocationData(LocationIDs.ch2_swatchs_cafe_3.value,                 Ch2Regions.mansion.value,     lambda world: world.is_all_recruits()),
  Ch2Locations.swatch_cafe_4.value:                   ConditionalLocationData(LocationIDs.ch2_swatchs_cafe_4.value,                 Ch2Regions.mansion.value,     lambda world: world.is_all_recruits()),
  Ch2Locations.spamton_shop_1.value:                  ConditionalLocationData(LocationIDs.ch2_spamtons_shop_1.value,                Ch2Regions.mansion.value,     lambda world: world.is_all_recruits()),
  Ch2Locations.spamton_shop_2.value:                  ConditionalLocationData(LocationIDs.ch2_spamtons_shop_2.value,                Ch2Regions.mansion.value,     lambda world: world.is_all_recruits()),
  Ch2Locations.spamton_shop_3.value:                  ConditionalLocationData(LocationIDs.ch2_spamtons_shop_3.value,                Ch2Regions.mansion.value,     lambda world: world.is_all_recruits()),
  Ch2Locations.spamton_shop_3.value:                  ConditionalLocationData(LocationIDs.ch2_spamtons_shop_4.value,                Ch2Regions.mansion.value,     lambda world: world.is_all_recruits()),
  Ch2Locations.recruit_werewerewire.value:                      ConditionalLocationData(LocationIDs.ch2_recruit_werewerewire.value,                       Ch2Regions.mansion.value, lambda world: world.is_all_recruits()),
  Ch2Locations.castle_town_tasque_manager_says_challenge.value: ConditionalLocationData(LocationIDs.ch2_castle_town_tasque_manager_says_challenge.value,  Ch2Regions.mansion.value, lambda world: world.is_all_recruits()),
  Ch2Locations.castle_town_ch2_all_stars_challenge.value:       ConditionalLocationData(LocationIDs.ch2_castle_town_all_stars_challenge.value,            Ch2Regions.mansion.value, lambda world: world.is_all_recruits()),
  
  # Weird Route
  Ch2Locations.lost_werewire.value:                   ConditionalLocationData(LocationIDs.ch2_lost_werewire.value,                  Ch2Regions.cyber_field.value, lambda world: world.is_weird_route()),
  Ch2Locations.lost_tasque.value:                     ConditionalLocationData(LocationIDs.ch2_lost_tasque.value,                    Ch2Regions.cyber_field.value, lambda world: world.is_weird_route()),
  Ch2Locations.lost_virovirokun.value:                ConditionalLocationData(LocationIDs.ch2_lost_virovirokun.value,               Ch2Regions.cyber_field.value, lambda world: world.is_weird_route()),
  Ch2Locations.lost_poppup.value:                     ConditionalLocationData(LocationIDs.ch2_lost_poppup.value,                    Ch2Regions.cyber_city.value,  lambda world: world.is_weird_route()),
  Ch2Locations.lost_ambyulance.value:                 ConditionalLocationData(LocationIDs.ch2_lost_ambyu_lance.value,               Ch2Regions.cyber_city.value,  lambda world: world.is_weird_route()),
  Ch2Locations.cyber_city_purchase_freezering.value:  ConditionalLocationData(LocationIDs.ch2_cyber_city_purchase_freezering.value, Ch2Regions.cyber_city.value,  lambda world: world.is_weird_route()),
  Ch2Locations.lost_maus.value:                       ConditionalLocationData(LocationIDs.ch2_lost_maus.value,                      Ch2Regions.cyber_city.value,  lambda world: world.is_weird_route()),
  Ch2Locations.cyber_city_purchase_thornring.value:   ConditionalLocationData(LocationIDs.ch2_cyber_city_purchase_thornring.value,  Ch2Regions.cyber_city.value,  lambda world: world.is_weird_route()),
  # Can't lost swatchlings during weird route, only during all routes with a save reload
  Ch2Locations.lost_swatchlings.value:                ConditionalLocationData(LocationIDs.ch2_lost_swatchlings.value,               Ch2Regions.mansion.value, lambda world: world.is_all_routes()),
  Ch2Locations.lost_tasque_manager.value:             ConditionalLocationData(LocationIDs.ch2_lost_tasque_manager.value,            Ch2Regions.mansion.value, lambda world: world.is_weird_route()),
  Ch2Locations.lost_mauswheel.value:                  ConditionalLocationData(LocationIDs.ch2_lost_mauswheel.value,                 Ch2Regions.mansion.value, lambda world: world.is_weird_route()),
  Ch2Locations.lost_werewerewire.value:               ConditionalLocationData(LocationIDs.ch2_lost_werewerewire.value,              Ch2Regions.mansion.value, lambda world: world.is_weird_route()),
}

chapter2_regions = [
  (Ch2Regions.chapter_2.value, [Ch2Entrances.castle_town_entrance.value, fusion_access_entrance]),
  (Ch2Regions.castle_town.value, [Ch2Entrances.cyber_field_entrance.value]),
  (Ch2Regions.cyber_field.value, [Ch2Entrances.cyber_city_entrance.value]),
  (Ch2Regions.cyber_city.value, [Ch2Entrances.mansion_entrance.value]),
  (Ch2Regions.mansion.value, [Ch2Entrances.post_chapter_castle_town_entrance.value]),
  (Ch2Regions.post_chapter_castle_town.value, [])
]

chapter2_mandatory_connections = [
  (Ch2Entrances.castle_town_entrance.value, Ch2Regions.castle_town.value),
  (Ch2Entrances.cyber_field_entrance.value, Ch2Regions.cyber_field.value),
  (Ch2Entrances.cyber_city_entrance.value, Ch2Regions.cyber_city.value),
  (Ch2Entrances.mansion_entrance.value, Ch2Regions.mansion.value),
  (Ch2Entrances.post_chapter_castle_town_entrance.value, Ch2Regions.post_chapter_castle_town.value)
]

def create_regions(world: "DeltaruneWorld"):
  generic_create_regions(world, chapter2_regions, chapter2_locations, chapter2_conditional_locations)