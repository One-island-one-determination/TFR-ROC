input_text = """
navy_max_range = 0.15
"""

# 將每一行拆解並轉換成目標格式
print("custom_effect_tooltip = { IDEA = CHI_ROC_navy_dynamic localization_key = modify_idea_tt }")
for line in input_text.strip().split('\n'):
    if '=' in line:
        # 去除頭尾空白並以等號分割
        var_name, value = [item.strip() for item in line.split('=')]
        
        # 組合並印出 HOI4 腳本格式
        output_line = f"add_to_variable = {{ ROC_{var_name} = {value} tooltip = {var_name}_tooltip }}"
        print(output_line)