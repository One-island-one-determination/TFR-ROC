import os

# ==========================================
# 1. 在這裡輸入你的名單 (換行分隔)
# ==========================================
text_input = """
CHI_Self_sutureing_trauma
CHI_Eliminate_communist_traitors
CHI_Preserving_diverse_voices
CHI_Lifting_martial_law
CHI_Restart_Temporary_Provisions
CHI_Plum_blossoms_bloom_in_the_bitter_winter
CHI_Emergency_reconstruction_begins
CHI_Guarantee_basic_food_and_clothing
CHI_Post_war_personnel_issues
CHI_Emergency_repair_infrastructure
CHI_Request_international_assistance
CHI_Priority_to_residential_electricity
CHI_Temporarily_reserve_military_personnel
CHI_Demobilized_reservists
CHI_Repair_Taoyuan_Airport
CHI_Reopening_Kaohsiung_Port
CHI_Ending_wartime_economic
CHI_MilitaryCivilian_cooperation_reconstruction
CHI_Mobilizing_civil_society_groups
CHI_Connecting_lifelines
CHI_Surviving_disaster
CHI_Han_Post_war
CHI_new_ten_propositions
CHI_lone_tower_of_dragon
CHI_sledgehammer_brings_justice
CHI_tranquil_lake_in_the_storm
CHI_one_day_tea_party
CHI_broken_homeland_united_chinese
CHI_cyber_security_managment_act_amendement
CHI_finish_them
CHI_reestablish_special_investigation_division
CHI_hunt_down_spies
CHI_the_flag_is_fluttering
CHI_Post_war_review_status_quo
CHI_Pork_Rice
CHI_Special_budget
CHI_Eleplant_in_room
CHI_corruption
CHI_Political_donations_act
CHI_expand_control_yuan_power
CHI_negotiate_with_DPP
CHI_political_concession
CHI_enemys_enemy
CHI_Restore_provincial_government_functons
CHI_reestablish_hainan_province
CHI_Establish_local_officials
CHI_restore_government_information_office
CHI_reform_PTS
CHI_state_media_transformation
CHI_low_fertility_rate
CHI_Taipei_childcare
CHI_babysitter_selection
CHI_End_of_Chaos
CHI_blue_sky_white_sun_never_falls
CHI_efficient_government
CHI_Three_Labor_arrows
CHI_public_service_variable_pay
CHI_abolish_one_fixed_one_flexed
CHI_Establish_Taiwan_mining_Corporation
CHI_strategic_reserves
CHI_mineral_exporation
CHI_emergency_resources_extraction_mechanism
CHI_New_generation_education
CHI_community_drug_prevention_experiment
CHI_dilingual_education
CHI_Economy_Industry
CHI_Rebulid_7th_CT
CHI_Way_Of_Can_To_Asia
CHI_Expand_FPG
CHI_From_Material_To_Product
CHI_Civil_Military_Supply_Chain
CHI_Local_Heavy_Ind
CHI_Software_Tech_Park
CHI_ROC_First
CHI_Pacific_Trade_Zone
CHI_Investment_From_EU_JP
CHI_Free_Trade
CHI_TARIFF
CHI_Fiscal_Policy_Adjustment
CHI_Defence_Economic_Policy
CHI_Complete_Military_Idustry
CHI_NOMORE_Oil_Crisis
CHI_Maintain_Nuclear_Policy
CHI_Break_Solar_Monopoly
CHI_Self_Sufficiency
CHI_From_Downstream_To_Upstream
CHI_outward_expansion
CHI_support_foreign_research
CHI_international_division_of_labor
CHI_i_am_become_death
CHI_dont_forget_homeland
CHI_spirit_reaches_to_rainbow
CHI_need_of_equipment
CHI_funds_college
CHI_Air_force_special_allowance
CHI_relauch_ADF_project
CHI_american_fighters_reverse_enginnering
CHI_sino_japanese_fighter_cooperation_program
CHI_need_of_talent
CHI_strengthen_anti_corruption_measures
CHI_forming_air_force_political_warfare_command
CHI_carry_forward_the_inspiration_of_our_airman
CHI_modern_whampoa
CHI_new_whampoa_spirits
CHI_unity_of_knowledge_and
CHI_shining_spear_and_iron_horses
CHI_painful_lesson_of_drones
CHI_Camaraderie_Diligence_Sincerity
CHI_centralized_military_command
CHI_reform_combined_logistics_command
CHI_military_railway_underground
CHI_dominate_three_oceans
CHI_making_great_achievements_on_beachhead
CHI_renovate_Tsoying_naval_base
CHI_NCSIST_Project
CHI_relaunch_project_zhenhai
CHI_duty_of_the_helmsman
CHI_march_into_the_waves
CHI_focus_on_polwar_core
CHI_external_political_warfare_bureau
CHI_welcome_home_children
CHI_mainland_peoples_liaison
CHI_central_political_warfare_committee
CHI_expand_the_defense_line
CHI_pacific_military_exercise
CHI_the_giant_returns
CHI_underground_assenmly_point
CHI_thus_spoke_thucydides
CHI_eastern_terrain_mapping
CHI_coverage_priority_tactics
CHI_surpass_overlord
CHI_northern_joint_command
CHI_the_hunter
CHI_operation_peak_leaper
CHI_asia_pacific_armament
CHI_rekindle_confidence
CHI_changbai_foothills
CHI_under_yinshan
CHI_waves_of_nujiang
CHI_among_the_mountains
CHI_land_of_abundance
CHI_jiangnan_mist_and_rain
CHI_gather_at_yangtze
CHI_compete_for_central_plains
CHI_regional_political_tutelage
CHI_trust_localities
CHI_central_supervision_policy
CHI_republic_achieved
CHI_rapid_political_tutelage
CHI_establish_regional_seats
CHI_finally_free
CHI_mongolian_negotiations
CHI_tuva_problem
CHI_begonia_leaf

"""

