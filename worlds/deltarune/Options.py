from Options import Choice, Toggle, Range, PerGameCommonOptions, NamedRange
from dataclasses import dataclass
from enum import StrEnum

class Notice(Choice):
    """
    THIS IS NOT AN OPTION:

    SHOULD A CHAPTER BE EXCLUDED
    FROM BOTH OF ITS NEIGHBORS,

    GENERATION WILL FAIL.

    (For example: Including only chapter 2 and 3 or just doing a single chapter WILL work fine. 
    Including chapter 1, not including chapter 2, but including chapter 3 will not work.)"""
    display_name = "NOTICE: READ OPTION INFO"
    option_understood = 0
    default = 0

class ChosenRoute(Choice):
    """
    CHOOSE THE ROUTE
    THAT YOU PREFER.

    (All Recruits - Progress through the story normally. Recruit Everyone!!!)
    (Weird Route - Proceed through the "Weird Route" storyline while losing all possible recruits.)
    (Losing/Gaining recruits have been turned into checks.)"""
    display_name = "Chosen Route"
    option_all_recruits = 0
    option_weird_route = 1
    option_all_routes = 2
    default = 0

class ChosenRouteOptions(StrEnum):
    all_recruits = "all_recruits"
    weird_route = "weird_route"
    all_routes = "all_routes"

class RandomizeChapters(Choice):
    """
    HOW WILL YOU PROGRESS
    THROUGH THE CHAPTERS?

    (In Order - The next chapter will be unlocked once you complete the one you're in. This is the recommended option.)
    (Randomized Chapters - Chapters are unlocked through getting checks. In Multiplayer, be prepared to wait a while!)
    (All Unlocked - All chapters are unlocked from the start. You will be expected to play through another chapter once stuck.)
    
    AS A REMINDER,
    
    YOUR GOAL IS
    TO SEE THE END
    OF ALL CHAPTERS."""
    display_name = "Randomize Chapters"
    option_in_order = 0
    option_randomized = 1
    option_all_unlocked = 2
    default = 0

class RandomizeChapterOptions(StrEnum):
    in_order = "in_order"
    randomized = "randomized"
    all_unlocked = "all_unlocked"

class RandomizeSecretBosses(Choice):
    """
    ITEMS GIVEN BY THOSE
    POSSESSING SHADOW CRYSTALS
    WILL BE RANDOMIZED.

    
    SHOULD THE OPTION
    BE SET TO "MANDATORY",

    DEFEATING THESE CHALLENGES
    WILL BE REQUIRED TO PROGRESS.

    (If you don't choose "Mantleless" for the next option,
    The Shadow Mantle will also be included as a mandatory boss.)"""
    display_name = "Randomize Secret Bosses"
    option_false = 0
    option_true = 1
    option_mandatory = 2
    default = 0

class RandomizeSecretBossesOptions(StrEnum):
    false = "false"
    true = "true"
    mandatory = "mandatory"

class RandomizeMANTLE(Choice):
    """
    CHECKS RECIEVED
    IN THE ORIGINAL GAME
    OF THE THIRD CHAPTER
    WILL BE RANDOMIZED.

    
    SHOULD THE OPTION
    BE SET TO "MANTLELESS",
    
    THE CHECKS OF THE ORIGINAL GAME
    WILL STILL BE RANDOMIZED,
    
    HOWEVER 
    
    CHECK LOCATIONS SPECIFICALLY
    LOCKED BEHIND DEFEATING THE MANTLE
    WILL BE REMOVED.

    (So basically, if you choose "Mantleless", the game's still randomized, you just won't have to fight the Mantle.)
    (You can still get the items normally locked behind the boss fight from other checks, though.)
    (And of course, this only applies if you play Chapter 3.)"""
    display_name = "Randomize MANTLE"
    option_false = 0
    option_true = 1
    option_mantleless = 2
    default = 0

class RandomizeMANTLEOptions(StrEnum):
    false = "false"
    true = "true"
    mantleless = "mantleless"

class IncludeShadowMantle(Toggle):
    """
    THE SHADOW MANTLE WILL BE
    IN THE ITEM POOL
    OF THE THIRD CHAPTER.

    SHOULD THE OPTION
    BE SET TO "FALSE",

    THE SHADOW MANTLE WILL NOT
    BE IN LOGIC FOR THE DUEL
    WITH THE KNIGHT.

    (Of course, this only applies if you play Chapter 3.)"""
    display_name = "Include Shadow Mantle"
    default = 0

class IncludeTraps(Choice):
    """
    SOME CHECKS RECIEVED
    WILL ACTUALLY BE TRAPS.
    

    SHOULD THE OPTION
    BE SET TO "ALL TRAPS",

    THE JUNK POOL WILL
    BE ENTIRELY REPLACED
    BY TRAPS."""
    display_name = "Include Traps"
    option_false = 0
    option_true = 1
    option_all_traps = 2
    default = 0

class IncludeTRank(Toggle):
    """
    GETTING THE HIGHEST RANK
    OF THE THIRD CHAPTER
    WILL BE EXPECTED.

    (Of course, this only applies if you play Chapter 3.)"""
    display_name = "Include T Rank"
    default = 0

