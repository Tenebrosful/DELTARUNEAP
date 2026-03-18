from worlds.generic.Rules import set_rule
from BaseClasses import CollectionState
from typing import TYPE_CHECKING
from ..Options import RandomizeChapterOptions, RandomizeSecretBossesOptions
from .LocationsAndRegions import Ch3Entrances, Ch3Regions, Ch3Locations
from .Items import Ch3Items
from ..cross_chapter.LocationsAndRegions import CCEntrances
from ..cross_chapter.Items import CCItems

if TYPE_CHECKING:
    from .. import DeltaruneWorld

def set_rules(world: "DeltaruneWorld"): 
  player = world.player
  multiworld = world.multiworld
  
  # Chapter unlock
  if not world.is_all_chapters_unlocked():
    set_rule(multiworld.get_entrance(CCEntrances.chapter_3_entrance,  player), lambda state: state.has(Ch3Items.chapter_3_unlock, player))
    
  # Region lockers
  set_rule(multiworld.get_entrance(Ch3Entrances.board_2_entrance,   player),  lambda state: state.has(Ch3Items.board_2_cartridge, player))
  set_rule(multiworld.get_entrance(Ch3Entrances.tv_world_entrance,   player), lambda state: state.has(Ch3Items.vip_pass, player))
  
  # Macguffin
  if world.is_secret_bosses_mandatory():
    if world.is_final_chapter(3):
      set_rule(multiworld.get_entrance(Ch3Entrances.cold_place_entrance, player), lambda state: state.has(Ch3Items.remote_battery, player, world.options.goal_macguffin_amount)
                                                                                            and can_do_mantle(state, player))
    else:
        set_rule(multiworld.get_entrance(Ch3Entrances.cold_place_entrance, player), lambda state: can_do_mantle(state, player))
  elif world.is_final_chapter(3):
    set_rule(multiworld.get_entrance(Ch3Entrances.cold_place_entrance, player), lambda state: state.has(Ch3Items.remote_battery, player, world.options.goal_macguffin_amount))
  
  # SWORD GAME
  set_rule(multiworld.get_location(Ch3Locations.sword_1_ice_key,   player),         lambda state: state.has(Ch3Items.odd_controller, player))
  set_rule(multiworld.get_location(Ch3Locations.sword_2_shelter_key,   player),     lambda state: state.has(Ch3Items.odd_controller, player) and state.has(Ch3Items.ice_key, player))
  set_rule(multiworld.get_location(Ch3Locations.sword_3_mantle_defeat,   player),   lambda state: can_do_mantle(state, player))
  set_rule(multiworld.get_location(Ch3Locations.s_rank_room_susie_gift,   player),  lambda state: can_do_mantle(state, player))

  # Hidden items
  if not world.is_hidden_items_randomized():
    multiworld.get_location(Ch3Locations.tv_world_man, player).place_locked_item(world.create_item(Ch3Items.egg))
    multiworld.get_location(Ch3Locations.board_2_moss, player).place_locked_item(world.create_item(Ch3Items.board_moss))
    multiworld.get_location(Ch3Locations.s_rank_room_oddcontroller, player).place_locked_item(world.create_item(Ch3Items.odd_controller))
    multiworld.get_location(Ch3Locations.sword_1_ice_key, player).place_locked_item(world.create_item(Ch3Items.ice_key))
    multiworld.get_location(Ch3Locations.sword_2_shelter_key, player).place_locked_item(world.create_item(Ch3Items.shelter_key))
    multiworld.get_location(Ch3Locations.sword_3_mantle_defeat, player).place_locked_item(world.create_item(Ch3Items.shadowmantle))
    multiworld.get_location(Ch3Locations.s_rank_room_susie_gift, player).place_locked_item(world.create_item(Ch3Items.flatsoda))
    # Location not available in weird route to avoid potential soft-lock due to Zapper Lost
    if (not world.is_weird_route()):
      multiworld.get_location(Ch3Locations.tv_world_tripticket, player).place_locked_item(world.create_item(Ch3Items.tripticket))


def can_do_mantle(state: CollectionState, player: int):
  return state.has(Ch3Items.odd_controller, player) and state.has(Ch3Items.ice_key, player) and state.has(Ch3Items.shelter_key, player)