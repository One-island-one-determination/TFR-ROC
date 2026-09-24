factions = ["PS", "LOC", "PRC", "GA", "CCK", "CKS", "POL", "FB"]
slots = ["card_1", "card_2", "card_3", "card_4", "NDC", "LY", "MND", "EY"]

for s in slots:
    for f in factions:
        print(f"remove_dynamic_modifier = {{ modifier = CHI_PAP_{s}_{f} }}")