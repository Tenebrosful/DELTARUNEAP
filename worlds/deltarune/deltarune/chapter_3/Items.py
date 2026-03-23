from ..Items import ItemIDs, ItemData, ConditionalItemData, generic_create_items, generic_get_filler_items, DeltaruneItem, ItemGroups
from ..cross_chapter.Items import CCItems
from typing import TYPE_CHECKING
from BaseClasses import ItemClassification
from enum import StrEnum

if TYPE_CHECKING: from .. import DeltaruneWorld
    
class Ch3Items(StrEnum):
    chapter_3_unlock = "Chapter 3 Unlock"
  
    point_1 = "1 POINT"
    points_2 = "2 POINTs"
    points_10 = "10 POINTs"
    points_50 = "50 POINTs"
    points_120 = "120 POINTs"
    points_300 = "300 POINTs"
    points_500 = "500 POINTs"
    
    board_moss = "Board Moss"
    egg = "CH3 Egg"
    smile = "SMILE"
    
    # Heal
    tvslop = "TVSlop"
    tvdinner = "TVDinner"
    deluxedinner = "DeluxeDinner"
    flatsoda = "FlatSoda"
    tensionmax = "TensionMax"
        
    # Weapons
    saber10 = "Saber10"
    toxicaxe = "ToxicAxe"
    flexscarf = "FlexScarf"
    blackshard = "BlackShard"
    
    # Armor
    shadowmantle = "ShadowMantle"
    lodestone = "LodeStone"
    gingerguard = "GingerGuard"
    blue_ribbon = "Blue Ribbon"
    tennatie = "TennaTie"
    
    # Warps
    tv_world_entrace_warp = "TV World Entrance Warp"
    goulden_sam_warp = "Goulden Sam Warp"
    
    # Blockers
    board_2_cartridge = "Board 2 Cartridge"
    vip_pass = "VIP Pass"
    
    # SWORD GAME
    odd_controller = "Odd Controller"
    ice_key = "ICE KEY"
    shelter_key = "SHELTER KEY"
    
    tripticket = "TripTicket"
    
    remote_battery = "Remote Battery"
    
chapter3_macguffin_item = Ch3Items.remote_battery.value

chapter3_items = {
    Ch3Items.point_1.value:     ItemData(ItemIDs.point_1.value,     ItemClassification.filler, [ItemGroups.currencies]),
    Ch3Items.points_2.value:    ItemData(ItemIDs.points_2.value,    ItemClassification.filler, [ItemGroups.currencies]),
    Ch3Items.points_10.value:   ItemData(ItemIDs.points_10.value,   ItemClassification.filler, [ItemGroups.currencies], 5),
    Ch3Items.points_50.value:   ItemData(ItemIDs.points_50.value,   ItemClassification.filler, [ItemGroups.currencies]),
    Ch3Items.points_120.value:  ItemData(ItemIDs.points_120.value,  ItemClassification.filler, [ItemGroups.currencies]),
    Ch3Items.points_300.value:  ItemData(ItemIDs.points_300.value,  ItemClassification.useful, [ItemGroups.currencies]),
    Ch3Items.points_500.value:  ItemData(ItemIDs.points_500.value,  ItemClassification.useful, [ItemGroups.currencies]),
    
    Ch3Items.smile.value:       ItemData(ItemIDs.smile.value,       ItemClassification.useful),
    Ch3Items.lodestone.value:   ItemData(ItemIDs.lodestone.value,   ItemClassification.filler, [ItemGroups.armors]),
    Ch3Items.gingerguard.value: ItemData(ItemIDs.gingerguard.value, ItemClassification.filler, [ItemGroups.armors]),
    
    CCItems.tensiongem.value:   ItemData(ItemIDs.tensiongem.value,  ItemClassification.useful, [ItemGroups.tension_items]),
    
    Ch3Items.toxicaxe.value:    ItemData(ItemIDs.toxicaxe.value,    ItemClassification.useful, [ItemGroups.weapons]),
    Ch3Items.saber10.value:     ItemData(ItemIDs.saber10.value,     ItemClassification.useful, [ItemGroups.weapons]),
    Ch3Items.flexscarf.value:   ItemData(ItemIDs.flexscarf.value,   ItemClassification.useful, [ItemGroups.weapons]),
    
    CCItems.revivemint.value:  ItemData(ItemIDs.revivemint.value,  ItemClassification.useful, [ItemGroups.healing_item], 2),
    
    CCItems.execbuffet.value:   ItemData(ItemIDs.execbuffet.value,  ItemClassification.useful, [ItemGroups.healing_item]),

    CCItems.white_ribbon.value: ItemData(ItemIDs.white_ribbon.value,    ItemClassification.progression, [ItemGroups.armors, ItemGroups.fusion_ingredient]),
    CCItems.pink_ribbon.value:  ItemData(ItemIDs.pink_ribbon.value,     ItemClassification.progression, [ItemGroups.armors, ItemGroups.fusion_ingredient]),
    
    Ch3Items.board_2_cartridge.value:   ItemData(ItemIDs.board_2_cartridge.value, ItemClassification.progression, [ItemGroups.region_blockers]),
    Ch3Items.vip_pass.value:            ItemData(ItemIDs.vip_pass.value, ItemClassification.progression, [ItemGroups.region_blockers]),
}

