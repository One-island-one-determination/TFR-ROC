input_text = """
			foreign_minister_cost_factor = -0.05
				economic_minister_cost_factor = -0.05
				interior_minister_cost_factor = -0.05
				intelligence_minister_cost_factor = -0.05
				theorist_minister_cost_factor = -0.05
"""

# 將每一行拆解並轉換成目標格式
for line in input_text.strip().split('\n'):
    if '=' in line:
        # 去除頭尾空白並以等號分割
        var_name, value = [item.strip() for item in line.split('=')]
        
        # 組合並印出 HOI4 腳本格式
        output_line = f"add_to_variable = {{ CHI_D_{var_name} = {value} tooltip = {var_name}_tooltip }}"
        print(output_line)