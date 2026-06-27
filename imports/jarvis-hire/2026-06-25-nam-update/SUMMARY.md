# Jarvis Hire 6/25 進度彙報 — 全面彙整

> 來源：Nam (minh@jarvis-tec.com) 2026-06-25 透過 email 彙報
> 文件位置：`~/jarvis/imports/jarvis-hire/2026-06-25-nam-update/`
> - `01-strategy-deck.pdf` (29 頁，策略 deck，對內＋集團夥伴用)
> - `02-product-deck.pdf` (產品 deck，現有功能與三方輸出)
> - `03-sales-deck.pdf` (17 頁，BD/外部 outreach 用)

---

## 一、Nam 自陳已完成事項

| # | 項目 | 狀態 |
|---|------|------|
| 1 | 釐清供需雙邊市場痛點（雇主 + 候選人） | ✅ |
| 2 | 定義 Target Employer Persona + Candidate Persona | ✅ |
| 3 | 雙邊成長策略 | ✅ |
| 4 | Jarvis Hire 產品 V1 開發 | ✅（搬到新網域 `jarvis-hire.com`，本週五上線） |

## 二、Nam 自陳下一步

1. Finalize 產品 → 上線 `jarvis-hire.com` → 下月開始實戰測試市場
2. 籌備 Jarvis Hire 社群通路（FB / Threads / LinkedIn / Zalo）做直接 outreach
3. 提議下週一（6/29）下午 2 點開會

---

## 三、核心定位 One-liner

> **Vietnam's First Outcome-Based Hiring Engine**
> 為越南 FDI / 製造 / 物流 業者，提供「驗證過中文能力 + 產業適配 + 30 天試用後付費」的招募引擎。
> Tagline：「Hire faster with greater confidence.」

---

## 四、市場機會（Strategy Deck p.21）

| 指標 | 數值 | 意義 |
|------|------|------|
| 越中雙邊貿易 2025 | **$252B**（+26.5% YoY，歷史新高） | 中文人才需求底層動能 |
| 中文職缺 YoY 成長 | **+50%**（2024→2025） | 需求高速擴張 |
| 北越 KCN 開放職缺（2026 Q1） | **10,000+** | 短期內可見的真實需求 |
| 合格候選人覆蓋率 | **25–30%** | 70–75% FDI 雇主需求無法被滿足 |
| TAM | ~$15M | 越南全部 CN-VN 雙語招募（約 10K roles/yr） |
| SAM | ~$8M | 製造 FDI + 物流 + Trading（鎖定 KCN 區） |
| SOM（Year 1） | ~$500K | 4–6 verified hires/月 × 15–20% fee |

---

## 五、痛點診斷（雙邊）

### 雇主端（從 Facebook Group / freelance 抓人的世界）

- **CV 量大，品質難驗證** → screening 立刻變瓶頸
- **HSK 證書 ≠ 實戰中文** → 面試才發現做不了，浪費 30–90 天
- **產業適配度模糊** → 製造、物流、採購用同一套篩選邏輯
- **先付費再交付** → 候選人入職 1 個月內離職，雇主吃下所有風險
- **沒有專為中文崗位設計的平台** → 越南市場上沒有對手做這件事

### 候選人端（三種 Persona）

| Persona | 特徵 | 通路 |
|---|---|---|
| **P1 The Fast Mover** | Gen Z 女性 21–25、0–2 年資、自學中文（TikTok + WeChat 跟單）、要快錢與不封頂佣金；怕鬼公司、怕 11 點 WeChat 老闆文化 | FB / TikTok / Closed FB Groups（inbound） |
| **P2 The Strategic Mover** | Gen Y 女性 26–34、3–8 年資、書面中文但不會口說、要 100% 真實薪資保險、要職缺真的吻合 JD；怕變「中國老闆秘書」、怕 kiêm nhiệm（無限職責蔓延） | Zalo / LinkedIn / Navigos（inbound） |
| **P3 The Silent Specialist** | 男性工程師（QC/QA/ME/PE）、要被當工程師而非翻譯 | LinkedIn InMail outbound 專屬，**不能跟 P1 共用內容**（會互斥） |

