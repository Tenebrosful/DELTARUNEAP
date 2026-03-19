from worlds.generic.Rules import set_rule
from BaseClasses import CollectionState
from typing import TYPE_CHECKING
from ..Options import RandomizeChapterOptions, RandomizeSecretBossesOptions
from .LocationsAndRegions import Ch4Entrances, Ch4Regions, Ch4Locations
from .Items import Ch4Items
from ..cross_chapter.LocationsAndRegions import CCEntrances
from ..cross_chapter.Items import CCItems

if TYPE_CHECKING: from .. import DeltaruneWorld

def set_rules(world: "DeltaruneWorld"): 
  player = world.player
  multiworld = world.multiworld
  
  # Chapter unlock
  if not world.is_all_chapters_unlocked():
    set_rule(multiworld.get_entrance(CCEntrances.chapter_4_entrance,  player), lambda state: state.has(Ch4Items.chapter_4_unlock, player))
    
  # Region lockers
  set_rule(multiworld.get_entrance(Ch4Entrances.dark_sanctuary_claimbclaws_entrance, player),   lambda state: state.has(Ch4Items.claimbclaws, player))
  set_rule(multiworld.get_entrance(Ch4Entrances.second_sanctuary_entrance, player),             lambda state: state.has(Ch4Items.sheetmusic, player))
  
  # Macguffin
  if world.is_final_chapter(4):
    set_rule(multiworld.get_entrance(Ch4Entrances.titan_fight_entrance, player), lambda state: state.has(Ch4Items.combination_lock_digit, player, world.options.goal_macguffin_amount))
  
  if not world.is_secret_bosses_randomized():
    multiworld.get_location(Ch4Locations.dark_sanctuary_hammer_of_justice_defeat_item_1, player).place_locked_item(world.create_item(Ch4Items.justiceaxe))
    multiworld.get_location(Ch4Locations.dark_sanctuary_hammer_of_justice_defeat_item_2, player).place_locked_item(world.create_item(CCItems.shadowcrystal))
  
  # Hidden Items
  if not world.is_hidden_items_randomized():
    multiworld.get_location(Ch4Locations.second_sanctuary_man, player).place_locked_item(world.create_item(Ch4Items.egg))
    multiworld.get_location(Ch4Locations.second_sanctuary_moss, player).place_locked_item(world.create_item(Ch4Items.holy_moss))