from BaseClasses import Item, ItemClassification
from enum import Enum
from . import DeltaruneWorld
import typing


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    classification: any

class ConditionalItemData(typing.NamedTuple):
    code: typing.Optional[int]
    classification: any
    should_be_included: typing.Callable[[DeltaruneWorld], bool]

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
    
    
    dd_burger = 22
    
    chapter_1_egg = 10002
    brokencake = 10003
    broken_key_a = 10004
    door_key = 10005
    broken_key_b = 10006
    broken_key_c = 10007
    
    bake_sale_ticket = 11001
    # king_chess_piece = 11002
    castle_key = 11003
    top_cake = 11004
    joe_life_savings = 11006
    
    amber_card = 20001
    dice_brace = 20002
    pink_ribbon = 20003
    white_ribbon = 20004
    ironshackle = 20005
    jevilstail = 20007
    silver_card = 20008
    twin_ribbon = 20009
    spikeband = 20013
    tensionbow = 20015
    
    devilsknife = 30007
    
    king_shape_key_piece = 70000
    key_gen_2_segment = 70001
    remote_battery = 70002
    combinaison_lock_digit = 70003
    
    chapter_1_unlock = 90000
    chapter_2_unlock = 90001
    chapter_3_unlock = 90002
    chapter_4_unlock = 90003
    chapter_5_unlock = 90004

