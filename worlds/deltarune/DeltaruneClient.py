from __future__ import annotations
import os
import asyncio
import typing
import bsdiff4
import shutil

import Utils

from NetUtils import NetworkItem, ClientStatus
from worlds import deltarune
from MultiServer import mark_raw, Context, Client
from Utils import async_start

# Try importing gui_enabled in Utils first before trying to import them from CommonClient
# Core AP will be officially moving it to Utils in the future, so this is in accommodation for that
gui_loaded_from_utils: bool = False
try:
    from Utils import gui_enabled
    gui_loaded_from_utils = True
except ImportError:
    pass

tracker_loaded = False
try:
    from worlds.tracker.TrackerClient import ClientCommandProcessor, TrackerGameContext as SuperContext, get_base_parser, server_loop
    tracker_loaded = True
    
    if not gui_loaded_from_utils: from worlds.tracker.TrackerClient import gui_enabled
    print("Tracker has been found !")
except ModuleNotFoundError:
    from CommonClient import ClientCommandProcessor, CommonContext as SuperContext, get_base_parser, server_loop
    if not gui_loaded_from_utils: from CommonClient import gui_enabled
    print("Tracker hasn't been found !")

class DeltaruneCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx):
        super().__init__(ctx)

    def _cmd_resync(self):
        """Manually trigger a resync."""
        if isinstance(self.ctx, DeltaruneContext):
            self.output(f"Syncing items.")
            self.ctx.syncing = True

    def _cmd_patch(self):
        """Patch the game. Only use this command if /auto_patch fails."""
        if isinstance(self.ctx, DeltaruneContext):
            os.makedirs(name=Utils.user_path("DELTARUNE"), exist_ok=True)
            self.ctx.patch_game()
            self.output("Patched.")

    def _cmd_savepath(self, directory: str):
        """Redirect to proper save data folder. This is necessary for Linux users to use before connecting."""
        if isinstance(self.ctx, DeltaruneContext):
            self.ctx.save_game_folder = directory
            self.output("""Changed to the following directory: """ + self.ctx.save_game_folder + """
If you're connected, you'll need to reconnect.""")\
            
    def _cmd_savereset(self):
        """Reset all save data for the Archipelago version of DELTARUNE. Use BEFORE connecting."""
        if isinstance(self.ctx, DeltaruneContext):
            path = self.ctx.save_game_folder
            self.finished_game = False
            for root, dirs, files in os.walk(path):
                for file in files:
                    if "check.spot" == file or "checkbackup.spot" == file or "scout" == file:
                        os.remove(os.path.join(root, file))
                    elif file.endswith((".item", ".victory", ".route", ".mine", ".flag", ".hint", ".complete")):
                        os.remove(os.path.join(root, file))
                    elif file.startswith(("filech", "vacationmemories", "dr")):
                        os.remove(os.path.join(root, file))
            self.output("Save data reset! If you're connected, you'll need to reconnect.")

    def _cmd_chosen_route(self):
        """Use this to figure out your chosen route, if you don't know or have forgotten."""
        if isinstance(self.ctx, DeltaruneContext):
            if self.ctx.chosen_route == "all_recruits":
                self.output("""You're doing "All Recruits" - Progress through the story normally. Recruit Everyone!!!
Gaining recruits has been turned into checks.""")
            elif self.ctx.chosen_route == "weird_route":
                self.output("""You're doing "Weird Route" - Proceed through the "Weird Route" storyline while losing all possible recruits.
Losing recruits has been turned into checks.""")
            elif self.ctx.chosen_route == "all_routes":
                self.output("""You're doing "All Routes" - All checks from doing both the normal and weird route storylines exist.
Both gaining and losing recruits have been turned into checks.""")
            else:
                self.output("You'll need to connect to a Multiworld, first.")

    

    @mark_raw
    def _cmd_auto_patch(self, steaminstall: typing.Optional[str] = None):
        """Patch the game automatically."""
        if isinstance(self.ctx, DeltaruneContext):
            os.path.exists("DELTARUNE")
            for root, dirs, files in os.walk("DELTARUNE"):
                for file in files:
                    os.remove(os.path.join(root, file))
            os.makedirs(name=Utils.user_path("DELTARUNE"), exist_ok=True)
            tempInstall = steaminstall
            if not os.path.isfile(os.path.join(tempInstall, "data.win")):
                tempInstall = None
            if tempInstall is None:
                tempInstall = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\DELTARUNE"
                if not os.path.exists(tempInstall):
                    tempInstall = "C:\\Program Files\\Steam\\steamapps\\common\\DELTARUNE"
            elif not os.path.exists(tempInstall):
                tempInstall = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\DELTARUNE"
                if not os.path.exists(tempInstall):
                    tempInstall = "C:\\Program Files\\Steam\\steamapps\\common\\DELTARUNE"
            if not os.path.exists(tempInstall) or not os.path.exists(tempInstall) or not os.path.isfile(os.path.join(tempInstall, "data.win")):
                self.output("ERROR: Cannot find DELTARUNE. Please rerun the command with the correct folder."
                            " command. \"/auto_patch (Steam directory)\".")
            else:
                shutil.copytree(tempInstall, Utils.user_path("DELTARUNE"), dirs_exist_ok=True)
                self.ctx.patch_game()
                self.output("Patching successful!")