# 清理字串：用換行符號分割，並自動去除頭尾空白與空行
focus_list = [f.strip() for f in text_input.split('\n') if f.strip()]

# 準備輸出的字串 (加上 P 社的 SpriteTypes 外殼)
base_output = "spriteTypes = {\n"
shine_output = "spriteTypes = {\n"

# ==========================================
# 2. 迴圈生成代碼
# ==========================================
for focus in focus_list:
    # --- 基礎圖示代碼 ---
    base_sprite = f"""
\tspriteType = {{
\t\tname = "GFX_focus_{focus}"
\t\ttexturefile = "gfx/interface/goals/CHI/{focus}.png"
\t}}"""
    base_output += base_sprite

    # --- 發光特效(Shine)代碼 ---
    shine_sprite = f"""
\tspriteType = {{
\t\tname = "GFX_focus_{focus}_shine"
\t\ttexturefile = "gfx/interface/goals/CHI/{focus}.png"
\t\teffectFile = "gfx/FX/buttonstate.lua"
\t\tanimation = {{
\t\t\tanimationmaskfile = "gfx/interface/goals/CHI/{focus}.png"
\t\t\tanimationtexturefile = "gfx/interface/goals/shine_overlay.dds"
\t\t\tanimationrotation = -90.0
\t\t\tanimationlooping = no
\t\t\tanimationtime = 0.75
\t\t\tanimationdelay = 0
\t\t\tanimationblendmode = "add"
\t\t\tanimationtype = "scrolling"
\t\t\tanimationrotationoffset = {{ x = 0.0 y = 0.0 }}
\t\t\tanimationtexturescale = {{ x = 1.0 y = 1.0 }}
\t\t}}
\t\tanimation = {{
\t\t\tanimationmaskfile = "gfx/interface/goals/CHI/{focus}.png"
\t\t\tanimationtexturefile = "gfx/interface/goals/shine_overlay.dds"
\t\t\tanimationrotation = 90.0
\t\t\tanimationlooping = no
\t\t\tanimationtime = 0.75
\t\t\tanimationdelay = 0
\t\t\tanimationblendmode = "add"
\t\t\tanimationtype = "scrolling"
\t\t\tanimationrotationoffset = {{ x = 0.0 y = 0.0 }}
\t\t\tanimationtexturescale = {{ x = 1.0 y = 1.0 }}
\t\t}}
\t\tlegacy_lazy_load = no
\t}}"""
    shine_output += shine_sprite

# 補上結尾括號
base_output += "\n}\n"
shine_output += "\n}\n"

# ==========================================
# 3. 匯出成檔案
# ==========================================
with open("goals_CHI_base.txt", "w", encoding="utf-8") as f:
    f.write(base_output)

with open("goals_CHI_shine.txt", "w", encoding="utf-8") as f:
    f.write(shine_output)

print(f"✅ 轉換完成！已成功處理 {len(focus_list)} 個國策圖示。")
print("📁 產出檔案：goals_CHI_base.txt, goals_CHI_shine.txt")