item_table = {
    "Dark Candy": ItemData(1, ItemClassification.filler),
    "ReviveMint": ItemData(2, ItemClassification.useful),
    "Glowshard": ItemData(3, ItemClassification.filler),
    "Manual": ItemData(4, ItemClassification.progression),
    "Spincake": ItemData(7, ItemClassification.useful),
    "Darkburger": ItemData(8, ItemClassification.filler),
    "LancerCookie": ItemData(9, ItemClassification.filler),
    "ClubsSandwich": ItemData(11, ItemClassification.filler),
    "HeartsDonut": ItemData(12, ItemClassification.filler),
    "ChocDiamond": ItemData(13, ItemClassification.filler),
    "RouxlsRoux": ItemData(15, ItemClassification.filler),
    
    "CD Bagel": ItemData(16, ItemClassification.filler),
    "Kris Tea": ItemData(18, ItemClassification.filler),
    "Noelle Tea": ItemData(19, ItemClassification.filler),
    "Ralsei Tea": ItemData(20, ItemClassification.filler),
    "Susie Tea": ItemData(21, ItemClassification.filler),
    "DD-Burger": ItemData(22, ItemClassification.filler),
    "LightCandy": ItemData(23, ItemClassification.filler),
    "ButJuice": ItemData(24, ItemClassification.filler),
    "SpagettiCode": ItemData(25, ItemClassification.filler),
    "TensionBit": ItemData(27, ItemClassification.progression),
    "TensionGem": ItemData(28, ItemClassification.filler),
    "TensionMax": ItemData(29, ItemClassification.useful),
    "ReviveDust": ItemData(30, ItemClassification.filler),
    "S.POISON": ItemData(32, ItemClassification.filler),
    "DogDollar": ItemData(33, ItemClassification.filler),
    "TVDinner": ItemData(34, ItemClassification.filler),
    "FlatSoda": ItemData(36, ItemClassification.filler),
    "TVSlop": ItemData(37, ItemClassification.filler),
    "ExecBuffet": ItemData(38, ItemClassification.useful),
    "DeluxeDinner": ItemData(39, ItemClassification.filler),
    "AncientSweet": ItemData(60, ItemClassification.useful),
    "Rhapsotea": ItemData(61, ItemClassification.filler),
    "Scarlixir": ItemData(62, ItemClassification.filler),
    "BitterTear": ItemData(63, ItemClassification.useful),
    
    "CH1 Egg": ItemData(10002, ItemClassification.useful),
    "BrokenCake": ItemData(10003, ItemClassification.progression),
    "Broken Key A": ItemData(10004, ItemClassification.progression),
    "Door Key": ItemData(10005, ItemClassification.progression),
    "Broken Key B": ItemData(10006, ItemClassification.progression),
    "Broken Key C": ItemData(10007, ItemClassification.progression),
    "EmptyDisk": ItemData(10010, ItemClassification.progression),
    "KeyGen": ItemData(10012, ItemClassification.progression),
    "ShadowCrystal": ItemData(10013, ItemClassification.progression),
    "OddController": ItemData(10016, ItemClassification.progression),
    "TripTicket": ItemData(10018, ItemClassification.progression),
    "SheetMusic": ItemData(10030, ItemClassification.progression),
    "ClaimbClaws": ItemData(10031, ItemClassification.progression),
    "Great Door Key": ItemData(11000, ItemClassification.progression),
    "Bake Sale Ticket": ItemData(11001, ItemClassification.progression),
    "King Chess Piece": ItemData(11002, ItemClassification.progression),
    "Castle Key": ItemData(11003, ItemClassification.progression),
    "Top Cake": ItemData(11004, ItemClassification.progression),
    "Castle Moss": ItemData(11005, ItemClassification.useful),
    "Joe's Life Savings": ItemData(11006, ItemClassification.useful),
    "City Moss": ItemData(11007, ItemClassification.useful),
    "Susie's Pencil": ItemData(11008, ItemClassification.progression),
    "Safety Vest": ItemData(11009, ItemClassification.progression),
    "Mansion Reservation": ItemData(11010, ItemClassification.progression),
    "CH2 Egg": ItemData(11011, ItemClassification.useful),
    "CH3 Egg": ItemData(11012, ItemClassification.useful),
    "Board 2 Game Cartridge": ItemData(11013, ItemClassification.progression),
    "VIP Pass": ItemData(11014, ItemClassification.progression),
    "SMILE": ItemData(11016, ItemClassification.useful),
    "Board Moss": ItemData(11017, ItemClassification.useful),
    "ICE KEY": ItemData(11018, ItemClassification.progression),
    "SHELTER KEY": ItemData(11019, ItemClassification.progression),
    "Sacred Moss": ItemData(11020, ItemClassification.useful),
    "CH4 Egg": ItemData(11021, ItemClassification.useful),
    "Amber Card": ItemData(20001, ItemClassification.useful),
    "Dice Brace": ItemData(20002, ItemClassification.useful),
    "Pink Ribbon": ItemData(20003, ItemClassification.progression),
    "White Ribbon": ItemData(20004, ItemClassification.progression),
    "IronShackle": ItemData(20005, ItemClassification.progression),
    "JevilsTail": ItemData(20007, ItemClassification.useful),
    "Silver Card": ItemData(20008, ItemClassification.useful),
    "Twin Ribbon": ItemData(20009, ItemClassification.useful),
    "GlowWrist": ItemData(20010, ItemClassification.progression),
    "ChainMail": ItemData(20011, ItemClassification.useful),
    "B.ShotBowtie": ItemData(20012, ItemClassification.progression),
    "Spikeband": ItemData(20013, ItemClassification.useful),
    "TensionBow": ItemData(20015, ItemClassification.useful),
    "Mannequin": ItemData(20016, ItemClassification.filler),
    "FrayedBowtie": ItemData(20020, ItemClassification.filler),
    "DealMaker": ItemData(20021, ItemClassification.useful),
    "RoyalPin": ItemData(20022, ItemClassification.useful),
    "ShadowMantle": ItemData(20023, ItemClassification.progression),
    "LodeStone": ItemData(20024, ItemClassification.useful),
    "GingerGuard": ItemData(20025, ItemClassification.useful),
    "Blue Ribbon": ItemData(20026, ItemClassification.useful),
    "TennaTie": ItemData(20027, ItemClassification.useful),
    "Waferguard": ItemData(20050, ItemClassification.useful),
    "MysticBand": ItemData(20051, ItemClassification.useful),
    "PowerBand": ItemData(20052, ItemClassification.useful),
    "PrincessRBN": ItemData(20053, ItemClassification.useful),
    "GoldWidow": ItemData(20054, ItemClassification.useful),
    "Spookysword": ItemData(30005, ItemClassification.useful),
    "Brave Ax": ItemData(30006, ItemClassification.useful),
    "DevilsKnife": ItemData(30007, ItemClassification.useful),
    "Ragger": ItemData(30009, ItemClassification.useful),
    "DaintyScarf": ItemData(30010, ItemClassification.useful),
    "ThornRing": ItemData(30013, ItemClassification.progression),
    "BounceBlade": ItemData(30014, ItemClassification.useful),
    "MechaSaber": ItemData(30016, ItemClassification.useful),
    "AutoAxe": ItemData(30017, ItemClassification.useful),
    "FiberScarf": ItemData(30018, ItemClassification.useful),
    "Ragger2": ItemData(30019, ItemClassification.useful),
    "BrokenSwd": ItemData(30020, ItemClassification.filler),
    "PuppetScarf": ItemData(30021, ItemClassification.useful),
    "FreezeRing": ItemData(30022, ItemClassification.progression),
    "Saber10": ItemData(30023, ItemClassification.useful),
    "ToxicAxe": ItemData(30024, ItemClassification.useful),
    "FlexScarf": ItemData(30025, ItemClassification.useful),
    "BlackShard": ItemData(30026, ItemClassification.useful),
    "JingleBlade": ItemData(30050, ItemClassification.useful),
    "ScarfMark": ItemData(30051, ItemClassification.useful),
    "JusticeAxe": ItemData(30052, ItemClassification.useful),
    "Winglade": ItemData(30053, ItemClassification.useful),
    "AbsorbAx": ItemData(30054, ItemClassification.useful),
    "1 Dark Dollar": ItemData(40001, ItemClassification.filler),
    "20 Dark Dollars": ItemData(40020, ItemClassification.filler),
    "40 Dark Dollars": ItemData(40040, ItemClassification.filler),
    "80 Dark Dollars": ItemData(40080, ItemClassification.filler),
    "100 Dark Dollars": ItemData(40100, ItemClassification.filler),
    "250 Dark Dollars": ItemData(40250, ItemClassification.filler),
    "500 Dark Dollars": ItemData(40500, ItemClassification.filler),
    "Fields Warp": ItemData(50000, ItemClassification.progression),
    "Forest Warp": ItemData(50001, ItemClassification.progression),
    "Bake Sale Warp": ItemData(50002, ItemClassification.progression),
    "Castle Warp": ItemData(50003, ItemClassification.progression),
    "Cyber Field Warp": ItemData(50004, ItemClassification.progression),
    "Trash Zone Warp": ItemData(50005, ItemClassification.progression),
    "Mansion Warp": ItemData(50006, ItemClassification.progression),
    "TV World Entrance Warp": ItemData(50007, ItemClassification.progression),
    "Goulden Sam Warp": ItemData(50008, ItemClassification.progression),
    "WHAT INTERESTING BEHAVIOR.": ItemData(66666, ItemClassification.progression),
    "King-Shaped Key Piece": ItemData(70000, ItemClassification.progression),
    "KeyGen 2 Segment": ItemData(70001, ItemClassification.progression),
    "Remote Battery": ItemData(70002, ItemClassification.progression),
    "Combination Lock Digit": ItemData(70003, ItemClassification.progression),
    "1 POINT": ItemData(80001, ItemClassification.filler),
    "2 POINTs": ItemData(80002, ItemClassification.filler),
    "10 POINTs": ItemData(80010, ItemClassification.filler),
    "50 POINTs": ItemData(80050, ItemClassification.filler),
    "120 POINTs": ItemData(80120, ItemClassification.filler),
    "300 POINTs": ItemData(80300, ItemClassification.filler),
    "500 POINTs": ItemData(80500, ItemClassification.filler),
    "Chapter 1 Unlock": ItemData(90000, ItemClassification.progression),
    "Chapter 2 Unlock": ItemData(90001, ItemClassification.progression),
    "Chapter 3 Unlock": ItemData(90002, ItemClassification.progression),
    "Chapter 4 Unlock": ItemData(90003, ItemClassification.progression),
    "This is where I would put my Chapter 5 Unlock... IF I HAD ONE!": ItemData(90004, ItemClassification.progression),
}

