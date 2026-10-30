# TFR-ROC: Modified & Overridden Files Reference

This document tracks all files in this submod that override or modify original files from base **The Fire Rises** (Steam Workshop ID `3350890356`).

---

## 1. Shared Scripted Files (Upstream Logic Overrides)

These files have identical paths to base TFR files and will overwrite them when the submod is active. Extra care must be taken when base TFR updates these files.

| File Path | Purpose of Override | Key Modifications |
| :--- | :--- | :--- |
| `events/TFR_events_ZZZ_news.txt` | Core news event triggers | • `news.121`: Immediate trigger for `CHI.10` (Third Oil Crisis).<br>• `news.126`: Immediate trigger for `CHI.TW.7` (Arab Republic Reconstruction).<br>• `news.139`: Branches ROC defense super event (`CHI_invasion_of_taiwan_super`) and music for `CHI`. |
| `common/ideologies/TFR_ideologies.txt` | Subideology definitions | Adds custom ROC subideologies:<br>• `social_democrat`: `tridemism_socdem`<br>• `social_liberal`: `Taiwanese_Progressivism`, `Taiwanese_Progressivism2`<br>• `market_liberal`: `taiwanese_liberal_populism2`<br>• `conservative`: `Taiwanese_constitutionalism`<br>• `authoritarian_democrat`: `han_kuo_yu_thoughts`<br>• `nationalist`: `CHI_ultimate_three_principles` |
| `common/scripted_localisation/TFR_subideology_scripted_loc.txt` | Subideology display loc | Maps the added ROC subideologies above to their localized display strings. |
| `common/scripted_localisation/TFR_peace_popup_scripted_localisation.txt` | Peace popup text | Adds custom OIOD peace popup scripted localization text for `CHI`. |
| `common/scripted_triggers/00_TFR_scripted_triggers_ZZZ_generic.txt` | Content triggers | Adds `tag = CHI` to `has_content_tag` so CHI is recognized as having full content. |
| `common/bookmarks/TFR_the_fire_rises.txt` | 2020 Bookmark | Sets `default_country = "CHI"` with 2020 ROC starting ideas, focuses, and scenario description. |
| `common/military_industrial_organization/organizations/TFR_organizations_ZZZ_generic.txt` | Generic MIOs | Prevents generic tank/air/materiel/ship organizations from being assigned to `CHI`. |
| `common/countries/cosmetic.txt` | Cosmetic tags | Adds `CHI_blackout` and ROC-specific dynamic cosmetic tags. |
| `common/map_modes/TFR_map_modes.txt` | Map modes | Adds custom international organizations map mode setup. |
| `common/scripted_guis/TFR_startup_menu.txt` | Startup guide GUI script | Adds `CHI_info_special_visible` check for the ROC startup guide popup. |
| `interface/frontendgamesetupview.gui` | Country selection screen | Adds ROC path preview flags and tooltips (`GFX_KMT` / `GFX_DPP`) in scenario setup. |
| `interface/frontendmainview.gui` | Main menu UI | Customizes submod main menu logo and positioning. |
| `interface/TFR_start_menu.gui` | Startup guide GUI layout | Adds `CHI_info_special` icon/button into the startup window. |
| `interface/fonts_chinese.gfx` | Font definition | Adjusts fallback font mapping for Simplified Chinese typography. |
| `Map/adjacencies.csv` | Map adjacencies | Custom strait crossings / adjacencies around Taiwan and Penghu / Kinmen / Matsu. |
| `Map/railways.txt` | Railway network | Taiwan railway infrastructure. |
| `Map/buildings.txt` | 3D Landmark spawn coordinates | Appends the 3D landmark spawn location in Nanjing state 1222 (`1222;landmark_spawn;4664.15;10.10;1177.28;-0.07;0`) to render the ported Nanjing Presidential Palace 3D model (`landmark_nanjing_presidential_palace`). |

---

