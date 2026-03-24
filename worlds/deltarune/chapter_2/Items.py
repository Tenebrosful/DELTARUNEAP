from ..Items import ItemGroups, ItemIDs, ItemData, ConditionalItemData, generic_create_items, generic_get_filler_items, DeltaruneItem
from ..cross_chapter.Items import CCItems
from typing import TYPE_CHECKING
from BaseClasses import ItemClassification
from enum import StrEnum

if TYPE_CHECKING:
    from .. import DeltaruneWorld

class Ch2Items(StrEnum):
  chapter_2_unlock = "Chapter 2 Unlock"
  
  # Healing Items
  cd_bagel      = "CD Bagel"
  kris_tea      = "Kris Tea"
  noelle_tea    = "Noelle Tea"
  ralsei_tea    = "Ralsei Tea"
  susie_tea     = "Susie Tea"
  lightcandy    = "LightCandy"
  butjuice      = "ButJuice"
  spagetticode  = "SpagettiCode"
  revivedust    = "ReviveDust"
  
  spoison       = "S.POISON"
  tensionbit    = "TensionBit"
  
  # Armors
  glowwrist     = "GlowWrist"
  dealmaker     = "DealMaker"
  mannequin     = "Mannequin"
  royalpin      = "RoyalPin"
  chainmail     = "ChainMail"
  frayedbowtie  = "FrayedBowtie"
  bshotbowtie   = "B.ShotBowtie"
  
  # Weapons
  mechasaber    = "MechaSaber"
  bounceblade   = "BounceBlade"
  autoaxe       = "AutoAxe"
  fiberscarf    = "FiberScarf"
  ragger2       = "Ragger2"
  puppetscarf   = "PuppetScarf"
  brokenswd     = "BrokenSwd"
  freezering    = "FreezeRing"
  thornring     = "ThornRing"
  
  egg               = "CH2 Egg"
  joe_life_savings  = "Jigsaw Joe's Life Savings"
  city_moss         = "City Moss"
  dogdollar         = "DogDollar"
  
  emptydisk     = "EmptyDisk"
  keygen        = "KeyGen"
  
  # Blockers
  safety_vest         = "Safety Vest"
  mansion_reservation = "Mansion Reservation"
  
  # Macguffins
  keygen_2_segment    = "KeyGen 2 Segment"
  
  # Warps
  cyber_field_warp    = "Cyber Field Warp"
  trash_zone_warp     = "Trash Zone Warp"
  mansion_warp        = "Mansion Warp"
  
chapter2_macguffin_item = Ch2Items.keygen_2_segment.value

chapter2_items = {
  Ch2Items.cd_bagel.value:        ItemData(ItemIDs.cd_bagel.value,          ItemClassification.filler, [ItemGroups.healing_item]),
  CCItems.dark_dollars_100.value: ItemData(ItemIDs.dark_dollars_100.value,  ItemClassification.filler, [ItemGroups.currencies]),
  CCItems.tensiongem.value:       ItemData(ItemIDs.tensiongem.value,        ItemClassification.useful, [ItemGroups.tension_items]),

  CCItems.dark_dollar_1.value:    ItemData(ItemIDs.dark_dollar_1.value,     ItemClassification.useful, [ItemGroups.currencies]),
  CCItems.dark_dollars_20.value:  ItemData(ItemIDs.dark_dollars_20.value,   ItemClassification.useful, [ItemGroups.currencies], 2),
  CCItems.dark_dollars_80.value:  ItemData(ItemIDs.dark_dollars_80.value,   ItemClassification.useful, [ItemGroups.currencies]),
  CCItems.dark_dollars_250.value: ItemData(ItemIDs.dark_dollars_250.value,  ItemClassification.useful, [ItemGroups.currencies]),
  
  CCItems.clubsSandwich.value:      ItemData(ItemIDs.clubsandwich.value,      ItemClassification.useful, [ItemGroups.healing_item]),
  Ch2Items.joe_life_savings.value:  ItemData(ItemIDs.joe_life_savings.value,  ItemClassification.useful, [ItemGroups.currencies]),
  Ch2Items.lightcandy.value:        ItemData(ItemIDs.lightcandy.value,        ItemClassification.useful, [ItemGroups.healing_item]),
  CCItems.spincake.value:           ItemData(ItemIDs.spincake.value,          ItemClassification.useful, [ItemGroups.healing_item]),
  
  CCItems.revivemint.value:        ItemData(ItemIDs.revivemint.value,        ItemClassification.useful, [ItemGroups.healing_item], 2),
  
  Ch2Items.mechasaber.value:        ItemData(ItemIDs.mechasaber.value,        ItemClassification.useful, [ItemGroups.weapons]),
  Ch2Items.autoaxe.value:           ItemData(ItemIDs.autoaxe.value,           ItemClassification.useful, [ItemGroups.weapons]),
  Ch2Items.fiberscarf.value:        ItemData(ItemIDs.fiberscarf.value,        ItemClassification.useful, [ItemGroups.weapons]),
  Ch2Items.ragger2.value:           ItemData(ItemIDs.ragger2.value,           ItemClassification.useful, [ItemGroups.weapons]),
  Ch2Items.bounceblade.value:       ItemData(ItemIDs.bounceblade.value,       ItemClassification.useful, [ItemGroups.weapons]),
  
  Ch2Items.mannequin.value:         ItemData(ItemIDs.mannequin.value,         ItemClassification.useful, [ItemGroups.armors]),
  # Noelle royal pin
  Ch2Items.royalpin.value:          ItemData(ItemIDs.royalpin.value,          ItemClassification.useful, [ItemGroups.armors]),
  
  Ch2Items.tensionbit.value:          ItemData(ItemIDs.tensionbit.value,        ItemClassification.progression | ItemClassification.useful, [ItemGroups.weapons]),
  Ch2Items.glowwrist.value:           ItemData(ItemIDs.glowwrist.value,         ItemClassification.progression | ItemClassification.useful, [ItemGroups.armors, ItemGroups.fusion_ingredient], 2),
  CCItems.pink_ribbon.value:          ItemData(ItemIDs.pink_ribbon.value,       ItemClassification.progression, [ItemGroups.armors, ItemGroups.fusion_ingredient]),
  Ch2Items.safety_vest.value:         ItemData(ItemIDs.safety_vest.value,       ItemClassification.progression, [ItemGroups.region_blockers]),
}

