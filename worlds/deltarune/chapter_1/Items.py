from ..Items import ItemIDs, ItemData, ConditionalItemData
from ..cross_chapter import Items as CrossChapterItems
from BaseClasses import ItemClassification
from enum import StrEnum

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
  Ch1Items.dark_candy:     ItemData(ItemIDs.dark_candy,    ItemClassification.filler),
  Ch1Items.clubsSandwich:  ItemData(ItemIDs.clubsandwich,  ItemClassification.filler),
  Ch1Items.heartsdonut:    ItemData(ItemIDs.heartsdonut,   ItemClassification.filler),
  Ch1Items.chocdiamond:    ItemData(ItemIDs.chocdiamond,   ItemClassification.filler),
  Ch1Items.rouxlsroux:     ItemData(ItemIDs.rouxlsroux,    ItemClassification.filler),
  
  Ch1Items.dice_brace:     ItemData(ItemIDs.dice_brace,    ItemClassification.useful),
  Ch1Items.jevilstail:     ItemData(ItemIDs.jevilstail,    ItemClassification.useful),
  Ch1Items.devilsknife:    ItemData(ItemIDs.devilsknife,   ItemClassification.useful),
  # After throw away
  Ch1Items.manual:         ItemData(ItemIDs.manual,        ItemClassification.useful),
  
  Ch1Items.egg:            ItemData(ItemIDs.chapter_1_egg,     ItemClassification.useful),
  Ch1Items.castle_moss:    ItemData(ItemIDs.joe_life_savings,  ItemClassification.useful),
  
  # Before throw away
  Ch1Items.manual:         ItemData(ItemIDs.manual,        ItemClassification.progression),
  Ch1Items.brokencake:     ItemData(ItemIDs.brokencake,    ItemClassification.progression),
  Ch1Items.top_cake:       ItemData(ItemIDs.top_cake,      ItemClassification.progression),
  Ch1Items.ironshackle:    ItemData(ItemIDs.ironshackle,   ItemClassification.progression),
  
  Ch1Items.broken_key_a:   ItemData(ItemIDs.broken_key_a,  ItemClassification.progression),
  Ch1Items.broken_key_b:   ItemData(ItemIDs.broken_key_b,  ItemClassification.progression),
  Ch1Items.broken_key_c:   ItemData(ItemIDs.broken_key_c,  ItemClassification.progression),
  Ch1Items.door_key:       ItemData(ItemIDs.door_key,      ItemClassification.progression),
  
  Ch1Items.bake_sale_ticket: ItemData(ItemIDs.bake_sale_ticket,  ItemClassification.progression),
  Ch1Items.castle_key:       ItemData(ItemIDs.castle_key,        ItemClassification.progression),
  
  CrossChapterItems.CCItems.white_ribbon: ItemData(ItemIDs.white_ribbon, ItemClassification.progression),
}

chapter1_conditional_items = {
  Ch1Items.chapter_1_unlock:     ConditionalItemData(ItemIDs.chapter_1_unlock,     ItemClassification.progression, lambda world: not world.is_all_chapters_unlocked()),
  Ch1Items.king_shape_key_piece: ConditionalItemData(ItemIDs.king_shape_key_piece, ItemClassification.progression, lambda world: world.is_final_chapter(1))
}