non_key_items_ch1 = {
    "Glowshard": 1,
    "Spincake": 1,
    "ReviveMint": 2,
    "Ragger": 1,
    "Dice Brace": 1,
    "40 Dark Dollars": 1,
    "ClubsSandwich": 1,
    "Manual": 1,
    "CH1 Egg": 1,
    "ShadowCrystal": 1,
    "DevilsKnife": 1,
    "JevilsTail": 1,
    "Amber Card": 2,
    "Brave Ax": 1,
    "DaintyScarf": 1,
    "Spookysword": 1,
    "Castle Moss": 1,
}

key_items_ch1 = {
    "White Ribbon": 1,
    "Top Cake": 1,
    "Manual": 1,
    "IronShackle": 1,
    "Broken Key C": 1,
    "Broken Key B": 1,
    "BrokenCake": 1,
    "Door Key": 1,
    "Broken Key A": 1,
    "Bake Sale Warp": 1,
    "Castle Warp": 1,
    "Bake Sale Ticket": 1,
    "Castle Key": 1,
    "Chapter 1 Unlock": 1,
}

junk_weights_ch1 = {
    "Dark Candy": 500-40,
    "Darkburger": 500-70,
    "LancerCookie": 500-50,
    "HeartsDonut": 500-60,
    "ChocDiamond": 500-60,
    "RouxlsRoux": 500-60,
}

