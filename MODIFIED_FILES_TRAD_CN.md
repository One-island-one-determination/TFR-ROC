# TFR-ROC：修改與覆寫檔案參考指南

本文件記錄此子模組（Submod）中所有覆寫或修改 **《烈焰升騰》（The Fire Rises）** 本體模組（Steam 工作坊 ID `3350890356`）原始檔案的項目。

---

## 1. 共用腳本檔案（上游邏輯覆寫）

這些檔案與 TFR 本體模組的檔案路徑完全相同，啟用子模組時將會直接覆寫本體檔案。當 TFR 本體更新這些檔案時，需特別留意相容性。

| 檔案路徑 | 覆寫目的 | 主要修改內容 |
| :--- | :--- | :--- |
| `events/TFR_events_ZZZ_news.txt` | 核心新聞事件觸發器 | • `news.121`：立即觸發 `CHI.10`（第三次石油危機）。<br>• `news.126`：立即觸發 `CHI.TW.7`（阿拉伯共和國重建）。<br>• `news.139`：為 `CHI` 分支觸發中華民國防衛超事件（`CHI_invasion_of_taiwan_super`）與專屬音樂。 |
| `common/ideologies/TFR_ideologies.txt` | 子意識形態定義 | 新增中華民國（ROC）自訂子意識形態：<br>• `social_democrat`：`tridemism_socdem`<br>• `social_liberal`：`Taiwanese_Progressivism`、`Taiwanese_Progressivism2`<br>• `market_liberal`：`taiwanese_liberal_populism2`<br>• `conservative`：`Taiwanese_constitutionalism`<br>• `authoritarian_democrat`：`han_kuo_yu_thoughts`<br>• `nationalist`：`CHI_ultimate_three_principles` |
| `common/scripted_localisation/TFR_subideology_scripted_loc.txt` | 子意識形態顯示本地化 | 將上述新增的中華民國子意識形態映射至對應的本地化顯示字串。 |
| `common/scripted_localisation/TFR_peace_popup_scripted_localisation.txt` | 議和彈窗文本 | 為 `CHI` 新增自訂的 OIOD 議和彈窗腳本本地化文本。 |
| `common/scripted_triggers/00_TFR_scripted_triggers_ZZZ_generic.txt` | 內容觸發器 | 在 `has_content_tag` 中加入 `tag = CHI`，使 `CHI` 被識別為擁有完整內容的國家。 |
| `common/bookmarks/TFR_the_fire_rises.txt` | 2020 劇本書籤 | 設定 `default_country = "CHI"`，並配置 2020 年中華民國開局精神、國策與劇本說明。 |
| `common/military_industrial_organization/organizations/TFR_organizations_ZZZ_generic.txt` | 通用軍工組織（MIO） | 防止通用裝甲／航空／軍需／造船軍工組織被分配給 `CHI`。 |
| `common/countries/cosmetic.txt` | 外觀標籤（Cosmetic tags） | 新增 `CHI_blackout` 以及中華民國專屬的動態外觀標籤。 |
| `common/map_modes/TFR_map_modes.txt` | 地圖模式 | 新增自訂國際組織地圖模式設定。 |
| `common/scripted_guis/TFR_startup_menu.txt` | 開局指南 GUI 腳本 | 為中華民國開局指南彈窗新增 `CHI_info_special_visible` 判定檢查。 |
| `interface/frontendgamesetupview.gui` | 國家選擇畫面 | 在劇本設定畫面中新增中華民國路線預覽旗幟與提示框（`GFX_KMT` / `GFX_DPP`）。 |
| `interface/frontendmainview.gui` | 主選單 UI | 自訂子模組主選單標誌（Logo）與位置配置。 |
| `interface/TFR_start_menu.gui` | 開局指南 GUI 佈局 | 在開局視窗中加入 `CHI_info_special` 圖示／按鈕。 |
| `interface/fonts_chinese.gfx` | 字型定義 | 調整簡體中文排版的備用字型映射（Fallback font mapping）。 |
| `Map/adjacencies.csv` | 地圖鄰接關係 | 自訂台灣本島與澎湖／金門／馬祖之間的跨海通道與鄰接設定。 |
| `Map/railways.txt` | 鐵路網路 | 台灣鐵路基礎設施配置。 |
| `Map/buildings.txt` | 3D 地標生成座標 | 在南京地塊 1222 新增 3D 地標生成位置（`1222;landmark_spawn;4664.15;10.10;1177.28;-0.07;0`），以渲染移植的南京總統府 3D 模型（`landmark_nanjing_presidential_palace`）。 |