chapter2_conditional_items = {
  Ch2Items.butjuice.value:        ConditionalItemData(ItemIDs.butjuice.value,       ItemClassification.filler, lambda world: not world.is_weird_route() or world.is_all_routes(), [ItemGroups.healing_item]),
  Ch2Items.spagetticode.value:    ConditionalItemData(ItemIDs.spagetticode.value,   ItemClassification.filler, lambda world: not world.is_weird_route() or world.is_all_routes(), [ItemGroups.healing_item]),
  Ch2Items.spoison.value:         ConditionalItemData(ItemIDs.spoison.value,        ItemClassification.filler, lambda world: not world.is_weird_route() or world.is_all_routes(), [ItemGroups.healing_item]),
  Ch2Items.kris_tea.value:        ConditionalItemData(ItemIDs.kris_tea.value,       ItemClassification.filler, lambda world: not world.is_weird_route() or world.is_all_routes(), [ItemGroups.healing_item]),
  Ch2Items.noelle_tea.value:      ConditionalItemData(ItemIDs.noelle_tea.value,     ItemClassification.filler, lambda world: not world.is_weird_route() or world.is_all_routes(), [ItemGroups.healing_item]),
  Ch2Items.ralsei_tea.value:      ConditionalItemData(ItemIDs.ralsei_tea.value,     ItemClassification.filler, lambda world: not world.is_weird_route() or world.is_all_routes(), [ItemGroups.healing_item]),
  Ch2Items.susie_tea.value:       ConditionalItemData(ItemIDs.susie_tea.value,      ItemClassification.filler, lambda world: not world.is_weird_route() or world.is_all_routes(), [ItemGroups.healing_item]),
  Ch2Items.spoison.value:         ConditionalItemData(ItemIDs.spoison.value,        ItemClassification.filler, lambda world: not world.is_weird_route() or world.is_all_routes(), [ItemGroups.healing_item]),
  Ch2Items.royalpin.value:        ConditionalItemData(ItemIDs.royalpin.value,       ItemClassification.filler, lambda world: not world.is_weird_route() or world.is_all_routes(), [ItemGroups.armors]),
  Ch2Items.frayedbowtie.value:    ConditionalItemData(ItemIDs.frayedbowtie.value,   ItemClassification.filler, lambda world: not world.is_weird_route() or world.is_all_routes(), [ItemGroups.armors]),
  
  CCItems.glowshard.value:    ConditionalItemData(ItemIDs.glowshard.value,      ItemClassification.useful, lambda world: not world.is_weird_route() or world.is_all_routes(), [ItemGroups.currencies]),
  Ch2Items.egg.value:         ConditionalItemData(ItemIDs.chapter_2_egg.value,  ItemClassification.useful, lambda world: (not world.is_weird_route() or world.is_all_routes()) and world.is_hidden_items_randomized(), [ItemGroups.eggs]),
  Ch2Items.city_moss.value:   ConditionalItemData(ItemIDs.city_moss.value,      ItemClassification.useful, lambda world: (not world.is_weird_route() or world.is_all_routes()) and world.is_hidden_items_randomized(), [ItemGroups.moss]),
  CCItems.dogdollard.value:   ConditionalItemData(ItemIDs.dogdollar.value,      ItemClassification.useful, lambda world: (not world.is_weird_route() or world.is_all_routes()) and world.is_hidden_items_randomized(), [ItemGroups.currencies]),
  Ch2Items.revivedust.value:  ConditionalItemData(ItemIDs.revivedust.value,     ItemClassification.useful, lambda world: not world.is_weird_route() or world.is_all_routes(), [ItemGroups.healing_item]),
  Ch2Items.chainmail.value:   ConditionalItemData(ItemIDs.chainmail.value,      ItemClassification.useful, lambda world: not world.is_weird_route() or world.is_all_routes(), [ItemGroups.armors]),
  Ch2Items.brokenswd.value:   ConditionalItemData(ItemIDs.brokenswd.value,      ItemClassification.useful, lambda world: not world.is_weird_route() or world.is_all_routes(), [ItemGroups.weapons]),
  
  Ch2Items.mansion_reservation.value: ConditionalItemData(ItemIDs.mansion_reservation.value,  ItemClassification.progression, lambda world: not world.is_weird_route() or world.is_all_routes(), [ItemGroups.region_blockers]),
  
  Ch2Items.bshotbowtie.value:         ConditionalItemData(ItemIDs.bshotbowtie.value,          ItemClassification.progression | ItemClassification.useful, lambda world: not world.is_weird_route() or world.is_all_routes(), [ItemGroups.armors]),
  
  # Weird route
  Ch2Items.freezering.value:  ConditionalItemData(ItemIDs.freezering.value,     ItemClassification.useful, lambda world: world.is_weird_route(), [ItemGroups.weapons]),
  Ch2Items.thornring.value:   ConditionalItemData(ItemIDs.thornring.value,      ItemClassification.progression | ItemClassification.useful, lambda world: world.is_weird_route(), [ItemGroups.weapons]),
  
  Ch2Items.chapter_2_unlock.value:  ConditionalItemData(ItemIDs.chapter_2_unlock.value, ItemClassification.progression, lambda world: world.is_chapters_randomized(), [ItemGroups.region_blockers]),
  # Amount is handle in __init__.py handle_macguffins_items()
  Ch2Items.keygen_2_segment.value: ConditionalItemData(ItemIDs.key_gen_2_segment.value, ItemClassification.progression, lambda world: world.is_final_chapter(2), [ItemGroups.region_blockers], 0),
  
  # Secret Boss
  Ch2Items.emptydisk.value:   ConditionalItemData(ItemIDs.emptydisk.value,  ItemClassification.progression, lambda world: (not world.is_weird_route() or world.is_all_routes()) and world.is_hidden_items_randomized(), [ItemGroups.spamton_access]),
  Ch2Items.keygen.value:      ConditionalItemData(ItemIDs.keygen.value,     ItemClassification.progression, lambda world: (not world.is_weird_route() or world.is_all_routes()) and world.is_hidden_items_randomized(), [ItemGroups.spamton_access]),
  Ch2Items.dealmaker.value:   ConditionalItemData(ItemIDs.dealmaker.value,  ItemClassification.useful,      lambda world: (not world.is_weird_route() or world.is_all_routes()) and world.is_secret_bosses_randomized(), [ItemGroups.armors]),
  Ch2Items.puppetscarf.value: ConditionalItemData(ItemIDs.puppetscarf.value,ItemClassification.useful,      lambda world: world.is_secret_bosses_randomized(), [ItemGroups.weapons]),
  CCItems.shadowcrystal.value:ConditionalItemData(ItemIDs.shadowcrystal.value,ItemClassification.useful,    lambda world: world.is_secret_bosses_randomized()),
  
  # Warps
  Ch2Items.cyber_field_warp.value:  ConditionalItemData(ItemIDs.cyber_field_warp.value, ItemClassification.progression, lambda world: world.is_warps_randomized(), [ItemGroups.warps], 0),
  Ch2Items.trash_zone_warp.value:   ConditionalItemData(ItemIDs.trash_zone_warp.value,  ItemClassification.progression, lambda world: world.is_warps_randomized(), [ItemGroups.warps], 0),
  Ch2Items.mansion_warp.value:      ConditionalItemData(ItemIDs.mansion_warp.value,     ItemClassification.progression, lambda world: world.is_warps_randomized(), [ItemGroups.warps], 0),
}

def create_items(world: "DeltaruneWorld") -> list[DeltaruneItem]:
  return generic_create_items(world, chapter2_items, chapter2_conditional_items)
  
def get_filler_items(world: "DeltaruneWorld"):
  return generic_get_filler_items(world, chapter2_items, chapter2_conditional_items)