class ItemBalancing(Toggle):
    """
    IF AN ITEM IS
    OBTAINED EARLY,

    ITS POWER WILL
    BE SCALED DOWN.

    (For example, Chapter 4's AbsorbAx in chapter 1 will only give +3 attack instead of +8.)"""
    display_name = "ItemBalancing"
    default = 0

class IncludeHiddenItems(Toggle):
    """
    RANDOMIZES ITEMS
    THAT ARE CONSIDERABLY MORE
    DIFFICULT TO FIND
    OR TEDIOUS TO OBTAIN.

    (Examples:
    - The Golden Prizes in Chapter 3
    - The Eggs
    - Items Needed for Secret Bosses
    - Dog Dollars
    - Moss)"""
    display_name = "Include Grindy/Hidden Items"
    default = 0


class RandomizeWarpDoors(Toggle):
    """SHORTCUT DOORS
    WILL BE AN ALTERNATIVE
    TO THE LOCATION KEY.

    (Chapter 1 is the only chapter that's affected as of current.)"""
    display_name = "Randomize Warp Doors"
    default = 0

class IncludeChapter1(Toggle):
    """DO YOU WISH
    TO PLAY CHAPTER 1?"""
    display_name = "Include Chapter 1"
    default = 1


class IncludeChapter2(Toggle):
    """
    DO YOU WISH
    TO PLAY CHAPTER 2?"""
    display_name = "Include Chapter 2"
    default = 1
    

class IncludeChapter3(Toggle):
    """
    DO YOU WISH
    TO PLAY CHAPTER 3?"""
    display_name = "Include Chapter 3"
    default = 1

class IncludeChapter4(Toggle):
    """
    DO YOU WISH
    TO PLAY CHAPTER 4?"""
    display_name = "Include Chapter 4"
    default = 1

class GoalMacGuffinAmount(Range):
    """
    A NEW ROADBLOCK WILL
    APPEAR BEFORE THE
    FINAL BOSS OF THE LAST
    CHAPTER CHOSEN.

    THIS OPTION DETERMINES
    HOW MANY OF THESE ITEMS
    WILL BE REQUIRED
    TO PROGRESS.

    (Chapter 1: King-Shaped Key Pieces)
    (Chapter 2: KeyGen 2 Segments)
    (Chapter 3: Remote Batteries)
    (Chapter 4: Combination Lock Digits)"""
    display_name = "Macguffin Amount"
    default = 3
    range_start = 1
    range_end = 10

class DeathLink(Toggle):
    """
    YOUR FAILURE
    CAUSES THE FAILURE
    OF EVERYONE
    WHO HAS ENABLED
    THIS OPTION.
    
    TO COMPLIMENT,
    THE REVERSE
    IS TRUE AS WELL."""
    display_name = "Death Link"
    default = 0

class ProgressionBalancing(NamedRange):
    """
    ATTEMPTS TO BALANCE
    THE PROGRESSION
    OF YOUR ITEMS.

    SETTING THE VALUE LOWER
    WILL RESULT IN MORE WAITING
    TO RECIEVE ITEMS.

    SETTING THE VALUE HIGHER
    WILL RESULT IN LESS WAITING
    TO RECIEVE ITEMS.
    """
    default = 50
    range_start = 0
    range_end = 99
    display_name = "Progression Balancing"
    rich_text_doc = True
    special_range_names = {
        "disabled": 0,
        "normal": 50,
        "extreme": 99,
    }

class Accessibility(Choice):
    """
    SETS THE RULES 
    FOR THE ABILITY 
    TO REACH ALL ITEMS.

    **Full:** GUARANTEES THAT ALL ITEMS CAN BE OBTAINED.

    **Minimal:** GUARANTEES ONLY WHAT IS NECESSARY, BUT NO MORE.
    """
    display_name = "Accessibility"
    rich_text_doc = True
    option_full = 0
    option_minimal = 2
    alias_none = 2
    alias_locations = 0
    alias_items = 0
    default = 0


@dataclass
class DeltaruneOptions(PerGameCommonOptions):
    progression_balancing:                            ProgressionBalancing
    accessibility:                                    Accessibility
    include_chapter_1:                                IncludeChapter1
    include_chapter_2:                                IncludeChapter2
    include_chapter_3:                                IncludeChapter3
    include_chapter_4:                                IncludeChapter4
    randomize_chapters:                               RandomizeChapters
    chosen_route:                                     ChosenRoute
    item_balancing:                                   ItemBalancing
    goal_macguffin_amount:                            GoalMacGuffinAmount
    randomize_warp_doors:                             RandomizeWarpDoors
    randomize_secret_bosses:                          RandomizeSecretBosses
    randomize_mantle:                                 RandomizeMANTLE
    include_shadow_mantle:                            IncludeShadowMantle
    include_t_rank:                                   IncludeTRank
    include_hidden_items:                             IncludeHiddenItems
    death_link:                                       DeathLink
#    include_traps:                                    IncludeTraps