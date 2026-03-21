from worlds.deltarune.Regions import link_deltarune_areas

from .Items import DeltaruneItem, ItemData, ConditionalItemData
from .Rules import set_completion_rules
from .Locations import LocationData, ConditionalLocationData
from BaseClasses import ItemClassification, Tutorial
from .Options import DeltaruneOptions, RandomizeChapterOptions, ChosenRouteOptions, RandomizeSecretBossesOptions, RandomizeMANTLEOptions
from worlds.AutoWorld import World, WebWorld
from worlds.LauncherComponents import components, Component, Type, icon_paths
from multiprocessing import Process

from .cross_chapter import Items as CCItems, LocationsAndRegions as CCLocationsAndRegions, Rules as CCRules
from .chapter_1 import LocationsAndRegions as Ch1LocationAndRegions, Rules as Ch1Rules, Items as Ch1Items
from .chapter_2 import LocationsAndRegions as Ch2LocationAndRegions, Rules as Ch2Rules, Items as Ch2Items
from .chapter_3 import LocationsAndRegions as Ch3LocationAndRegions, Rules as Ch3Rules, Items as Ch3Items
from .chapter_4 import LocationsAndRegions as Ch4LocationAndRegions, Rules as Ch4Rules, Items as Ch4Items

def run_client():
    print('running deltarune client')
    from .DeltaruneClient import main  # lazy import
    p = Process(target=main)
    p.start()


# components.append(Component("DELTARUNE Client", "DELTARUNEClient"))
components.append(Component("DELTARUNE Client",
                            func=run_client,
                            component_type=Type.CLIENT,
                            icon="deltarune"))

#I apologize for the name of the icon - Emerald
icon_paths["deltarune"] = f"ap:{__name__}/icons/gay_deltarune.png"

max_deltarune_chapter = 4
fusion_access_chapter = [2, 4]

every_items: dict[str, ItemData | ConditionalItemData] = {
    **CCItems.cross_chapter_items,
    **CCItems.cross_chapter_conditional_items,
    **Ch1Items.chapter1_items,
    **Ch1Items.chapter1_conditional_items,
    **Ch2Items.chapter2_items,
    **Ch2Items.chapter2_conditional_items,
    **Ch3Items.chapter3_items,
    **Ch3Items.chapter3_conditional_items,
    **Ch4Items.chapter4_items,
    **Ch4Items.chapter4_conditional_items,
}

every_locations: dict[str, LocationData | ConditionalItemData] = {
    **CCLocationsAndRegions.cross_chapter_locations,
    **CCLocationsAndRegions.cross_chapter_conditional_locations,
    **Ch1LocationAndRegions.chapter1_locations,
    **Ch1LocationAndRegions.chapter1_conditional_locations,
    **Ch2LocationAndRegions.chapter2_locations,
    **Ch2LocationAndRegions.chapter2_conditional_locations,
    **Ch3LocationAndRegions.chapter3_locations,
    **Ch3LocationAndRegions.chapter3_conditional_locations,
    **Ch4LocationAndRegions.chapter4_locations,
    **Ch4LocationAndRegions.chapter4_conditional_locations,
}

def data_path(file_name: str):
    import pkgutil
    return pkgutil.get_data(__name__, "data/" + file_name)


class DeltaruneWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Archipelago DELTARUNE software on your computer. This guide covers "
        "single-player, multiworld, and related software.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Mewlif"]
    )]


