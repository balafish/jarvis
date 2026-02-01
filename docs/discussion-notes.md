# 討論筆記

> 此檔案記錄與 AI 助手的討論進度，方便下次繼續

---

## 最後更新：2026-02-01

## 進行中的主題

### 主題一：2026 公司計劃
- 狀態：已建立文件框架，內容待填入
- 文件：goals.md, strategy.md, budget.md, timeline.md

### 主題二：集團業務概覽（以 Jarvis 為主軸）
- 狀態：討論中，收集公司資訊
- 對象：Jarvis 全體員工
- 目的：說明集團業務與各公司關係

---

## 已收集的集團資訊

### 集團架構

**母公司：獨角獸國際投資有限公司**

```
獨角獸國際投資有限公司 (控股母公司)
    │
    ├── Siraya (雲端/CDN/安全服務商)
    │
    ├── Jarvis (軟體開發)
    │       └── Siraya 產品：客戶後台、防劫持
    │
    ├── 勝海科技 (iGaming 研發)
    │       └── 包網、金融、支付、自動化
    │
    ├── Tomo (AI 新創)
    │       └── AI HR、AI SRE、AI Dealer
    │
    ├── 艾瑞爾 (遊戲發行代理)
    │       └── RO、一拳超人等
    │
    ├── 宇洋數位 (金融科技)
    │       └── 移工跨境小額匯兌
    │
    └── 凱尹訊息 (數位點數販售)
            └── 遊戲虛擬點數卡
```

### 集團總覽表

| 公司 | 定位 | 主要業務 |
|------|------|----------|
| **獨角獸國際投資** | 控股母公司 | 投資管理 |
| **Siraya** | 雲端/CDN/安全服務商 | Compute、CDN、Security、Streaming |
| **Jarvis** | 軟體開發 | 客戶後台、防劫持產品 |
| **勝海科技** | iGaming 研發 | 包網、金融、支付、自動化 |
| **Tomo** | AI 新創 | AI HR、AI SRE、AI Dealer |
| **艾瑞爾** | 遊戲發行代理 | RO、一拳超人等 |
| **宇洋數位** | 金融科技 | 移工跨境小額匯兌 |
| **凱尹訊息** | 數位點數販售 | 遊戲虛擬點數卡 |

---

## 各公司詳細資訊

### Siraya Technologies
- 官網：https://www.sirayatech.com/
- 定位：雲端運算、邊緣交付與安全服務供應商
- 產品線：
  - Compute：Cloud Services、Co-Location、VPS、AI Services
  - Edge Delivery：CDN、Edge Compute
  - Streaming：Live Streaming、Low Latency Streaming、Real-Time Communication
  - Cloud Security：Anti-DDoS、WAF、Bot Management、API Protection
  - Professional Services：Cloud Migration、Kubernetes、DevOps、滲透測試、SOC
- 解決方案：Global To China、互動娛樂與直播、Anti-Hijacking、iGaming Platform
- 合作夥伴：AWS、Azure、Google Cloud、Alibaba Cloud、Akamai、Cloudflare 等

### Jarvis
- 定位：軟體開發公司
- 主要業務（目前為 Siraya 開發）：
  1. 客戶後台管理系統 — 整合雲服務、CDN、數據監控、帳號管理
  2. 防劫持產品 — Anti-Hijacking Solution

### 勝海科技 (Katsumitec)
- 官網：https://katsumitec.com/
- 成立時間：2020年11月
- 定位：iGaming 研發公司
- 主要研發項目：
  - 包網系統
  - 金融系統
  - 支付系統
  - 自動化程序
- 過去曾與 Siraya 合作

### Tomo（AI 新創）
- 定位：AI 解決方案提供者
- 願景：推動 AI 技術成為產業創新的核心動能
- 產品線：
  1. **AI HR (MVP)** — 智能招募系統
     - 自動 AI Sourcing、7大面向評分、產生面試提問、即時推播
     - 成效：審閱時間節省16倍、招募時間減少2.66倍
  2. **AI SRE (PoC)** — 智能運維系統
     - Multi-Agents 框架、多資料源 RCA、視覺化圖表、Human Feedback
  3. **AI Dealer (Prototype)** — 數位荷官
     - 即時換牌/換人/換背景、Streaming 或 API 串接、客製化機率控制

### 艾瑞爾 (Ariel)
- 官網：https://www.ariel.com.tw/
- 定位：遊戲發行代理
- 知名代理遊戲：RO（仙境傳說）、一拳超人

### 宇洋數位股份有限公司
- 成立時間：2024年
- 定位：金融科技新創公司
- 主要業務：移工跨境小額匯兌、電子商務服務
- 服務對象：移工族群

### 凱尹訊息股份有限公司
- 成立時間：2024年
- 定位：數位遊戲點數販售
- 主要業務：數位卡（虛擬點數卡）銷售服務

---

## Jarvis 與集團公司合作關係

| 合作公司 | 合作內容 | 時期 |
|----------|----------|------|
| **Siraya** | 客戶後台管理系統、防劫持產品 | **目前主要業務** |
| **勝海科技** | Telegram 原生產品、ClickHouse 大數據調研、支付渠道串接 | 過去（Jarvis 剛成立時） |
| **Tomo** | AI HR 產品展示 → 未來可能在越南市場合作客製化研發 | 未來規劃 |
| 艾瑞爾 | 無直接合作 | — |
| 宇洋數位 | 無直接合作 | — |
| 凱尹訊息 | 無直接合作 | — |

### Jarvis 發展歷程

```
過去 ──────────────────────────> 現在 ──────────> 未來

[勝海科技合作]                    [Siraya 專屬開發]     [Tomo 合作]
 • Telegram 產品                   • 客戶後台系統        • AI HR 越南市場推行
 • ClickHouse 調研                 • 防劫持產品          • 客製化研發合作
 • 支付渠道串接
```

---

## 待確認事項

- [ ] 各公司股權結構/持股比例
- [ ] Jarvis 在越南市場的優勢說明（有辦公室/團隊？優勢是什麼？）
- [ ] 各公司基本資料（員工人數、地點等）
- [ ] Jarvis 公司基本資料（成立時間、員工人數等）
- [ ] 獨角獸國際投資的更多資訊（成立時間等）

---

## 下次繼續

1. 補充 Jarvis 在越南市場的優勢資訊
2. 確認其他待確認事項
3. 開始填入集團業務概覽文件內容
4. 接續討論 2026 公司計劃

---

*提醒：每次討論結束前更新此檔案並推送到 Git*
