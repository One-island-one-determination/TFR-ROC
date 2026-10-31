#PS LOC PRC GA CCK CKS POL FB #
factions = ["PS", "LOC", "PRC", "GA", "CCK", "CKS", "POL", "FB"]
govs = ["NDC", "LY", "MND", "EY"]
types = ["support", "power", "modifiers", "effect"]

# for g in govs:
for f in factions:
    print(f"""CHI_PAP_remove_{f} = {{
    clr_country_flag = CHI_PAP_NDC_{f}_flag
    clr_country_flag = CHI_PAP_LY_{f}_flag
    clr_country_flag = CHI_PAP_MND_{f}_flag
    clr_country_flag = CHI_PAP_EY_{f}_flag
    remove_dynamic_modifier = {{ modifier = CHI_PAP_{f} }}
}}""")