---

## 六、目標雇主分群（ICP）

### Phase 1 主攻

| Tier | 對象 | 員工數 | 地點 | 核心痛 |
|---|---|---|---|---|
| **E1 Priority 1** | 製造 FDI（CN/TW/HK）HR/TA Manager | 100–1,500 | Bac Ninh / Hai Phong / Dong Nai 工業區 | 雙語職缺 30–90 天填不滿、TopCV 來的都不會中文 |
| **E2 Priority 1** | 物流供應鏈 HR / Operations Director | 50–1,000 | Hanoi / HCMC / Hai Phong | Sales Logistics 3–6 個月就離職、中國客戶岌岌可危 |

### Phase 1 次要

| Tier | 對象 | 痛點 |
|---|---|---|
| E3 | Electronics OEM/ODM 工程經理 | 技術中文工程師難找，候選人都跑去 Foxconn / Luxshare / Goertek（Phase 2 才主攻，因為需要技術文件驗證） |
| E4 | Tech SME / 中資 startup 創辦人 | 創辦人親自篩 CV、跨境溝通崩盤 |
| E5 | Trading / Sourcing 創辦人/GM | 創辦人翻譯供應商對話、PO 流程拖慢 |

### Strict non-ICP 過濾條件

員工 <20 人無 HR 編制 / 急迫性 ＜30 天 / 需求不清 / 一次性招募 / 付款紀錄差 / 在越南沒實體營運

---

## 七、產品架構（RPO 引擎）

### 6 個核心模組

```
1. JD Intake          → AI 結構化雙語 JD，分離 must-have / nice-to-have
2. Candidate Pool     → 用中文程度、年資、薪資、空閒度做主動 sourcing
3. Language Fit       → HSK 1–6 線上測驗 + AI 評分 + 跨應用徽章重用
4. Domain Fit         → 從雇主訓練文件生成客製測驗，候選人申請前必過
5. AI Matching        → 8 維度（embeddings + GPT 判斷）排序產出 shortlist
6. Pipeline Dashboard → Kanban + SLA + 轉換分析 + drop-off 原因
```

### 已上線（What's Live Now）

- ✅ 線上中文能力測驗（AI 評分）
- ✅ HSK 證書 OCR 自動驗證 + Jarvis verified badge
- ✅ AI Match Score + 給雇主的摘要報告（含優勢/弱勢/風險）
- ✅ 客製 Domain screening test（候選人申請前必過）
- ✅ Hiring pipeline + 候選人池 + AI 智能搜尋
- ✅ 30 天到職驗證流程（Ops 確認真實到職才開發票）

### 候選人申請流程（5 步）

```
Submit CV → Chinese Verification → Domain Assessment → AI Match Score → HR Shortlist
```

### 雇主招募流程（5 步）

```
Submit JD → Jarvis pre-qualify（48h 內 shortlist）→ 面試 → 30 天試用 → 90 天保證（離職免費補人）
```

---

## 八、定價策略（Sales Deck p.13–15）

四套方案：

| 方案 | 月費 | 主要功能 |
|---|---|---|
| **Starter** | 0 VND | 發職缺 + 主動配對 Top 20 |
| **Standard** | 3,000,000 VND | + AI CV 篩選 + AI 面試題 + 主動配對 Top 50 + flight risk 分析 |
| **Pro** | 5,500,000 VND | + 優先配對 + 中文測驗 + Domain 測驗 + 完整 AI Suite |
| **Success Fee** ⭐ Recommended | **15–20% / 年薪** | 全部功能 + 客戶整合 + 月度 HR 報告 + 保固。**無到職不收費**，發票要等候選人做滿 30 天才出 |

關鍵原則：**No upfront fees**、**Pay-for-performance**、 **與雇主同站一邊**

---

## 九、競爭定位（Strategy Deck p.7）

二維象限：橫軸（廣度／中文專精度）× 縱軸（AI workflow / 純人工 service）

