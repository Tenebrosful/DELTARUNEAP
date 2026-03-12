from enum import StrEnum
from .. import DeltaruneWorld
from ..Regions import link_deltarune_areas, DeltaruneRegion, generic_create_regions
from .Locations import chapter1_locations, chapter1_conditional_locations

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
  chapter1_entrance       = "Chapter 1 Entrance"
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
  
chapter1_regions = [
  (Ch1Regions.chapter_1,       [Ch1Entrances.castle_town_entrance]),
  (Ch1Regions.castle_town,     [Ch1Entrances.fields_entrance]),
  (Ch1Regions.fields,          [Ch1Entrances.forest_entrance, Ch1Entrances.fields_warp]),
  (Ch1Regions.forest,          [Ch1Entrances.bake_sale_entrance, Ch1Entrances.forest_warp]),
  (Ch1Regions.bake_sale,       [Ch1Entrances.card_castle_entrance, Ch1Entrances.bake_sale_warp]),
  (Ch1Regions.card_castle,     [Ch1Entrances.light_world_entrance, Ch1Entrances.card_castle_warp]),
  (Ch1Regions.warp_hub,        [Ch1Entrances.fields_warp, Ch1Entrances.forest_warp, Ch1Entrances.bake_sale_warp, Ch1Entrances.card_castle_warp]),
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

def create_regions(world: DeltaruneWorld):
  generic_create_regions(world, chapter1_regions, chapter1_locations, chapter1_conditional_locations, chapter1_mandatory_connections)