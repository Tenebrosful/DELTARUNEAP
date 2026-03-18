from worlds.generic.Rules import set_rule, add_rule
from typing import TYPE_CHECKING
from .chapter_1.LocationsAndRegions import chapter1_end_region
from .chapter_2.LocationsAndRegions import chapter2_end_region
from .chapter_3.LocationsAndRegions import chapter3_end_region
# from .chapter_3.Locations import chapter3_end_location
# from .chapter_4.Locations import chapter4_end_location

if TYPE_CHECKING: from . import DeltaruneWorld

def set_completion_rules(world: "DeltaruneWorld"):
    player = world.player
    multiworld = world.multiworld
    # Code by my brother; Thanks!
    # chapters to reach for completion condition to be true
    chapter_reach = {
                    # 4: "CH4: Titan Fight",
                    3: chapter3_end_region,
                    2: chapter2_end_region,
                    1: chapter1_end_region
                 }

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