| 競爭者 | 位置 | 評語 |
|---|---|---|
| VietnamWorks | 廣度大 + 一般化 | 廣度贏，深度輸 |
| TopCV | 廣度大 + HR 生態強 | 仍是 generalist |
| JobsGO | 廣度大 + 一般化 | broad market |
| Yufei HR | 中文專精 + **純人工** | 唯一垂直對手，但無 AI 與 workflow |
| **Jarvis Hire** | 中文專精 + AI workflow | **獨佔象限：AI x Chinese-Language Specialist** |

護城河（Flywheel）：
```
更多成功招募 → 更精準演算法（Data Moat）
              ↓
              更多雇主來 → 吸引更多候選人（Network Effect）
              ↓
              反覆成功 → 品牌信任 + 推薦（Brand Trust）
              ↓
              workflow 嵌入越深 → switching cost 越高（Product Lock-in）
```

---

## 十、商業節奏（Phased Roadmap）

### 四階段

| 階段 | 目標 | 訊號 |
|---|---|---|
| **Phase 1 PMF** | 窄場景證明招募成果，不亂長功能 | Repeat employers |
| **Phase 2 Monetize** | Pilot 轉付費，學習買家真正願意付什麼 | Stable ARR |
| **Phase 3 Scale** | 啟動 partner channel，擴運營 | Low churn |
| **Phase 4 Platform** | 廣生態 + 整合 + 數據護城河 | Platform revenue |

**重要原則**：候選人留存功能放在後面做，先把雇主端 wedge 打通。

### Ecosystem Timeline（生態擴張）

```
2026 │ Candidates + Employers   核心配對引擎上線
2027 │ RPO Services             為越南企業客戶做完整 RPO
2028 │ Taiwan Companies         拓展到台廠招越南人才
2029 │ SEA Talent Pool          跨境人才網絡（東南亞 + 大中華）
```

### Education → Recruitment 補給線

學生社團 → 中文補習中心 → 中國 FDI 企業（訓練場域）→ Jarvis Education（AI 工作訓練）→ Jarvis Hire → FDI 雇主

時程：Q3 2026 簽 MOU → Q4 2026 第一期學員入池 → Q1 2027 AI 課程上線 → Q2 2027 開始收訓練安置費

---

## 十一、KPI / 北極星

### 長期北極星

**Successful Paid Hires**（不是 DAU / 不是 engagement）

### Phase 1（接下來 3 個月）目標

| 量化指標 | 目標 |
|---|---|
| Candidate signups | 150 |
| Activated candidates | 60 |
| Employer signups | 30 |
| Active employers | 15 |
| Jobs posted | 15 |
| **Paid pilots** | **2–3** |

### Operating signals（PMF 早期訊號）

| 訊號 | 門檻 |
|---|---|
| Time to first shortlist | **<48h** |
| Repeat employer rate | **>30%** |
| Qualified candidate ratio | **>70%** |
| Day-30 hire retention | **>95%** |

---

## 十二、Go-to-Market 通路

| 通路 | 適用 |
|---|---|
| **Direct Enterprise**（主力） | 有反覆招中文人才需求的越南雇主 |
| **Agency / RPO** | 需要「篩選層」的招募夥伴（用 Jarvis 當 screening tool） |
| **Embedded** | HR 軟體商想加上 AI 招募能力 |
| **Managed RPO** | 雇主把整個招募流程外包給 Jarvis |

### 雇主 5 階段 Acquisition Funnel

```
01 Awareness   → FB Group / FDI Community / Logistics Community / LinkedIn（戳痛點）
02 Credibility → Fanpage / LinkedIn / Zalo / WeChat（薪資 benchmark、Mandarin badge、OCR HSK、Work-Ready Mandarin）
03 Micro-conv  → Fanpage DM / LinkedIn InMail / Zalo Direct（P1：送 JD 免費 review、P2：15 分鐘市場通話、P3：DM "48H"）
04 Qualification → 直接電話 / Email / Zalo（過 ICP 篩網：急 ≤30 天、預算清楚、簽 success fee）
05 Placement   → 48h SLA 給 shortlist，**Day 30 才開發票**
```

每丟掉一個 deal 都要有「Lost Reason Code」回饋給 Marketing / BD。

---

## 十三、營運紀律（Operating Discipline）

四條鐵律：

