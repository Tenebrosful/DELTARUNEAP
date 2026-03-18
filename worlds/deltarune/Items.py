from BaseClasses import Item, ItemClassification
from enum import Enum
from typing import TYPE_CHECKING, NamedTuple, Optional, Callable

if TYPE_CHECKING: from . import DeltaruneWorld

class ItemData(NamedTuple):
    code: Optional[int]
    classification: any
    amount: Optional[int] = 1

class ConditionalItemData(NamedTuple):
    code: Optional[int]
    classification: any
    should_be_included: Callable[["DeltaruneWorld"], bool]
    amount: Optional[int] = 1

class DeltaruneItem(Item):
    game: str = "Deltarune"

class ItemIDs(Enum):
    dark_candy = 1
    revivemint = 2
    glowshard = 3
    manual = 4
    #nothing = 6
    spincake = 7
    darkburger = 8
    lancer_cookie = 9
    #nothing = 10
    clubsandwich = 11
    heartsdonut = 12
    chocdiamond = 13
    #nothing = 14
    rouxlsroux = 15
    
    cd_bagel = 16
    #nothing = 17
    kris_tea = 18
    noelle_tea = 19
    ralsei_tea = 20
    susie_tea = 21
    dd_burger = 22
    lightcandy = 23
    butjuice = 24
    spagetticode = 25
    #nothing = 26
    tensionbit = 27
    tensiongem = 28
    tensionmax = 29
    revivedust = 30
    #nothing = 31
    spoison = 32
    dogdollar = 33
    tvdinner = 34
    #nothing = 35
    flatsoda = 36
    tvslop = 37
    execbuffet = 38
    deluxedinner = 39
    
    ancientsweet = 60
    rhapsotea = 61
    scarlixir = 62
    bittertear = 63
        
    chapter_1_egg = 10002
    brokencake = 10003
    broken_key_a = 10004
    door_key = 10005
    broken_key_b = 10006
    broken_key_c = 10007
    
    emptydisk = 10010
    # nothing
    keygen = 10012
    shadowcrystal = 10013
    
    oddcontroller = 10016
    # nothing
    tripticket = 10018
    
    sheetmusic = 10030
    claimbclaws = 10031
    
    # great_door_key = 11000
    bake_sale_ticket = 11001
    # king_chess_piece = 11002
    castle_key = 11003
    top_cake = 11004
    castle_moss = 11005
    joe_life_savings = 11006
    city_moss = 11007
    # susie_pencil = 11008
    safety_vest = 11009
    mansion_reservation = 11010
    chapter_2_egg = 11011
    chapter_3_egg = 11012
    board_2_cartridge = 11013
    vip_pass = 11014
    # nothing = 11015
    smile = 11016
    board_moss = 11017
    ice_key = 11018
    shelter_key = 11019
    sacred_moss = 11020
    chapter_4_egg = 11021
    
    amber_card = 20001
    dice_brace = 20002
    pink_ribbon = 20003
    white_ribbon = 20004
    ironshackle = 20005
    jevilstail = 20007
    silver_card = 20008
    twin_ribbon = 20009
    glowwrist = 20010
    chainmail = 20011
    spikeband = 20013
    tensionbow = 20015
    mannequin = 20016
    
    frayedbowtie = 20020
    dealmaker = 20021
    royalpin = 20022
    shadowmantle = 20023
    lodestone = 20024
    gingerguard = 20025
    blue_ribbon = 20026
    tennatie = 20027
    
    waferguard = 20050
    mysticband = 20051
    powerband = 20052
    princessrbn = 20053
    goldwidow = 20054
        
    spookysword = 30005
    brave_ax = 30006
    devilsknife = 30007
    ragger = 30009
    daintyscarf = 30010
    thornring = 30013
    bounceblade = 30014
    # nothing = 30015
    mechasaber = 30016
    autoaxe = 30017
    fiberscarf = 30018
    ragger2 = 30019
    brokenswd = 30020
    puppetscarf = 30021
    freezering = 30022
    saber10 = 30023
    toxicaxe = 30024
    flexscarf = 30025
    blackshard = 30026
    
    jingleblade = 30050
    scarfmark = 30051
    justiceaxe = 30052
    wingblade = 30053
    absorbaxe = 30054
    
    dark_dollar_1 = 40001
    dark_dollars_20 = 40020
    dark_dollars_40 = 40040
    dark_dollars_80 = 40080
    dark_dollars_100 = 40100
    dark_dollars_250 = 40250
    dark_dollars_500 = 40500
    
    fields_warp = 50000
    forest_warp = 50001
    bake_sale_warp = 50002
    card_castle_warp = 50003
    cyber_field_warp = 50004
    trash_zone_warp = 50005
    mansion_warp = 50006
    tv_world_entrace_warp = 50007
    goulden_sam_warp = 50008
    
    what_interesting_behavior = 66666
    
    king_shape_key_piece = 70000
    key_gen_2_segment = 70001
    remote_battery = 70002
    combinaison_lock_digit = 70003
    
    point_1 = 80001
    points_2 = 80002
    points_10 = 80010
    points_50 = 80050
    points_120 = 80120
    points_300 = 80300
    points_500 = 80500
    
    chapter_1_unlock = 90000
    chapter_2_unlock = 90001
    chapter_3_unlock = 90002
    chapter_4_unlock = 90003
    chapter_5_unlock = 90004

def generic_create_items(world: "DeltaruneWorld", items: dict[str, ItemData], conditional_items: dict[str, ConditionalItemData]) -> list[str]:
    item_pool: list[str] = []
  
    for item_name, item_data in items.items():
        item_pool += [item_name] * item_data.amount
        
    for item_name, item_data in conditional_items.items():
        if item_data.should_be_included(world):
            item_pool += [item_name] * item_data.amount

    return item_pool
    
def generic_get_filler_items(world: "DeltaruneWorld", items: dict[str, ItemData], conditional_items: dict[str, ConditionalItemData]) -> dict[str, float]:
    filler_items = []
  
    filler_items += [item_name for item_name, item_data in items.items() if item_data.classification == ItemClassification.filler]
    filler_items += [item_name for item_name, item_data in conditional_items.items() if item_data.classification == ItemClassification.filler and item_data.should_be_included(world)]
    
    if len(filler_items) == 0: return {}
    
    weigth = 100 / len(filler_items)
    
    # return map(lambda item_name: {item_name: weigth}, filler_items)
    return {item_name: weigth for item_name in filler_items}