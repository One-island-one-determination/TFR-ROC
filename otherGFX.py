from pathlib import Path

# ===== 修改成你的圖片資料夾 =====
image_folder = Path(r"C:\Users\hsieh\Documents\GitHub\TFR-ROC\gfx\interface\gaw")

# ===== HOI4 mod 中的相對路徑 =====
gfx_path = "gfx/interface/gaw"

# ===== 輸出的 .gfx 檔 =====
output_file = image_folder / "gaw.gfx"

with open(output_file, "w", encoding="utf-8") as f:
    f.write("spriteTypes = {\n\n")

    for png in sorted(image_folder.glob("*.png")):
        name = png.stem

        f.write(f'''    SpriteType = {{
        name = "{name}"
        texturefile = "{gfx_path}/{png.name}"
    }}

''')

    f.write("}\n")

print(f"完成！共輸出 {len(list(image_folder.glob('*.png')))} 個 SpriteType")
print(f"輸出位置：{output_file}")