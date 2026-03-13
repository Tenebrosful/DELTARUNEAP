from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import DeltaruneWorld

def set_rules(world: "DeltaruneWorld"):
  player = world.player
  multiworld = world.multiworld
  
  