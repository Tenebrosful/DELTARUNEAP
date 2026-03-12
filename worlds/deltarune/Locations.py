from BaseClasses import Location
import typing
from enum import Enum
from . import DeltaruneWorld

class LocationData(typing.NamedTuple):
  id: typing.Optional[int]
  region: str

class ConditionalLocationData(typing.NamedTuple):
    id: typing.Optional[int]
    region: str
    should_be_included: typing.Callable[[DeltaruneWorld], bool]
  
class DeltaruneLocation(Location):
  game: str = "Deltarune"

    
class LocationIDs(Enum):
    ch1_unknown_hidden_item         = 1
    ch1_field_dark_candy_tree_1     = 2
    ch1_field_dark_candy_tree_2     = 3
    ch1_field_dark_candy_tree_3     = 4
    ch1_field_dark_candy_tree_4     = 5
    ch1_bake_repair_top_cake        = 6
    ch1_bake_diamond_stand          = 7
    ch1_bake_heart_stand            = 8
    ch1_bake_spade_stand            = 9
    ch1_card_castle_rudinn_gift     = 10
    ch1_field_return_top_cake       = 11
    ch1_castle_town_manual          = 12
    ch1_field_maze_of_death_chest       = 13
    ch1_field_chest_before_great_board  = 14
    ch1_forest_scissor_dancers_chest    = 15
    ch1_forest_hidden_chest_near_dancers   = 16
    ch1_forest_coat_rack_chest             = 17
    ch1_forest_letter_block_chest          = 18
    ch1_forest_chest_near_worm             = 19
    ch1_card_castle_2f_chest        = 20
    ch1_card_castle_4f_chest        = 21
    ch1_throw_away_manual           = 22
    ch1_field_brokencake            = 23
    ch1_forest_man                  = 24
    ch1_card_castle_jevil_1         = 25
    ch1_card_castle_jevil_2         = 26
    ch1_card_castle_jevil_3         = 27
    ch1_bake_repair_door_key        = 28
    ch1_seam_seap_talk_about_strange_prisoner = 29
    ch1_card_castle_ironshackle     = 30
    ch1_field_warp_door             = 31
    ch1_forest_warp_door            = 32
    ch1_bake_sale_warp_door         = 33
    ch1_card_castle_warp_door       = 34
    ch1_card_castle_moss            = 35
    ch2_castle_town_jigsaw_joe_challenge        = 36
    ch2_castle_town_graze_challenge_1           = 37
    ch2_castle_town_clover_rematch_challenge    = 38
    ch2_castle_town_top_chef_gift               = 39
    cc_castle_town_dd_burger_fusion             = 40
    ch2_castle_town_silver_card_fusion          = 41
    ch2_castle_town_spike_band_fusion           = 42
    ch2_cyber_field_first_chest                 = 43
    ch2_cyber_field_nubert_chest                = 44
    ch2_cyber_field_tasque_maze_checkmark       = 45
    ch2_cyber_field_chest_near_music_shop       = 46
    ch2_cyber_field_virovirokun_puzzle_chest    = 47
    ch2_cyber_field_teacup_puzzle_chest         = 48
    ch2_recruit_werewire    = 49
    ch1_seam_seap_1         = 50
    ch1_seam_seap_2         = 51
    ch1_seam_seap_3         = 52
    ch1_seam_seap_4         = 53
    ch2_recruit_tasque      = 54
    ch2_recruit_virovirokun = 55
    ch2_trash_zone_trash_can    = 56
    ch2_cyber_city_trash_can_1  = 57
    ch2_cyber_city_trash_can_2  = 58
    ch2_cyber_city_queen_poster_chest = 59
    ch1_rouxls_shop_1       = 60
    ch1_rouxls_shop_2       = 61
    ch1_rouxls_shop_3       = 62
    ch1_rouxls_shop_4       = 63
    ch2_cyber_city_chest_guarded_by_virovirokun = 64
    ch2_cyber_city_purchase_mannequin           = 65
    ch2_cyber_city_annoying_dog                 = 66
    ch2_cyber_city_man                          = 67
    ch2_cyber_city_cheese_maze_chest            = 68
    ch2_cyber_city_trash_can_3                  = 69
    ch2_music_shop_1        = 70
    ch2_music_shop_2        = 71
    ch2_music_shop_3        = 72
    ch2_music_shop_4        = 73
    ch2_cyber_city_trash_can_4 = 74
    ch2_cyber_city_trash_can_5 = 75
    ch2_recruit_poppup      = 76
    ch2_recruit_ambyu_lance = 77
    ch2_recruit_maus        = 78
    ch2_mansion_painting_chest = 79
    ch2_swatchs_cafe_1      = 80
    ch2_swatchs_cafe_2      = 81
    ch2_swatchs_cafe_3      = 82
    ch2_swatchs_cafe_4      = 83
    ch2_mansion_sculpture_room_chest    = 84
    ch2_mansion_platter_chest           = 85
    ch2_mansion_tunnel_of_love_chest    = 86
    ch2_recruit_swatchling              = 87
    ch2_recruit_tasque_manager          = 88
    ch2_recruit_mauswheel               = 89
    ch2_spamtons_shop_1     = 90
    ch2_spamtons_shop_2     = 91
    ch2_spamtons_shop_3     = 92
    ch2_spamtons_shop_4     = 93
    ch2_recruit_werewerewire                = 94
    ch2_mansion_basement_chest              = 95
    ch2_mansion_basement_mechanism          = 96
    ch2_mansion_spamton_neo_defeat_item_1   = 97
    ch2_mansion_spamton_neo_defeat_item_2   = 98
    ch2_mansion_spamton_neo_defeat_item_3   = 99
    ch2_castle_town_tasque_manager_says_challenge = 100
    ch2_castle_town_all_stars_challenge     = 101
    cc_castle_town_twin_ribbon_fusion       = 102
    cc_castle_town_tension_bow_fusion       = 103
    ch2_cyber_field_warp_door               = 104
    ch2_trash_zone_warp_door                = 105
    ch2_mansion_warp_door                   = 106
    ch2_cyber_city_moss                     = 107
    ch2_cyber_city_purchase_kris_tea        = 108
    ch2_cyber_city_purchase_noelle_tea      = 109
    ch2_cyber_city_purchase_susie_tea       = 110
    ch2_cyber_city_purchase_ralsei_tea      = 111
    ch2_cyber_city_purchase_freezering      = 112
    ch2_cyber_city_purchase_thornring       = 113
    ch3_couch_cliffs_dust_pile_chest        = 114
    ch3_board_1_c_rank      = 115
    ch3_board_1_b_rank      = 116
    ch3_board_1_a_rank      = 117
    ch3_board_1_s_rank      = 118
    ch3_board_1_t_rank      = 119
    ch3_green_room_vending_machine_1 = 120
    ch3_green_room_vending_machine_2 = 121
    ch3_green_room_vending_machine_3 = 122
    ch3_green_room_vending_machine_4 = 123
    ch3_green_room_vending_machine_5 = 124
    ch3_green_room_vending_machine_6 = 125
    ch3_green_room_vending_machine_7 = 126
    ch3_green_room_vending_machine_8 = 127
    ch3_green_room_board_1_ramb_gift = 128
    ch3_recruit_watercooler = 129
    ch3_b_rank_room_golden_prize_1 = 130
    ch3_b_rank_room_golden_prize_2 = 131
    ch3_b_rank_room_golden_prize_3 = 132
    ch3_b_rank_room_golden_prize_4 = 133
    ch3_b_rank_room_golden_prize_5 = 134
    #nothing = 135
    ch3_s_rank_room_person_behind_curtain = 136
    ch3_s_rank_room_vending_machine_1 = 137
    ch3_s_rank_room_vending_machine_2 = 138
    ch3_s_rank_room_vending_machine_3 = 139
    ch3_s_rank_room_vending_machine_4 = 140
    ch3_s_rank_room_oddcontroller = 141
    ch3_board_2_c_rank      = 142
    ch3_board_2_b_rank      = 143
    ch3_board_2_a_rank      = 144
    ch3_board_2_s_rank      = 145
    ch3_board_2_t_rank      = 146
    ch3_green_room_board_2_ramb_gift = 147
    ch3_tv_world_chest_near_shadowmen = 148
    ch3_tv_world_board_puzzle_1 = 149
    ch3_tv_world_trash_can_1 = 150
    ch3_tv_world_trash_can_2 = 151
    ch3_tv_world_trash_can_3 = 152
    ch3_water_cooler_chest = 153
    ch3_tv_world_trash_can_4 = 154
    ch3_tv_world_trash_can_5 = 155
    ch3_tv_world_board_puzzle_2 = 156
    ch3_tv_world_serious_trashy_chest = 157
    ch3_tv_world_bonus_zone_chest_1 = 158
    ch3_tv_world_bonus_zone_chest_2 = 159
    ch3_tv_world_bonus_zone_chest_3 = 160
    ch3_recruit_elnina = 161
    ch3_recruit_lanino = 162
    ch3_tv_world_chest_outside_green_room = 163
    ch3_recruit_shadowguy = 164
    ch3_recruit_shuttah = 165
    ch3_recruit_zapper = 166
    ch3_recruit_ribbick = 167
    ch3_recruit_pippins = 168
    ch3_tv_world_tripticket = 169
    ch3_tv_world_man = 170
    ch3_mantle_defeat = 171
    ch3_cold_place_knight_defeat_item_1 = 172
    ch3_cold_place_knight_defeat_item_2 = 173
    ch3_couch_cliffs_warp_door = 174
    ch3_green_room_warp_door = 175
    ch3_tv_world_entrance_warp_door = 176
    ch3_tv_world_goulden_sam_warp_door = 177
    #nothing = 178
    ch3_board_1_extra_key = 179
    ch3_board_2_extra_photo = 180
    ch3_board_2_moss = 181
    ch3_mantle_out_of_bounds_chest = 182
    ch3_mantle_northern_light_item = 183
    ch3_s_rank_room_susie_gift = 184
    ch1_fountain_seal = 185
    ch2_fountain_seal = 186
    ch3_fountain_seal = 187
    ch4_castle_town_lanino_elnina_challenge = 188
    ch4_castle_town_top_chef_gift = 189
    ch4_dark_sanctuary_jockington_prophecy_chest = 190
    ch4_dark_sanctuary_chest_in_first_dark_area = 191
    ch4_old_man_shop_1 = 192
    ch4_old_man_shop_2 = 193
    ch4_old_man_shop_3 = 194
    ch4_old_man_shop_4 = 195
    ch4_dark_sanctuary_library_chest_1 = 196
    ch4_dark_sanctuary_worship_room_chest = 197
    ch4_dark_sanctuary_lantern_puzzle_chest = 198
    ch4_dark_sanctuary_library_chest_2 = 199
    ch4_dark_sanctuary_jackenstein_gift = 200
    ch4_dark_santuary_climbing_tutorial_chest = 201
    ch4_dark_sanctuary_cuptain_pillar_chest = 202
    ch4_dark_sanctuary_sleeping_mizzle_chest = 203
    ch4_dark_sanctuary_hidden_climbing_chest = 204
    ch4_dark_sanctuary_sheet_music = 205
    ch4_dark_sanctuary_hammer_of_justice_defeat_item_1 = 206
    ch4_dark_sanctuary_hammer_of_justice_defeat_item_2 = 207
    ch4_dark_sanctuary_fontain_seal = 208
    ch4_second_sanctuary_wall_climbing_chest = 209
    ch4_second_sanctuary_waterfall_chest = 210
    ch4_second_sanctuary_man = 211
    ch4_second_sanctuary_gallery_prohecy_chest = 212
    ch4_second_sanctuary_fountain_seal = 213
    ch4_dark_sanctuary_annoying_dog = 214
    ch4_third_sanctuary_speed_climbing_chest = 215
    ch4_third_sanctuary_dark_area_chest = 216
    ch4_recruit_guei = 217
    ch4_recruit_balthizard = 218
    ch4_recruit_bibliox = 219
    ch4_recruit_mizzle = 220
    ch4_recruit_miss_mizzle = 221
    ch4_recruit_wicabel = 222
    ch4_recruit_winglade = 223
    ch4_recruit_organikk = 224
    ch4_third_sanctuary_fontain_seal = 225
    ch4_second_sanctuary_moss = 226
    ch4_third_sanctuary_titan_defeat = 227
    ch4_second_sanctuary_destroyed_piano_block_chest = 228
    ch2_cyber_field_teacup_ride_checkmark = 229
    ch2_cyber_field_giasfelfebrehber_checkmark = 230
    
    
    ch2_lost_werewire = 1049
    ch2_lost_tasque = 1054
    ch2_lost_virovirokun = 1055
    ch2_lost_poppup = 1076
    ch2_lost_ambyu_lance = 1077
    ch2_lost_maus = 1078
    ch2_lost_tasque_manager = 1088
    ch2_lost_mauswheel = 1089
    ch2_lost_werewerewire = 1094
    ch3_lost_water_cooler = 1129
    ch3_lost_shadowguy = 1164
    ch3_lost_shuttah = 1165
    ch3_lost_zapper = 1166
    ch3_lost_ribbick = 1167
    ch3_lost_pippins = 1168
    ch4_lost_guei = 1217
    ch4_lost_balthizard = 1218
    ch4_lost_bibliox = 1219
    ch4_lost_mizzle = 1220
    ch4_lost_miss_mizzle = 1221
    ch4_lost_wicabel = 1222
    ch4_lost_winglade = 1223
    ch4_lost_organikk = 1224

