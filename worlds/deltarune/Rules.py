from worlds.generic.Rules import set_rule, add_rule
from BaseClasses import CollectionState
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import DeltaruneWorld

# Sets rules on entrances and advancements that are always applied
def set_rules(world: "DeltaruneWorld"):
    player = world.player
    multiworld = world.multiworld
    if world.options.include_chapter_1.value == 1:
        # if all unlocked, obviously no unlocks required
        if not world.options.randomize_chapters.current_key == "all_unlocked":
            set_rule(multiworld.get_entrance("Chapter 1 Entrance", player), lambda state: state.has("Chapter 1 Unlock", player))
        set_rule(multiworld.get_entrance("CH1: Bake Sale Entrance", player), lambda state: state.has("Bake Sale Ticket", player))
        set_rule(multiworld.get_entrance("CH1: Card Castle Entrance", player), lambda state: state.has("Castle Key", player))
        # Warp Doors obviously require, well, the warp item
        set_rule(multiworld.get_entrance("CH1: Bake Sale Warp", player), lambda state: state.has("Bake Sale Warp", player))
        set_rule(multiworld.get_entrance("CH1: Castle Warp", player), lambda state: state.has("Castle Warp", player))
        set_rule(multiworld.get_entrance("CH1: Bake Sale Warp Hub", player), lambda state: state.has("Bake Sale Warp", player))
        set_rule(multiworld.get_entrance("CH1: Castle Warp Hub", player), lambda state: state.has("Castle Warp", player))
        # I don't think you actually need to get to Card Castle to fix Door Key? Mewlif made this and I'm lowkirkenuinely too lazy to check :skull: 
        set_rule(multiworld.get_location("CH1: Bake Sale - Repair Door Key", player), lambda state: state.can_reach("CH1: Card Castle", "Region", player) and state.has("Broken Key A", player) and state.has("Broken Key B", player) and state.has("Broken Key C", player))
        set_rule(multiworld.get_location("CH1: Bake Sale - Repair Top Cake", player), lambda state: state.has("BrokenCake", player))
        set_rule(multiworld.get_location("CH1: Field - Return Top Cake", player), lambda state: state.has("Top Cake", player))
        set_rule(multiworld.get_location("CH1: Throw Away Manual", player), lambda state: state.has("Manual", player))
        # Jevil requires Door Key
        set_rule(multiworld.get_location("CH1: Card Castle - Jevil Defeat Item #1", player), lambda state: state.has("Door Key", player))
        set_rule(multiworld.get_location("CH1: Card Castle - Jevil Defeat Item #2", player), lambda state: state.has("Door Key", player))
        set_rule(multiworld.get_location("CH1: Card Castle - Jevil Defeat Item #3", player), lambda state: state.has("Door Key", player))
        # Need to be able to get to Jevil to get Seam to talk about him
        set_rule(multiworld.get_location("CH1: Seam's Seap - Talk About Strange Prisoner", player), lambda state: state.can_reach("CH1: Card Castle", "Region", player))
        # sets "mandatory" secret boss logic
        if world.options.randomize_secret_bosses.current_key == "mandatory":
            # There are better ways to do this, but for now this if statement works.
            if world.options.include_chapter_2.value == 0 and world.options.include_chapter_3.value == 0 and world.options.include_chapter_4.value == 0:
                # No future chapters = put macguffin items in logic as well as the secret boss item
                set_rule(multiworld.get_entrance("CH1: Light World Entrance", player), lambda state: state.has("King-Shaped Key Piece", player, world.options.goal_macguffin_amount.value) and state.has("Door Key", player))
            else:
                # Locked behind secret boss item if set to mandatory
                set_rule(multiworld.get_entrance("CH1: Light World Entrance", player), lambda state: state.has("Door Key", player))
        elif world.options.include_chapter_2.value == 0 and world.options.include_chapter_3.value == 0 and world.options.include_chapter_4.value == 0:
            # No future chapters = put macguffin items in logic, but if not "mandatory" then no secret boss items required
            set_rule(multiworld.get_entrance("CH1: Light World Entrance", player), lambda state: state.has("King-Shaped Key Piece", player, world.options.goal_macguffin_amount.value))
    if world.options.include_chapter_2.value == 1:
        # if all unlocked, obviously no unlocks required
        if not world.options.randomize_chapters.current_key == "all_unlocked":
            set_rule(multiworld.get_entrance("Chapter 2 Entrance", player), lambda state: state.has("Chapter 2 Unlock", player))
        # if you play in order and play chapter 1 first, you don't get the white ribbon Ralsei starts with
        if world.options.include_chapter_1.value == 1 and world.options.randomize_chapters.current_key == "in order":
            set_rule(multiworld.get_location("CH2: Castle Town - Twin Ribbon Fusion", player), lambda state: state.has("Pink Ribbon", player) and state.has("White Ribbon", player))
        else:
            set_rule(multiworld.get_location("CH2: Castle Town - Twin Ribbon Fusion", player), lambda state: state.has("Pink Ribbon", player))
        if world.options.include_chapter_1.value == 1:
            set_rule(multiworld.get_location("CH2: Castle Town - Spike Band Fusion", player), lambda state: state.has("IronShackle", player) and state.has("GlowWrist", player))
        set_rule(multiworld.get_location("CH2: Castle Town - TensionBow Fusion", player), lambda state: state.has("TensionBit", player) and state.has("B.ShotBowtie", player))
        set_rule(multiworld.get_entrance("CH2: Cyber City Entrance", player), lambda state: state.has("Safety Vest", player))
        # sets "mandatory" secret boss logic. This doesn't apply in weird route since you have to fight Spamton NEO anyway
        if world.options.randomize_secret_bosses.current_key == "mandatory" and not world.options.chosen_route.current_key == "weird_route":
            # There are better ways to do this, but for now this if statement works.
            if world.options.include_chapter_3.value == 0 and world.options.include_chapter_4.value == 0:
                # No future chapters = put macguffin items in logic as well as the secret boss item
                set_rule(multiworld.get_entrance("CH2: Post-Chapter Castle Town Entrance", player), lambda state: state.has("KeyGen 2 Segment", player, world.options.goal_macguffin_amount.value) and state.has("EmptyDisk", player) and state.has("KeyGen", player))
            else:
                # Locked behind secret boss item if set to mandatory
                set_rule(multiworld.get_entrance("CH2: Post-Chapter Castle Town Entrance", player), lambda state: state.has("EmptyDisk", player) and state.has("KeyGen", player))
        elif world.options.include_chapter_3.value == 0 and world.options.include_chapter_4.value == 0:
            # No future chapters = put macguffin items in logic, but if not "mandatory" then no secret boss items required
            set_rule(multiworld.get_entrance("CH2: Post-Chapter Castle Town Entrance", player), lambda state: state.has("KeyGen 2 Segment", player, world.options.goal_macguffin_amount.value))
        # Mansion locked behind Mansion reservation normally
        if world.options.chosen_route.current_key == "all_recruits" or world.options.chosen_route.current_key == "all_routes":
            set_rule(multiworld.get_entrance("CH2: Mansion Entrance", player), lambda state: state.has("Mansion Reservation", player))
            # You need the KeyGen for basement checks
            set_rule(multiworld.get_location("CH2: Mansion - Basement Chest", player), lambda state: state.has("KeyGen", player))
            set_rule(multiworld.get_location("CH2: Mansion - Basement Mechanism", player), lambda state: state.has("KeyGen", player))
        # Mansion locked behind ThornRing in Weird Route
        if world.options.chosen_route.current_key == "weird_route":
            set_rule(multiworld.get_entrance("CH2: Mansion Entrance", player), lambda state: state.has("ThornRing", player))
        # Normally Spamton NEO requires EmptyDisk + KeyGen
        if world.options.chosen_route.current_key == "all_recruits" or world.options.chosen_route.current_key == "all_routes":
            set_rule(multiworld.get_location("CH2: Mansion - Spamton NEO Defeat Item #1", player), lambda state: state.has("EmptyDisk", player) and state.has("KeyGen", player))
            set_rule(multiworld.get_location("CH2: Mansion - Spamton NEO Defeat Item #2", player), lambda state: state.has("EmptyDisk", player) and state.has("KeyGen", player))
            set_rule(multiworld.get_location("CH2: Mansion - Spamton NEO Defeat Item #3", player), lambda state: state.has("EmptyDisk", player) and state.has("KeyGen", player))
        # In Weird Route Spamton NEO requires getting past KeyGen 2 unless there's a later available chapter
        if world.options.chosen_route.current_key == "weird_route" and world.options.include_chapter_3.value == 0 and world.options.include_chapter_4.value == 0:
            set_rule(multiworld.get_location("CH2: Mansion - Spamton NEO Defeat Item #1", player), lambda state: state.has("KeyGen 2 Segment", player, world.options.goal_macguffin_amount.value))
            set_rule(multiworld.get_location("CH2: Mansion - Spamton NEO Defeat Item #2", player), lambda state: state.has("KeyGen 2 Segment", player, world.options.goal_macguffin_amount.value))
            set_rule(multiworld.get_location("CH2: Mansion - Spamton NEO Defeat Item #3", player), lambda state:state.has("KeyGen 2 Segment", player, world.options.goal_macguffin_amount.value))
    if world.options.include_chapter_3.value == 1:
        # if all unlocked, obviously no unlocks required
        if not world.options.randomize_chapters.current_key == "all_unlocked":
            set_rule(multiworld.get_entrance("Chapter 3 Entrance", player), lambda state: state.has("Chapter 3 Unlock", player))
        set_rule(multiworld.get_entrance("CH3: Board 2 Entrance", player), lambda state: state.has("Board 2 Game Cartridge", player))
        set_rule(multiworld.get_entrance("CH3: TV World Entrance", player), lambda state: state.has("VIP Pass", player))
        # sets "mandatory" secret boss logic.
        if world.options.randomize_secret_bosses.current_key == "mandatory":
            # There are better ways to do this, but for now this if statement works.
            if world.options.include_chapter_4.value == 0:
                # No future chapters = put macguffin items in logic as well as the secret boss item
                set_rule(multiworld.get_entrance("CH3: Cold Place Entrance", player), lambda state: state.has("Remote Battery", player, world.options.goal_macguffin_amount.value) and state.has("ShadowMantle", player) and state.has("OddController", player) and state.has("ICE KEY", player) and state.has("SHELTER KEY", player))
            else:
                # Locked behind secret boss item if set to mandatory
                set_rule(multiworld.get_entrance("CH3: Cold Place Entrance", player), lambda state: state.has("ShadowMantle", player) and state.has("OddController", player) and state.has("ICE KEY", player) and state.has("SHELTER KEY", player))
        elif world.options.include_chapter_4.value == 0:
            # No future chapters = put macguffin items in logic, but if not "mandatory" then no secret boss items required
            set_rule(multiworld.get_entrance("CH3: Cold Place Entrance", player), lambda state: state.has("Remote Battery", player, world.options.goal_macguffin_amount.value))    
        if world.options.chosen_route.current_key == "all_recruits" or world.options.chosen_route.current_key == "all_routes":
            set_rule(multiworld.get_location("CH3: TV World - Man", player), lambda state: state.has("TripTicket", player))
        # MANTLE 1 requires OddController
        set_rule(multiworld.get_location("CH3: MANTLE - Out of Bounds Chest", player), lambda state: state.has("OddController", player))
        # MANTLE 2 requires OddController and ICE KEY
        set_rule(multiworld.get_location("CH3: MANTLE - Northern Light Item", player), lambda state: state.has("OddController", player) and state.has("ICE KEY", player))
        # MANTLE 3 requires OddController and ICE KEY and SHELTER KEY
        set_rule(multiworld.get_location("CH3: MANTLE - Defeat", player), lambda state: state.has("OddController", player) and state.has("ICE KEY", player) and state.has("SHELTER KEY", player))
        set_rule(multiworld.get_location("CH3: S-Rank Room - Susie's Gift", player), lambda state: state.has("OddController", player) and state.has("ICE KEY", player) and state.has("SHELTER KEY", player))
        # Knight currently requires Shadow Mantle in logic to beat
        set_rule(multiworld.get_location("CH3: Cold Place - Knight Defeat Item #1", player), lambda state: state.has("ShadowMantle", player))
        set_rule(multiworld.get_location("CH3: Cold Place - Knight Defeat Item #2", player), lambda state: state.has("ShadowMantle", player))
    if world.options.include_chapter_4.value == 1:
        # if all unlocked, obviously no unlocks required
        if not world.options.randomize_chapters.current_key == "all_unlocked":
            set_rule(multiworld.get_entrance("Chapter 4 Entrance", player), lambda state: state.has("Chapter 4 Unlock", player))
        set_rule(multiworld.get_entrance("CH4: Dark Sanctuary (Claimb Required) Entrance", player), lambda state: state.has("ClaimbClaws", player))
        set_rule(multiworld.get_entrance("CH4: Second Sanctuary Entrance", player), lambda state: state.has("SheetMusic", player))
        # for future reference
        # if world.options.include_chapter_5.value == 0:
        set_rule(multiworld.get_entrance("CH4: Titan Fight Entrance", player), lambda state: state.has("Combination Lock Digit", player, world.options.goal_macguffin_amount.value))

# Sets rules on completion condition
def set_completion_rules(world: "DeltaruneWorld"):
    player = world.player
    multiworld = world.multiworld
# Code by my brother; Thanks!
# chapters to reach for completion condition to be true
    chapter_reach = {4: "CH4: Titan Fight",
                 3: "CH3: Cold Place",
                 2: "CH2: Post-Chapter Castle Town",
                 1: "CH1: Light World"}

# copy the chapter numbers to a list so they don't get deleted in the loop
    chapter_numbers = list(chapter_reach.keys())
# loop over the chapter numbers
    for chapter_number in chapter_numbers:
    # if world.options does not include the chapter number
        if getattr(world.options, f"include_chapter_{chapter_number}").value == 0:
        # delete that chapter from the chapters to reach
            del chapter_reach[chapter_number]

# define the completion condition function
    def completion_condition(state):
# loop over the names of the chapters to reach
        for chapter_name in chapter_reach.values():
# if the given chapter name hasn't been reached yet
            if not state.can_reach(chapter_name, "Region", player):
# return false and end the function there
                return False
# if none of the chapters to reach were not reached
# (they were all reached) then return true
        return True

# set the multiworld completion condition of the player
    # to the completion condition that was just defined above
    multiworld.completion_condition[player] = completion_condition