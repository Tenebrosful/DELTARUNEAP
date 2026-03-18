from BaseClasses import Location
from enum import StrEnum
from ..Locations import LocationIDs, LocationData, ConditionalLocationData
from ..Regions import generic_create_regions, fusion_access_entrance
from typing import TYPE_CHECKING

if TYPE_CHECKING: from .. import DeltaruneWorld

class Ch3Locations(StrEnum):
  couch_cliffs_dust_pile_chest = "CH3: Couch Cliffs - Dust Pile Chest"
  
  board_1_c_rank = "CH3: Board 1 - C-Rank"
  board_1_b_rank = "CH3: Board 1 - B-Rank"
  board_1_a_rank = "CH3: Board 1 - A-Rank"
  board_1_s_rank = "CH3: Board 1 - S-Rank"
  board_1_t_rank = "CH3: Board 1 - T-Rank"
  board_1_extra_key = "CH3: Board 1 - Extra Key"
  
  green_room_vending_machine_1 = "CH3: Green Room - Vending Machine 1"
  green_room_vending_machine_2 = "CH3: Green Room - Vending Machine 2"
  green_room_vending_machine_3 = "CH3: Green Room - Vending Machine 3"
  green_room_vending_machine_4 = "CH3: Green Room - Vending Machine 4"
  green_room_vending_machine_5 = "CH3: Green Room - Vending Machine 5"
  green_room_vending_machine_6 = "CH3: Green Room - Vending Machine 6"
  green_room_vending_machine_7 = "CH3: Green Room - Vending Machine 7"
  green_room_vending_machine_8 = "CH3: Green Room - Vending Machine 8"
  green_room_board_1_ramb_gift = "CH3: Green Room - Board 1 Ramb Gift"
  green_room_board_2_ramb_gift = "CH3: Green Room - Board 2 Ramb Gift"
  
  b_rank_room_golden_prize_1 = "CH3: B-Rank Room - Golden Prize 1"
  b_rank_room_golden_prize_2 = "CH3: B-Rank Room - Golden Prize 2"
  b_rank_room_golden_prize_3 = "CH3: B-Rank Room - Golden Prize 3"
  b_rank_room_golden_prize_4 = "CH3: B-Rank Room - Golden Prize 4"
  b_rank_room_golden_prize_5 = "CH3: B-Rank Room - Golden Prize 5"
  
  s_rank_room_person_behing_curtain = "CH3: S-Rank Room - Person Behind Curtain"
  s_rank_room_vending_machine_1 = "CH3: S-Rank Room - Vending Machine 1"
  s_rank_room_vending_machine_2 = "CH3: S-Rank Room - Vending Machine 2"
  s_rank_room_vending_machine_3 = "CH3: S-Rank Room - Vending Machine 3"
  s_rank_room_vending_machine_4 = "CH3: S-Rank Room - Vending Machine 4"
  s_rank_room_oddcontroller = "CH3: S-Rank Room - OddController"
  s_rank_room_susie_gift = "CH3: S-Rank Room - Susie's Gift"
  
  board_2_c_rank = "CH3: Board 2 - C-Rank"
  board_2_b_rank = "CH3: Board 2 - B-Rank"
  board_2_a_rank = "CH3: Board 2 - A-Rank"
  board_2_s_rank = "CH3: Board 2 - S-Rank"
  board_2_t_rank = "CH3: Board 2 - T-Rank"
  board_2_extra_photo = "CH3: Board 2 - Extra Photo"
  board_2_moss = "CH3: Board 2 - Moss"
  
  tv_world_chest_near_shadowmen = "CH3: TV World - Chest near shadowmen"
  tv_world_board_puzzle_1_chest = "CH3: TV World - Board Puzzle 1 Chest"
  tv_world_trash_can_1 = "CH3: TV World - Trash Can 1"
  tv_world_trash_can_2 = "CH3: TV World - Trash Can 2"
  tv_world_trash_can_3 = "CH3: TV World - Trash Can 3"
  tv_world_trash_can_4 = "CH3: TV World - Trash Can 4"
  tv_world_trash_can_5 = "CH3: TV World - Trash Can 5"
  tv_world_water_cooler_chest = "CH3: TV World - Water Cooler Chest"
  tv_world_board_puzzle_2_chest = "CH3: TV World - Board Puzzle 2 Chest"
  tw_world_serious_trashy_chest = "CH3: TV World - Serious Trashy Chest"
  tv_world_bonus_zone_chest_1 = "CH3: TV World - Bonus Zone Chest 1"
  tv_world_bonus_zone_chest_2 = "CH3: TV World - Bonus Zone Chest 2"
  tv_world_bonus_zone_chest_3 = "CH3: TV World - Bonus Zone Chest 3"
  tv_world_chest_outside_green_room = "CH3: TV World - Chest Outside Green Room"
  tv_world_tripticket = "CH3: TV World - TripTicket"
  tv_world_man = "CH3: TV World - Man"
  
  recruit_elnina = "CH3: Recruit Elnina"
  recruit_lanino = "CH3: Recruit Lanino"
  recruit_shadowguy = "CH3: Recruit Shadowguy"
  recruit_shuttah = "CH3: Recruit Shuttah"
  recruit_zapper = "CH3: Recruit Zapper"
  recruit_ribbick = "CH3: Recruit Ribbick"
  recruit_pippins = "CH3: Recruit Pippins"
  recruit_water_cooler = "CH3: Recruit Water Cooler"
  
  lost_shadowguy = "CH3: Lost Shadowguy"
  lost_shuttah = "CH3: Lost Shuttah"
  lost_zapper = "CH3: Lost Zapper"
  lost_ribbick = "CH3: Lost Ribbick"
  lost_pippins = "CH3: Lost Pippins"
  lost_water_cooler = "CH3: Lost Water Cooler"
  
  mantle_out_of_bounds_chest = "CH3: MANTLE - Out of Bounds Chest"
  mantle_northern_light_item = "CH3: MANTLE - Northern Light Item"
  mantle_defeat = "CH3: MANTLE - Defeat"
  
  cold_place_knight_defeat_item_1 = "CH3: Cold Place - Knight Defeat Item 1"
  cold_place_knight_defeat_item_2 = "CH3: Cold Place - Knight Defeat Item 2"
  
  # Warps
  couch_cliffs_warp_door = "CH3: Couch Cliffs - Warp Door"
  green_room_warp_door = "CH3: Green Room - Warp Door"
  tv_world_entrance_warp_door = "CH3: TV World - Entrance Warp Door"
  tv_world_goulden_sam_warp_door = "CH3: TV World - Goulden Sam Warp Door"
  
  fountain_sealed = "CH3: TV World - Fountain Sealed"
  
