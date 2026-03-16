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
  heartsdonut = "HeartsDonut"
  chocdiamond = "ChocDiamond"
  rouxlsroux = "RouxlsRoux"
  
  # Armors
  dice_brace = "Dice Bracelet"
  ironshackle = "IronShackle"
  jevilstail = "JevilsTail"
  devilsknife = "Devilsknife"
  
  # Weapons
  spokysword = "Spookysword"
  brave_ax = "Brave Ax"
  ragger = "Ragger"
  daintyscarf = "DaintyScarf"
  
  egg = "CH1 Egg"
  castle_moss = "Castle Moss"
  
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
  Ch1Items.heartsdonut.value:    ItemData(ItemIDs.heartsdonut.value,   ItemClassification.filler),
  Ch1Items.chocdiamond.value:    ItemData(ItemIDs.chocdiamond.value,   ItemClassification.filler),
  Ch1Items.rouxlsroux.value:     ItemData(ItemIDs.rouxlsroux.value,    ItemClassification.filler),
  CCItems.amber_card.value:      ItemData(ItemIDs.amber_card.value,    ItemClassification.filler),
  
  CCItems.clubsSandwich.value:    ItemData(ItemIDs.clubsandwich.value,    ItemClassification.useful),
  CCItems.dark_dollars_40.value:  ItemData(ItemIDs.dark_dollars_40.value, ItemClassification.useful),
  Ch1Items.dice_brace.value:      ItemData(ItemIDs.dice_brace.value,      ItemClassification.useful),
  CCItems.spincake.value:         ItemData(ItemIDs.spincake.value,        ItemClassification.useful),
  Ch1Items.spokysword.value:      ItemData(ItemIDs.spookysword.value,     ItemClassification.useful),
  Ch1Items.brave_ax.value:        ItemData(ItemIDs.brave_ax.value,        ItemClassification.useful),
  Ch1Items.ragger.value:          ItemData(ItemIDs.ragger.value,          ItemClassification.useful),
  Ch1Items.daintyscarf.value:     ItemData(ItemIDs.daintyscarf.value,     ItemClassification.useful),

  CCItems.revive_mint.value:      ItemData(ItemIDs.revivemint.value,      ItemClassification.useful, 2),
  
  
  
  Ch1Items.manual.value:          ItemData(ItemIDs.manual.value,        ItemClassification.useful),
  "[P]" + Ch1Items.manual.value:  ItemData(ItemIDs.manual.value,        ItemClassification.progression),
  
  # Blockers
  Ch1Items.bake_sale_ticket.value: ItemData(ItemIDs.bake_sale_ticket.value,  ItemClassification.progression),
  Ch1Items.castle_key.value:       ItemData(ItemIDs.castle_key.value,        ItemClassification.progression),
  
  Ch1Items.brokencake.value:     ItemData(ItemIDs.brokencake.value,    ItemClassification.progression),
  Ch1Items.top_cake.value:       ItemData(ItemIDs.top_cake.value,      ItemClassification.progression),
  CCItems.glowshard.value:       ItemData(ItemIDs.glowshard.value,     ItemClassification.progression),
  Ch1Items.ironshackle.value:    ItemData(ItemIDs.ironshackle.value,   ItemClassification.progression),
    
  CCItems.white_ribbon.value: ItemData(ItemIDs.white_ribbon.value, ItemClassification.progression),
}

chapter1_conditional_items = {
  # Hidden Items
  Ch1Items.egg.value:             ConditionalItemData(ItemIDs.chapter_1_egg.value,     ItemClassification.useful, lambda world: world.is_hidden_items_randomized()),
  Ch1Items.castle_moss.value:     ConditionalItemData(ItemIDs.castle_moss.value,       ItemClassification.useful, lambda world: world.is_hidden_items_randomized()),
  
  Ch1Items.broken_key_a.value:   ConditionalItemData(ItemIDs.broken_key_a.value,  ItemClassification.progression, lambda world: world.is_hidden_items_randomized()),
  Ch1Items.broken_key_b.value:   ConditionalItemData(ItemIDs.broken_key_b.value,  ItemClassification.progression, lambda world: world.is_hidden_items_randomized()),
  Ch1Items.broken_key_c.value:   ConditionalItemData(ItemIDs.broken_key_c.value,  ItemClassification.progression, lambda world: world.is_hidden_items_randomized()),
  Ch1Items.door_key.value:       ConditionalItemData(ItemIDs.door_key.value,      ItemClassification.progression, lambda world: world.is_hidden_items_randomized()),
  
  # Secret boss
  Ch1Items.jevilstail.value:        ConditionalItemData(ItemIDs.jevilstail.value,       ItemClassification.useful, lambda world: world.is_secret_bosses_randomized()),
  Ch1Items.devilsknife.value:       ConditionalItemData(ItemIDs.devilsknife.value,      ItemClassification.useful, lambda world: world.is_secret_bosses_randomized()),
  CCItems.shadowcrystal.value:      ConditionalItemData(ItemIDs.shadowcrystal.value,    ItemClassification.useful, lambda world: world.is_secret_bosses_randomized()),
  
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