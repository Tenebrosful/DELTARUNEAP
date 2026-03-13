from ..Items import ItemIDs, ItemData, ConditionalItemData, generic_create_items, generic_get_filler_items, DeltaruneItem
from ..cross_chapter.Items import CCItems
from typing import TYPE_CHECKING
from BaseClasses import ItemClassification
from enum import StrEnum

if TYPE_CHECKING:
    from .. import DeltaruneWorld

class Ch1Items(StrEnum):
  chapter_1_unlock = "Chapter 1 Unlock"
  
  # Healing Items
  dark_candy = "Dark Candy"
  clubsSandwich = "ClubSandwich"
  heartsdonut = "HeartsDonut"
  chocdiamond = "ChocDiamond"
  rouxlsroux = "RouxlsRoux"
  
  # Armors
  dice_brace = "Dice Bracelet"
  ironshackle = "IronShackle"
  jevilstail = "JevilsTail"
  devilsknife = "Devilsknife"
  
  # Weapons
  brave_ax = "Brave Ax"
  
  egg = "CH1 Egg"
  castle_moss = "Castle Moss"
  joe_life_savings = "Joe's Life Savings"
  
  manual = "Manual"
  
  brokencake = "BrokenCake"
  top_cake = "Top Cake"
  
  broken_key_a = "Broken Key A"
  broken_key_b = "Broken Key B"
  broken_key_c = "Broken Key C"
  
  # Blockers
  # great_door_key = "Great Door Key"
  # king_chess_piece = "King Chess Piece"
  bake_sale_ticket = "Bake Sale Ticket"
  castle_key = "Castle Key"
  door_key = "Door Key"
  
  # Macguffins
  king_shape_key_piece = "King-Shaped Key Piece"
  
  # Warps
  bake_sale_warp = "Bake Sale Warp"
  forest_warp = "Forest Warp"
  fields_warp = "Fields Warp"
  card_castle_warp = "Card Castle Warp"
  
chapter1_items = {
  Ch1Items.dark_candy.value:     ItemData(ItemIDs.dark_candy.value,    ItemClassification.filler),
  CCItems.dark_burger.value:     ItemData(ItemIDs.darkburger.value,    ItemClassification.filler),
  Ch1Items.clubsSandwich.value:  ItemData(ItemIDs.clubsandwich.value,  ItemClassification.filler),
  Ch1Items.heartsdonut.value:    ItemData(ItemIDs.heartsdonut.value,   ItemClassification.filler),
  Ch1Items.chocdiamond.value:    ItemData(ItemIDs.chocdiamond.value,   ItemClassification.filler),
  Ch1Items.rouxlsroux.value:     ItemData(ItemIDs.rouxlsroux.value,    ItemClassification.filler),
  
  CCItems.dark_dollars_40.value:  ItemData(ItemIDs.dark_dollars_40.value, ItemClassification.useful),
  Ch1Items.dice_brace.value:      ItemData(ItemIDs.dice_brace.value,      ItemClassification.useful),
  Ch1Items.jevilstail.value:      ItemData(ItemIDs.jevilstail.value,      ItemClassification.useful),
  Ch1Items.devilsknife.value:     ItemData(ItemIDs.devilsknife.value,     ItemClassification.useful),
  CCItems.spincake.value:         ItemData(ItemIDs.spincake.value,        ItemClassification.useful),
  CCItems.spokysword.value:       ItemData(ItemIDs.spookysword.value,     ItemClassification.useful),
  Ch1Items.brave_ax.value:        ItemData(ItemIDs.brave_ax.value,        ItemClassification.useful),
  
  # ReviveMint x2
  CCItems.revive_mint.value:     ItemData(ItemIDs.revivemint.value,    ItemClassification.useful, 2),
  
  Ch1Items.manual.value:         ItemData(ItemIDs.manual.value,        ItemClassification.progression, 2),
  
  Ch1Items.egg.value:            ItemData(ItemIDs.chapter_1_egg.value,     ItemClassification.useful),
  Ch1Items.castle_moss.value:    ItemData(ItemIDs.joe_life_savings.value,  ItemClassification.useful),
  
  # Blockers
  Ch1Items.bake_sale_ticket.value: ItemData(ItemIDs.bake_sale_ticket.value,  ItemClassification.progression),
  Ch1Items.castle_key.value:       ItemData(ItemIDs.castle_key.value,        ItemClassification.progression),
  
  Ch1Items.brokencake.value:     ItemData(ItemIDs.brokencake.value,    ItemClassification.progression),
  Ch1Items.top_cake.value:       ItemData(ItemIDs.top_cake.value,      ItemClassification.progression),
  CCItems.glowshard.value:       ItemData(ItemIDs.glowshard.value,     ItemClassification.progression),
  Ch1Items.ironshackle.value:    ItemData(ItemIDs.ironshackle.value,   ItemClassification.progression),
  
  Ch1Items.broken_key_a.value:   ItemData(ItemIDs.broken_key_a.value,  ItemClassification.progression),
  Ch1Items.broken_key_b.value:   ItemData(ItemIDs.broken_key_b.value,  ItemClassification.progression),
  Ch1Items.broken_key_c.value:   ItemData(ItemIDs.broken_key_c.value,  ItemClassification.progression),
  Ch1Items.door_key.value:       ItemData(ItemIDs.door_key.value,      ItemClassification.progression),
    
  CCItems.white_ribbon.value: ItemData(ItemIDs.white_ribbon.value, ItemClassification.progression),
}

chapter1_conditional_items = {
  # Warps
  Ch1Items.fields_warp.value:       ConditionalItemData(ItemIDs.fields_warp.value,       ItemClassification.progression, lambda world: world.is_warps_randomized()),
  Ch1Items.forest_warp.value:       ConditionalItemData(ItemIDs.forest_warp.value,       ItemClassification.progression, lambda world: world.is_warps_randomized()),
  Ch1Items.bake_sale_warp.value:    ConditionalItemData(ItemIDs.bake_sale_warp.value,    ItemClassification.progression, lambda world: world.is_warps_randomized()),
  Ch1Items.card_castle_warp.value:  ConditionalItemData(ItemIDs.card_castle_warp.value,  ItemClassification.progression, lambda world: world.is_warps_randomized()),
  
  Ch1Items.chapter_1_unlock.value:     ConditionalItemData(ItemIDs.chapter_1_unlock.value,     ItemClassification.progression, lambda world: not world.is_all_chapters_unlocked()),
  Ch1Items.king_shape_key_piece.value: ConditionalItemData(ItemIDs.king_shape_key_piece.value, ItemClassification.progression, lambda world: world.is_final_chapter(1))
}

def create_items(world: "DeltaruneWorld") -> list[DeltaruneItem]:
  return generic_create_items(world, chapter1_items, chapter1_conditional_items)
  
def get_filler_items(world: "DeltaruneWorld"):
  return generic_get_filler_items(world, chapter1_items, chapter1_conditional_items)