class DeltaruneContext(SuperContext):
    tags = {"AP"}
    game = "DELTARUNE"
    command_processor = DeltaruneCommandProcessor
    items_handling = 0b111
    chapters = None
    chapter1 = 0 
    chapter2 = 0
    chapter3 = 0
    chapter4 = 0
    completechapter1 = 0 
    completechapter2 = 0
    completechapter3 = 0
    completechapter4 = 0
    ranchapters = 0
    item_balancing = 0
    goal_macguffin_amount = 1
    chosen_route = 0
    mandatoryboss = 0
    mandatorymantle = 0
    save_game_folder = os.path.expandvars(r"%localappdata%/DELTARUNEAP")

    def __init__(self, server_address, password):
        super().__init__(server_address, password)
        self.finished_game = False
        self.got_deathlink = False
        self.syncing = False
        self.deathlink_status = False
        self.game = "DELTARUNE"
        self.chapters = []
        self.chosen_route = 0
        self.goal_macguffin_amount = 1
        # self.save_game_folder: files go in this path to pass data between us and the actual game
        self.save_game_folder = os.path.expandvars(r"%localappdata%/DELTARUNEAP")

    def patch_game(self):
        with open(Utils.user_path("DELTARUNE", "chapter1_windows", "data.win"), "rb") as f:
            patchedFile = bsdiff4.patch(f.read(), deltarune.data_path("ch1.bsdiff"))
        with open(Utils.user_path("DELTARUNE", "chapter1_windows", "data.win"), "wb") as f:
            f.write(patchedFile)
        with open(Utils.user_path("DELTARUNE", "chapter2_windows", "data.win"), "rb") as f:
            patchedFile = bsdiff4.patch(f.read(), deltarune.data_path("ch2.bsdiff"))
        with open(Utils.user_path("DELTARUNE", "chapter2_windows", "data.win"), "wb") as f:
            f.write(patchedFile)
        with open(Utils.user_path("DELTARUNE", "chapter3_windows", "data.win"), "rb") as f:
            patchedFile = bsdiff4.patch(f.read(), deltarune.data_path("ch3.bsdiff"))
        with open(Utils.user_path("DELTARUNE", "chapter3_windows", "data.win"), "wb") as f:
            f.write(patchedFile)
        with open(Utils.user_path("DELTARUNE", "chapter4_windows", "data.win"), "rb") as f:
            patchedFile = bsdiff4.patch(f.read(), deltarune.data_path("ch4.bsdiff"))
        with open(Utils.user_path("DELTARUNE", "chapter4_windows", "data.win"), "wb") as f:
            f.write(patchedFile)
        with open(Utils.user_path("DELTARUNE", "data.win"), "rb") as f:
            patchedFile = bsdiff4.patch(f.read(), deltarune.data_path("deltarune.bsdiff"))
        with open(Utils.user_path("DELTARUNE", "data.win"), "wb") as f:
            f.write(patchedFile)

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super().server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    def clear_deltarune_files_disconnect(self):
        path = self.save_game_folder
        self.finished_game = False
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith((".item", ".mine", ".flag", ".hint")):
                    os.remove(os.path.join(root, file))


    def clear_deltarune_files(self):
        path = self.save_game_folder
        self.finished_game = False
        for root, dirs, files in os.walk(path):
            for file in files:
                if "check.spot" == file or "scout" == file:
                    os.remove(os.path.join(root, file))
                elif file.endswith((".item", ".victory", ".route", ".mine", ".flag", ".hint", ".complete")):
                    os.remove(os.path.join(root, file))

    # no delete certain files on connect/lost connect, but disconnecting manually and closing the client still deletes all
    async def connect(self, address: typing.Optional[str] = None):
        self.clear_deltarune_files_disconnect()
        await super().connect(address)

    async def disconnect(self, allow_autoreconnect: bool = False):
        self.clear_deltarune_files_disconnect()
        await super().disconnect(allow_autoreconnect)

    async def connection_closed(self):
        self.clear_deltarune_files()
        await super().connection_closed()

    async def shutdown(self):
        self.clear_deltarune_files()
        await super().shutdown()

    def on_package(self, cmd: str, args: dict):
        super().on_package(cmd, args)
        if cmd == "Connected":
            self.game = self.slot_info[self.slot].game
        async_start(process_deltarune_cmd(self, cmd, args))

    def make_gui(self):
        ui = super().make_gui()
        ui.base_title = "Archipelago DELTARUNE Client"
        ui.logging_pairs = [
                ("Client", "Archipelago")
            ]
        return ui

    def on_deathlink(self, data: typing.Dict[str, typing.Any]):
        self.got_deathlink = True
        super().on_deathlink(data)

