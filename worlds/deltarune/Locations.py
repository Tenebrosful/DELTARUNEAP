from BaseClasses import Location
import typing
from enum import Enum

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
        
class AdvData(typing.NamedTuple):
    id: typing.Optional[int]
    region: str


class DeltaruneAdvancement(Location):
    game: str = "Deltarune"


advancement_table = {
    "CH1: ?????? - Hidden Item": AdvData(1, "CH1: Castle Town"),
    "CH1: Field - Dark Candy Tree 1": AdvData(2, "CH1: Fields"),
    "CH1: Field - Dark Candy Tree 2": AdvData(3, "CH1: Fields"),
    "CH1: Field - Dark Candy Tree 3": AdvData(4, "CH1: Fields"),
    "CH1: Field - Dark Candy Tree 4": AdvData(5, "CH1: Fields"),
    "CH1: Bake Sale - Repair Top Cake": AdvData(6, "CH1: Bake Sale"),
    "CH1: Bake Sale - Diamond Stand": AdvData(7, "CH1: Bake Sale"),
    "CH1: Bake Sale - Heart Stand": AdvData(8, "CH1: Bake Sale"),
    "CH1: Bake Sale - Spade Stand": AdvData(9, "CH1: Bake Sale"),
    "CH1: Card Castle - Rudinn Gift": AdvData(10, "CH1: Card Castle"),
    "CH1: Field - Return Top Cake": AdvData(11, "CH1: Fields"),
    "CH1: Castle Town - Manual": AdvData(12, "CH1: Castle Town"),
    "CH1: Field - Maze of Death Chest": AdvData(13, "CH1: Fields"),
    "CH1: Field - Chest Before Great Board": AdvData(14, "CH1: Fields"),
    
    "CH1: Forest - Scissor Dancers Chest": AdvData(15, "CH1: Bake Sale"),
    "CH1: Forest - Hidden Chest Near Dancers": AdvData(16, "CH1: Bake Sale"),
    "CH1: Forest - Coat Rack's Chest": AdvData(17, "CH1: Forest"),
    "CH1: Forest - Letter Block Chest": AdvData(18, "CH1: Forest"),
    "CH1: Forest - Chest Near Worm": AdvData(19, "CH1: Bake Sale"),
    "CH1: Card Castle - 2F Chest": AdvData(20, "CH1: Card Castle"),
    "CH1: Card Castle - 4F Chest": AdvData(21, "CH1: Card Castle"),
    "CH1: Throw Away Manual": AdvData(22, "CH1: Castle Town"),
    "CH1: Field - BrokenCake": AdvData(23, "CH1: Fields"),
    
    "CH1: Forest - Man": AdvData(24, "CH1: Bake Sale"),
    "CH1: Card Castle - Jevil Defeat Item #1": AdvData(25, "CH1: Card Castle"),
    "CH1: Card Castle - Jevil Defeat Item #2": AdvData(26, "CH1: Card Castle"),
    "CH1: Card Castle - Jevil Defeat Item #3": AdvData(27, "CH1: Card Castle"),
    
    "CH1: Bake Sale - Repair Door Key": AdvData(28, "CH1: Bake Sale"),
    "CH1: Seam's Seap - Talk About Strange Prisoner": AdvData(29, "CH1: Fields"),
    
    "CH1: Card Castle - IronShackle": AdvData(30, "CH1: Card Castle"),
    "CH1: Field - Warp Door": AdvData(31, "CH1: Fields"),
    "CH1: Forest - Warp Door": AdvData(32, "CH1: Fields"),
    "CH1: Bake Sale - Warp Door": AdvData(33, "CH1: Bake Sale"),
    "CH1: Card Castle - Warp Door": AdvData(34, "CH1: Card Castle"),
    
    "CH1: Card Castle - Moss": AdvData(35, "CH1: Card Castle"),
    "CH2: Castle Town - Jigsaw Joe Challenge": AdvData(36, "CH2: Castle Town"),
    "CH2: Castle Town - Graze Challenge 1": AdvData(37, "CH2: Castle Town"),
    "CH2: Castle Town - Clover Rematch Challenge": AdvData(38, "CH2: Castle Town"),
    "CH2: Castle Town - Top Chef Gift": AdvData(39, "CH2: Castle Town"),
    "CH2: Castle Town - DD-Burger Fusion": AdvData(40, "CH2: Castle Town"),
    "CH2: Castle Town - Silver Card Fusion": AdvData(41, "CH2: Castle Town"),
    "CH2: Castle Town - Spike Band Fusion": AdvData(42, "CH2: Castle Town"),
    "CH2: Cyber Field - First Chest": AdvData(43, "CH2: Cyber Field"),
    "CH2: Cyber Field - Nubert's Chest": AdvData(44, "CH2: Cyber Field"),
    "CH2: Cyber Field - Tasque Maze Checkmark": AdvData(45, "CH2: Cyber Field"),
    "CH2: Cyber Field - Chest Near Music Shop": AdvData(46, "CH2: Cyber Field"),
    "CH2: Cyber Field - Virovirokun Puzzle Chest": AdvData(47, "CH2: Cyber Field"),
    "CH2: Cyber Field - Teacup Puzzle Chest": AdvData(48, "CH2: Cyber Field"),
    "CH2: Recruit Werewire": AdvData(49, "CH2: Cyber Field"),
    "CH1: Seam's Seap 1": AdvData(50, "CH1: Fields"),
    "CH1: Seam's Seap 2": AdvData(51, "CH1: Fields"),
    "CH1: Seam's Seap 3": AdvData(52, "CH1: Fields"),
    "CH1: Seam's Seap 4": AdvData(53, "CH1: Fields"),
    "CH2: Recruit Tasque": AdvData(54, "CH2: Cyber Field"),
    "CH2: Recruit Virovirokun": AdvData(55, "CH2: Cyber Field"),
    "CH2: Trash Zone - Trash Can": AdvData(56, "CH2: Cyber City"),
    "CH2: Cyber City - Trash Can #1": AdvData(57, "CH2: Cyber City"),
    "CH2: Cyber City - Trash Can #2": AdvData(58, "CH2: Cyber City"),
    "CH2: Cyber City - Queen Poster Chest": AdvData(59, "CH2: Cyber City"),    
    "CH1: Rouxls' Shop 1": AdvData(60, "CH1: Card Castle"),
    "CH1: Rouxls' Shop 2": AdvData(61, "CH1: Card Castle"),
    "CH1: Rouxls' Shop 3": AdvData(62, "CH1: Card Castle"),
    "CH1: Rouxls' Shop 4": AdvData(63, "CH1: Card Castle"),
    "CH2: Cyber City - Chest Guarded By Virovirokun": AdvData(64, "CH2: Cyber City"),
    "CH2: Cyber City - Purchase Mannequin": AdvData(65, "CH2: Cyber City"),
    "CH2: Cyber City - Annoying Dog...?": AdvData(66, "CH2: Cyber City"),
    "CH2: Cyber City - Man": AdvData(67, "CH2: Cyber City"),
    "CH2: Cyber City - Cheese Maze Chest": AdvData(68, "CH2: Cyber City"),
    "CH2: Cyber City - Trash Can #3": AdvData(69, "CH2: Cyber City"),
    "CH2: Music Shop 1": AdvData(70, "CH2: Cyber Field"),
    "CH2: Music Shop 2": AdvData(71, "CH2: Cyber Field"),
    "CH2: Music Shop 3": AdvData(72, "CH2: Cyber Field"),
    "CH2: Music Shop 4": AdvData(73, "CH2: Cyber Field"),
    "CH2: Cyber City - Trash Can #4": AdvData(74, "CH2: Cyber City"),
    "CH2: Cyber City - Trash Can #5": AdvData(75, "CH2: Cyber City"),
    "CH2: Recruit Poppup": AdvData(76, "CH2: Cyber City"),
    "CH2: Recruit Ambyu-lance": AdvData(77, "CH2: Cyber City"),
    "CH2: Recruit Maus": AdvData(78, "CH2: Cyber City"),
    "CH2: Mansion - Painting Chest": AdvData(79, "CH2: Mansion"),
    "CH2: Swatch's Cafe 1": AdvData(80, "CH2: Cyber City"),
    "CH2: Swatch's Cafe 2": AdvData(81, "CH2: Cyber City"),
    "CH2: Swatch's Cafe 3": AdvData(82, "CH2: Cyber City"),
    "CH2: Swatch's Cafe 4": AdvData(83, "CH2: Cyber City"),
    "CH2: Mansion - Sculpture Room Chest": AdvData(84, "CH2: Mansion"),
    "CH2: Mansion - Platter Chest": AdvData(85, "CH2: Mansion"),
    "CH2: Mansion - Tunnel of Love Chest": AdvData(86, "CH2: Mansion"),
    "CH2: Recruit Swatchling": AdvData(87, "CH2: Mansion"),
    "CH2: Recruit Tasque Manager": AdvData(88, "CH2: Mansion"),
    "CH2: Recruit Mauswheel": AdvData(89, "CH2: Mansion"),
    "CH2: Spamton's Shop 1": AdvData(90, "CH2: Cyber City"),
    "CH2: Spamton's Shop 2": AdvData(91, "CH2: Cyber City"),
    "CH2: Spamton's Shop 3": AdvData(92, "CH2: Cyber City"),
    "CH2: Spamton's Shop 4": AdvData(93, "CH2: Cyber City"),
    "CH2: Recruit Werewerewire": AdvData(94, "CH2: Mansion"),
    "CH2: Mansion - Basement Chest": AdvData(95, "CH2: Mansion"),
    "CH2: Mansion - Basement Mechanism": AdvData(96, "CH2: Mansion"),
    "CH2: Mansion - Spamton NEO Defeat Item #1": AdvData(97, "CH2: Mansion"),
    "CH2: Mansion - Spamton NEO Defeat Item #2": AdvData(98, "CH2: Mansion"),
    "CH2: Mansion - Spamton NEO Defeat Item #3": AdvData(99, "CH2: Mansion"),
    "CH2: Castle Town - Tasque Manager Says Challenge": AdvData(100, "CH2: Post-Chapter Castle Town"),
    "CH2: Castle Town - Ch2 All Stars Challenge": AdvData(101, "CH2: Post-Chapter Castle Town"),
    "CH2: Castle Town - Twin Ribbon Fusion": AdvData(102, "CH2: Castle Town"),
    "CH2: Castle Town - TensionBow Fusion": AdvData(103, "CH2: Castle Town"),
    "CH2: Cyber Field - Warp Door": AdvData(104, "CH2: Cyber Field"),
    "CH2: Trash Zone - Warp Door": AdvData(105, "CH2: Cyber City"),
    "CH2: Mansion - Warp Door": AdvData(106, "CH2: Mansion"),
    "CH2: Cyber City - Moss": AdvData(107, "CH2: Cyber City"),
    "CH2: Cyber City - Purchase Kris Tea": AdvData(108, "CH2: Cyber City"),
    "CH2: Cyber City - Purchase Noelle Tea": AdvData(109, "CH2: Cyber City"),
    "CH2: Cyber City - Purchase Susie Tea": AdvData(110, "CH2: Cyber City"),
    "CH2: Cyber City - Purchase Ralsei Tea": AdvData(111, "CH2: Cyber City"),
    """CH2: Cyber City - "Purchase" FreezeRing""": AdvData(112, "CH2: Cyber City"),
    "CH2: Cyber City - Purchase ThornRing": AdvData(113, "CH2: Cyber City"),
    "CH3: Couch Cliffs - Dust Pile Chest": AdvData(114, "CH3: Couch Cliffs"),
    "CH3: Board 1 C-Rank": AdvData(115, "CH3: Board 1"),
    "CH3: Board 1 B-Rank": AdvData(116, "CH3: Board 1"),
    "CH3: Board 1 A-Rank": AdvData(117, "CH3: Board 1"),
    "CH3: Board 1 S-Rank": AdvData(118, "CH3: Board 1"),
    "CH3: Board 1 T-Rank": AdvData(119, "CH3: Board 1"),
    "CH3: Green Room - Vending Machine 1": AdvData(120, "CH3: Green Room"),
    "CH3: Green Room - Vending Machine 2": AdvData(121, "CH3: Green Room"),
    "CH3: Green Room - Vending Machine 3": AdvData(122, "CH3: Green Room"),
    "CH3: Green Room - Vending Machine 4": AdvData(123, "CH3: Green Room"),
    "CH3: Green Room - Vending Machine 5": AdvData(124, "CH3: Green Room"),
    "CH3: Green Room - Vending Machine 6": AdvData(125, "CH3: Green Room"),
    "CH3: Green Room - Vending Machine 7": AdvData(126, "CH3: Green Room"),
    "CH3: Green Room - Vending Machine 8": AdvData(127, "CH3: Green Room"),
    "CH3: Green Room - Board 1 Ramb Gift": AdvData(128, "CH3: Green Room"),
    "CH3: Recruit Water Cooler": AdvData(129, "CH3: Green Room"),
    "CH3: B-Rank Room - Golden Prize 1": AdvData(130, "CH3: Green Room"),
    "CH3: B-Rank Room - Golden Prize 2": AdvData(131, "CH3: Green Room"),
    "CH3: B-Rank Room - Golden Prize 3": AdvData(132, "CH3: Green Room"),
    "CH3: B-Rank Room - Golden Prize 4": AdvData(133, "CH3: Green Room"),
    "CH3: B-Rank Room - Golden Prize 5": AdvData(134, "CH3: Green Room"),
    "CH3: S-Rank Room - Person Behind Curtain": AdvData(136, "CH3: Green Room"),
    "CH3: S-Rank Room - Vending Machine 1": AdvData(137, "CH3: Green Room"),    
    "CH3: S-Rank Room - Vending Machine 2": AdvData(138, "CH3: Green Room"),
    "CH3: S-Rank Room - Vending Machine 3": AdvData(139, "CH3: Green Room"),
    "CH3: S-Rank Room - Vending Machine 4": AdvData(140, "CH3: Green Room"),
    "CH3: S-Rank Room - OddController": AdvData(141, "CH3: Green Room"),
    "CH3: Board 2 C-Rank": AdvData(142, "CH3: Board 2"),
    "CH3: Board 2 B-Rank": AdvData(143, "CH3: Board 2"),
    "CH3: Board 2 A-Rank": AdvData(144, "CH3: Board 2"),
    "CH3: Board 2 S-Rank": AdvData(145, "CH3: Board 2"),
    "CH3: Board 2 T-Rank": AdvData(146, "CH3: Board 2"),
    "CH3: Green Room - Board 2 Ramb Gift": AdvData(147, "CH3: Board 2"),
    "CH3: TV World - Chest Near Shadowmen": AdvData(148, "CH3: TV World"),
    "CH3: TV World - Board Puzzle 1 Chest": AdvData(149, "CH3: TV World"),
    "CH3: TV World - Trash Can #1": AdvData(150, "CH3: Goulden Sam"),
    "CH3: TV World - Trash Can #2": AdvData(151, "CH3: Goulden Sam"),
    "CH3: TV World - Trash Can #3": AdvData(152, "CH3: Goulden Sam"),
    "CH3: TV World - Water Cooler Chest": AdvData(153, "CH3: Goulden Sam"),
    "CH3: TV World - Trash Can #4": AdvData(154, "CH3: Goulden Sam"),
    "CH3: TV World - Trash Can #5": AdvData(155, "CH3: Goulden Sam"),
    "CH3: TV World - Board Puzzle 2 Chest": AdvData(156, "CH3: Goulden Sam"),
    "CH3: TV World - Serious Trashy Chest": AdvData(157, "CH3: Goulden Sam"),
    "CH3: TV World - Bonus Zone Chest 1": AdvData(158, "CH3: Goulden Sam"),
    "CH3: TV World - Bonus Zone Chest 2": AdvData(159, "CH3: Goulden Sam"),
    "CH3: TV World - Bonus Zone Chest 3": AdvData(160, "CH3: Goulden Sam"),
    "CH3: Recruit Elnina": AdvData(161, "CH3: Goulden Sam"),
    "CH3: Recruit Lanino": AdvData(162, "CH3: Goulden Sam"),
    "CH3: TV World - Chest Outside Green Room": AdvData(163, "CH3: Goulden Sam"),
    "CH3: Recruit Shadowguy": AdvData(164, "CH3: Goulden Sam"),
    "CH3: Recruit Shuttah": AdvData(165, "CH3: TV World"),
    "CH3: Recruit Zapper": AdvData(166, "CH3: Goulden Sam"),
    "CH3: Recruit Ribbick": AdvData(167, "CH3: TV World"),
    "CH3: Recruit Pippins": AdvData(168, "CH3: Board 2"),
    "CH3: TV World - TripTicket": AdvData(169, "CH3: Goulden Sam"),
    "CH3: TV World - Man": AdvData(170, "CH3: Goulden Sam"),
    "CH3: MANTLE - Defeat": AdvData(171, "CH3: Cold Place"),
    "CH3: Cold Place - Knight Defeat Item #1": AdvData(172, "CH3: Cold Place"),
    "CH3: Cold Place - Knight Defeat Item #2": AdvData(173, "CH3: Cold Place"),
    "CH3: Couch Cliffs - Warp Door": AdvData(174, "CH3: Couch Cliffs"),
    "CH3: Green Room - Warp Door": AdvData(175, "CH3: Green Room"),
    "CH3: TV World - Entrance Warp Door": AdvData(176, "CH3: TV World"),
    "CH3: TV World - Goulden Sam Warp Door": AdvData(177, "CH3: Goulden Sam"),
    "CH3: Board 1 Extra Key": AdvData(179, "CH3: Board 1"),
    "CH3: Board 2 Extra Photo": AdvData(180, "CH3: Board 2"),
    "CH3: Board 2 Moss": AdvData(181, "CH3: Board 2"),
    "CH3: MANTLE - Out of Bounds Chest": AdvData(182, "CH3: Board 1"),
    "CH3: MANTLE - Northern Light Item": AdvData(183, "CH3: Board 2"),
    "CH3: S-Rank Room - Susie's Gift": AdvData(184, "CH3: Cold Place"),
    "CH1: Card Kingdom - Fountain Sealed": AdvData(185, "CH1: Light World"),
    "CH2: Cyber World - Fountain Sealed": AdvData(186, "CH2: Post-Chapter Castle Town"),
    "CH3: TV World - Fountain Sealed": AdvData(187, "CH3: Cold Place"),
    "CH4: Castle Town - Lanino&Elnina Challenge": AdvData(188, "CH4: Castle Town"),
    "CH4: Castle Town - Top Chef Gift": AdvData(189, "CH4: Castle Town"),
    "CH4: Dark Sanctuary - Jockington Prophecy Chest": AdvData(190, "CH4: Dark Sanctuary"),
    "CH4: Dark Sanctuary - Chest in First Dark Area": AdvData(191, "CH4: Dark Sanctuary"),
    "CH4: Old Man's Shop 1": AdvData(192, "CH4: Dark Sanctuary"),
    "CH4: Old Man's Shop 2": AdvData(193, "CH4: Dark Sanctuary"),
    "CH4: Old Man's Shop 3": AdvData(194, "CH4: Dark Sanctuary"),
    "CH4: Old Man's Shop 4": AdvData(195, "CH4: Dark Sanctuary"),
    "CH4: Dark Sanctuary - Library Chest 1": AdvData(196, "CH4: Dark Sanctuary"),
    "CH4: Dark Sanctuary - Worship Room Chest": AdvData(197, "CH4: Dark Sanctuary"),
    "CH4: Dark Sanctuary - Lantern Puzzle Chest": AdvData(198, "CH4: Dark Sanctuary"),
    "CH4: Dark Sanctuary - Library Chest 2": AdvData(199, "CH4: Dark Sanctuary"),
    "CH4: Dark Sanctuary - Jackenstein Gift": AdvData(200, "CH4: Dark Sanctuary (Claimb Required)"),
    "CH4: Dark Sanctuary - Climbing Tutorial Chest": AdvData(201, "CH4: Dark Sanctuary (Claimb Required)"),
    "CH4: Dark Sanctuary - Cuptain Pillar Chest": AdvData(202, "CH4: Dark Sanctuary (Claimb Required)"),
    "CH4: Dark Sanctuary - Sleeping Mizzle Chest": AdvData(203, "CH4: Dark Sanctuary (Claimb Required)"),
    "CH4: Dark Sanctuary - Hidden Climbing Chest": AdvData(204, "CH4: Dark Sanctuary (Claimb Required)"),
    "CH4: Dark Sanctuary - Sheet Music": AdvData(205, "CH4: Dark Sanctuary (Claimb Required)"),
    "CH4: Dark Sanctuary - Hammer of Justice Defeat Item #1": AdvData(206, "CH4: Dark Sanctuary (Claimb Required)"),
    "CH4: Dark Sanctuary - Hammer of Justice Defeat Item #2": AdvData(207, "CH4: Dark Sanctuary (Claimb Required)"),
    "CH4: Dark Sanctuary - Fountain Sealed": AdvData(208, "CH4: Second Sanctuary"),
    "CH4: Second Sanctuary - Wall Climbing Chest": AdvData(209, "CH4: Second Sanctuary"),
    "CH4: Second Sanctuary - Waterfall Chest": AdvData(210, "CH4: Second Sanctuary"),
    "CH4: Second Sanctuary - Man": AdvData(211, "CH4: Second Sanctuary"),
    "CH4: Second Sanctuary - Gallery Prophecy Chest": AdvData(212, "CH4: Second Sanctuary"),
    "CH4: Second Sanctuary - Fountain Sealed": AdvData(213, "CH4: Second Sanctuary"),
    "CH4: Dark Sanctuary - Annoying Dog...?": AdvData(214, "CH4: Third Sanctuary"),
    "CH4: Third Sanctuary - Speed Climbing Chest": AdvData(215, "CH4: Third Sanctuary"),
    "CH4: Third Sanctuary - Dark Area Chest": AdvData(216, "CH4: Third Sanctuary"),
    "CH4: Recruit Guei": AdvData(217, "CH4: Dark Sanctuary"),
    "CH4: Recruit Balthizard": AdvData(218, "CH4: Dark Sanctuary"),
    "CH4: Recruit Bibliox": AdvData(219, "CH4: Dark Sanctuary"),
    "CH4: Recruit Mizzle": AdvData(220, "CH4: Dark Sanctuary"),
    "CH4: Recruit Miss Mizzle": AdvData(221, "CH4: Dark Sanctuary (Claimb Required)"),
    "CH4: Recruit Wicabel": AdvData(222, "CH4: Second Sanctuary"),
    "CH4: Recruit Winglade": AdvData(223, "CH4: Second Sanctuary"),
    "CH4: Recruit Organikk": AdvData(224, "CH4: Second Sanctuary"),
    "CH4: Third Sanctuary - Fountain Sealed": AdvData(225, "CH4: Titan Fight"),
    "CH4: Second Sanctuary - Moss": AdvData(226, "CH4: Second Sanctuary"),
    "CH4: Third Sanctuary - Titan Defeat": AdvData(227, "CH4: Titan Fight"),
    "CH4: Second Sanctuary - Destroyed Piano Block Chest": AdvData(228, "CH4: Second Sanctuary"),
    "CH2: Cyber Field - Teacup Ride Checkmark": AdvData(229, "CH2: Cyber Field"),
    "CH2: Cyber Field - Giasfelfebrehber Checkmark": AdvData(230, "CH2: Cyber Field"),
    "CH2: Lost Werewire": AdvData(1049, "CH2: Cyber Field"),
    "CH2: Lost Tasque": AdvData(1054, "CH2: Cyber Field"),
    "CH2: Lost Virovirokun": AdvData(1055, "CH2: Cyber Field"),
    "CH2: Lost Poppup": AdvData(1076, "CH2: Cyber City"),
    "CH2: Lost Ambyu-lance": AdvData(1077, "CH2: Cyber City"),
    "CH2: Lost Maus": AdvData(1078, "CH2: Cyber City"),
    "CH2: Lost Tasque Manager": AdvData(1088, "CH2: Mansion"),
    "CH2: Lost Mauswheel": AdvData(1089, "CH2: Mansion"),
    "CH2: Lost Werewerewire": AdvData(1094, "CH2: Mansion"),
    "CH3: Lost Water Cooler": AdvData(1129, "CH3: Green Room"),
    "CH3: Lost Shadowguy": AdvData(1164, "CH3: Goulden Sam"),
    "CH3: Lost Shuttah": AdvData(1165, "CH3: TV World"),
    "CH3: Lost Zapper": AdvData(1166, "CH3: Goulden Sam"),
    "CH3: Lost Ribbick": AdvData(1167, "CH3: TV World"),
    "CH3: Lost Pippins": AdvData(1168, "CH3: TV World"),
    "CH4: Lost Guei": AdvData(1217, "CH4: Dark Sanctuary"),
    "CH4: Lost Balthizard": AdvData(1218, "CH4: Dark Sanctuary"),
    "CH4: Lost Bibliox": AdvData(1219, "CH4: Dark Sanctuary"),
    "CH4: Lost Mizzle": AdvData(1220, "CH4: Dark Sanctuary"),
    "CH4: Lost Miss Mizzle": AdvData(1221, "CH4: Dark Sanctuary (Claimb Required)"),
    "CH4: Lost Wicabel": AdvData(1222, "CH4: Second Sanctuary"),
    "CH4: Lost Winglade": AdvData(1223, "CH4: Second Sanctuary"),
    "CH4: Lost Organikk": AdvData(1224, "CH4: Second Sanctuary"),
}

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
