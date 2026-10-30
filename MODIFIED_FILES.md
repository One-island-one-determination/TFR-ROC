# TFR-ROC: Modified & Overridden Files Reference

This document tracks all files in this submod that override or modify original files from base **The Fire Rises** (Steam Workshop ID `3350890356`).

---

## 1. Shared Scripted Files (Upstream Logic Overrides)

These files have identical paths to base TFR files and will overwrite them when the submod is active. Extra care must be taken when base TFR updates these files.

| File Path | Purpose of Override | Key Modifications |
| :--- | :--- | :--- |
| `events/TFR_events_ZZZ_news.txt` | Core news event triggers | • `news.121`: Immediate trigger for `CHI.10` (Third Oil Crisis).<br>• `news.126`: Immediate trigger for `CHI.TW.7` (Arab Republic Reconstruction).<br>• `news.139`: Branches ROC defense super event (`CHI_invasion_of_taiwan_super`) and music for `CHI`. |
| `common/game_rules/00_game_rules.txt` | Custom game rules | Adds custom ROC game rules:<br>• `CHI_election_2020_gamerule`<br>• `CHI_election_2024_KMT`<br>• `CHI_japan_return_land` |
| `common/ideologies/TFR_ideologies.txt` | Subideology definitions | Adds custom ROC subideologies:<br>• `social_democrat`: `tridemism_socdem`<br>• `social_liberal`: `Taiwanese_Progressivism`, `Taiwanese_Progressivism2`<br>• `market_liberal`: `taiwanese_liberal_populism2`<br>• `conservative`: `Taiwanese_constitutionalism`<br>• `authoritarian_democrat`: `han_kuo_yu_thoughts`<br>• `nationalist`: `CHI_ultimate_three_principles` |
| `common/scripted_localisation/TFR_subideology_scripted_loc.txt` | Subideology display loc | Maps the added ROC subideologies above to their localized display strings. |
| `common/scripted_localisation/TFR_peace_popup_scripted_localisation.txt` | Peace popup text | Adds custom OIOD peace popup scripted localization text for `CHI`. |
| `common/scripted_triggers/00_TFR_scripted_triggers_ZZZ_generic.txt` | Content triggers | Adds `tag = CHI` to `has_content_tag` so CHI is recognized as having full content. |
| `common/bookmarks/TFR_the_fire_rises.txt` | 2020 Bookmark | Sets `default_country = "CHI"` with 2020 ROC starting ideas, focuses, and scenario description. |
| `common/military_industrial_organization/organizations/TFR_organizations_ZZZ_generic.txt` | Generic MIOs | Prevents generic tank/air/materiel/ship organizations from being assigned to `CHI`. |
| `common/countries/cosmetic.txt` | Cosmetic tags | Adds `CHI_blackout` and ROC-specific dynamic cosmetic tags. |
| `common/map_modes/TFR_map_modes.txt` | Map modes | Adds custom international organizations map mode setup. |
| `common/opinion_modifiers/china_modifier.txt` | Cross-strait diplomacy | Adds cross-strait opinion modifiers (`banned_falun_gong`, `chinese_american_rivalry`, etc.). |
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
| `gfx/interface/ideologies/reformist_socialism_PRC.png` | Subideology icon: PRC Reformist Socialism |
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

---

## 4. Dedicated Submod Content Files

These files are either unique to the submod or contain the primary content for Republic of China (`CHI`):

* **National Focus**: `common/national_focus/TFR_national_focus_CHI.txt`
* **Events**: `events/TFR_events_CHI.txt`, `events/TFR_event_CHI_phase2.txt`~`phase4.txt`, `events/taiwan.txt`, `events/CHI_MIO_event.txt`
* **Decisions**: `common/decisions/TFR_decisions_CHI.txt`, `common/decisions/categories/TFR_decision_categories_CHI.txt`
* **Characters & Leaders**: `common/characters/TFR_characters_CHI.txt`
* **Ideas & Dynamic Modifiers**: `common/ideas/TFR_ideas_CHI.txt`, `common/dynamic_modifiers/TFR_dynamic_modifiers_CHI.txt`
* **MIOs**: `common/military_industrial_organization/organizations/TFR_organizations_CHI.txt`
* **History**: `history/countries/CHI - China.txt`, `history/states/` (Taipei 1148, Taichung 1149, Tainan 1150, Taiwan 524, Kinmen 648), `history/units/`
* **GUI & Super Events**: `interface/CHI_superevent.gui`, `common/scripted_guis/CHI_super_events.txt`, `sound/CHI_superevent_sounds.asset`
* **Localisation**: `localisation/simp_chinese/` (`TFR_country_localisation_CHI_l_simp_chinese.yml`, `TFR_events_CHI_l_simp_chinese.yml`, `CHI_super_events_l_simp_chinese.yml`, etc.)

---

## 5. Upstream Sync Checklist

When base TFR updates on the Steam Workshop (`\SteamLibrary\steamapps\workshop\content\394360\3350890356`):

1. **Diff `events/TFR_events_ZZZ_news.txt`**: Ensure base TFR hasn't restructured news event IDs.
2. **Diff `common/game_rules/00_game_rules.txt`**: Ensure base TFR hasn't changed rule categories or added conflicting rule IDs.
3. **Diff `common/scripted_triggers/00_TFR_scripted_triggers_ZZZ_generic.txt`**: Verify any newly added skeleton or content tags from upstream.
4. **Diff `common/ideologies/TFR_ideologies.txt`**: Check if base TFR added new base ideologies or changed subideology properties.
