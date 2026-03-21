from ..Items import ItemIDs, ItemData, ConditionalItemData, generic_create_items, generic_get_filler_items, DeltaruneItem
from ..cross_chapter.Items import CCItems
from typing import TYPE_CHECKING
from BaseClasses import ItemClassification
from enum import StrEnum

if TYPE_CHECKING: from .. import DeltaruneWorld

class Ch4Items(StrEnum):
  chapter_4_unlock = "Chapter 4 Unlock"
  
  egg = "CH4 Egg"
  holy_moss = "Sacred Moss"
  
  # Healing
  rhapsotea = "Rhapsotea"
  scarlixir = "Scarlixir"
    
  # Armors
  mysticband = "MysticBand"
  powerband = "PowerBand"
  princessrbn = "PrincessRBN"
  
  # Weapons
  scarfmark = "ScarfMark"
  absobax = "AbsorbAx"
  wingblade = "Wingblade"
  justiceaxe = "JusticeAxe"
  
  # Macguffin
  combination_lock_digit = "Combination Lock Digit"
  
  claimbclaws = "ClaimbClaws"
  sheetmusic = "SheetMusic"
  
chapter4_macguffin_item = Ch4Items.combination_lock_digit.value
  
chapter4_items = {
  Ch4Items.rhapsotea.value:  ItemData(ItemIDs.rhapsotea.value, ItemClassification.filler),
  Ch4Items.scarlixir.value:  ItemData(ItemIDs.scarlixir.value, ItemClassification.filler),
  # Darker candy
  CCItems.dark_candy.value:  ItemData(ItemIDs.dark_candy.value, ItemClassification.filler),
  
  CCItems.tensiongem.value:     ItemData(ItemIDs.tensiongem.value,    ItemClassification.useful),
  Ch4Items.mysticband.value:    ItemData(ItemIDs.mysticband.value,    ItemClassification.useful),
  Ch4Items.powerband.value:     ItemData(ItemIDs.powerband.value,     ItemClassification.useful),
  Ch4Items.princessrbn.value:   ItemData(ItemIDs.princessrbn.value,   ItemClassification.useful),
  
  Ch4Items.scarfmark.value:     ItemData(ItemIDs.scarfmark.value,     ItemClassification.useful),
  Ch4Items.absobax.value:       ItemData(ItemIDs.absorbaxe.value,     ItemClassification.useful),
  Ch4Items.wingblade.value:     ItemData(ItemIDs.wingblade.value,     ItemClassification.useful),
  
  Ch4Items.claimbclaws.value:   ItemData(ItemIDs.claimbclaws.value,   ItemClassification.progression),
  Ch4Items.sheetmusic.value:    ItemData(ItemIDs.sheetmusic.value,    ItemClassification.progression),
}

chapter4_conditional_items = {
  Ch4Items.justiceaxe.value:    ConditionalItemData(ItemIDs.justiceaxe.value,     ItemClassification.useful, lambda world: world.is_secret_bosses_randomized()),
  CCItems.shadowcrystal.value:  ConditionalItemData(ItemIDs.shadowcrystal.value,  ItemClassification.useful, lambda world: world.is_secret_bosses_randomized()),
  
  Ch4Items.egg.value:           ConditionalItemData(ItemIDs.chapter_4_egg.value,  ItemClassification.useful, lambda world: world.is_hidden_items_randomized()),
  Ch4Items.holy_moss.value:     ConditionalItemData(ItemIDs.sacred_moss.value,    ItemClassification.useful, lambda world: world.is_hidden_items_randomized()),
  CCItems.dogdollard.value:     ConditionalItemData(ItemIDs.dogdollar.value,      ItemClassification.useful, lambda world: world.is_hidden_items_randomized()),
  
  Ch4Items.chapter_4_unlock.value:  ConditionalItemData(ItemIDs.chapter_4_unlock.value, ItemClassification.progression, lambda world: world.is_chapters_randomized()),
  # Amount is handle in __init__.py handle_macguffins_items()
  Ch4Items.combination_lock_digit.value:  ConditionalItemData(ItemIDs.combinaison_lock_digit.value, ItemClassification.progression, lambda world: world.is_final_chapter(4), 0),
}

def create_items(world: "DeltaruneWorld") -> list[DeltaruneItem]:
  return generic_create_items(world, chapter4_items, chapter4_conditional_items)
  
def get_filler_items(world: "DeltaruneWorld"):
  return generic_get_filler_items(world, chapter4_items, chapter4_conditional_items)