async def process_deltarune_cmd(ctx: DeltaruneContext, cmd: str, args: dict):
    Context.broadcast_text_all(f"{tracker_loaded}, {gui_loaded_from_utils}")
    if cmd == "Connected":
        if not os.path.exists(ctx.save_game_folder):
            os.mkdir(os.path.join(ctx.save_game_folder))\
        # Umm idk how this works but it does so you know... no touchie
        await ctx.send_msgs([{"cmd": "Get", "keys": [str(ctx.slot)+" complete chapter1",
                                                     str(ctx.slot)+" complete chapter2",
                                                     str(ctx.slot)+" complete chapter3",
                                                     str(ctx.slot)+" complete chapter4"]}])
        await ctx.send_msgs([{"cmd": "SetNotify", "keys": [str(ctx.slot)+" complete chapter1",
                                                           str(ctx.slot)+" complete chapter2",
                                                           str(ctx.slot)+" complete chapter3",
                                                           str(ctx.slot)+" complete chapter4"]}])
        # flags are files so that i can just do `file_exists("weird_route.route")` in DELTARUNE code
        ctx.chosen_route = args["slot_data"]["chosen_route"]
        filename = f"{str(ctx.chosen_route)}.route"
        with open(os.path.join(ctx.save_game_folder, filename), "w") as f:
            f.close()
        ctx.item_balancing = args["slot_data"]["item_balancing"]
        if ctx.item_balancing == 1:
            filename = f"balancing.flag"
            with open(os.path.join(ctx.save_game_folder, filename), "w") as f:
                f.close()
        ctx.deathlink_status = args["slot_data"]["death_link"]
        if ctx.deathlink_status == 1:
            filename = f"deathlink.flag"
            with open(os.path.join(ctx.save_game_folder, filename), "w") as f:
                f.close()
        ctx.mandatoryboss = args["slot_data"]["randomize_secret_bosses"]
        if ctx.mandatoryboss == "mandatory":
            filename = f"super.flag"
            with open(os.path.join(ctx.save_game_folder, filename), "w") as f:
                f.close()
            ctx.mandatorymantle = args["slot_data"]["randomize_mantle"]
            if ctx.mandatorymantle != "mantleless":
                filename = f"mantle.flag"
                with open(os.path.join(ctx.save_game_folder, filename), "w") as f:
                    f.close()
        ctx.mandatorymantle = args["slot_data"]["randomize_mantle"]
        if ctx.mandatorymantle == "mantleless":
            filename = f"nomantle.flag"
            with open(os.path.join(ctx.save_game_folder, filename), "w") as f:
                f.close()
        ctx.ranchapters = args["slot_data"]["randomize_chapters"]
        if ctx.ranchapters == "all_unlocked":
            filename = f"all.route"
            with open(os.path.join(ctx.save_game_folder, filename), "w") as f:
                f.close()
        ctx.chapter1 = args["slot_data"]["include_chapter_1"]
        if ctx.chapter1 == 1:
            filename = f"ch1.route"
            with open(os.path.join(ctx.save_game_folder, filename), "w") as f:
                f.close()
        ctx.chapter2 = args["slot_data"]["include_chapter_2"]
        if ctx.chapter2 == 1:
            filename = f"ch2.route"
            with open(os.path.join(ctx.save_game_folder, filename), "w") as f:
                f.close()
        ctx.chapter3 = args["slot_data"]["include_chapter_3"]
        if ctx.chapter3 == 1:
            filename = f"ch3.route"
            with open(os.path.join(ctx.save_game_folder, filename), "w") as f:
                f.close()
        ctx.chapter4 = args["slot_data"]["include_chapter_4"]
        if ctx.chapter4 == 1:
            filename = f"ch4.route"
            with open(os.path.join(ctx.save_game_folder, filename), "w") as f:
                f.close()
        ctx.goal_macguffin_amount = 3 #by default
        ctx.goal_macguffin_amount = args["slot_data"]["goal_macguffin_amount"]
        filename = f"macguffin_amount.flag"
        with open(os.path.join(ctx.save_game_folder, filename), "w") as f:
            f.write(str(ctx.goal_macguffin_amount))
            f.close()
        filename = f"check.spot"
        with open(os.path.join(ctx.save_game_folder, filename), "a") as f:
            for ss in set(args["checked_locations"]):
                f.write(str(ss)+"\n")
            f.close()
    elif cmd == "Retrieved":
        # makes completion data
        if str(ctx.slot)+" complete chapter1" in args["keys"]:
            if args["keys"][str(ctx.slot)+" complete chapter1"] is not None:
                ctx.completechapter1 = args["keys"][str(ctx.slot)+" complete chapter1"]
                filename = f"ch1.complete"
                with open(os.path.join(ctx.save_game_folder, filename), "w") as f:
                    f.close()
        if str(ctx.slot)+" complete chapter2" in args["keys"]:
            if args["keys"][str(ctx.slot)+" complete chapter2"] is not None:
                ctx.completechapter2 = args["keys"][str(ctx.slot)+" complete chapter2"]
                filename = f"ch2.complete"
                with open(os.path.join(ctx.save_game_folder, filename), "w") as f:
                    f.close()
        if str(ctx.slot)+" complete chapter3" in args["keys"]:
            if args["keys"][str(ctx.slot)+" complete chapter3"] is not None:
                ctx.completechapter3 = args["keys"][str(ctx.slot)+" complete chapter3"]
                filename = f"ch3.complete"
                with open(os.path.join(ctx.save_game_folder, filename), "w") as f:
                    f.close()
        if str(ctx.slot)+" complete chapter4" in args["keys"]:
            if args["keys"][str(ctx.slot)+" complete chapter4"] is not None:
                ctx.completechapter4 = args["keys"][str(ctx.slot)+" complete chapter4"]
                filename = f"ch4.complete"
                with open(os.path.join(ctx.save_game_folder, filename), "w") as f:
                    f.close()
    elif cmd == "SetReply":
        if args["value"] is not None:
            if str(ctx.slot)+" complete chapter1" == args["key"]:
                ctx.completechapter1 = args["value"]
                filename = f"ch1.complete"
                with open(os.path.join(ctx.save_game_folder, filename), "w") as f:
                    f.close()
            elif str(ctx.slot)+" complete chapter2" == args["key"]:
                ctx.completechapter2 = args["value"]
                filename = f"ch2.complete"
                with open(os.path.join(ctx.save_game_folder, filename), "w") as f:
                    f.close()
            elif str(ctx.slot)+" complete chapter3" == args["key"]:
                ctx.completechapter3 = args["value"]
                filename = f"ch3.complete"
                with open(os.path.join(ctx.save_game_folder, filename), "w") as f:
                    f.close()
            elif str(ctx.slot)+" complete chapter4" == args["key"]:
                ctx.completechapter4 = args["value"]
                filename = f"ch4.complete"
                with open(os.path.join(ctx.save_game_folder, filename), "w") as f:
                    f.close()
    if cmd == "LocationInfo":
        for l in args["locations"]:
            locationid = l.location
            filename = f"{str(locationid)}.hint"
            with open(os.path.join(ctx.save_game_folder, filename), "w") as f:
                toDraw = ""
                for i in range(20):
                    if i < len(str(ctx.item_names.lookup_in_game(l.item))):
                        toDraw += str(ctx.item_names.lookup_in_game(l.item))[i]
                    else:
                        break
                f.write(toDraw)
                f.close()
    elif cmd == "ReceivedItems":
        start_index = args["index"]

        if start_index == 0:
            ctx.items_received = []
        elif start_index != len(ctx.items_received):
            sync_msg = [{"cmd": "Sync"}]
            if ctx.locations_checked:
                sync_msg.append({"cmd": "LocationChecks",
                                 "locations": list(ctx.locations_checked)})
            if ctx.locations_scouted:
                sync_msg.append({"cmd": "LocationScouts",
                                 "locations": list(ctx.locations_scouted)})
            await ctx.send_msgs(sync_msg)
        if start_index == len(ctx.items_received):
            counter = -1
            for item in args["items"]:
                id = NetworkItem(*item).location
                while NetworkItem(*item).location < 0 and \
                        counter <= id:
                    id -= 1
                if NetworkItem(*item).location < 0:
                    counter -= 1
                filename = f"{str(id)}PLR{str(NetworkItem(*item).player)}.item"
                with open(os.path.join(ctx.save_game_folder, filename), "w") as f:
                    f.write(str(NetworkItem(*item).item))
                    f.close()
                ctx.items_received.append(NetworkItem(*item))
        ctx.watcher_event.set()

    elif cmd == "RoomUpdate":
        if "checked_locations" in args:
            filename = f"check.spot"
            with open(os.path.join(ctx.save_game_folder, filename), "a") as f:
                for ss in set(args["checked_locations"]):
                    f.write(str(ss)+"\n")
                f.close()