chapter3_conditional_items = {
    # Ball Machine
    CCItems.execbuffet.value:       ConditionalItemData(ItemIDs.execbuffet.value,   ItemClassification.useful, lambda world: world.is_hidden_items_randomized(), [ItemGroups.healing_item]),
    Ch3Items.tennatie.value:        ConditionalItemData(ItemIDs.tennatie.value,     ItemClassification.useful, lambda world: world.is_hidden_items_randomized(), [ItemGroups.armors]),
    Ch3Items.tensionmax.value:      ConditionalItemData(ItemIDs.tensionmax.value,   ItemClassification.useful, lambda world: world.is_hidden_items_randomized(), [ItemGroups.tension_items]),
    Ch3Items.blue_ribbon.value:     ConditionalItemData(ItemIDs.blue_ribbon.value,  ItemClassification.useful, lambda world: world.is_hidden_items_randomized(), [ItemGroups.armors]),
    CCItems.revivemint.value:       ConditionalItemData(ItemIDs.revivemint.value,    ItemClassification.useful, lambda world: world.is_hidden_items_randomized(), [ItemGroups.healing_item]),
    CCItems.dogdollard.value:       ConditionalItemData(ItemIDs.dogdollar.value,    ItemClassification.useful, lambda world: world.is_hidden_items_randomized(), [ItemGroups.currencies]),
    
    Ch3Items.shadowmantle.value:    ConditionalItemData(ItemIDs.shadowmantle.value, ItemClassification.progression, lambda world: world.is_shadow_mantle_included() and (world.is_mantle_randomized() or world.is_mantleless()), [ItemGroups.armors]),

    Ch3Items.flatsoda.value:        ConditionalItemData(ItemIDs.flatsoda.value,     ItemClassification.useful, lambda world: world.is_mantle_randomized() or world.is_mantleless(), [ItemGroups.healing_item]),
    Ch3Items.blackshard.value:      ConditionalItemData(ItemIDs.blackshard.value,   ItemClassification.useful, lambda world: world.is_secret_bosses_randomized(), [ItemGroups.armors]),
    CCItems.shadowcrystal.value:    ConditionalItemData(ItemIDs.shadowcrystal.value,ItemClassification.useful, lambda world: world.is_secret_bosses_randomized()),
    
    Ch3Items.egg.value:             ConditionalItemData(ItemIDs.chapter_3_egg.value,   ItemClassification.useful, lambda world: world.is_hidden_items_randomized(), [ItemGroups.eggs]),
    Ch3Items.board_moss.value:      ConditionalItemData(ItemIDs.board_moss.value,      ItemClassification.useful, lambda world: world.is_hidden_items_randomized() and ((not world.is_weird_route()) or world.is_all_routes()), [ItemGroups.moss]),
    
    Ch3Items.chapter_3_unlock.value:  ConditionalItemData(ItemIDs.chapter_3_unlock.value, ItemClassification.progression, lambda world: world.is_chapters_randomized(), [ItemGroups.region_blockers]),
    # Amount is handle in __init__.py handle_macguffins_items()
    Ch3Items.remote_battery.value:    ConditionalItemData(ItemIDs.remote_battery.value, ItemClassification.progression, lambda world: world.is_final_chapter(3), [ItemGroups.region_blockers], 0),
    
    Ch3Items.odd_controller.value:  ConditionalItemData(ItemIDs.oddcontroller.value,   ItemClassification.progression, lambda world: world.is_mantle_randomized() or world.is_mantleless(), [ItemGroups.mantle_items]),
    Ch3Items.ice_key.value:         ConditionalItemData(ItemIDs.ice_key.value,         ItemClassification.progression, lambda world: world.is_mantle_randomized() or world.is_mantleless(), [ItemGroups.mantle_items]),
    Ch3Items.shelter_key.value:     ConditionalItemData(ItemIDs.shelter_key.value,     ItemClassification.progression, lambda world: world.is_mantle_randomized() or world.is_mantleless(), [ItemGroups.mantle_items]),
    Ch3Items.tripticket.value:      ConditionalItemData(ItemIDs.tripticket.value,      ItemClassification.progression, lambda world: world.is_hidden_items_randomized() and ((not world.is_weird_route()) or world.is_all_routes())),
}

def create_items(world: "DeltaruneWorld") -> list[DeltaruneItem]:
  return generic_create_items(world, chapter3_items, chapter3_conditional_items)
  
def get_filler_items(world: "DeltaruneWorld"):
  return generic_get_filler_items(world, chapter3_items, chapter3_conditional_items)