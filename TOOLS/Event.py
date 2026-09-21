import os
import csv

def parse_canvas_id(canvas_id, country_tag="CHI"):
    """
    解析企劃編號並轉換為 HOI4 程式 ID
    支援格式: 
    1. H2-01-01 -> CHI.H2.11
    2. TW-02    -> CHI.TW.2
    """
    canvas_id = canvas_id.strip()
    parts = canvas_id.split('-')
    
    if len(parts) == 3:
        return f"{country_tag}.{parts[0]}.{int(parts[1])}{int(parts[2])}"
    elif len(parts) == 2:
        return f"{country_tag}.{parts[0]}.{int(parts[1])}"
    return None

def generate_event_code(hoi4_id):
    """生成單一事件的代碼與圖片名稱"""
    parts = hoi4_id.split('.')
    
    base_pic_name = f"{parts[0]}_Event_{parts[1]}_{parts[2]}"
    gfx_name = f"{base_pic_name}"
    
    code = f"""country_event = {{
    id = {hoi4_id}
    title = {hoi4_id}.t
    desc = {hoi4_id}.d
    picture = {gfx_name}
    fire_only_once = yes
    is_triggered_only = yes
    
    option = {{
        name = {hoi4_id}.a
    }}
}}
"""
    return code, base_pic_name, gfx_name

def generate_localisation(hoi4_id, title, desc, option_a):
    """生成單一事件的翻譯檔格式"""
    desc_formatted = desc.replace('\n', '\\n\\n') 
    loc = f""" {hoi4_id}.t: "{title}"
 {hoi4_id}.d: "{desc_formatted}"
 {hoi4_id}.a: "{option_a}"

"""
    return loc

def generate_gfx_entry(base_pic_name, gfx_name):
    """生成單一圖片的 gfx 註冊碼"""
    entry = f"""\tspriteType = {{
\t\tname = "{gfx_name}"
\t\ttexturefile = "gfx/event_pictures/{base_pic_name}.png"
\t}}"""
    return entry

def main():
    print("==========================================")
    print("   🇹🇼 TFRROC 批次事件生成器 v3.1 (CSV+GFX in TOOLS) ")
    print("==========================================")
    
    # --- 關鍵修改：獲取目前 Event.py 所在的資料夾路徑 ---
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 定義所有檔案的絕對路徑，確保它們都在 TOOLS 資料夾內
    csv_filename = os.path.join(script_dir, "事件企劃表模板.csv")
    output_events = os.path.join(script_dir, "output_events.txt")
    output_loc = os.path.join(script_dir, "output_loc_l_simp_chinese.yml")
    output_gfx = os.path.join(script_dir, "output_event_pictures.gfx")
    # ---------------------------------------------------

    if not os.path.exists(csv_filename):
        with open(csv_filename, 'w', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["事件標題", "選項A文字", "企劃編號", "事件內容"])
            writer.writerow(["測試標題", "了解。", "H2-01-01", "這是一段測試內容。\n這是第二段。"])
            writer.writerow(["台灣事件", "確認。", "TW-02", "兩段式編號測試。"])
        print(f"⚠️ 找不到資料表！已自動在 TOOLS 資料夾為您生成『事件企劃表模板.csv』。")
        print("👉 請用 Excel 打開它，填入您的事件資料後，再重新執行本程式！")
        return

    all_events_code = ""
    all_loc_code = "l_simp_chinese:\n"
    all_gfx_code = "spriteTypes = {\n"
    success_count = 0

    print("讀取資料表中，開始量產...")
    with open(csv_filename, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            canvas_id = row.get("企劃編號", "").strip()
            title = row.get("事件標題", "").strip()
            desc = row.get("事件內容", "").strip()
            option_a = row.get("選項A文字", "").strip()
            
            if not canvas_id:
                continue
                
            hoi4_id = parse_canvas_id(canvas_id)
            if not hoi4_id:
                print(f"❌ 警告: 企劃編號 '{canvas_id}' 格式不符，已跳過。")
                continue
                
            event_code, base_pic_name, gfx_name = generate_event_code(hoi4_id)
            loc_code = generate_localisation(hoi4_id, title, desc, option_a)
            gfx_entry = generate_gfx_entry(base_pic_name, gfx_name)
            
            all_events_code += event_code + "\n"
            all_loc_code += loc_code
            all_gfx_code += gfx_entry + "\n\n"
            
            success_count += 1
            print(f"  ✓ 成功轉換: {canvas_id} -> {hoi4_id}")

    all_gfx_code += "}\n"

    if success_count == 0:
        print("🤷 資料表裡沒有有效的事件可以生成。")
        return

    # --- 寫入檔案時使用絕對路徑 ---
    with open(output_events, "w", encoding="utf-8-sig") as f:
        f.write(all_events_code)
        
    with open(output_loc, "w", encoding="utf-8-sig") as f:
        f.write(all_loc_code)
        
    with open(output_gfx, "w", encoding="utf-8") as f:
        f.write(all_gfx_code)
    # ------------------------------

    print("\n==========================================")
    print(f"🎉 批次生成完畢！共成功轉換 {success_count} 個事件！")
    print(f"📁 檔案已全部輸出至 TOOLS 資料夾：")
    print("  - output_events.txt")
    print("  - output_loc_l_simp_chinese.yml")
    print("  - output_event_pictures.gfx")
    print("💡 記得將對應的圖片放入模組的 gfx/event_pictures/ 資料夾中！")
    print("==========================================")

if __name__ == "__main__":
    main()