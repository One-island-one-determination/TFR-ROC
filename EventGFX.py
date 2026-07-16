import os

def convert_id_to_gfx_name(event_id):
    """將 CHI.1 轉換為 CHI_Event_1，將 CHI.H1.11 轉換為 CHI_Event_H1_11"""
    parts = event_id.split('.')
    if len(parts) == 1:
        return f"{parts[0]}_Event"
    
    prefix = parts[0]
    suffix = "_".join(parts[1:])
    return f"{prefix}_Event_{suffix}"

# ==========================================
# 1. 在這裡輸入你的名單 (換行分隔)
# ==========================================
text_input = """
CHI.9
CHI.101
CHI.103
CHI.105
CHI.106
CHI.110
CHI.111
CHI.121
CHI.141
CHI.BF.11
CHI.H2.11
CHI.H2.41
CHI.H2.61
CHI.H2.81
CHI.H2.82
CHI.H2.101
CHI.H2.121
CHI.H2.141
CHI.H2.151
CHI.H2.161
CHI.H2.181
CHI.H2.222
CHI.H2.251
CHI.H2.261
CHI.H2.301
CHI.H2.391
CHI.H2.411
CHI.H2.431
ROC.21
ROC.22
ROC.32
ROC.88
taiwan.3
"""

# 清理字串：用換行符號分割，並自動去除頭尾空白與空行
event_list = [e.strip() for e in text_input.split('\n') if e.strip()]

# 準備輸出的字串 (加上 P 社的 SpriteTypes 外殼)
base_output = ""

# ==========================================
# 2. 迴圈生成代碼
# ==========================================
for event_id in event_list:
    # 轉換名稱 (例: CHI.1 -> CHI_Event_1)
    gfx_name = convert_id_to_gfx_name(event_id)
    
    # --- 基礎圖示代碼 ---
    # 注意：HOI4 習慣在 name 前面加上 GFX_，而在 texturefile 裡面不加
    base_sprite = f"""
\tspriteType = {{
\t\tname = "{gfx_name}"
\t\ttexturefile = "gfx/event_pictures/{gfx_name}.png"
\t}}"""
    base_output += base_sprite

# 補上最後的右大括號
base_output += ""

# ==========================================
# 3. 匯出成檔案
# ==========================================
output_filename = "event_GFX.txt"

with open(output_filename, "w", encoding="utf-8") as f:
    f.write(base_output)

print("==========================================")
print(f"✅ 轉換完成！已成功處理 {len(event_list)} 個事件圖示。")
print(f"📁 產出檔案：{output_filename}")
print("==========================================")