class Ch3Regions(StrEnum):
  chapter_3 = "Chapter 3"
  couch_cliffs = "CH3: Couch Cliffs"
  board_1 = "CH3: Board 1"
  green_room = "CH3: Green Room"
  board_2 = "CH3: Board 2"
  tv_world = "CH3: TV World"
  goulden_sam = "CH3: Goulden Sam"
  cold_place = "CH3: Cold Place"
  
class Ch3Entrances(StrEnum):
  couch_cliffs_entrance = "CH3: Couch Cliffs Entrance"
  board_1_entrance = "CH3: Board 1 Entrance"
  green_room_entrance = "CH3: Green Room Entrance"
  board_2_entrance = "CH3: Board 2 Entrance"
  tv_world_entrance = "CH3: TV World Entrance"
  goulden_sam_entrance = "CH3: Goulden Sam Entrance"
  cold_place_entrance = "CH3: Cold Place Entrance"

chapter3_end_region = Ch3Regions.cold_place.value

chapter3_locations = {
  Ch3Locations.couch_cliffs_dust_pile_chest.value:  LocationData(LocationIDs.ch3_couch_cliffs_dust_pile_chest.value,  Ch3Regions.couch_cliffs),
  Ch3Locations.couch_cliffs_warp_door.value:        LocationData(LocationIDs.ch3_couch_cliffs_warp_door.value,        Ch3Regions.couch_cliffs),
  
  Ch3Locations.board_1_c_rank.value:                LocationData(LocationIDs.ch3_board_1_c_rank.value,                Ch3Regions.board_1),
  Ch3Locations.board_1_b_rank.value:                LocationData(LocationIDs.ch3_board_1_b_rank.value,                Ch3Regions.board_1),
  Ch3Locations.board_1_a_rank.value:                LocationData(LocationIDs.ch3_board_1_a_rank.value,                Ch3Regions.board_1),
  Ch3Locations.board_1_s_rank.value:                LocationData(LocationIDs.ch3_board_1_s_rank.value,                Ch3Regions.board_1),
  Ch3Locations.board_1_extra_key.value:             LocationData(LocationIDs.ch3_board_1_extra_key.value,             Ch3Regions.board_1),
  
  Ch3Locations.green_room_vending_machine_1.value:  LocationData(LocationIDs.ch3_green_room_vending_machine_1.value,  Ch3Regions.green_room),
  Ch3Locations.green_room_vending_machine_2.value:  LocationData(LocationIDs.ch3_green_room_vending_machine_2.value,  Ch3Regions.green_room),
  Ch3Locations.green_room_vending_machine_3.value:  LocationData(LocationIDs.ch3_green_room_vending_machine_3.value,  Ch3Regions.green_room),
  Ch3Locations.green_room_vending_machine_4.value:  LocationData(LocationIDs.ch3_green_room_vending_machine_4.value,  Ch3Regions.green_room),
  Ch3Locations.green_room_vending_machine_5.value:  LocationData(LocationIDs.ch3_green_room_vending_machine_5.value,  Ch3Regions.green_room),
  Ch3Locations.green_room_vending_machine_6.value:  LocationData(LocationIDs.ch3_green_room_vending_machine_6.value,  Ch3Regions.green_room),
  Ch3Locations.green_room_vending_machine_7.value:  LocationData(LocationIDs.ch3_green_room_vending_machine_7.value,  Ch3Regions.green_room),
  Ch3Locations.green_room_vending_machine_8.value:  LocationData(LocationIDs.ch3_green_room_vending_machine_8.value,  Ch3Regions.green_room),
  Ch3Locations.green_room_board_1_ramb_gift.value:  LocationData(LocationIDs.ch3_green_room_board_1_ramb_gift.value,  Ch3Regions.green_room),
  Ch3Locations.b_rank_room_golden_prize_1.value:  LocationData(LocationIDs.ch3_b_rank_room_golden_prize_1.value,      Ch3Regions.green_room),
  Ch3Locations.b_rank_room_golden_prize_2.value:  LocationData(LocationIDs.ch3_b_rank_room_golden_prize_2.value,      Ch3Regions.green_room),
  Ch3Locations.b_rank_room_golden_prize_3.value:  LocationData(LocationIDs.ch3_b_rank_room_golden_prize_3.value,      Ch3Regions.green_room),
  Ch3Locations.b_rank_room_golden_prize_4.value:  LocationData(LocationIDs.ch3_b_rank_room_golden_prize_4.value,      Ch3Regions.green_room),
  Ch3Locations.b_rank_room_golden_prize_5.value:  LocationData(LocationIDs.ch3_b_rank_room_golden_prize_5.value,      Ch3Regions.green_room),
  Ch3Locations.s_rank_room_person_behing_curtain.value:  LocationData(LocationIDs.ch3_s_rank_room_person_behind_curtain.value,      Ch3Regions.green_room),
  Ch3Locations.s_rank_room_vending_machine_1.value:  LocationData(LocationIDs.ch3_s_rank_room_vending_machine_1.value,      Ch3Regions.green_room),
  Ch3Locations.s_rank_room_vending_machine_2.value:  LocationData(LocationIDs.ch3_s_rank_room_vending_machine_2.value,      Ch3Regions.green_room),
  Ch3Locations.s_rank_room_vending_machine_3.value:  LocationData(LocationIDs.ch3_s_rank_room_vending_machine_3.value,      Ch3Regions.green_room),
  Ch3Locations.s_rank_room_vending_machine_4.value:  LocationData(LocationIDs.ch3_s_rank_room_vending_machine_4.value,      Ch3Regions.green_room),
  Ch3Locations.s_rank_room_oddcontroller.value:  LocationData(LocationIDs.ch3_s_rank_room_oddcontroller.value,      Ch3Regions.green_room),
  
  Ch3Locations.board_2_c_rank.value:                LocationData(LocationIDs.ch3_board_2_c_rank.value,                Ch3Regions.board_2),
  Ch3Locations.board_2_b_rank.value:                LocationData(LocationIDs.ch3_board_2_b_rank.value,                Ch3Regions.board_2),
  Ch3Locations.board_2_a_rank.value:                LocationData(LocationIDs.ch3_board_2_a_rank.value,                Ch3Regions.board_2),
  Ch3Locations.board_2_s_rank.value:                LocationData(LocationIDs.ch3_board_2_s_rank.value,                Ch3Regions.board_2),
  Ch3Locations.board_2_extra_photo.value:           LocationData(LocationIDs.ch3_board_2_extra_photo.value,           Ch3Regions.board_2),
  Ch3Locations.board_2_moss.value:                  LocationData(LocationIDs.ch3_board_2_moss.value,                  Ch3Regions.board_2),
  Ch3Locations.green_room_board_2_ramb_gift.value:  LocationData(LocationIDs.ch3_green_room_board_2_ramb_gift.value,  Ch3Regions.board_2),
  
  Ch3Locations.tv_world_chest_near_shadowmen.value: LocationData(LocationIDs.ch3_tv_world_chest_near_shadowmen.value, Ch3Regions.tv_world),
  Ch3Locations.tv_world_board_puzzle_1_chest.value: LocationData(LocationIDs.ch3_tv_world_board_puzzle_1_chest.value, Ch3Regions.tv_world),
  
  Ch3Locations.tv_world_trash_can_1.value:          LocationData(LocationIDs.ch3_tv_world_trash_can_1.value,          Ch3Regions.goulden_sam),
  Ch3Locations.tv_world_trash_can_2.value:          LocationData(LocationIDs.ch3_tv_world_trash_can_2.value,          Ch3Regions.goulden_sam),
  Ch3Locations.tv_world_trash_can_3.value:          LocationData(LocationIDs.ch3_tv_world_trash_can_3.value,          Ch3Regions.goulden_sam),
  Ch3Locations.tv_world_trash_can_4.value:          LocationData(LocationIDs.ch3_tv_world_trash_can_4.value,          Ch3Regions.goulden_sam),
  Ch3Locations.tv_world_trash_can_5.value:          LocationData(LocationIDs.ch3_tv_world_trash_can_5.value,          Ch3Regions.goulden_sam),
  Ch3Locations.tv_world_board_puzzle_2_chest.value: LocationData(LocationIDs.ch3_tv_world_board_puzzle_2_chest.value, Ch3Regions.goulden_sam),
  Ch3Locations.tw_world_serious_trashy_chest.value: LocationData(LocationIDs.ch3_tv_world_serious_trashy_chest.value, Ch3Regions.goulden_sam),
  Ch3Locations.tv_world_bonus_zone_chest_1.value:   LocationData(LocationIDs.ch3_tv_world_bonus_zone_chest_1.value,   Ch3Regions.goulden_sam),
  Ch3Locations.tv_world_bonus_zone_chest_2.value:   LocationData(LocationIDs.ch3_tv_world_bonus_zone_chest_2.value,   Ch3Regions.goulden_sam),
  Ch3Locations.tv_world_bonus_zone_chest_3.value:   LocationData(LocationIDs.ch3_tv_world_bonus_zone_chest_3.value,   Ch3Regions.goulden_sam),
  Ch3Locations.tv_world_chest_outside_green_room.value:   LocationData(LocationIDs.ch3_tv_world_chest_outside_green_room.value,   Ch3Regions.goulden_sam),
  Ch3Locations.tv_world_man.value:                        LocationData(LocationIDs.ch3_tv_world_man.value,                        Ch3Regions.goulden_sam),
  
  # SWORD
  Ch3Locations.mantle_out_of_bounds_chest.value:       LocationData(LocationIDs.ch3_mantle_out_of_bounds_chest.value,       Ch3Regions.board_1),
  Ch3Locations.mantle_northern_light_item.value:   LocationData(LocationIDs.ch3_mantle_northern_light_item.value,   Ch3Regions.board_2),
  Ch3Locations.mantle_defeat.value: LocationData(LocationIDs.ch3_mantle_defeat.value, Ch3Regions.goulden_sam),
  Ch3Locations.s_rank_room_susie_gift.value:LocationData(LocationIDs.ch3_s_rank_room_susie_gift.value,Ch3Regions.goulden_sam),
  
  Ch3Locations.cold_place_knight_defeat_item_1.value:   LocationData(LocationIDs.ch3_cold_place_knight_defeat_item_1.value,   Ch3Regions.cold_place),
  Ch3Locations.cold_place_knight_defeat_item_2.value:   LocationData(LocationIDs.ch3_cold_place_knight_defeat_item_2.value,   Ch3Regions.cold_place),
  Ch3Locations.fountain_sealed.value:                   LocationData(LocationIDs.ch3_fountain_sealed.value,                   Ch3Regions.cold_place),
  
  # Warps
  Ch3Locations.couch_cliffs_warp_door.value:                LocationData(LocationIDs.ch3_couch_cliffs_warp_door.value,        Ch3Regions.couch_cliffs),
  Ch3Locations.green_room_warp_door.value:                  LocationData(LocationIDs.ch3_green_room_warp_door.value,          Ch3Regions.green_room),
  Ch3Locations.tv_world_entrance_warp_door.value:           LocationData(LocationIDs.ch3_tv_world_entrance_warp_door.value,   Ch3Regions.board_2),
  Ch3Locations.tv_world_goulden_sam_warp_door.value:        LocationData(LocationIDs.ch3_tv_world_goulden_sam_warp_door.value,Ch3Regions.goulden_sam),
}