---

## 2. 覆寫之圖像、材質與視覺資源

以下二進位圖片與材質檔案將直接替換 TFR 本體模組的資源：

### 旗幟（`gfx/flags/`）
| 檔案路徑 | 說明 |
| :--- | :--- |
| `gfx/flags/CHI_taiwan_republic.tga` | 台灣共和國旗幟（標準尺寸） |
| `gfx/flags/medium/CHI_taiwan_republic.tga` | 台灣共和國旗幟（中等尺寸） |
| `gfx/flags/small/CHI_taiwan_republic.tga` | 台灣共和國旗幟（小型／兵牌尺寸） |
| `gfx/flags/medium/HKN_conservative.tga` | 香港保守派陣營旗幟（中等尺寸） |

### UI 材質與介面美術（`gfx/interface/`）
| 檔案路徑 | 說明 |
| :--- | :--- |
| `gfx/interface/country_selection_bg.dds` | 國家選擇畫面背景美術圖 |
| `gfx/interface/logo_game.dds` | 遊戲／子模組標題畫面標誌（Logo） |
| `gfx/interface/thisisdog.dds` | 介面美術資源 |
| `gfx/texticons/banners/decisions/PROXY_saudi_cw_cat_banner.png` | 沙烏地內戰決議分類橫幅材質 |

### 肖像與領導人（`gfx/leaders/`）
| 檔案路徑 | 說明 |
| :--- | :--- |
| `gfx/leaders/CHI/CHI_chu_li_luan.png` | 領導人肖像：朱立倫（Eric Chu） |
| `gfx/leaders/CHI/CHI_hou_yu_ih.png` | 領導人肖像：侯友宜（Hou Yu-ih） |
| `gfx/leaders/CHI/generals/CHI_hsu_yen_pu.png` | 將領肖像：徐衍璞（Hsu Yen-pu） |
| `gfx/leaders/CHI/generals/Chiu_Kuo_Cheng.png` | 將領肖像：邱國正（Chiu Kuo-cheng） |

### 國策、科技與意識形態圖示（`gfx/interface/`）
| 檔案路徑 | 說明 |
| :--- | :--- |
| `gfx/interface/goals/CHI/CHI_grant_emergency_powers.png` | 國策圖示：授予緊急權力（Grant Emergency Powers） |
| `gfx/interface/ideas/CHI/mio_CHI_Jong_Shyn.png` | 軍工組織（MIO）圖示：中信造船（Jong Shyn Shipbuilding） |
| `gfx/interface/ideas/ZZZ_government_type/ZZZ_taiwanese_semi_presidential_system.png` | 國家精神圖示：中華五權共和制（ZZZ_taiwanese_semi_presidential_system） |
| `gfx/interface/ideologies/reformist_socialism_PRC.png` | 子意識形態圖示：左翼三民主義（PRC Reformist Socialism） |
| `gfx/interface/technologies/infantry/CHI_infantry1.dds` 至 `CHI_infantry6.dds` | 自訂步兵科技等級圖示（第 1 至 6 級） |

### 載入畫面桌布（`gfx/loadingscreens/` — 共 51 個檔案）
所有 TFR 本體模組的標準載入畫面皆已替換為子模組自訂的載入畫面美術圖：
* **編號檔案**：`load_1.dds` 至 `load_34.dds`
* **DLC／資料片命名檔案**：`load_aat.dds`、`load_aat2.dds`、`load_bba.dds`、`load_botb.dds`、`load_dod.dds`、`load_goe.dds`、`load_lar.dds`、`load_mtg.dds`、`load_mtg_2.dds`、`load_ncns_chi.dds`、`load_ncns_jap.dds`、`load_nsb.dds`、`load_nsb2.dds`、`load_tfv.dds`、`load_tiger.dds`、`load_toa.dds`、`load_ww.dds`

---

## 3. 已移除之覆寫檔案（清理完畢）

以下上游檔案曾被本子模組覆寫，但為了最大化與 TFR 本體模組的相容性，目前已**移除**並改用更簡潔的掛鉤（Hooks）方式實作：

