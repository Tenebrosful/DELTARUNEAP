from worlds.deltarune.Regions import link_deltarune_areas

from .Items import DeltaruneItem, ItemData, ConditionalItemData
from .Rules import set_completion_rules
from .Locations import LocationData, ConditionalLocationData
from BaseClasses import ItemClassification, Tutorial
from .Options import DeltaruneOptions, RandomizeChapterOptions, ChosenRouteOptions, RandomizeSecretBossesOptions
from worlds.AutoWorld import World, WebWorld
from worlds.LauncherComponents import components, Component, Type, icon_paths
from multiprocessing import Process

from .cross_chapter import Items as CCItems, LocationsAndRegions as CCLocationsAndRegions, Rules as CCRules
from .chapter_1 import LocationsAndRegions as Ch1LocationAndRegions, Rules as Ch1Rules, Items as Ch1Items

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
    **Ch1Items.chapter1_conditional_items
}

every_locations: dict[str, LocationData | ConditionalItemData] = {
    **CCLocationsAndRegions.cross_chapter_locations,
    **CCLocationsAndRegions.cross_chapter_conditional_locations,
    **Ch1LocationAndRegions.chapter1_locations
}

every_connections = CCLocationsAndRegions.cross_chapter_mandatory_connections + Ch1LocationAndRegions.chapter1_mandatory_connections

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
        }
        
    def create_item(self, name: str) -> DeltaruneItem:
        if (name.startswith("[P]")): name = name.removeprefix("[P]")
        item_data = every_items[name]
        return DeltaruneItem(name, item_data.classification, item_data.code, self.player)

    def get_filler_item_name(self):
        junk_pool: dict[str, int] = CCItems.get_filler_items(self)
        
        if self.options.include_chapter_1: junk_pool.update(Ch1Items.get_filler_items(self))
        # if self.options.include_chapter_2: junk_pool.update(Ch2Items.get_filler_items(self))
        # if self.options.include_chapter_3: junk_pool.update(Ch3Items.get_filler_items(self))
        # if self.options.include_chapter_4: junk_pool.update(Ch4Items.get_filler_items(self))
        
        return self.random.choices(list(junk_pool.keys()), weights=list(junk_pool.values()))[0]

    # def create_items(self):
    #     # Generate item pool
    #     itempool: list[str] = []
    #     # Add all required progression items
    #     playable_chapters: list[str] = []
    #     if self.options.include_chapter_1:
    #         playable_chapters += ["1"]
    #         if not (self.options.include_chapter_2 or self.options.include_chapter_3 or self.options.include_chapter_4):
    #             itempool += ["King-Shaped Key Piece"] * self.options.goal_macguffin_amount
    #         for name, num in key_items_ch1.items():
    #             itempool += [name] * num
    #         for name, num in non_key_items_ch1.items():
    #             itempool += [name] * num
    #     if self.options.include_chapter_2:
    #         playable_chapters += ["2"]
    #         if not (self.options.include_chapter_3 or self.options.include_chapter_4):
    #             itempool += ["KeyGen 2 Segment"] * self.options.goal_macguffin_amount
    #         if self.options.chosen_route.current_key == "weird_route":
    #             for name, num in key_items_ch2_weird.items():
    #                itempool += [name] * num
    #             for name, num in non_key_items_ch2_weird.items():
    #                itempool += [name] * num
    #         elif self.options.chosen_route.current_key == "all_recruits":
    #             for name, num in key_items_ch2.items():
    #                 itempool += [name] * num
    #             for name, num in non_key_items_ch2.items():
    #                 itempool += [name] * num
    #         else:
    #             for name, num in key_items_ch2_all.items():
    #                 itempool += [name] * num
    #             for name, num in non_key_items_ch2.items():
    #                 itempool += [name] * num
    #     if self.options.include_chapter_3:
    #         playable_chapters += ["3"]
    #         if not self.options.include_chapter_4:
    #             itempool += ["Remote Battery"] * self.options.goal_macguffin_amount
    #         if self.options.chosen_route.current_key == "weird_route":
    #             for name, num in key_items_ch3_weird.items():
    #                 itempool += [name] * num
    #             for name, num in non_key_items_ch3_weird.items():
    #                 itempool += [name] * num
    #         else:
    #             for name, num in key_items_ch3.items():
    #                 itempool += [name] * num
    #             for name, num in non_key_items_ch3.items():
    #                 itempool += [name] * num
    #     if self.options.include_chapter_4:
    #         playable_chapters += ["4"]
    #         # if not self.options.include_chapter_5:
    #         itempool += ["Combination Lock Digit"] * self.options.goal_macguffin_amount
    #         for name, num in key_items_ch4.items():
    #             itempool += [name] * num
    #         for name, num in non_key_items_ch4.items():
    #             itempool += [name] * num
    #     if playable_chapters == []:
    #         self.multiworld.push_precollected(self.create_item("WHAT INTERESTING BEHAVIOR."))
    #     else:
    #         if not self.options.include_hidden_items:
    #             itempool = [item for item in itempool if item not in hidden_items]
    #             if self.options.include_chapter_1:
    #                 self.multiworld.get_location("CH1: Forest - Man", self.player).place_locked_item(self.create_item("CH1 Egg"))
    #                 self.multiworld.get_location("CH1: Card Castle - Moss", self.player).place_locked_item(self.create_item("Castle Moss"))
    #                 self.multiworld.get_location("CH1: Seam's Seap - Talk About Strange Prisoner", self.player).place_locked_item(self.create_item("Broken Key A"))
    #                 self.multiworld.get_location("CH1: Field - Chest Before Great Board", self.player).place_locked_item(self.create_item("Broken Key B"))
    #                 self.multiworld.get_location("CH1: Forest - Hidden Chest Near Dancers", self.player).place_locked_item(self.create_item("Broken Key C"))
    #                 self.multiworld.get_location("CH1: Bake Sale - Repair Door Key", self.player).place_locked_item(self.create_item("Door Key"))
    #             if self.options.include_chapter_2 and not self.options.chosen_route.current_key == "weird_route":
    #                 self.multiworld.get_location("CH2: Cyber City - Man", self.player).place_locked_item(self.create_item("CH2 Egg"))
    #                 self.multiworld.get_location("CH2: Cyber City - Annoying Dog...?", self.player).place_locked_item(self.create_item("DogDollar"))
    #                 self.multiworld.get_location("CH2: Spamton's Shop 1", self.player).place_locked_item(self.create_item("KeyGen"))
    #                 self.multiworld.get_location("CH2: Mansion - Basement Mechanism", self.player).place_locked_item(self.create_item("EmptyDisk"))
    #                 self.multiworld.get_location("CH2: Cyber City - Moss", self.player).place_locked_item(self.create_item("City Moss"))
    #             if self.options.include_chapter_3:
    #                 self.multiworld.get_location("CH3: MANTLE - Out of Bounds Chest", self.player).place_locked_item(self.create_item("ICE KEY"))
    #                 self.multiworld.get_location("CH3: MANTLE - Northern Light Item", self.player).place_locked_item(self.create_item("SHELTER KEY"))
    #                 if not self.options.chosen_route.current_key == "weird_route":
    #                     self.multiworld.get_location("CH3: TV World - TripTicket", self.player).place_locked_item(self.create_item("TripTicket"))
    #                     self.multiworld.get_location("CH3: TV World - Man", self.player).place_locked_item(self.create_item("CH3 Egg"))
    #                 self.multiworld.get_location("CH3: Board 2 Moss", self.player).place_locked_item(self.create_item("Board Moss"))
    #                 self.multiworld.get_location("CH3: S-Rank Room - Person Behind Curtain", self.player).place_locked_item(self.create_item("Saber10"))
    #                 self.multiworld.get_location("CH3: B-Rank Room - Golden Prize 1", self.player).place_locked_item(self.create_item("TennaTie"))
    #                 self.multiworld.get_location("CH3: B-Rank Room - Golden Prize 2", self.player).place_locked_item(self.create_item("TensionMax"))
    #                 self.multiworld.get_location("CH3: B-Rank Room - Golden Prize 3", self.player).place_locked_item(self.create_item("Blue Ribbon"))
    #                 self.multiworld.get_location("CH3: B-Rank Room - Golden Prize 4", self.player).place_locked_item(self.create_item("ReviveMint"))
    #                 self.multiworld.get_location("CH3: B-Rank Room - Golden Prize 5", self.player).place_locked_item(self.create_item("ExecBuffet"))
    #             if self.options.include_chapter_4:
    #                 self.multiworld.get_location("CH4: Second Sanctuary - Moss", self.player).place_locked_item(self.create_item("Sacred Moss"))
    #                 self.multiworld.get_location("CH4: Second Sanctuary - Man", self.player).place_locked_item(self.create_item("CH4 Egg"))
    #                 self.multiworld.get_location("CH4: Dark Sanctuary - Annoying Dog...?", self.player).place_locked_item(self.create_item("DogDollar"))
    #         if not self.options.randomize_warp_doors:
    #             itempool = [item for item in itempool if item not in warp_doors]
    #             if self.options.include_chapter_1:
    #                 self.multiworld.get_location("CH1: Bake Sale - Warp Door", self.player).place_locked_item(self.create_item("Bake Sale Warp"))
    #                 self.multiworld.get_location("CH1: Card Castle - Warp Door", self.player).place_locked_item(self.create_item("Castle Warp"))
    #             # if self.options.include_chapter_2: (Currently Chapter 2 locations aren't randomized)
    #                 # self.multiworld.get_location("CH2: Cyber Field Warp Door", self.player).place_locked_item(self.create_item("Cyber Field Warp"))
    #                 # self.multiworld.get_location("CH2: Trash Zone Warp Door", self.player).place_locked_item(self.create_item("Trash Zone Warp"))
    #                 # self.multiworld.get_location("CH2: Mansion Warp Door", self.player).place_locked_item(self.create_item("Mansion Warp"))
    #         if self.options.randomize_secret_bosses.current_key == "false":
    #             itempool = [item for item in itempool if item not in secret_boss_rewards]
    #             if self.options.include_chapter_1:
    #                 self.multiworld.get_location("CH1: Card Castle - Jevil Defeat Item #1", self.player).place_locked_item(self.create_item("JevilsTail"))
    #                 self.multiworld.get_location("CH1: Card Castle - Jevil Defeat Item #2", self.player).place_locked_item(self.create_item("ShadowCrystal"))
    #                 self.multiworld.get_location("CH1: Card Castle - Jevil Defeat Item #3", self.player).place_locked_item(self.create_item("DevilsKnife"))
    #             if self.options.include_chapter_2:
    #                 self.multiworld.get_location("CH2: Mansion - Spamton NEO Defeat Item #1", self.player).place_locked_item(self.create_item("PuppetScarf"))
    #                 self.multiworld.get_location("CH2: Mansion - Spamton NEO Defeat Item #2", self.player).place_locked_item(self.create_item("ShadowCrystal"))
    #                 self.multiworld.get_location("CH2: Mansion - Spamton NEO Defeat Item #3", self.player).place_locked_item(self.create_item("DealMaker"))
    #             if self.options.include_chapter_3:
    #                 self.multiworld.get_location("CH3: MANTLE - Defeat", self.player).place_locked_item(self.create_item("ShadowMantle"))
    #                 self.multiworld.get_location("CH3: Cold Place - Knight Defeat Item #1", self.player).place_locked_item(self.create_item("ShadowCrystal"))
    #                 self.multiworld.get_location("CH3: Cold Place - Knight Defeat Item #2", self.player).place_locked_item(self.create_item("BlackShard"))
    #                 self.multiworld.get_location("CH3: S-Rank Room - Susie's Gift", self.player).place_locked_item(self.create_item("FlatSoda"))
    #             if self.options.include_chapter_4:
    #                 self.multiworld.get_location("CH4: Dark Sanctuary - Hammer of Justice Defeat Item #1", self.player).place_locked_item(self.create_item("ShadowCrystal"))
    #                 self.multiworld.get_location("CH4: Dark Sanctuary - Hammer of Justice Defeat Item #2", self.player).place_locked_item(self.create_item("JusticeAxe"))
    #         if self.options.randomize_chapters.current_key == "in_order":
    #             beginningrange = 0
    #             for index in range(1, 5):
    #                 if getattr(self.options, f"include_chapter_{index}").value == 1:            
    #                     beginningrange = index
    #                     break
    #             starting_chapter = beginningrange
    #             starting_key = "Chapter " + str(starting_chapter) + " Unlock"
    #             itempool.remove(starting_key)
    #             self.multiworld.push_precollected(self.create_item(starting_key))
    #             itempool = [item for item in itempool if item not in chapters]
    #             nextchapter = 0
    #             if self.options.include_chapter_1:
    #                 for index in range(2, 5):
    #                     if getattr(self.options, f"include_chapter_{index}").value == 1:            
    #                         nextchapter = index
    #                         break
    #                 if nextchapter == 0:
    #                     nextchapter = 2
    #                 self.multiworld.get_location("CH1: Card Kingdom - Fountain Sealed", self.player).place_locked_item(self.create_item(f"Chapter {nextchapter} Unlock"))
    #             if self.options.include_chapter_2:
    #                 for index in range(3, 5):
    #                     if getattr(self.options, f"include_chapter_{index}").value == 1:            
    #                         nextchapter = index
    #                         break
    #                 if nextchapter == 0:
    #                     nextchapter = 3
    #                 self.multiworld.get_location("CH2: Cyber World - Fountain Sealed", self.player).place_locked_item(self.create_item(f"Chapter {nextchapter} Unlock"))
    #             if self.options.include_chapter_3:
    #                 for index in range(4, 5):
    #                     if getattr(self.options, f"include_chapter_{index}").value == 1:            
    #                         nextchapter = index
    #                         break
    #                 if nextchapter == 0:
    #                     nextchapter = 4
    #                 self.multiworld.get_location("CH3: TV World - Fountain Sealed", self.player).place_locked_item(self.create_item(f"Chapter {nextchapter} Unlock"))
    #             if self.options.include_chapter_4:
    #                 self.multiworld.get_location("CH4: Third Sanctuary - Fountain Sealed", self.player).place_locked_item(self.create_item("This is where I would put my Chapter 5 Unlock... IF I HAD ONE!"))
    #         if self.options.include_chapter_2.value == 1 and self.options.include_chapter_1.value == 0:
    #             itempool.remove("Spikeband")
    #         if self.options.randomize_chapters.current_key == "randomized":
    #             starting_chapter = self.random.choice(playable_chapters)
    #             starting_key = "Chapter " + str(starting_chapter) + " Unlock"
    #             itempool.remove(starting_key)
    #             self.multiworld.push_precollected(self.create_item(starting_key))
    #         if self.options.randomize_chapters.current_key == "all_unlocked":
    #             if self.options.include_chapter_1:
    #                 itempool.remove("Chapter 1 Unlock")
    #             if self.options.include_chapter_2:
    #                 itempool.remove("Chapter 2 Unlock")
    #             if self.options.include_chapter_3:
    #                 itempool.remove("Chapter 3 Unlock")
    #             if self.options.include_chapter_4:
    #                 itempool.remove("Chapter 4 Unlock")
        
    #     # Choose locations to automatically exclude based on settings
    #     exclusion_pool = set()
    #     exclusion_pool.update(exclusion_table[self.options.chosen_route.current_key])
    #     if not self.options.include_t_rank:
    #         exclusion_pool.update(exclusion_table["t_rank"])
    #     exclusion_rules(self.multiworld, self.player, exclusion_pool)

    #     # Convert itempool into real items
    #     itempool_converted = [item for item in map(lambda name: self.create_item(name), itempool)]
    #     # Remove random junk items if the item pool overflows
    #     if len(itempool_converted) > len(self.multiworld.get_unfilled_locations(self.player)):
    #         print(len(itempool_converted) - len(self.multiworld.get_unfilled_locations(self.player)))
    #     while len(itempool_converted) > len(self.multiworld.get_unfilled_locations(self.player)):
    #         itempool_converted.remove(self.random.choice([item for item in itempool_converted if item.classification == ItemClassification.filler]))
    #     # Fill remaining items with randomly generated junk
    #     while len(itempool_converted) < len(self.multiworld.get_unfilled_locations(self.player)):
    #         itempool_converted.append(self.create_filler())

    #     self.multiworld.itempool += itempool_converted

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
    
    def is_hidden_items_randomized(self):
        return self.options.include_hidden_items.value == 1
    
    # Check if you have at least one chapter that give you access to fusions
    def can_access_fusion(self) -> bool:
        return self.has_at_least_one_chapter_included(fusion_access_chapter)
    
    def count_chapter_included(self, chapters=list(range(1,max_deltarune_chapter + 1))):
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
            if getattr(self.options, f"include_chapter_{chapter}"): return False
            
    def get_previous_in_order_chapter(self, chapter:int):
        if chapter <= 1: return -1
        
        for chapterToCheck in range(chapter - 1, 0, -1):
            if getattr(self.options, f"include_chapter_{chapter}"): return chapterToCheck
        
        return -1
    
    def get_next_in_order_chapter(self, chapter:int):
        if chapter > max_deltarune_chapter: return -1
        
        for chapterToCheck in range(1, max_deltarune_chapter + 1, 1):
            if getattr(self.options, f"include_chapter_{chapter}"): return chapterToCheck
        
        return -1
        
    def create_regions(self):
        CCLocationsAndRegions.create_regions(self)
        if self.include_chapter(1): Ch1LocationAndRegions.create_regions(self)
        # if self.include_chapter(2): Ch2LocationAndRegions.create_regions(self)
        # if self.include_chapter(3): Ch3LocationAndRegions.create_regions(self)
        # if self.include_chapter(4): Ch4LocationAndRegions.create_regions(self)
        # if self.include_chapter(5): Ch5LocationAndRegions.create_regions(self)
        # if self.include_chapter(6): Ch6LocationAndRegions.create_regions(self)
        # if self.include_chapter(7): Ch7LocationAndRegions.create_regions(self)
        
        link_deltarune_areas(self.multiworld, self.player, every_connections)
        
    def create_items(self):
        item_pool: list[str] = []
        
        item_pool += CCItems.create_items(self)
        if self.include_chapter(1): item_pool += Ch1Items.create_items(self)
        # if self.include_chapter(2): Ch2Items.create_items(self)
        # if self.include_chapter(3): Ch3Items.create_items(self)
        # if self.include_chapter(4): Ch4Items.create_items(self)
        # if self.include_chapter(5): Ch5Items.create_items(self)
        # if self.include_chapter(6): Ch6Items.create_items(self)
        # if self.include_chapter(7): Ch7Items.create_items(self)
        
        self.handle_chapter_keys(item_pool)
        
        item_pool_converted = [item for item in map(lambda name: self.create_item(name), item_pool)]
        self.handle_item_unfill_and_overflows(item_pool_converted)

        self.multiworld.itempool += item_pool_converted
        
    def handle_chapter_keys(self, item_pool: list):
        if self.is_all_chapters_unlocked(): return
        
        starting_chapter = -1
        
        if self.is_chapters_in_order():
            starting_chapter = self.get_first_chapter()
        elif self.options.randomize_chapters == RandomizeChapterOptions.randomized:
            starting_chapter = self.random.choice(self.get_playable_chapters())
            
        if starting_chapter == -1: return
        
        item_name = f"Chapter {starting_chapter} Unlock"

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
        # if self.include_chapter(2): Ch2Rules.set_rules(self)
        # if self.include_chapter(3): Ch3Rules.set_rules(self)
        # if self.include_chapter(4): Ch4Rules.set_rules(self)
        # if self.include_chapter(5): Ch5Rules.set_rules(self)
        # if self.include_chapter(6): Ch6Rules.set_rules(self)
        # if self.include_chapter(7): Ch7Rules.set_rules(self)
        
        set_completion_rules(self)