non_key_items_ch2_weird = {
    "Joe's Life Savings": 1,
    "ClubsSandwich": 1,
    "Spincake": 1,
    "DD-Burger": 1,
    "Silver Card": 1,
    "Spikeband": 1,
    "GlowWrist": 2,
    "FiberScarf": 1,
    "MechaSaber": 1,
    "AutoAxe": 1,
    "ReviveMint": 2,
    "Ragger2": 1,
    "20 Dark Dollars": 2,
    "BounceBlade": 1,
    "80 Dark Dollars": 1,
    "Glowshard": 1,
    "ReviveDust": 1,
    "1 Dark Dollar": 1,
    "PuppetScarf": 1,
    "DealMaker": 1,
    "ShadowCrystal": 1,
    "250 Dark Dollars": 1,
    "Twin Ribbon": 1,
    "TensionBit": 1,
}

non_key_items_ch2 = {
    "Joe's Life Savings": 1,
    "ClubsSandwich": 1,
    "Spincake": 1,
    "DD-Burger": 1,
    "Silver Card": 1,
    "Spikeband": 1,
    "GlowWrist": 2,
    "FiberScarf": 1,
    "MechaSaber": 1,
    "AutoAxe": 1,
    "ReviveMint": 2,
    "Ragger2": 1,
    "20 Dark Dollars": 2,
    "BounceBlade": 1,
    "Mannequin": 1,
    "Noelle Tea": 1,
    "Kris Tea": 1,
    "Susie Tea": 1,
    "Ralsei Tea": 1,
    "DogDollar": 1,
    "CH2 Egg": 1,
    "80 Dark Dollars": 1,
    "SpagettiCode": 1,
    "RoyalPin": 1,
    "Glowshard": 1,
    "ReviveDust": 1,
    "ChainMail": 1,
    "S.POISON": 1,
    "BrokenSwd": 1,
    "FrayedBowtie": 1,
    "1 Dark Dollar": 1,
    "PuppetScarf": 1,
    "DealMaker": 1,
    "ShadowCrystal": 1,
    "250 Dark Dollars": 1,
    "TensionGem": 1,
    "Twin Ribbon": 1,
    "TensionBow": 1, 
    "City Moss": 1,   
}

key_items_ch2_weird = {
    "GlowWrist": 1,
    "Pink Ribbon": 1,
    "FreezeRing": 1,
    "ThornRing": 1,
    "Safety Vest": 1,
    "Chapter 2 Unlock": 1,
}

key_items_ch2 = {
    "TensionBit": 1,
    "GlowWrist": 1,
    "B.ShotBowtie": 1,
    "Pink Ribbon": 1,
    "KeyGen": 1,
    "EmptyDisk": 1,
    "Safety Vest": 1,
    "Mansion Reservation": 1,
    "Chapter 2 Unlock": 1,
}

key_items_ch2_all = {
    "TensionBit": 1,
    "GlowWrist": 1,
    "B.ShotBowtie": 1,
    "Pink Ribbon": 1,
    "KeyGen": 1,
    "EmptyDisk": 1,
    "Safety Vest": 1,
    "Mansion Reservation": 1,
    "FreezeRing": 1,
    "ThornRing": 1,
    "Chapter 2 Unlock": 1,
}


junk_weights_ch2 = {
    "CD Bagel": 500-40,
    "100 Dark Dollars": 500-50,
    "ButJuice": 500-70,
}

non_key_items_ch3 = {
    "10 POINTs": 5,
    "LodeStone": 1,
    "GingerGuard": 1,
    "White Ribbon": 1,
    "ToxicAxe": 1,
    "Saber10": 2,
    "FlexScarf": 1,
    "TennaTie": 1,
    "TensionMax": 1,
    "Blue Ribbon": 1,
    "ReviveMint": 1,
    "ExecBuffet": 1,
    "SMILE": 1,
    "Pink Ribbon": 1,
    "ReviveMint": 1,
    "2 POINTs": 1,
    "500 POINTs": 1,
    "120 POINTs": 1,
    "300 POINTs": 1,
    "1 POINT": 1,
    "CH3 Egg": 1,
    "ShadowCrystal": 1,
    "BlackShard": 1,
    "FlatSoda": 1,
    "Board Moss": 1,
}

non_key_items_ch3_weird = {
    "10 POINTs": 5,
    "LodeStone": 1,
    "GingerGuard": 1,
    "White Ribbon": 1,
    "ToxicAxe": 1,
    "Saber10": 2,
    "FlexScarf": 1,
    "TennaTie": 1,
    "TensionMax": 1,
    "Blue Ribbon": 1,
    "ReviveMint": 1,
    "ExecBuffet": 1,
    "SMILE": 1,
    "Pink Ribbon": 1,
    "ReviveMint": 1,
    "2 POINTs": 1,
    "500 POINTs": 1,
    "120 POINTs": 1,
    "300 POINTs": 1,
    "1 POINT": 1,
    "ShadowCrystal": 1,
    "BlackShard": 1,
    "FlatSoda": 1,
    "Board Moss": 1,
}

