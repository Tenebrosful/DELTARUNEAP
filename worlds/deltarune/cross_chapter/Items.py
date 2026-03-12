from enum import StrEnum
from .Items import ConditionalItemData, ItemIDs
from BaseClasses import ItemClassification

class Items(StrEnum):
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
  
cross_chapter_items_conditional = {
  Items.spincake: ConditionalItemData(ItemIDs.spincake, ItemClassification.useful, lambda world: world.has_at_least_one_chapter_included([1, 2, 4])),
}