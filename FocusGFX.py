import os

# ==========================================
# 1. 在這裡輸入你的名單 (換行分隔)
# ==========================================
text_input = """
CHI_solidarity
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