1. **No sourcing without qualified demand** — 沒有合格需求不去找人
2. **No hire without Day 30 verification** — 沒做滿 30 天不算 hire
3. **No invoice without verification completion** — 驗證沒完成不開發票
4. **No automation before process stability** — 流程沒穩之前不上自動化

→ 全部 manual-first，先把流程跑順再上系統。

---

## 十四、Reflections / 我的觀察與建議

### 做得好的地方

1. **定位非常乾淨** — 「outcome-based + Chinese-language specialist」直接切走 generalist 平台的擁擠戰場，competitive map（Strategy p.7）那張圖是整套故事的精華。
2. **市場數據紮實** — $252B 雙邊貿易、+50% JD 成長、25–30% 覆蓋率，這三個數字串起來能直接拿去 pitch。
3. **PMF 訊號定義對** — 北極星拒絕 DAU/engagement，鎖定「verified paid hires + repeat employer」，這在招募業是對的選擇。
4. **產品確實已經跑起來** — Live now 那 6 個模組（含 HSK OCR + AI Match + Domain test + Day-30 verification）是有實體的，不只是 deck。
5. **Pricing 策略聰明** — Starter 免費鋪量、Success Fee 對齊雇主風險，這個組合在越南市場有差異化。

### 值得追問 / 需要驗證

| 問題 | 為什麼重要 |
|---|---|
| 「Active employers 15 / Jobs posted 15」是不是已經有了？還是 3 個月後的目標？ | 直接決定我們現在是 pre-PMF 還是 in-PMF |
| Phase 1 target「2–3 paid hires in 3 months」是否包含本月（6 月）跑出來的數字？ | 看實際進度落後或超前 |
| Success Fee 15–20% 在越南製造 FDI 是否賣得動？同業是 1–2 個月底薪 | 需要 BD 實測，可能要分產業 anchor |
| `jarvis-hire.com` 上線後第一週流量／註冊轉換率 | 7/3（週五）後一週要看 |
| Day-30 驗證機制怎麼防雇主和候選人串通造假？ | 影響 Success Fee 模型的 unit economics |
| Education → Recruitment 補給線是否會稀釋焦點？Phase 1 應該 100% 收斂在 wedge 上 | 時間分配風險 |

### 我建議週一會議要對齊的事

1. **目前 jarvis-hire.com 上線時程 + 完成清單**（Friday go-live 風險評估）
2. **6 月已實際接觸 / 簽約的雇主 logo**（讓 KPI 數字落地）
3. **15–20% Success Fee 已經報過幾家、有沒有拿到 verbal/written buy-in**
4. **三份 deck 的對外溝通邊界**（哪份能對誰）：
   - Strategy Deck → 集團內 + 投資人 + 長期 partner
   - Product Deck → 對 prospect 做產品教育
   - Sales Deck → BD outreach 第一份遞出去的
5. **Phase 1 過 3 個月後如果 paid pilots 沒達到 2–3，是否預設 stop & re-plan 觸發條件**
6. **社群通路（FB/Threads/LinkedIn/Zalo）內容團隊資源**（是 Nam 自己寫還是有 content support）

---

## 十五、附錄：檔案位置與雜訊清理

```
~/jarvis/imports/jarvis-hire/
├── 2026-06-24/                        ← 舊版本（檔名其實命名錯誤：實為 sales + strategy）
│   ├── 01-strategy-deck.pdf           = 跟今天的 03-sales-deck.pdf MD5 相同
│   └── 02-product-deck.pdf            = 跟今天的 01-strategy-deck.pdf MD5 相同
└── 2026-06-25-nam-update/             ← 本次 Nam 彙報的正確版本
    ├── 01-strategy-deck.pdf  (4.2MB, 29 頁)
    ├── 02-product-deck.pdf   (7.9MB)
    ├── 03-sales-deck.pdf     (1.3MB, 17 頁)
    └── SUMMARY.md            ← 本檔
```

> ⚠️ Note：6/24 那批檔案命名跟內容對不上（02-product-deck.pdf 其實是 strategy 內容），建議下次回頭整理時把 6/24 那組也修正或標註。