exclusion_table = {
    "t_rank": {
        "CH3: Board 1 T-Rank",
        "CH3: Board 2 T-Rank",
    },
    "all_routes": {
    },
    "least_recruits": {
        "CH2: Recruit Werewire",
        "CH2: Recruit Tasque",
        "CH2: Recruit Virovirokun",
        "CH2: Recruit Poppup",
        "CH2: Recruit Ambyu-lance",
        "CH2: Recruit Maus",
        "CH2: Recruit Swatchling",
        "CH2: Recruit Tasque Manager",
        "CH2: Recruit Mauswheel",
        "CH2: Recruit Werewerewire",
        "CH2: Cyber City - Man",
        "CH2: Castle Town - Tasque Manager Says Challenge",
        "CH2: Castle Town - Ch2 All Stars Challenge",
        "CH3: Recruit Water Cooler",
        "CH3: Recruit Elnina",
        "CH3: Recruit Lanino",
        "CH3: Recruit Shadowguy",
        "CH3: Recruit Shuttah",
        "CH3: Recruit Zapper",
        "CH3: Recruit Ribbick",
        "CH3: Recruit Pippins",
        "CH3: TV World - TripTicket",
        "CH3: TV World - Man",
        "CH4: Recruit Guei",
        "CH4: Recruit Balthizard",
        "CH4: Recruit Bibliox",
        "CH4: Recruit Mizzle",
        "CH4: Recruit Miss Mizzle",
        "CH4: Recruit Wicabel",
        "CH4: Recruit Winglade",
        "CH4: Recruit Organikk",
    },
    "weird_route": {
        "CH2: Recruit Werewire",
        "CH2: Recruit Tasque",
        "CH2: Recruit Virovirokun",
        "CH2: Recruit Poppup",
        "CH2: Recruit Ambyu-lance",
        "CH2: Recruit Maus",
        "CH2: Recruit Swatchling",
        "CH2: Recruit Tasque Manager",
        "CH2: Recruit Mauswheel",
        "CH2: Recruit Werewerewire",
        "CH2: Cyber City - Purchase Mannequin",
        "CH2: Cyber City - Annoying Dog...?",
        "CH2: Cyber City - Man",
        "CH2: Swatch's Cafe 1",
        "CH2: Swatch's Cafe 2",
        "CH2: Swatch's Cafe 3",
        "CH2: Swatch's Cafe 4",
        "CH2: Mansion - Sculpture Room Chest",
        "CH2: Mansion - Platter Chest",
        "CH2: Mansion - Painting Chest",
        "CH2: Mansion - Tunnel of Love Chest",
        "CH2: Spamton's Shop 1",
        "CH2: Spamton's Shop 2",
        "CH2: Spamton's Shop 3",
        "CH2: Spamton's Shop 4",
        "CH2: Mansion - Basement Chest",
        "CH2: Mansion - Basement Mechanism",
        "CH2: Castle Town - Tasque Manager Says Challenge",
        "CH2: Castle Town - Ch2 All Stars Challenge",
        "CH2: Cyber City - Purchase Kris Tea",
        "CH2: Cyber City - Purchase Noelle Tea",
        "CH2: Cyber City - Purchase Susie Tea",
        "CH2: Cyber City - Purchase Ralsei Tea",
        "CH2: Cyber City - Moss",
        "CH2: Castle Town - TensionBow Fusion",
        "CH3: Recruit Water Cooler",
        "CH3: Recruit Shadowguy",
        "CH3: Recruit Shuttah",
        "CH3: Recruit Zapper",
        "CH3: Recruit Ribbick",
        "CH3: Recruit Pippins",
        "CH3: TV World - TripTicket",
        "CH3: TV World - Man",
        "CH4: Recruit Guei",
        "CH4: Recruit Balthizard",
        "CH4: Recruit Bibliox",
        "CH4: Recruit Mizzle",
        "CH4: Recruit Miss Mizzle",
        "CH4: Recruit Wicabel",
        "CH4: Recruit Winglade",
        "CH4: Recruit Organikk",
    },
    "all_recruits": {
        """CH2: Cyber City - "Purchase" FreezeRing""",
        "CH2: Cyber City - Purchase ThornRing",
        "CH2: Lost Werewire",
        "CH2: Lost Tasque",
        "CH2: Lost Virovirokun",
        "CH2: Lost Poppup",
        "CH2: Lost Ambyu-lance",
        "CH2: Lost Maus",
        "CH2: Lost Tasque Manager",
        "CH2: Lost Mauswheel",
        "CH2: Lost Werewerewire",
        "CH3: Lost Water Cooler",
        "CH3: Lost Shadowguy",
        "CH3: Lost Shuttah",
        "CH3: Lost Zapper",
        "CH3: Lost Ribbick",
        "CH3: Lost Pippins",
        "CH4: Lost Guei",
        "CH4: Lost Balthizard",
        "CH4: Lost Bibliox",
        "CH4: Lost Mizzle",
        "CH4: Lost Miss Mizzle",
        "CH4: Lost Wicabel",
        "CH4: Lost Winglade",
        "CH4: Lost Organikk",
    }
}

events_table = {
}
