import os
import csv

def generate_base_gfx(focus_id):
    """生成基礎 GFX 代碼"""
    return f"""\tspriteType = {{
\t\tname = "GFX_focus_{focus_id}"
\t\ttexturefile = "gfx/interface/goals/CHI/{focus_id}.png"
\t}}"""

def generate_shine_gfx(focus_id):
    """生成 Shine (發光) GFX 代碼"""
    return f"""\tspriteType = {{
\t\tname = "GFX_focus_{focus_id}_shine"
\t\ttexturefile = "gfx/interface/goals/CHI/{focus_id}.png"
\t\teffectFile = "gfx/FX/buttonstate.lua"
\t\tanimation = {{
\t\t\tanimationmaskfile = "gfx/interface/goals/CHI/{focus_id}.png"
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
\t\t\tanimationmaskfile = "gfx/interface/goals/CHI/{focus_id}.png"
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

def generate_focus_node(focus_id, x_pos, y_pos, cost):
    """生成無效果國策節點代碼"""
    return f"""\tfocus = {{
\t\tid = {focus_id}
\t\ticon = GFX_focus_{focus_id}
\t\tx = {x_pos}
\t\ty = {y_pos}
\t\tcost = {cost}
\t\tcompletion_reward = {{
\t\t\t# TODO: 添加完成獎勵
\t\t}}
\t}}"""

def main():
    print("==========================================")
    print("   🌳 TFR 批次國策生成器 (CSV+GFX in TOOLS) ")
    print("==========================================")
    
    # 獲取目前 FocusGFX.py 所在的絕對路徑 (TOOLS)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 定義檔案路徑
    csv_filename = os.path.join(script_dir, "國策企劃表模板.csv")
    output_base_gfx = os.path.join(script_dir, "output_goals_base.gfx")
    output_shine_gfx = os.path.join(script_dir, "output_goals_shine.gfx")
    output_focus = os.path.join(script_dir, "output_national_focus.txt")
    output_loc = os.path.join(script_dir, "output_focus_l_simp_chinese.yml")

    # 如果 CSV 不存在，自動生成一個模板
    if not os.path.exists(csv_filename):
        with open(csv_filename, 'w', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["國策ID", "X座標", "Y座標", "耗費時間(通常是3,5,11)", "國策標題", "國策描述"])
            writer.writerow(["CHI_test_focus_1", "0", "0", "3", "測試國策一", "這是國策一的描述。"])
            writer.writerow(["CHI_test_focus_2", "0", "1", "5", "測試國策二", "這是國策二的描述。"])
        print(f"⚠️ 找不到資料表！已自動在 TOOLS 資料夾為您生成『國策企劃表模板.csv』。")
        print("👉 請用 Excel 打開它，填入您的國策資料後，再重新執行本程式！")
        return

    # 準備輸出的字串變數
    all_base_gfx = "\n"
    all_shine_gfx = "\n"
    all_focus_code = ""
    
    # 將文本分為標題與描述兩個區塊收集
    all_loc_titles = ""
    all_loc_descs = ""
    
    success_count = 0

    print("讀取國策資料表中，開始量產...")
    with open(csv_filename, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            focus_id = row.get("國策ID", "").strip()
            
            # 讀取並處理數值，若為空則給予預設值
            x_pos = row.get("X座標", "0").strip() or "0"
            y_pos = row.get("Y座標", "0").strip() or "0"
            cost = row.get("耗費時間(通常是3,5,11)", "3").strip() or "3"
            
            title = row.get("國策標題", "").strip()
            desc = row.get("國策描述", "").strip()
            
            if not focus_id:
                continue
                
            # 生成代碼並追加到對應的字串中
            all_base_gfx += generate_base_gfx(focus_id) + "\n"
            all_shine_gfx += generate_shine_gfx(focus_id) + "\n"
            all_focus_code += generate_focus_node(focus_id, x_pos, y_pos, cost) + "\n"
            
            # 分離標題與描述
            desc_formatted = desc.replace('\n', '\\n\\n')
            all_loc_titles += f' {focus_id}: "{title}"\n'
            all_loc_descs += f' {focus_id}_desc: "{desc_formatted}"\n'
            
            success_count += 1
            print(f"  ✓ 成功轉換國策: {focus_id}")

    # 收尾結構
    all_base_gfx += "\n"
    all_shine_gfx += "\n"
    
    # 組合最終的文本檔案結構：l_simp_chinese 標頭 + 所有標題 + 空行 + 所有描述
    all_loc_code = "l_simp_chinese:\n" + all_loc_titles + "\n" + all_loc_descs

    if success_count == 0:
        print("🤷 資料表裡沒有有效的國策可以生成。")
        return

    # 寫入檔案
    with open(output_base_gfx, "w", encoding="utf-8") as f:
        f.write(all_base_gfx)
        
    with open(output_shine_gfx, "w", encoding="utf-8") as f:
        f.write(all_shine_gfx)
        
    with open(output_focus, "w", encoding="utf-8") as f:
        f.write(all_focus_code)
        
    with open(output_loc, "w", encoding="utf-8-sig") as f:
        f.write(all_loc_code)

    print("\n==========================================")
    print(f"🎉 批次生成完畢！共成功轉換 {success_count} 個國策！")
    print(f"📁 檔案已全部輸出至 TOOLS 資料夾：")
    print("  - output_national_focus.txt (無效果國策本體)")
    print("  - output_focus_l_simp_chinese.yml (翻譯文本，已分離名稱與描述)")
    print("  - output_goals_base.gfx (基礎圖示註冊)")
    print("  - output_goals_shine.gfx (發光特效註冊)")
    print("==========================================")

if __name__ == "__main__":
    main()