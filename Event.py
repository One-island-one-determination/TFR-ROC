import re
import os
import csv

def parse_canvas_id(canvas_id, country_tag="CHI"):
    """
    解析企劃編號並轉換為 HOI4 程式 ID
    例如: H2-01-01 -> CHI.H2.11
    """
    match = re.match(r"([A-Za-z]+)(\d+)-(\d+)-(\d+)", canvas_id.strip())
    if not match:
        return None

    route = match.group(1)       
    phase = match.group(2)       
    focus_num = int(match.group(3))  
    event_num = int(match.group(4))  
    
    hoi4_id = f"{country_tag}.{route}{phase}.{focus_num}{event_num}"
    return hoi4_id

def generate_event_code(hoi4_id):
    """生成單一事件的代碼"""
    # 【新增】將 CHI.H2.11 自動轉換為 CHI_Event_H2_11
    parts = hoi4_id.split('.')
    picture = f"{parts[0]}_Event_{parts[1]}_{parts[2]}"
    
    code = f"""country_event = {{
    id = {hoi4_id}
    title = {hoi4_id}.t
    desc = {hoi4_id}.d
    picture = {picture}
    fire_only_once = yes
    is_triggered_only = yes
    
    option = {{
        name = {hoi4_id}.a
    }}
}}
"""
    return code

def generate_localisation(hoi4_id, title, desc, option_a):
    """生成單一事件的翻譯檔格式"""
    # 處理 Excel 裡的換行，轉換成 HOI4 的雙換行
    desc_formatted = desc.replace('\n', '\\n\\n') 
    
    loc = f""" {hoi4_id}.t: "{title}"
 {hoi4_id}.d: "{desc_formatted}"
 {hoi4_id}.a: "{option_a}"
"""
    return loc

def main():
    print("==========================================")
    print("   🇹🇼 TFRROC 批次事件生成器 v2.0 (CSV版)   ")
    print("==========================================")
    
    csv_filename = "事件企劃表模板.csv"
    
    # 如果找不到 CSV 檔案，就幫企劃生成一個模板
    if not os.path.exists(csv_filename):
        with open(csv_filename, 'w', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["事件標題", "選項A文字", "企劃編號", "事件內容"])
            writer.writerow(["測試標題", "了解。", "H2-01-01", "這是一段測試內容。\n這是第二段。"])
        print(f"⚠️ 找不到資料表！已自動為您生成『{csv_filename}』。")
        print("👉 請用 Excel 打開它，填入您的事件資料後，再重新執行本程式！")
        return

    # 讀取 CSV 進行量產
    all_events_code = ""
    all_loc_code = "l_simp_chinese:\n"
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
                
            event_code = generate_event_code(hoi4_id)
            loc_code = generate_localisation(hoi4_id, title, desc, option_a)
            
            all_events_code += event_code + "\n"
            all_loc_code += loc_code + "\n"
            success_count += 1
            print(f"  ✓ 成功轉換: {canvas_id} -> {hoi4_id}")

    if success_count == 0:
        print("🤷 資料表裡沒有有效的事件可以生成。")
        return

    # 寫入 txt (事件本體) - 使用 UTF-8 帶 BOM
    with open("output_events.txt", "w", encoding="utf-8-sig") as f:
        f.write(all_events_code)
        
    # 寫入 yml (翻譯檔) - 使用 UTF-8 帶 BOM
    with open("output_loc_l_simp_chinese.yml", "w", encoding="utf-8-sig") as f:
        f.write(all_loc_code)

    print("\n==========================================")
    print(f"🎉 批次生成完畢！共成功轉換 {success_count} 個事件！")
    print("📁 已生成 output_events.txt")
    print("📁 已生成 output_loc_l_simp_chinese.yml (已處理 BOM 格式)")
    print("==========================================")

if __name__ == "__main__":
    main()