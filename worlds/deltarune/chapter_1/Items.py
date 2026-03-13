from ..Items import ItemIDs, ItemData, ConditionalItemData, generic_create_items, generic_get_filler_items, DeltaruneItem
from ..cross_chapter.Items import CCItems
from typing import TYPE_CHECKING
from BaseClasses import ItemClassification
from enum import StrEnum

if TYPE_CHECKING:
    from . import DeltaruneWorld

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
  Ch1Items.dark_candy:     ItemData(ItemIDs.dark_candy.value,    ItemClassification.filler),
  CCItems.dark_burger:     ItemData(ItemIDs.darkburger.value,    ItemClassification.filler),
  Ch1Items.clubsSandwich:  ItemData(ItemIDs.clubsandwich.value,  ItemClassification.filler),
  Ch1Items.heartsdonut:    ItemData(ItemIDs.heartsdonut.value,   ItemClassification.filler),
  Ch1Items.chocdiamond:    ItemData(ItemIDs.chocdiamond.value,   ItemClassification.filler),
  Ch1Items.rouxlsroux:     ItemData(ItemIDs.rouxlsroux.value,    ItemClassification.filler),
  
  CCItems.dark_dollars_40:  ItemData(ItemIDs.dark_dollars_40.value, ItemClassification.useful),
  Ch1Items.dice_brace:      ItemData(ItemIDs.dice_brace.value,      ItemClassification.useful),
  Ch1Items.jevilstail:      ItemData(ItemIDs.jevilstail.value,      ItemClassification.useful),
  Ch1Items.devilsknife:     ItemData(ItemIDs.devilsknife.value,     ItemClassification.useful),
  CCItems.spincake:         ItemData(ItemIDs.spincake.value,        ItemClassification.useful),
  CCItems.spokysword:       ItemData(ItemIDs.spookysword.value,     ItemClassification.useful),
  Ch1Items.brave_ax:        ItemData(ItemIDs.brave_ax.value,        ItemClassification.useful),
  
  # ReviveMint x2
  CCItems.revive_mint:     ItemData(ItemIDs.revivemint.value,    ItemClassification.useful, 2),
  
  Ch1Items.manual:         ItemData(ItemIDs.manual.value,        ItemClassification.progression, 2),
  
  Ch1Items.egg:            ItemData(ItemIDs.chapter_1_egg.value,     ItemClassification.useful),
  Ch1Items.castle_moss:    ItemData(ItemIDs.joe_life_savings.value,  ItemClassification.useful),
  
  # Blockers
  Ch1Items.bake_sale_ticket: ItemData(ItemIDs.bake_sale_ticket.value,  ItemClassification.progression),
  Ch1Items.castle_key:       ItemData(ItemIDs.castle_key.value,        ItemClassification.progression),
  
  # Warps
  Ch1Items.fields_warp:       ItemData(ItemIDs.fields_warp.value,       ItemClassification.progression),
  Ch1Items.forest_warp:       ItemData(ItemIDs.forest_warp.value,       ItemClassification.progression),
  Ch1Items.bake_sale_warp:    ItemData(ItemIDs.bake_sale_warp.value,    ItemClassification.progression),
  Ch1Items.card_castle_warp:  ItemData(ItemIDs.card_castle_warp.value,  ItemClassification.progression),
  
  Ch1Items.brokencake:     ItemData(ItemIDs.brokencake.value,    ItemClassification.progression),
  Ch1Items.top_cake:       ItemData(ItemIDs.top_cake.value,      ItemClassification.progression),
  CCItems.glowshard:       ItemData(ItemIDs.glowshard.value,     ItemClassification.progression),
  Ch1Items.ironshackle:    ItemData(ItemIDs.ironshackle.value,   ItemClassification.progression),
  
  Ch1Items.broken_key_a:   ItemData(ItemIDs.broken_key_a.value,  ItemClassification.progression),
  Ch1Items.broken_key_b:   ItemData(ItemIDs.broken_key_b.value,  ItemClassification.progression),
  Ch1Items.broken_key_c:   ItemData(ItemIDs.broken_key_c.value,  ItemClassification.progression),
  Ch1Items.door_key:       ItemData(ItemIDs.door_key.value,      ItemClassification.progression),
    
  CCItems.white_ribbon: ItemData(ItemIDs.white_ribbon.value, ItemClassification.progression),
}

chapter1_conditional_items = {
  Ch1Items.chapter_1_unlock:     ConditionalItemData(ItemIDs.chapter_1_unlock.value,     ItemClassification.progression, lambda world: not world.is_all_chapters_unlocked()),
  Ch1Items.king_shape_key_piece: ConditionalItemData(ItemIDs.king_shape_key_piece.value, ItemClassification.progression, lambda world: world.is_final_chapter(1))
}

def create_items(world: "DeltaruneWorld") -> list[DeltaruneItem]:
  return generic_create_items(world, chapter1_items, chapter1_conditional_items)
  
def get_filler_items(world: "DeltaruneWorld"):
  return generic_get_filler_items(world, chapter1_items, chapter1_conditional_items)