## 2. Overridden Graphics, Textures, & Visual Assets

These binary image and texture files replace base TFR assets directly:

### Flags (`gfx/flags/`)
| File Path | Description |
| :--- | :--- |
| `gfx/flags/CHI_taiwan_republic.tga` | Taiwan Republic / Republic of Taiwan flag (standard) |
| `gfx/flags/medium/CHI_taiwan_republic.tga` | Taiwan Republic flag (medium size) |
| `gfx/flags/small/CHI_taiwan_republic.tga` | Taiwan Republic flag (small / counter size) |
| `gfx/flags/medium/HKN_conservative.tga` | Hong Kong conservative faction flag (medium) |

### UI Textures & Interface Art (`gfx/interface/`)
| File Path | Description |
| :--- | :--- |
| `gfx/interface/country_selection_bg.dds` | Country selection background artwork |
| `gfx/interface/logo_game.dds` | Game / submod title screen logo |
| `gfx/interface/thisisdog.dds` | Interface art asset |
| `gfx/texticons/banners/decisions/PROXY_saudi_cw_cat_banner.png` | Saudi Civil War decision category banner texture |

### Portraits & Leaders (`gfx/leaders/`)
| File Path | Description |
| :--- | :--- |
| `gfx/leaders/CHI/CHI_chu_li_luan.png` | Leader portrait: Eric Chu (朱立倫) |
| `gfx/leaders/CHI/CHI_hou_yu_ih.png` | Leader portrait: Hou Yu-ih (侯友宜) |
| `gfx/leaders/CHI/generals/CHI_hsu_yen_pu.png` | General portrait: Hsu Yen-pu (徐衍璞) |
| `gfx/leaders/CHI/generals/Chiu_Kuo_Cheng.png` | General portrait: Chiu Kuo-cheng (邱國正) |

### Focus, Technology, & Ideology Icons (`gfx/interface/`)
| File Path | Description |
| :--- | :--- |
| `gfx/interface/goals/CHI/CHI_grant_emergency_powers.png` | National focus icon: Grant Emergency Powers |
| `gfx/interface/ideas/CHI/mio_CHI_Jong_Shyn.png` | MIO icon: Jong Shyn Shipbuilding (中信造船) |
| `gfx/interface/ideas/ZZZ_government_type/ZZZ_taiwanese_semi_presidential_system.png` | Idea icon: Taiwanese Semi-Presidential System / 中華五權共和制 |
| `gfx/interface/ideologies/reformist_socialism_PRC.png` | Subideology icon: PRC Reformist Socialism / Left-wing Tridemism |
| `gfx/interface/technologies/infantry/CHI_infantry1.dds` to `CHI_infantry6.dds` | Custom infantry technology tier icons (Tiers 1–6) |

### Loading Screen Wallpapers (`gfx/loadingscreens/` — 51 files)
All standard base TFR loading screens are replaced with custom submod loading screen artwork:
* **Numbered**: `load_1.dds` through `load_34.dds`
* **DLC / Expansion Named**: `load_aat.dds`, `load_aat2.dds`, `load_bba.dds`, `load_botb.dds`, `load_dod.dds`, `load_goe.dds`, `load_lar.dds`, `load_mtg.dds`, `load_mtg_2.dds`, `load_ncns_chi.dds`, `load_ncns_jap.dds`, `load_nsb.dds`, `load_nsb2.dds`, `load_tfv.dds`, `load_tiger.dds`, `load_toa.dds`, `load_ww.dds`

---

## 3. Eliminated Overrides (Cleaned Up)

The following upstream files were previously overridden by this submod, but have been **removed** in favor of cleaner hooks to maximize base TFR compatibility:

