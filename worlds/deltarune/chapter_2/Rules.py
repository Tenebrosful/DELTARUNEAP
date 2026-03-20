from worlds.generic.Rules import set_rule
from typing import TYPE_CHECKING
from ..Options import RandomizeChapterOptions, RandomizeSecretBossesOptions
from .LocationsAndRegions import Ch2Entrances, Ch2Regions, Ch2Locations
from .Items import Ch2Items
from ..cross_chapter.LocationsAndRegions import CCEntrances
from ..cross_chapter.Items import CCItems

if TYPE_CHECKING:
    from .. import DeltaruneWorld

def set_rules(world: "DeltaruneWorld"): 
  player = world.player
  multiworld = world.multiworld
  
  # Chapter unlock
  if not world.is_all_chapters_unlocked():
    set_rule(multiworld.get_entrance(CCEntrances.chapter_2_entrance,  player), lambda state: state.has(Ch2Items.chapter_2_unlock, player))

  if world.is_all_routes():
    set_all_routes_rules(world)
  elif world.is_weird_route():
    set_weird_route_rules(world)
  elif world.is_all_recruits():
    set_all_recruits_rules(world)
    
  if world.is_all_recruits():
    set_rule(multiworld.get_entrance(Ch2Entrances.mansion_entrance, player), lambda state: state.has(Ch2Items.mansion_reservation, player))
    set_rule(multiworld.get_location(Ch2Locations.mansion_basement_chest, player), lambda state: state.has(Ch2Items.keygen, player))
    set_rule(multiworld.get_location(Ch2Locations.mansion_basement_mechanism, player), lambda state: state.has(Ch2Items.keygen, player))
    
  # Region lockers
  set_rule(multiworld.get_entrance(Ch2Entrances.cyber_city_entrance,   player), lambda state: state.has(Ch2Items.safety_vest, player))
  # Mansion have special logic, need either thornring or mansion reservation depending of the route
  
  # set_rule(multiworld.get_entrance(Ch2Entrances.cyber_field_entrance,          player), lambda state: state.has(Ch2Items.cyber_field_warp, player))
  # set_rule(multiworld.get_entrance(Ch2Entrances.cyber_city_entrance,          player), lambda state: state.has(Ch2Items.trash_zone_warp, player))
  # set_rule(multiworld.get_entrance(Ch2Entrances.mansion_entrance,       player), lambda state: state.has(Ch2Items.mansion_warp, player))
  
  if not world.is_secret_bosses_randomized():
    multiworld.get_location(Ch2Locations.mansion_spamton_neo_defeat_item_1, player).place_locked_item(world.create_item(Ch2Items.puppetscarf))
    multiworld.get_location(Ch2Locations.mansion_spamton_neo_defeat_item_2, player).place_locked_item(world.create_item(CCItems.shadowcrystal))
    if (not world.is_weird_route() or world.is_all_routes()):
      multiworld.get_location(Ch2Locations.mansion_spamton_neo_defeat_item_3, player).place_locked_item(world.create_item(Ch2Items.dealmaker))
  
  # if not world.is_warps_randomized():
  if True:
        multiworld.get_location(Ch2Locations.cyber_field_warp_door, player).place_locked_item(world.create_item(Ch2Items.cyber_field_warp))
        multiworld.get_location(Ch2Locations.trash_zone_warp_door, player).place_locked_item(world.create_item(Ch2Items.trash_zone_warp))
        multiworld.get_location(Ch2Locations.mansion_warp_door, player).place_locked_item(world.create_item(Ch2Items.mansion_warp))
  
  # Hidden items
  if not world.is_hidden_items_randomized():
    if (not world.is_weird_route() or world.is_all_routes()):
      multiworld.get_location(Ch2Locations.spamton_shop_1, player).place_locked_item(world.create_item(Ch2Items.keygen))
      multiworld.get_location(Ch2Locations.mansion_basement_mechanism, player).place_locked_item(world.create_item(Ch2Items.emptydisk))
      multiworld.get_location(Ch2Locations.cyber_city_man, player).place_locked_item(world.create_item(Ch2Items.egg))
      multiworld.get_location(Ch2Locations.cyber_city_moss, player).place_locked_item(world.create_item(Ch2Items.city_moss))
      multiworld.get_location(Ch2Locations.cyber_city_annoying_dog, player).place_locked_item(world.create_item(CCItems.dogdollard))
      
  
def set_weird_route_rules(world: "DeltaruneWorld"):
  player = world.player
  multiworld = world.multiworld
  
  set_rule(multiworld.get_entrance(Ch2Entrances.mansion_entrance, player), lambda state: state.has(Ch2Items.thornring, player))
  
  if world.is_final_chapter(2):
    set_rule(multiworld.get_entrance(Ch2Entrances.post_chapter_castle_town_entrance, player), lambda state: 
                                                                                        state.has(Ch2Items.keygen_2_segment, player, world.options.goal_macguffin_amount.value)
                                                                                    and state.has(Ch2Items.thornring, player))
    set_rule(multiworld.get_location(Ch2Locations.mansion_spamton_neo_defeat_item_1, player), lambda state: 
                                                                                        state.has(Ch2Items.keygen_2_segment, player, world.options.goal_macguffin_amount.value)
                                                                                    and state.has(Ch2Items.thornring, player))
    set_rule(multiworld.get_location(Ch2Locations.mansion_spamton_neo_defeat_item_2, player), lambda state: 
                                                                                        state.has(Ch2Items.keygen_2_segment, player, world.options.goal_macguffin_amount.value)
                                                                                    and state.has(Ch2Items.thornring, player))
  else:
    set_rule(multiworld.get_entrance(Ch2Entrances.post_chapter_castle_town_entrance, player), lambda state: state.has(Ch2Items.thornring, player))
    set_rule(multiworld.get_location(Ch2Locations.mansion_spamton_neo_defeat_item_1, player), lambda state: state.has(Ch2Items.thornring, player))
    set_rule(multiworld.get_location(Ch2Locations.mansion_spamton_neo_defeat_item_2, player), lambda state: state.has(Ch2Items.thornring, player))
      
