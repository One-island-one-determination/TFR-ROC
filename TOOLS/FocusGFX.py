import os

# ==========================================
# 1. 在這裡輸入你的名單 (換行分隔)
# ==========================================
text_input = """
CHI_reclaim_national_father_thought
CHI_new_practice_of_three_principles
CHI_perfect_civil_rights
CHI_chinese_nation
CHI_of_by_for_the_people
CHI_restore_refugee_naturalization
CHI_preparatory_provincial_government
CHI_strength_in_numbers
CHI_sun_yat_sen_thought_research_society
CHI_easy_know_hard_do
CHI_birth_planning
CHI_reform_health_insurance
CHI_crack_down_on_housing_prices
CHI_conventional_economic_direction
CHI_lankai_model_experiment
CHI_government_calculation_unit
CHI_auxiliary_civil_service_system
CHI_ai_ruled_economy
CHI_limited_capital_market
CHI_people_livelihood
CHI_restore_control_yuan_functions
CHI_grant_disciplinary_power
CHI_control_yuan_election_system
CHI_new_worker_peasant_policy
CHI_inspect_labor_law_implementation
CHI_labor_union_law_reform
CHI_food_control
CHI_fund_council_of_agriculture
CHI_labor_insurance_reform_bill
CHI_welfare_enterprise_plan
CHI_public_insurance_bonds
CHI_cabinet_meeting
CHI_premier_johnny_chiang
CHI_premier_jaw_shaw_kong
CHI_utilize_bureaucracy
CHI_establish_ministry_of_civil_rights
CHI_separate_department_of_child_and_youth
CHI_blooming_rose
CHI_national_civil_servant_plan
CHI_massive_pay_raise_for_public_officials
CHI_overturn_108_curriculum
CHI_reforge_iron_army
CHI_military_democracy
CHI_follow_the_principle
CHI_conscription_training_crash_course
CHI_national_defense_diplomacy
CHI_fully_promote_cabinet_system
CHI_elderly_care_policy
CHI_labor_insurance_benefit_system_amendment
CHI_new_labor_policy
CHI_promote_new_learning
CHI_three_principles_curriculum
CHI_live_up_to_expectations
CHI_bottom_of_rivers
CHI_do_not_disband_the_group
CHI_do_not_lose_ambition
"""

# 清理字串：用換行符號分割，並自動去除頭尾空白與空行
focus_list = [f.strip() for f in text_input.split('\n') if f.strip()]

# 準備輸出的字串 (加上 P 社的 SpriteTypes 外殼)
base_output = ""
shine_output = ""

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

# ==========================================
# 3. 匯出成檔案
# ==========================================
with open("goals_CHI_base.txt", "w", encoding="utf-8") as f:
    f.write(base_output)

with open("goals_CHI_shine.txt", "w", encoding="utf-8") as f:
    f.write(shine_output)

print(f" 轉換完成！已成功處理 {len(focus_list)} 個國策圖示。")
print(" 產出檔案：goals_CHI_base.txt, goals_CHI_shine.txt")