* **`events/TFR_events_USA.txt`**: Removed. Base TFR's `usa.103` already triggers `taiwan.2` for CHI upon the outbreak of the 2nd American Civil War. The submod event `CHI.3` ("太平洋之殤") is now hooked directly inside `taiwan.2`'s `hidden_effect` in `events/TFR_events_CHI.txt`.
* **`events/TFR_events_SAU.txt`**: Removed. Its only custom calls were `CHI.10` (Oil Crisis) and `CHI.TW.7` (Arab Victory). These are now triggered via `news.121` and `news.126` in `events/TFR_events_ZZZ_news.txt`, which the submod already maintains.
* **`common/opinion_modifiers/china_modifier.txt`**: Removed. Opinion modifiers are additive in HoI4; the 6 custom ROC modifiers (`CHI_Block_tourists`, `CHI_ARR_humanitarian_aid`, `CHI_Diplomatic_countries`, `CHI_Assist_reconstruction`, `CHI_support_us`, `CHI_opposed_us`) were merged into our existing submod file `common/opinion_modifiers/TFR_CHI_opinion_modifiers.txt`. Base TFR's `china_modifier.txt` is no longer overridden.
* **`common/game_rules/00_game_rules.txt`**: Removed. HoI4 loads game rules additively; the 3 custom ROC game rules (`CHI_election_2020_gamerule`, `CHI_election_2024_KMT`, `CHI_japan_return_land`) were moved into `common/game_rules/000_TFR_ROC_game_rules.txt` under a custom top-level group `RULE_GROUP_TFR_ROC` ("烈焰升騰：同島一命"). Base TFR's 5,760-line `00_game_rules.txt` is no longer overridden.

---

## 4. Dedicated Submod Content Files

These files are either unique to the submod or contain the primary content for Republic of China (`CHI`):

* **National Focus**: `common/national_focus/TFR_national_focus_CHI.txt`
* **Events**: `events/TFR_events_CHI.txt`, `events/TFR_event_CHI_phase2.txt`~`phase4.txt`, `events/taiwan.txt`, `events/CHI_MIO_event.txt`
* **Decisions**: `common/decisions/TFR_decisions_CHI.txt`, `common/decisions/categories/TFR_decision_categories_CHI.txt`
* **Game Rules**: `common/game_rules/000_TFR_ROC_game_rules.txt`
* **Opinion Modifiers**: `common/opinion_modifiers/TFR_CHI_opinion_modifiers.txt`
* **Characters & Leaders**: `common/characters/TFR_characters_CHI.txt`
* **Ideas & Dynamic Modifiers**: `common/ideas/TFR_ideas_CHI.txt`, `common/dynamic_modifiers/TFR_dynamic_modifiers_CHI.txt`
* **MIOs**: `common/military_industrial_organization/organizations/TFR_organizations_CHI.txt`
* **History**: `history/countries/CHI - China.txt`, `history/states/` (Taipei 1148, Taichung 1149, Tainan 1150, Taiwan 524, Kinmen 648), `history/units/`
* **GUI & Super Events**: `interface/CHI_superevent.gui`, `common/scripted_guis/CHI_super_events.txt`, `sound/CHI_superevent_sounds.asset`
* **Localisation**: `localisation/simp_chinese/` (`TFR_country_localisation_CHI_l_simp_chinese.yml`, `TFR_events_CHI_l_simp_chinese.yml`, `CHI_super_events_l_simp_chinese.yml`, etc.)

---

## 5. Third-Party Submod Compatibility & Patching Guide