key_items_ch3_weird = {
    "OddController": 1,
    "ICE KEY": 1,
    "SHELTER KEY": 1,
    "ShadowMantle": 1,
    "Board 2 Game Cartridge": 1,
    "VIP Pass": 1,
    "Chapter 3 Unlock": 1,
}

key_items_ch3 = {
    "OddController": 1,
    "TripTicket": 1,
    "ICE KEY": 1,
    "SHELTER KEY": 1,
    "ShadowMantle": 1,
    "Board 2 Game Cartridge": 1,
    "VIP Pass": 1,
    "Chapter 3 Unlock": 1,
}

junk_weights_ch3 = {
    "TVSlop": 500-60,
    "50 POINTs": 500-50,
    "TVDinner": 500-40,
    "DeluxeDinner": 500-70,
}

non_key_items_ch4 = {
    "ExecBuffet": 1,
    "Spincake": 1,
    "Waferguard": 2,
    "ScarfMark": 1,
    "AbsorbAx": 1,
    "MysticBand": 1,
    "ReviveMint": 2,
    "500 Dark Dollars": 2,
    "Winglade": 1,
    "PowerBand": 1,
    "TensionGem": 1,
    "ShadowCrystal": 1,
    "JusticeAxe": 1,
    "CH4 Egg": 1,
    "DogDollar": 1,
    "PrincessRBN": 1,
    "Sacred Moss": 1,
}

key_items_ch4 = {
    "ClaimbClaws": 1,
    "SheetMusic": 1,
    "Chapter 4 Unlock": 1,
}

next_chapter_ch4 = {
    "This is where I would put my Chapter 5 Unlock... IF I HAD ONE!": 1,
}

junk_weights_ch4 = {
    "Rhapsotea": 500-40,
    "Dark Candy": 500-50,
    "Scarlixir": 500-60,
    "250 Dark Dollars": 500-100,
}

hidden_items = [
    "TennaTie",
    "TensionMax",
    "Blue Ribbon",
    "ReviveMint",
    "ExecBuffet",
    "CH1 Egg",
    "CH2 Egg",
    "TripTicket",
    "CH3 Egg",
    "DogDollar",
    "Broken Key A",
    "Broken Key B",
    "Broken Key C",
    "Door Key",
    "KeyGen",
    "EmptyDisk",
    "ICE KEY",
    "SHELTER KEY",
    "Castle Moss",
    "City Moss",
    "Board Moss",
]

warp_doors = [
    "Fields Warp",
    "Forest Warp",
    "Bake Sale Warp",
    "Castle Warp",
    "Cyber Field Warp",
    "Trash Zone Warp",
    "Mansion Warp",
    "Goulden Sam Warp",
]

secret_boss_rewards = [
    "JevilsTail",
    "DevilsKnife",
    "ShadowCrystal",
    "PuppetScarf",
    "DealMaker",
    "BlackShard",
    "ShadowMantle",
    "FlatSoda",
    "JusticeAxe",
]

chapters = [
    "Chapter 1 Unlock",
    "Chapter 2 Unlock",
    "Chapter 3 Unlock",
    "Chapter 4 Unlock",
    "This is where I would put my Chapter 5 Unlock... IF I HAD ONE!",
]

def generic_create_items(world: DeltaruneWorld, items: dict[str, ItemData], conditional_items: dict[str, ConditionalItemData]):
    itempool: list[Item] = []
  
    for item_name, item_data in items.items():
        itempool += DeltaruneItem(item_name, item_data.classification, item_data.code, world.player)
        
    for item_name, item_data in conditional_items.items():
        if item_data.should_be_included(world):
            itempool += DeltaruneItem(item_name, item_data.classification, item_data.code, world.player)
            
    world.multiworld.itempool += itempool
    
def get_generic_filler_items(world: DeltaruneWorld, items: dict[str, ItemData], conditional_items: dict[str, ConditionalItemData]):
    filler_items = []
  
    filler_items += [item_name for item_name, item_data in items.items() if item_data.classification == ItemClassification.filler]
    filler_items += [item_name for item_name, item_data in conditional_items.items() if item_data.classification == ItemClassification.filler and item_data.should_be_included(world)]
    
    weigth = 100 / len(filler_items)
    
    return [filler_item for filler_item in map(lambda item_name: {item_name: weigth}, filler_items)]