class DeltaruneWorld(World):
    """
    DELTARUNE is an RPG.
    """
    game = "DELTARUNE"
    options_dataclass = DeltaruneOptions
    options: DeltaruneOptions
    web = DeltaruneWeb()

    item_name_to_id = {name: data.code for name, data in every_items.items()}
    location_name_to_id = {name: data.id for name, data in every_locations.items()}

    def _get_deltarune_data(self):
        return {
            "world_seed": self.random.getrandbits(32),
            "seed_name": self.multiworld.seed_name,
            "player_name": self.multiworld.get_player_name(self.player),
            "player_id": self.player,
            "client_version": self.required_client_version,
            "race": self.multiworld.is_race,
            "randomize_warp_doors": bool(self.options.randomize_warp_doors.value),
            "randomize_secret_bosses": self.options.randomize_secret_bosses.current_key,
            "goal_macguffin_amount": int(self.options.goal_macguffin_amount.value),
            "include_chapter_1": bool(self.options.include_chapter_1.value),
            "include_chapter_2": bool(self.options.include_chapter_2.value),
            "include_chapter_3": bool(self.options.include_chapter_3.value),
            "include_chapter_4": bool(self.options.include_chapter_4.value),
            "include_t_rank": bool(self.options.include_t_rank.value),
            "chosen_route": self.options.chosen_route.current_key,
            "randomize_chapters": self.options.randomize_chapters.current_key,
            "include_hidden_items": bool(self.options.include_hidden_items.value),
            "death_link": bool(self.options.death_link.value),
            "item_balancing": bool(self.options.item_balancing.value),
            "include_shadow_mantle": bool(self.options.include_shadow_mantle.value),
            "randomize_mantle": bool(self.options.randomize_mantle.current_key),
        }
        
    def create_item(self, name: str) -> DeltaruneItem:
        item_data = every_items[name]

        return DeltaruneItem(name, item_data.classification, item_data.code, self.player)

    def get_filler_item_name(self):
        junk_pool: dict[str, int] = CCItems.get_filler_items(self)
        
        if self.options.include_chapter_1: junk_pool.update(Ch1Items.get_filler_items(self))
        if self.options.include_chapter_2: junk_pool.update(Ch2Items.get_filler_items(self))
        if self.options.include_chapter_3: junk_pool.update(Ch3Items.get_filler_items(self))
        if self.options.include_chapter_4: junk_pool.update(Ch4Items.get_filler_items(self))
        
        return self.random.choices(list(junk_pool.keys()), weights=list(junk_pool.values()))[0]

    def fill_slot_data(self):
        return self._get_deltarune_data()
    
    def include_chapter(self, chapter: int) -> bool:
        return getattr(self.options, f"include_chapter_{chapter}").value == 1

    def is_warps_randomized(self) -> bool:
        return self.options.randomize_warp_doors.value == 1
        
    def is_chapters_in_order(self):
        return self.options.randomize_chapters == RandomizeChapterOptions.in_order

    def is_all_chapters_unlocked(self):
        return self.options.randomize_chapters == RandomizeChapterOptions.all_unlocked
    
    def is_chapters_randomized(self):
        return self.options.randomize_chapters == RandomizeChapterOptions.randomized
    
    def is_all_recruits(self):
        return self.options.chosen_route == ChosenRouteOptions.all_recruits or self.is_all_routes()
    
    def is_weird_route(self):
        return self.options.chosen_route == ChosenRouteOptions.weird_route or self.is_all_routes()
    
    def is_all_routes(self):
        return self.options.chosen_route == ChosenRouteOptions.all_routes
    
    def is_secret_bosses_randomized(self):
        return self.options.randomize_secret_bosses == RandomizeSecretBossesOptions.true or self.is_secret_bosses_mandatory()
        
    def is_secret_bosses_mandatory(self):
        return self.options.randomize_secret_bosses == RandomizeSecretBossesOptions.mandatory
    
    def is_mantle_randomized(self):
        return self.options.randomize_mantle == RandomizeMANTLEOptions.true

    def is_mantleless(self):
        return self.options.randomize_mantle == RandomizeMANTLEOptions.mantleless

    def is_shadow_mantle_included(self):
        return self.options.include_shadow_mantle.value == 1

    def is_hidden_items_randomized(self):
        return self.options.include_hidden_items.value == 1
    
    # Check if you have at least one chapter that give you access to fusions
    def can_access_fusion(self) -> bool:
        result = self.has_at_least_one_chapter_included(fusion_access_chapter)
        return result
    
    def count_chapter_included(self, chapters=list(range(1, max_deltarune_chapter + 1))):
        count = 0
        for chapterToCheck in chapters:
            if getattr(self.options, f"include_chapter_{chapterToCheck}").value == 1: count += 1
        return count
    
    # Check if at least one of specified chapters is included
    def has_at_least_one_chapter_included(self, chapters: list[int]) -> bool:
        return any(getattr(self.options, f"include_chapter_{chapter}").value == 1 for chapter in chapters)

    def have_all_chapters_included(self, chapters: list[int]) -> bool:
        return all(getattr(self.options, f"include_chapter_{chapter}").value == 1 for chapter in chapters)
    
    def get_first_chapter(self) -> int:
        for chapterToCheck in range (1, max_deltarune_chapter + 1, 1):
            if self.include_chapter(chapterToCheck): return chapterToCheck
        return -1
    
    def get_playable_chapters(self) -> list[int]:
        playable_chapters = []
        for chapterToCheck in range(1, max_deltarune_chapter + 1, 1):
            if getattr(self.options, f"include_chapter_{chapterToCheck}"): playable_chapters.append(chapterToCheck)
        return playable_chapters
    
    def is_final_chapter(self, chapter: int) -> bool:
        for chapterToCheck in range(max_deltarune_chapter, 0, -1):
            if chapterToCheck == chapter: return True
            if getattr(self.options, f"include_chapter_{chapterToCheck}"): return False
            
    def get_previous_in_order_chapter(self, chapter:int):
        if chapter <= 1: return -1
        
        for chapterToCheck in range(chapter - 1, 0, -1):
            if getattr(self.options, f"include_chapter_{chapterToCheck}"): return chapterToCheck
        
        return -1
    
    def get_next_in_order_chapter(self, chapter:int):
        if chapter > max_deltarune_chapter: return -1
        
        for chapterToCheck in range(chapter + 1, max_deltarune_chapter + 1, 1):
            if getattr(self.options, f"include_chapter_{chapterToCheck}"): return chapterToCheck
        
        return -1
        
    def create_regions(self):
        every_connections = CCLocationsAndRegions.get_cross_chapter_mandatory_connection(self)
        
        CCLocationsAndRegions.create_regions(self)
        if self.include_chapter(1): 
            Ch1LocationAndRegions.create_regions(self)
            every_connections += Ch1LocationAndRegions.chapter1_mandatory_connections
        if self.include_chapter(2):
            Ch2LocationAndRegions.create_regions(self)
            every_connections += Ch2LocationAndRegions.chapter2_mandatory_connections
        if self.include_chapter(3):
            Ch3LocationAndRegions.create_regions(self)
            every_connections += Ch3LocationAndRegions.chapter3_mandatory_connections
        if self.include_chapter(4):
            Ch4LocationAndRegions.create_regions(self)
            every_connections += Ch4LocationAndRegions.chapter4_mandatory_connections
        # if self.include_chapter(5): Ch5LocationAndRegions.create_regions(self)
        # if self.include_chapter(6): Ch6LocationAndRegions.create_regions(self)
        # if self.include_chapter(7): Ch7LocationAndRegions.create_regions(self)
        
        link_deltarune_areas(self.multiworld, self.player, every_connections)
        
    def create_items(self):
        if self.get_playable_chapters() == []:
            self.multiworld.push_precollected(self.create_item(CCItems.CCItems.what_interresting_behavior))
            return
        
        item_pool: list[str] = []
        
        item_pool += CCItems.create_items(self)
        CCRules.handle_locked_items(self)
        if self.include_chapter(1):
            item_pool += Ch1Items.create_items(self)
            Ch1Rules.handle_locked_items(self)
        if self.include_chapter(2):
            item_pool += Ch2Items.create_items(self)
            Ch2Rules.handle_locked_items(self)
        if self.include_chapter(3):
            item_pool += Ch3Items.create_items(self)
            Ch3Rules.handle_locked_items(self)
        if self.include_chapter(4):
            item_pool += Ch4Items.create_items(self)
            Ch4Rules.handle_locked_items(self)
        # if self.include_chapter(5): Ch5Items.create_items(self)
        # if self.include_chapter(6): Ch6Items.create_items(self)
        # if self.include_chapter(7): Ch7Items.create_items(self)
        
        self.handle_chapter_keys(item_pool)
        self.handle_macguffins_items(item_pool)
        
        item_pool_converted = [item for item in map(lambda name: self.create_item(name), item_pool)]
        self.handle_item_unfill_and_overflows(item_pool_converted)

        self.multiworld.itempool += item_pool_converted
    
    def get_macguffins_item(self):
        if self.is_final_chapter(1): return Ch1Items.chapter1_macguffin_item
        if self.is_final_chapter(2): return Ch2Items.chapter2_macguffin_item
        if self.is_final_chapter(3): return Ch3Items.chapter3_macguffin_item
        if self.is_final_chapter(4): return Ch4Items.chapter4_macguffin_item
    
    def handle_macguffins_items(self, item_pool: list):
        item_to_add = self.get_macguffins_item()
        
        item_pool += [item_to_add] * self.options.goal_macguffin_amount
    
    def handle_chapter_keys(self, item_pool: list):
        if self.is_all_chapters_unlocked(): return
        
        starting_chapter = -1
        
        if self.is_chapters_in_order():
            starting_chapter = self.get_first_chapter()
        elif self.is_chapters_randomized():
            starting_chapter = self.random.choice(self.get_playable_chapters())
            
        if starting_chapter == -1: return
        
        item_name = f"Chapter {starting_chapter} Unlock"
        
        if self.is_chapters_randomized():
            item_pool.remove(item_name)
            
        self.multiworld.push_precollected(self.create_item(item_name))
            
    def handle_item_unfill_and_overflows(self, item_pool: list[DeltaruneItem]):
        # Remove random junk items if the item pool overflows       
        if len(item_pool) > len(self.multiworld.get_unfilled_locations(self.player)):
            print(len(item_pool) - len(self.multiworld.get_unfilled_locations(self.player)))
            while len(item_pool) > len(self.multiworld.get_unfilled_locations(self.player)):
                item_pool.remove(self.random.choice([item for item in item_pool if item.classification == ItemClassification.filler]))
                
        # Fill remaining items with randomly generated junk
        while len(item_pool) < len(self.multiworld.get_unfilled_locations(self.player)):
            item_pool.append(self.create_filler())
        
    def set_rules(self):
        CCRules.set_rules(self)
        if self.include_chapter(1): Ch1Rules.set_rules(self)
        if self.include_chapter(2): Ch2Rules.set_rules(self)
        if self.include_chapter(3): Ch3Rules.set_rules(self)
        if self.include_chapter(4): Ch4Rules.set_rules(self)
        # if self.include_chapter(5): Ch5Rules.set_rules(self)
        # if self.include_chapter(6): Ch6Rules.set_rules(self)
        # if self.include_chapter(7): Ch7Rules.set_rules(self)
        
        set_completion_rules(self)