If you are developing another submod for **The Fire Rises** (such as regional reworks like *Korea Plus*) or creating a dedicated compatibility patch to make multiple TFR submods work seamlessly together with **TFR-ROC**, **the files listed in [Section 1 (Shared Scripted Files)](#1-shared-scripted-files-upstream-logic-overrides) are the exact files that must be merged.**

Because Hearts of Iron IV overrides files on a whole-file basis rather than line-by-line, any two submods modifying the same upstream file will clobber each other based on mod load order. A downstream compatibility patch must merge both sets of modifications into a unified copy.

### Real-World Example: *The Fire Rises: Korea Plus (TFRKP)*
The *Korea Plus* team created an official compatibility patch between TFRKP and TFR-ROC:
* **Mod Name**: `TFRKP x ROC Compatibility`
* **Steam Workshop ID**: [`3791381497`](https://steamcommunity.com/sharedfiles/filedetails/?id=3791381497) (Local path: `F:\SteamLibrary\steamapps\workshop\content\394360\3791381497`)
* **Dependencies**: Loads after both `The Fire Rises: Korea Plus` and `The Fire Rises: One Island, One Determination` (formerly `TFR - Republic of China`, Workshop ID `3609728809`).

#### Files Merged in the TFRKP Patch:
| Target File | Merged Content from Both Submods |
| :--- | :--- |
| `common/bookmarks/TFR_the_fire_rises.txt` | Merges starting scenarios, country definitions, ideas, and initial focuses for both `CHI` and `KOR`. |
| `common/ideologies/TFR_ideologies.txt` | Combines ROC subideologies (`Taiwanese_constitutionalism`, `Taiwanese_Progressivism`, etc.) and KOR custom subideologies. |
| `common/scripted_localisation/TFR_subideology_scripted_loc.txt` | Combines dynamic subideology display names for both tags. |
| `common/scripted_triggers/00_TFR_scripted_triggers_ZZZ_generic.txt` | Appends both `tag = CHI` and `tag = KOR` into `has_content_tag`. |
| `common/military_industrial_organization/organizations/TFR_organizations_ZZZ_generic.txt` | Excludes both `CHI` and `KOR` from generic MIO assignments (`NOT = { tag = CHI }`, `NOT = { tag = KOR }`). |
| `interface/frontendgamesetupview.gui` | Merges country selection screen buttons, leader portraits, and path tooltips for both nations. |
| `interface/frontendmainview.gui` & `gfx/interface/country_selection_bg.dds` | Resolves title screen and country selection art conflicts. |
| `events/TFR_events_ZZZ_news.txt` | If both submods hook news events or music branches, triggers must be unified here. |

> [!WARNING]
> **Status of the TFRKP Compatibility Patch**:
> According to the Korea Plus development team, the `TFRKP x ROC Compatibility` patch is an **early prototype** (*"It just proto-type so that make some unexpected bugs."*). While it provides a functional reference for which files need patching, players and developers should expect potential unexpected bugs, script conflicts, or outdated overrides. Thorough testing and maintenance against current versions of both mods are recommended before serious playthroughs.

### Files That Do NOT Require Patching (Cleanly Isolated):
You **do not** need to patch files listed under [Section 4 (Dedicated Submod Content Files)](#4-dedicated-submod-content-files):
* **Custom Game Rules** (`common/game_rules/000_TFR_ROC_game_rules.txt`): Loaded additively by HoI4 under `RULE_GROUP_TFR_ROC` without touching `00_game_rules.txt`.
* **Custom Opinion Modifiers** (`common/opinion_modifiers/TFR_CHI_opinion_modifiers.txt`): Loaded additively without touching `china_modifier.txt`.
* **National Focuses, Events, Decisions, MIOs, Characters**: Fully namespaced to `CHI` and completely independent.

---

## 6. Upstream Sync Checklist

When base TFR updates on the Steam Workshop (`\SteamLibrary\steamapps\workshop\content\394360\3350890356`):

1. **Diff `events/TFR_events_ZZZ_news.txt`**: Ensure base TFR hasn't restructured news event IDs.
2. **Diff `common/game_rules/00_game_rules.txt`**: Ensure base TFR hasn't added conflicting rule names (though our rules are now cleanly separated in `000_TFR_ROC_game_rules.txt`).
3. **Diff `common/scripted_triggers/00_TFR_scripted_triggers_ZZZ_generic.txt`**: Verify any newly added skeleton or content tags from upstream.
4. **Diff `common/ideologies/TFR_ideologies.txt`**: Check if base TFR added new base ideologies or changed subideology properties.