chapter3_conditional_locations = {
  # Prevent potential unreachable softlock
  Ch3Locations.tv_world_tripticket.value: ConditionalLocationData(LocationIDs.ch3_tv_world_tripticket.value,     Ch3Regions.goulden_sam, lambda world: not world.is_weird_route()),
  
  # T-Rank
  Ch3Locations.board_1_t_rank.value: ConditionalLocationData(LocationIDs.ch3_board_1_t_rank.value, Ch3Regions.board_1, lambda world: world.options.include_t_rank == 1),
  Ch3Locations.board_2_t_rank.value: ConditionalLocationData(LocationIDs.ch3_board_2_t_rank.value, Ch3Regions.board_2, lambda world: world.options.include_t_rank == 1),
  
  # All Recruits
  Ch3Locations.recruit_water_cooler.value:  ConditionalLocationData(LocationIDs.ch3_recruit_water_cooler.value,  Ch3Regions.green_room,  lambda world: world.is_all_recruits()),
  Ch3Locations.recruit_pippins.value:       ConditionalLocationData(LocationIDs.ch3_recruit_pippins.value,       Ch3Regions.board_2,     lambda world: world.is_all_recruits()),
  Ch3Locations.recruit_shuttah.value:       ConditionalLocationData(LocationIDs.ch3_recruit_shuttah.value,       Ch3Regions.tv_world,    lambda world: world.is_all_recruits()),
  Ch3Locations.recruit_shadowguy.value:     ConditionalLocationData(LocationIDs.ch3_recruit_shadowguy.value,     Ch3Regions.goulden_sam, lambda world: world.is_all_recruits()),
  Ch3Locations.recruit_zapper.value:        ConditionalLocationData(LocationIDs.ch3_recruit_zapper.value,        Ch3Regions.goulden_sam, lambda world: world.is_all_recruits()),
  Ch3Locations.recruit_ribbick.value:       ConditionalLocationData(LocationIDs.ch3_recruit_ribbick.value,       Ch3Regions.goulden_sam, lambda world: world.is_all_recruits()),
  Ch3Locations.recruit_lanino.value:        ConditionalLocationData(LocationIDs.ch3_recruit_lanino.value,        Ch3Regions.goulden_sam, lambda world: world.is_all_recruits()),
  Ch3Locations.recruit_elnina.value:        ConditionalLocationData(LocationIDs.ch3_recruit_elnina.value,        Ch3Regions.goulden_sam, lambda world: world.is_all_recruits()),
  
  # Weird Route
  Ch3Locations.lost_shadowguy.value:     ConditionalLocationData(LocationIDs.ch3_lost_shadowguy.value,     Ch3Regions.board_1,      lambda world: world.is_weird_route()),
  Ch3Locations.lost_water_cooler.value:  ConditionalLocationData(LocationIDs.ch3_lost_water_cooler.value,  Ch3Regions.green_room,   lambda world: world.is_weird_route()),
  Ch3Locations.lost_pippins.value:       ConditionalLocationData(LocationIDs.ch3_lost_pippins.value,       Ch3Regions.board_2,      lambda world: world.is_weird_route()),
  Ch3Locations.lost_shuttah.value:       ConditionalLocationData(LocationIDs.ch3_lost_shuttah.value,       Ch3Regions.board_2,      lambda world: world.is_weird_route()),
  Ch3Locations.lost_zapper.value:        ConditionalLocationData(LocationIDs.ch3_lost_zapper.value,        Ch3Regions.board_2,      lambda world: world.is_weird_route()),
  Ch3Locations.lost_ribbick.value:       ConditionalLocationData(LocationIDs.ch3_lost_ribbick.value,       Ch3Regions.goulden_sam,  lambda world: world.is_weird_route()),
}

