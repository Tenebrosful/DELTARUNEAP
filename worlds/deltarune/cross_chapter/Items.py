from enum import StrEnum
from ..Items import ItemData, ConditionalItemData, ItemIDs, generic_create_items, generic_get_filler_items
from typing import TYPE_CHECKING
from BaseClasses import ItemClassification

if TYPE_CHECKING:
    from .. import DeltaruneWorld
    
class CCItems(StrEnum):
  
  # Healing Items
  clubsSandwich   = "ClubSandwich"
  dark_burger     = "Dark Burger"
  dd_burger       = "DD-Burger"
  lancer_cookie   = "Lancer Cookie"
  spincake        = "Spincake"
  revive_mint     = "Revive Mint"
  
  # Currency
  glowshard         = "Glowshard"
  dogdollard        = "DogDollar"
  dark_dollar_1     = "1 Dark Dollar"
  dark_dollars_20   = "20 Dark Dollars"
  dark_dollars_40   = "40 Dark Dollars"
  dark_dollars_80   = "80 Dark Dollars"
  dark_dollars_100  = "100 Dark Dollars"
  dark_dollars_250  = "250 Dark Dollars"
  dark_dollars_500  = "500 Dark Dollars"
  
  # Weapons
  
  # Armors
  amber_card    = "Amber Card"
  pink_ribbon   = "Pink Ribbon"
  white_ribbon  = "White Ribbon"
  silver_card   = "Silver Card"
  spikeband     = "SpikeBand"
  twin_ribbon   = "Twin Ribbon"
  tensionbow    = "TensionBow"
  
  shadowcrystal = "ShadowCrystal"

cross_chapter_items = {
}

cross_chapter_conditional_items = {  
  # Fusions
  CCItems.dd_burger.value:    ConditionalItemData(ItemIDs.dd_burger.value,    ItemClassification.filler,    lambda world: world.can_access_fusion()),
  CCItems.silver_card.value:  ConditionalItemData(ItemIDs.silver_card.value,  ItemClassification.filler,    lambda world: world.can_access_fusion()),
  # Require Pink Ribbon that can be found in chapter 2 and 3 and White Ribbon that can be found in chapter 1 and 3 and starting armor for chapter 2
  CCItems.twin_ribbon.value:  ConditionalItemData(ItemIDs.twin_ribbon.value,  ItemClassification.useful,    lambda world: world.can_access_fusion() and world.has_at_least_one_chapter_included([2, 3]) and world.has_at_least_one_chapter_included([1, 2, 3])),
  # Require IronShackle that is exclusive to chapter 1 and Glow Wrist to chapter 2 (shop) and chapter 4 (starting armor like chapter 3 but chapter 3 can't fuse)
  CCItems.spikeband.value:    ConditionalItemData(ItemIDs.spikeband.value,    ItemClassification.useful,    lambda world: world.can_access_fusion() and world.include_chapter(1) and world.has_at_least_one_chapter_included([2, 4])),
  # Require B.ShotBowtie that is exclusive to chapter 2 and can't be obtained on weird route
  CCItems.tensionbow.value:   ConditionalItemData(ItemIDs.tensionbow.value,   ItemClassification.useful,    lambda world: world.can_access_fusion() and world.include_chapter(2) and not world.is_weird_route()),
}

def create_items(world: "DeltaruneWorld"):
  return generic_create_items(world, cross_chapter_items, cross_chapter_conditional_items)
  
def get_filler_items(world: "DeltaruneWorld"):
  return generic_get_filler_items(world, cross_chapter_items, cross_chapter_conditional_items)