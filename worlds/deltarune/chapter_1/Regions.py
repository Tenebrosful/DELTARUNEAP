from BaseClasses import MultiWorld
from enum import StrEnum

class Regions(StrEnum):  
  chapter_1       = "Chapter 1"
  light_world     = "CH1: Light World"
  castle_town     = "CH1: Castle Town"
  fields          = "CH1: Fields"
  forest          = "CH1: Forest"
  bake_sale       = "CH1: Bake Sale"
  card_castle     = "CH1: Card Castle"
  warp_hub        = "CH1: Warp Hub"
  
class Entrance(StrEnum):
  castle_town_entrance    = "CH1: Castle Town Entrance"
  fields_entrance         = "CH1: Fields Entrance"
  forest_entrance         = "CH1: Forest Entrance"
  bake_sale_entrance      = "CH1: Bake Sale Entrance"
  card_castle_entrance    = "CH1: Card Castle Entrance"
  light_world_entrance    = "CH1: Light World Entrance"
  
chapter1_regions = [
  (Regions.chapter_1,       [Entrance.castle_town_entrance]),
  (Regions.castle_town,     [Entrance.fields_entrance]),
  (Regions.fields,          [Entrance.forest_entrance, Entrance.fields_warp]),
  (Regions.forest,          [Entrance.bake_sale_entrance, Entrance.forest_warp]),
  (Regions.bake_sale,       [Entrance.card_castle_entrance, Entrance.bake_sale_warp]),
  (Regions.card_castle,     [Entrance.light_world_entrance, Entrance.card_castle_warp]),
  (Regions.warp_hub,        [Entrance.fields_warp, Entrance.forest_warp, Entrance.bake_sale_warp, Entrance.card_castle_warp]),
  (Regions.light_world,     []),
]

chapter1_mandatory_connections = [
  (Entrance.castle_town_entrance, Regions.castle_town),
  (Entrance.fields_entrance,      Regions.fields),
  (Entrance.forest_entrance,      Regions.forest),
  (Entrance.bake_sale_entrance,   Regions.bake_sale),
  (Entrance.card_castle_entrance, Regions.card_castle),
  (Entrance.light_world_entrance, Regions.light_world),
  (Entrance.fields_warp,          Regions.warp_hub),
  (Entrance.forest_warp,          Regions.warp_hub),
  (Entrance.bake_sale_warp,       Regions.warp_hub),
  (Entrance.card_castle_warp,     Regions.warp_hub),
]