chapter3_regions = [
  (Ch3Regions.chapter_3.value,    [Ch3Entrances.couch_cliffs_entrance.value]),
  (Ch3Regions.couch_cliffs.value, [Ch3Entrances.board_1_entrance.value]),
  (Ch3Regions.board_1.value,      [Ch3Entrances.green_room_entrance.value]),
  (Ch3Regions.green_room.value,   [Ch3Entrances.board_2_entrance.value]),
  (Ch3Regions.board_2.value,      [Ch3Entrances.tv_world_entrance.value]),
  (Ch3Regions.tv_world.value,     [Ch3Entrances.goulden_sam_entrance.value]),
  (Ch3Regions.goulden_sam.value,  [Ch3Entrances.cold_place_entrance.value]),
  (Ch3Regions.cold_place.value,   [])
]

chapter3_mandatory_connections = [
  (Ch3Entrances.couch_cliffs_entrance.value,  Ch3Regions.couch_cliffs),
  (Ch3Entrances.board_1_entrance.value,       Ch3Regions.board_1),
  (Ch3Entrances.green_room_entrance.value,    Ch3Regions.green_room),
  (Ch3Entrances.board_2_entrance.value,       Ch3Regions.board_2),
  (Ch3Entrances.tv_world_entrance.value,      Ch3Regions.tv_world),
  (Ch3Entrances.goulden_sam_entrance.value,   Ch3Regions.goulden_sam),
  (Ch3Entrances.cold_place_entrance.value,    Ch3Regions.cold_place),
]

def create_regions(world: "DeltaruneWorld"):
  generic_create_regions(world, chapter3_regions, chapter3_locations, chapter3_conditional_locations)