* **`events/TFR_events_USA.txt`**：已移除。TFR 本體的 `usa.103` 事件在第二次美國內戰爆發時，原本就會為 `CHI` 觸發 `taiwan.2`。子模組事件 `CHI.3`（「太平洋之殤」）現已直接掛鉤於 `events/TFR_events_CHI.txt` 中 `taiwan.2` 的 `hidden_effect` 內。
* **`events/TFR_events_SAU.txt`**：已移除。該檔案原先唯一的自訂呼叫為 `CHI.10`（石油危機）與 `CHI.TW.7`（阿拉伯勝利）。這兩個事件現已改由子模組本身維護的 `events/TFR_events_ZZZ_news.txt` 中的 `news.121` 與 `news.126` 觸發。
* **`common/opinion_modifiers/china_modifier.txt`**：已移除。HoI4 的關係評價修正是累加讀取的；6 個中華民國專屬修正（`CHI_Block_tourists`、`CHI_ARR_humanitarian_aid`、`CHI_Diplomatic_countries`、`CHI_Assist_reconstruction`、`CHI_support_us`、`CHI_opposed_us`）已合併至既有的專屬檔案 `common/opinion_modifiers/TFR_CHI_opinion_modifiers.txt`，不再覆寫本體的 `china_modifier.txt`。
* **`common/game_rules/00_game_rules.txt`**：已移除。HoI4 支援累加讀取遊戲規則；3 個中華民國專屬遊戲規則（`CHI_election_2020_gamerule`、`CHI_election_2024_KMT`、`CHI_japan_return_land`）已移入獨立檔案 `common/game_rules/000_TFR_ROC_game_rules.txt`，並配置於頂層分類群組 `RULE_GROUP_TFR_ROC`（「烈焰升騰：同島一命」）之下。不再覆寫本體 5,760 行的 `00_game_rules.txt`。

---

## 4. 子模組專屬內容檔案

以下檔案為本子模組獨有，或包含中華民國（`CHI`）的主要核心內容：

* **國策（National Focus）**：`common/national_focus/TFR_national_focus_CHI.txt`
* **事件（Events）**：`events/TFR_events_CHI.txt`、`events/TFR_event_CHI_phase2.txt`~`phase4.txt`、`events/taiwan.txt`、`events/CHI_MIO_event.txt`
* **決議（Decisions）**：`common/decisions/TFR_decisions_CHI.txt`、`common/decisions/categories/TFR_decision_categories_CHI.txt`
* **遊戲規則（Game Rules）**：`common/game_rules/000_TFR_ROC_game_rules.txt`
* **關係評價修正（Opinion Modifiers）**：`common/opinion_modifiers/TFR_CHI_opinion_modifiers.txt`
* **角色與領導人（Characters & Leaders）**：`common/characters/TFR_characters_CHI.txt`
* **國家精神與動態修正（Ideas & Dynamic Modifiers）**：`common/ideas/TFR_ideas_CHI.txt`、`common/dynamic_modifiers/TFR_dynamic_modifiers_CHI.txt`
* **軍工組織（MIOs）**：`common/military_industrial_organization/organizations/TFR_organizations_CHI.txt`
* **歷史設定（History）**：`history/countries/CHI - China.txt`、`history/states/`（台北 1148、台中 1149、台南 1150、台灣 524、金門 648）、`history/units/`
* **圖形介面與超事件（GUI & Super Events）**：`interface/CHI_superevent.gui`、`common/scripted_guis/CHI_super_events.txt`、`sound/CHI_superevent_sounds.asset`
* **本地化文本（Localisation）**：`localisation/simp_chinese/`（`TFR_country_localisation_CHI_l_simp_chinese.yml`、`TFR_events_CHI_l_simp_chinese.yml`、`CHI_super_events_l_simp_chinese.yml` 等）

---

## 5. 第三方子模組相容性與補丁製作指南

