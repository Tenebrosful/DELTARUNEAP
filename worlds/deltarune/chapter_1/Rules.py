from worlds.generic.Rules import set_rule
from typing import TYPE_CHECKING
from ..Options import RandomizeChapterOptions, RandomizeSecretBossesOptions
from .LocationsAndRegions import Ch1Entrances, Ch1Regions, Ch1Locations
from .Items import Ch1Items
from ..cross_chapter.LocationsAndRegions import CCEntrances

if TYPE_CHECKING:
    from .. import DeltaruneWorld

def set_rules(world: "DeltaruneWorld"): 
  player = world.player
  multiworld = world.multiworld
  
  # Chapter unlock
  if not world.is_all_chapters_unlocked():
    set_rule(multiworld.get_entrance(CCEntrances.chapter_1_entrance,  player), lambda state: state.has(Ch1Items.chapter_1_unlock, player))
    
  # Region lockers
  set_rule(multiworld.get_entrance(Ch1Entrances.bake_sale_entrance,   player), lambda state: state.has(Ch1Items.bake_sale_ticket, player))
  set_rule(multiworld.get_entrance(Ch1Entrances.card_castle_entrance, player), lambda state: state.has(Ch1Items.castle_key, player))
  
  # Warps
  set_rule(multiworld.get_entrance(Ch1Entrances.fields_warp,          player), lambda state: state.has(Ch1Items.fields_warp, player))
  set_rule(multiworld.get_entrance(Ch1Entrances.forest_warp,          player), lambda state: state.has(Ch1Items.forest_warp, player))
  set_rule(multiworld.get_entrance(Ch1Entrances.bake_sale_warp,       player), lambda state: state.has(Ch1Items.bake_sale_warp, player))
  set_rule(multiworld.get_entrance(Ch1Entrances.card_castle_warp,     player), lambda state: state.has(Ch1Items.card_castle_warp, player))
  
  # Warp Hubs
  set_rule(multiworld.get_entrance(Ch1Entrances.fields_warp_hub,      player), lambda state: state.has(Ch1Items.fields_warp, player))
  set_rule(multiworld.get_entrance(Ch1Entrances.forest_warp_hub,      player), lambda state: state.has(Ch1Items.forest_warp, player))
  set_rule(multiworld.get_entrance(Ch1Entrances.bake_sale_warp_hub,   player), lambda state: state.has(Ch1Items.bake_sale_warp, player))
  set_rule(multiworld.get_entrance(Ch1Entrances.card_castle_warp_hub, player), lambda state: state.has(Ch1Items.card_castle_warp, player))
  if not world.is_warps_randomized():
        multiworld.get_location(Ch1Locations.field_warp_door, player).place_locked_item(world.create_item(Ch1Items.fields_warp))
        multiworld.get_location(Ch1Locations.forest_warp_door, player).place_locked_item(world.create_item(Ch1Items.forest_warp))
        multiworld.get_location(Ch1Locations.bake_sale_warp_door, player).place_locked_item(world.create_item(Ch1Items.bake_sale_warp))
        multiworld.get_location(Ch1Locations.card_castle_warp_door, player).place_locked_item(world.create_item(Ch1Items.card_castle_warp))
  
  # Mandatory Secret boss option and macguffin
  if world.is_secret_bosses_mandatory():
    if world.is_final_chapter(1):
      set_rule(multiworld.get_entrance(Ch1Entrances.light_world_entrance, player), lambda state: 
                                                                                          state.has(Ch1Items.king_shape_key_piece, player, world.options.goal_macguffin_amount.value)
                                                                                      and state.has(Ch1Items.door_key, player))
    else:
      set_rule(multiworld.get_entrance(Ch1Entrances.light_world_entrance, player), lambda state: state.has(Ch1Items.door_key, player))
  elif world.is_final_chapter(1):
    set_rule(multiworld.get_entrance(Ch1Entrances.light_world_entrance, player), lambda state: state.has(Ch1Items.king_shape_key_piece, player, world.options.goal_macguffin_amount.value))
  
  # Jevil quest
  set_rule(multiworld.get_location(Ch1Locations.bake_sale_repair_door_key, player),             lambda state: state.has_all({
                                                                                                    Ch1Items.broken_key_a,
                                                                                                    Ch1Items.broken_key_b,
                                                                                                    Ch1Items.broken_key_c
                                                                                                  }, player))
  set_rule(multiworld.get_location(Ch1Locations.card_castle_jevil_1, player),                   lambda state: state.has(Ch1Items.door_key, player))
  set_rule(multiworld.get_location(Ch1Locations.card_castle_jevil_2, player),                   lambda state: state.has(Ch1Items.door_key, player))
  set_rule(multiworld.get_location(Ch1Locations.card_castle_jevil_3, player),                   lambda state: state.has(Ch1Items.door_key, player))
  set_rule(multiworld.get_location(Ch1Locations.seam_seap_talk_about_strange_prisoner, player), lambda state: state.can_reach(Ch1Regions.card_castle, "Region", player))
  
  # Cake quest
  set_rule(multiworld.get_location(Ch1Locations.bake_sale_repair_top_cake, player), lambda state: state.has(Ch1Items.brokencake, player))
  set_rule(multiworld.get_location(Ch1Locations.field_return_top_cake, player),     lambda state: state.has(Ch1Items.top_cake, player))
  
  set_rule(multiworld.get_location(Ch1Locations.throw_away_manual, player),         lambda state: state.has(Ch1Items.manual, player))
  
  # Hidden items
  if not world.is_hidden_items_randomized():
    multiworld.get_location(Ch1Locations.forest_man, player).place_locked_item(world.create_item(Ch1Items.egg))
    multiworld.get_location(Ch1Locations.card_castle_moss, player).place_locked_item(world.create_item(Ch1Items.castle_moss))
    multiworld.get_location(Ch1Locations.seam_seap_talk_about_strange_prisoner, player).place_locked_item(world.create_item(Ch1Items.broken_key_a))
    multiworld.get_location(Ch1Locations.forest_hidden_chest_near_dancers, player).place_locked_item(world.create_item(Ch1Items.broken_key_b))
    multiworld.get_location(Ch1Locations.field_chest_before_great_board, player).place_locked_item(world.create_item(Ch1Items.broken_key_c))
    multiworld.get_location(Ch1Locations.bake_sale_repair_door_key, player).place_locked_item(world.create_item(Ch1Items.door_key))