async def game_watcher(ctx: DeltaruneContext):
    while not ctx.exit_event.is_set():
        await ctx.update_death_link(ctx.deathlink_status)
        path = ctx.save_game_folder
        if ctx.syncing:
            for root, dirs, files in os.walk(path):
                for file in files:
                    if ".item" in file:
                        os.remove(os.path.join(root, file))
            sync_msg = [{"cmd": "Sync"}]
            if ctx.locations_checked:
                sync_msg.append({"cmd": "LocationChecks", "locations": list(ctx.locations_checked)})
            if ctx.locations_scouted:
                sync_msg.append({"cmd": "LocationScouts", "locations": list(ctx.locations_scouted)})
            await ctx.send_msgs(sync_msg)
            ctx.syncing = False
        if ctx.got_deathlink:
            ctx.got_deathlink = False
            with open(os.path.join(ctx.save_game_folder, "WelcomeToTheDead.youDied"), "w") as f:
                f.close()
        sending = []
        sendinghint = []
        victory = False
        skipped = 0
        for root, dirs, files in os.walk(path):
            for file in files:
                if "test" in file:
                    os.remove(os.path.join(root, file))
                    version_str = '.'.join(str(x) for x in Client.version)
                    await Context.broadcast_text_all(
                        f"{Context.get_aliased_name(ctx.team, ctx.slot)} (Team #{ctx.team + 1}) has tested this thing. "
                        f"Client({version_str}), {ctx.tags}.",
                        {"type": "Part", "team": ctx.team, "slot": ctx.slot})
                if "DontBeMad.mad" in file:
                    os.remove(os.path.join(root, file))
                    if "DeathLink" in ctx.tags:
                        for file in files:
                            # "skipped.smh" is a file created by DELTARUNE if you somehow skip to a future area
                            if "skipped.smh" in file:
                                os.remove(os.path.join(root, file))
                                skipped = 1
                        if skipped:
                            await ctx.send_death(f"{ctx.player_names[ctx.slot]} has attempted to skip a necessary item. Nice try.")
                        else:                           
                            await ctx.send_death()
                if "skipped.smh" in file:
                    os.remove(os.path.join(root, file))
                if "scout" == file:
                    sendinghint = []
                    try:
                        with open(os.path.join(root, file), "r") as f:
                            lines = f.readlines()
                        for l in lines:
                            if not l.rstrip('\n') == "":
                                if ctx.server_locations.__contains__(int(l)):
                                    sendinghint = sendinghint + [int(l.rstrip('\n'))]
                    finally:
                        await ctx.send_msgs([{"cmd": "LocationScouts", "locations": sendinghint,
                                                          "create_as_hint": int(2)}])
                if "check.spot" in file:
                    sending = []
                    try:
                        with open(os.path.join(root, file), "r") as f:
                            lines = f.readlines()
                        for l in lines:
                            if not l.rstrip('\n') == "":
                                sending = sending+[(int(l.rstrip('\n')))]
                    finally:
                        await ctx.send_msgs([{"cmd": "LocationChecks", "locations": sending}])
                if "victory" in file:
                    victory = True
                    os.remove(os.path.join(root, file))
                if "complete" in file:
                    if "ch1" in file and ctx.completechapter1 != 1:
                            await ctx.send_msgs([{"cmd": "Set", "key": str(ctx.slot)+" complete chapter1",
                                                  "default": 0, "want_reply": True, "operations": [{"operation": "max",
                                                                                                    "value": 1}]}])
                    elif "ch2" in file and ctx.completechapter2 != 1:
                            await ctx.send_msgs([{"cmd": "Set", "key": str(ctx.slot)+" complete chapter2",
                                                  "default": 0, "want_reply": True, "operations": [{"operation": "max",
                                                                                                    "value": 1}]}])
                    elif "ch3" in file and ctx.completechapter3 != 1:
                            await ctx.send_msgs([{"cmd": "Set", "key": str(ctx.slot)+" complete chapter3",
                                                  "default": 0, "want_reply": True, "operations": [{"operation": "max",
                                                                                                    "value": 1}]}])
                    elif "ch4" in file and ctx.completechapter4 != 1:
                            await ctx.send_msgs([{"cmd": "Set", "key": str(ctx.slot)+" complete chapter4",
                                                  "default": 0, "want_reply": True, "operations": [{"operation": "max",
                                                                                                    "value": 1}]}])
        ctx.locations_checked = sending
        ctx.locations_scouted = sendinghint
        if (not ctx.finished_game) and victory:
            await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
            ctx.finished_game = True
        await asyncio.sleep(0.1)

async def send_testy():
        """i like to test oh yeah."""
        logger.info("I am testing yippeee...")

def main():
    Utils.init_logging("DeltaruneClient", exception_logger="Client")

    async def _main():
        ctx = DeltaruneContext(None, None)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")
        asyncio.create_task(
            game_watcher(ctx), name="DeltaruneProgressionWatcher")

        if tracker_loaded:
            ctx.run_generator()
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        await ctx.exit_event.wait()
        await ctx.shutdown()

    import colorama

    colorama.init()

    asyncio.run(_main())
    colorama.deinit()


if __name__ == "__main__":
    parser = get_base_parser(description="DELTARUNE Client, for text interfacing.")
    args = parser.parse_args()
    main()
