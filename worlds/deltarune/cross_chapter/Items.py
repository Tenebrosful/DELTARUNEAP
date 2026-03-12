from enum import StrEnum
from ..Items import ItemData, ConditionalItemData, ItemIDs, generic_create_items, get_generic_filler_items
from .. import DeltaruneWorld
from BaseClasses import ItemClassification

class CCItems(StrEnum):
  spincake = "Spincake"
  glowshard = "Glowshard"
  dark_burger = "Dark Burger"
  dd_burger = "DD-Burger"
  lancer_cookie = "Lancer Cookie"
  revive_mind = "Revive Mind"
  dogdollard = "DogDollar"
  amber_card = "Amber Card"
  pink_ribbon = "Pink Ribbon"
  white_ribbon = "White Ribbon"
  silver_card = "Silver Card"
  spikeband = "SpikeBand"
  twin_ribbon = "Twin Ribbon"
  tensionbow = "TensionBow"

cross_chapter_items = {
  CCItems.revive_mind:  ItemData(ItemIDs.revivemint, ItemClassification.useful)
}

cross_chapter_conditional_items = {
  CCItems.spincake:     ConditionalItemData(ItemIDs.spincake,   ItemClassification.useful,      lambda world: world.has_at_least_one_chapter_included([1, 2, 4])),
  CCItems.glowshard:    ConditionalItemData(ItemIDs.glowshard,  ItemClassification.progression, lambda world: world.has_at_least_one_chapter_included([1, 2, 3])),
  CCItems.dark_burger:  ConditionalItemData(ItemIDs.darkburger, ItemClassification.filler,      lambda world: world.has_at_least_one_chapter_included([1, 2, 4])),
  
  # Fusions
  CCItems.dd_burger:    ConditionalItemData(ItemIDs.dd_burger,    ItemClassification.filler,    lambda world: world.can_access_fusion()),
  CCItems.silver_card:  ConditionalItemData(ItemIDs.silver_card,  ItemClassification.useful,    lambda world: world.can_access_fusion()),
  CCItems.twin_ribbon:  ConditionalItemData(ItemIDs.twin_ribbon,  ItemClassification.useful,    lambda world: world.can_access_fusion()),
  # Require IronShackle that is exclusive to chapter 1
  CCItems.spikeband:    ConditionalItemData(ItemIDs.spikeband,    ItemClassification.useful,    lambda world: world.can_access_fusion() and world.have_all_chapters_included([1])),
  # Require B.ShotBowtie that is exclusive to chapter 2
  CCItems.tensionbow:   ConditionalItemData(ItemIDs.tensionbow,   ItemClassification.useful,    lambda world: world.can_access_fusion() and world.have_all_chapters_included([2])),
}

def create_items(world: DeltaruneWorld):
  generic_create_items(world, create_items, cross_chapter_conditional_items)
  
def get_filler_items(world: DeltaruneWorld):
  return get_generic_filler_items(world, cross_chapter_items, cross_chapter_conditional_items)