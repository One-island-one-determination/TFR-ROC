input_text = """
consumer_goods_factor = -0.05
	production_factory_max_efficiency_factor = 0.04
	production_speed_buildings_factor = 0.04
	stability_factor = 0.04
	business_value_factor = 0.04
	poverty_development_monthly = 0.004
	factory_energy_consumption = -0.06
"""

# 將每一行拆解並轉換成目標格式
for line in input_text.strip().split('\n'):
    if '=' in line:
        # 去除頭尾空白並以等號分割
        var_name, value = [item.strip() for item in line.split('=')]
        
        # 組合並印出 HOI4 腳本格式
        output_line = f"add_to_variable = {{ CHI_OC_{var_name} = {value} tooltip = {var_name}_tooltip }}"
        print(output_line)