def set_all_recruits_rules(world: "DeltaruneWorld"):
  player = world.player
  multiworld = world.multiworld
  
  set_rule(multiworld.get_location(Ch2Locations.mansion_spamton_neo_defeat_item_1, player), lambda state: state.has(Ch2Items.emptydisk, player) and state.has(Ch2Items.keygen, player))
  set_rule(multiworld.get_location(Ch2Locations.mansion_spamton_neo_defeat_item_2, player), lambda state: state.has(Ch2Items.emptydisk, player) and state.has(Ch2Items.keygen, player))
  set_rule(multiworld.get_location(Ch2Locations.mansion_spamton_neo_defeat_item_3, player), lambda state: state.has(Ch2Items.emptydisk, player) and state.has(Ch2Items.keygen, player))
  
  if world.is_secret_bosses_mandatory():
    if world.is_final_chapter(2):
      set_rule(multiworld.get_entrance(Ch2Entrances.post_chapter_castle_town_entrance, player), lambda state: 
                                                                                          state.has(Ch2Items.keygen_2_segment, player, world.options.goal_macguffin_amount.value)
                                                                                      and state.has(Ch2Items.emptydisk, player)
                                                                                      and state.has(Ch2Items.keygen, player))
    else:
      set_rule(multiworld.get_entrance(Ch2Entrances.post_chapter_castle_town_entrance, player), lambda state: state.has(Ch2Items.emptydisk, player) and state.has(Ch2Items.keygen, player))
  elif world.is_final_chapter(2):
    set_rule(multiworld.get_entrance(Ch2Entrances.post_chapter_castle_town_entrance, player), lambda state: state.has(Ch2Items.keygen_2_segment, player, world.options.goal_macguffin_amount.value))

def set_all_routes_rules(world: "DeltaruneWorld"):
  player = world.player
  multiworld = world.multiworld
  
  set_rule(multiworld.get_entrance(Ch2Entrances.mansion_entrance, player), lambda state: state.has(Ch2Items.mansion_reservation, player) or state.has(Ch2Items.thornring, player))
  
  if world.is_final_chapter(2):
    set_rule(multiworld.get_location(Ch2Locations.mansion_spamton_neo_defeat_item_1, player), lambda state: state.has(Ch2Items.keygen_2_segment, player, world.options.goal_macguffin_amount.value) 
                                                                                                        and (state.has(Ch2Items.thornring, player)
                                                                                                              or (state.has(Ch2Items.emptydisk, player) and state.has(Ch2Items.keygen, player))
                                                                                                            ))
    set_rule(multiworld.get_location(Ch2Locations.mansion_spamton_neo_defeat_item_2, player), lambda state: state.has(Ch2Items.keygen_2_segment, player, world.options.goal_macguffin_amount.value) 
                                                                                                        and (state.has(Ch2Items.thornring, player)
                                                                                                              or (state.has(Ch2Items.emptydisk, player) and state.has(Ch2Items.keygen, player))
                                                                                                            ))
    set_rule(multiworld.get_location(Ch2Locations.mansion_spamton_neo_defeat_item_3, player), lambda state: lambda state: state.has(Ch2Items.keygen_2_segment, player, world.options.goal_macguffin_amount.value) 
                                                                                                        and (state.has(Ch2Items.thornring, player)
                                                                                                              or (state.has(Ch2Items.emptydisk, player) and state.has(Ch2Items.keygen, player))
                                                                                                            ))
  else:
    set_rule(multiworld.get_location(Ch2Locations.mansion_spamton_neo_defeat_item_1, player), lambda state: state.has(Ch2Items.thornring, player) or (state.has(Ch2Items.emptydisk, player) and state.has(Ch2Items.keygen, player)))
    set_rule(multiworld.get_location(Ch2Locations.mansion_spamton_neo_defeat_item_2, player), lambda state: state.has(Ch2Items.thornring, player) or (state.has(Ch2Items.emptydisk, player) and state.has(Ch2Items.keygen, player)))
    set_rule(multiworld.get_location(Ch2Locations.mansion_spamton_neo_defeat_item_3, player), lambda state: state.has(Ch2Items.thornring, player) or (state.has(Ch2Items.emptydisk, player) and state.has(Ch2Items.keygen, player)))
  
  if world.is_secret_bosses_mandatory():
    if world.is_final_chapter(2):
      set_rule(multiworld.get_entrance(Ch2Entrances.post_chapter_castle_town_entrance, player), lambda state: 
                                                                                          state.has(Ch2Items.keygen_2_segment, player, world.options.goal_macguffin_amount.value)
                                                                                      and (state.has(Ch2Items.thornring, player) or (state.has(Ch2Items.emptydisk, player) and state.has(Ch2Items.keygen, player))))
    else:
      set_rule(multiworld.get_entrance(Ch2Entrances.post_chapter_castle_town_entrance, player), lambda state: state.has(Ch2Items.thornring, player) or (state.has(Ch2Items.emptydisk, player) and state.has(Ch2Items.keygen, player)))
  elif world.is_final_chapter(2):
    set_rule(multiworld.get_entrance(Ch2Entrances.post_chapter_castle_town_entrance, player), lambda state: state.has(Ch2Items.keygen_2_segment, player, world.options.goal_macguffin_amount.value))