若你正在開發 **The Fire Rises** 的其他子模組（例如像《Korea Plus 韓國擴展》等地區擴展子模組），或是打算製作讓多個 TFR 子模組與 **TFR-ROC** 同時運行的相容性補丁（Compatibility Patch），**[第 1 節（共有腳本檔案）](#1-共有腳本檔案上游邏輯覆寫) 所列出的檔案就是你必須進行合併（Merge）修改的目標。**

由於《鋼鐵雄心 IV》（HoI4）在處理同路徑檔案時是以「整個檔案覆寫」而非「逐行合併」的方式運作，只要兩個子模組修改了同一個 TFR 本體檔案，就會依據載入順序互相覆蓋。因此必須透過後置載入的相容性補丁將雙方的改動整合至同一份檔案中。

### 實際範例：韓國擴展子模組《The Fire Rises: Korea Plus (TFRKP)》
《Korea Plus》團隊曾針對 TFRKP 與 TFR-ROC 製作相容性補丁：
* **補丁名稱**：`TFRKP x ROC Compatibility`
* **Steam 工作坊 ID**：[`3791381497`](https://steamcommunity.com/sharedfiles/filedetails/?id=3791381497)（本地路徑：`F:\SteamLibrary\steamapps\workshop\content\394360\3791381497`）
* **相依關係（Dependencies）**：設定於 `The Fire Rises: Korea Plus` 與 `The Fire Rises: One Island, One Determination`（原名 `TFR - Republic of China`，工作坊 ID `3609728809`）之後載入。

#### 該補丁所合併的檔案一覽：
| 目標檔案路徑 | 雙方子模組合併內容說明 |
| :--- | :--- |
| `common/bookmarks/TFR_the_fire_rises.txt` | 合併 2020 開局書籤設定，整合 `CHI` 與 `KOR` 兩國的自訂開局敘述、精神與初始國策。 |
| `common/ideologies/TFR_ideologies.txt` | 合併 ROC 子意識形態（如 `Taiwanese_constitutionalism`、`Taiwanese_Progressivism`）與 KOR 的自訂子意識形態。 |
| `common/scripted_localisation/TFR_subideology_scripted_loc.txt` | 合併雙方子意識形態的動態顯示文字腳本。 |
| `common/scripted_triggers/00_TFR_scripted_triggers_ZZZ_generic.txt` | 將 `tag = CHI` 與 `tag = KOR` 一併加入 `has_content_tag` 判定。 |
| `common/military_industrial_organization/organizations/TFR_organizations_ZZZ_generic.txt` | 排除兩國分配通用軍工組織（加入 `NOT = { tag = CHI }` 與 `NOT = { tag = KOR }`）。 |
| `interface/frontendgamesetupview.gui` | 合併開局國家選擇介面，整合雙方的國旗按鈕、主要領導人圖像與路線提示。 |
| `interface/frontendmainview.gui` 與 `gfx/interface/country_selection_bg.dds` | 協調主選單排版與開局選角背景圖片衝突。 |
| `events/TFR_events_ZZZ_news.txt` | 若雙方皆有自訂新聞事件或超事件音樂分流，需在此處整合。 |

> [!WARNING]
> **TFRKP 相容補丁現況說明**：
> 依據《Korea Plus》開發團隊的說明，該 `TFRKP x ROC Compatibility` 補丁目前屬於**概念原型（Prototype）**階段（原話：*「It just proto-type so that make some unexpected bugs.」*）。雖然它提供了正確的補丁結構示範，但在實機運行中仍可能產生意料之外的 Bug、過時覆寫或腳本邏輯衝突，在正式遊玩或整合前建議先針對兩邊的最新版本進行測試與除錯。

### 無需製作相容補丁的檔案（已完全獨立隔離）：
[第 4 節（子模組專屬內容檔案）](#4-子模組專屬內容檔案) 所列之內容**完全不需要**製作補丁：
* **自訂遊戲規則**（`common/game_rules/000_TFR_ROC_game_rules.txt`）：採用獨立檔案累加載入至 `RULE_GROUP_TFR_ROC`，不覆寫本體 `00_game_rules.txt`。
* **關係評價修正**（`common/opinion_modifiers/TFR_CHI_opinion_modifiers.txt`）：累加載入，不覆寫本體 `china_modifier.txt`。
* **專屬國策、事件、決議、角色、軍工組織**：皆使用 `CHI` 專屬前綴獨立命名，互不干擾。

---

## 6. 上游更新同步檢查清單

當 TFR 本體模組於 Steam 工作坊更新時（路徑：`\SteamLibrary\steamapps\workshop\content\394360\3350890356`）：

1. **比對 `events/TFR_events_ZZZ_news.txt`**：確認 TFR 本體未重構新聞事件 ID。
2. **比對 `common/game_rules/00_game_rules.txt`**：確認 TFR 本體未變更規則分類或新增衝突的規則 ID（雖然我方已改用獨立檔案 `000_TFR_ROC_game_rules.txt`，仍需確認頂層分類有無衝突）。
3. **比對 `common/scripted_triggers/00_TFR_scripted_triggers_ZZZ_generic.txt`**：確認上游是否新增了任何骨架內容（Skeleton）或完整內容國家標籤（Content tags）。
4. **比對 `common/ideologies/TFR_ideologies.txt`**：檢查 TFR 本體是否新增了基礎意識形態或變更了子意識形態屬性。