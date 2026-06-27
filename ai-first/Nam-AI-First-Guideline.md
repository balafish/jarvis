# Nam AI-First Engineering Guideline

> 來源：越南主管 Nam 分享的 AI-First 工程指南
> Google Drive: https://drive.google.com/drive/folders/17HnltOWk6UJgznzBbpmMjG8twUTe3vrX
> 建立日期：2026-04-23

---

## #0 — AI Engineering Playbook（工具手冊）

### 快速決策表

| 使用場景 | 工具 |
|---|---|
| 快速思考 / 腦力激盪 | ChatGPT |
| 深度推理 / 架構設計 | Claude |
| 文件理解 / 知識整理 | NotebookLM |
| UI 原型設計 | Google Stitch |
| IDE 內編程輔助 | GitHub Copilot |
| 私有 / 離線工作 | Local LLM (Ollama) |
| 多 Agent 並行任務 | Paperclip |

### 工具重點

- **ChatGPT**：速度快，適合快速答案，但邏輯需驗證
- **Claude**：最適合深度、複雜推理；提供完整 context
- **NotebookLM**：閱讀文件、萃取洞見；不適合寫程式
- **Google Stitch**：UI 快速原型，非正式產品 code
- **GitHub Copilot**：填補重複性 code，需 review（可能 hallucinate）
- **Ollama**：私有資料、離線需求；品質低於雲端
- **Paperclip**：Plan → Execute → Review → Refine 的多 Agent 工作流
- **LocalCodeSearch**：語意搜尋 codebase，適合大型或新專案 onboarding

---

## #1 — Foundation: Mindset & Principles（思維與原則）

### AI-First vs AI-Assisted

| 面向 | AI-Assisted（現況） | AI-First（目標） |
|---|---|---|
| AI 角色 | 輔助工具 | 主要執行者 |
| 人類角色 | 建造者 | 控制者 |
| 工作流程 | 手動優先 | 系統優先 |
| 擴展性 | 線性 | 指數型 |

### Harness Engineering 核心思想

> 不是讓人類寫更快，而是設計讓 AI Agent 能正確產出的系統

- 失敗原因不是「人不夠努力」
- 失敗原因是「系統缺少能力或約束」
- 修法：改善 prompt、retrieval、結構、驗證層

### 工程師角色轉變：Coder → Controller

**舊角色（Coder）**：手動實作、逐行 debug、擁有執行
**新角色（Controller）**：
1. 深入理解問題
2. 擷取相關系統 context
3. 指示 AI 生成解決方案
4. Review 並精煉輸出
5. 確保系統正確性

> 你的薪水不是為了寫程式，而是確保系統產出正確的程式。

### 5 大核心操作原則

1. **AI 是預設執行者**：所有實作的第一版由 AI 生成
2. **先取回再生成**：每次 AI 請求前，先搜尋現有 code 和知識
3. **結構化輸入產出結構化輸出**：必須包含 Feature、Constraints、Expected behavior、Edge cases
4. **人類做驗證，不做生產**：人類負責正確性、安全性、業務對齊
5. **一切都是系統，不是任務**：每次變更需考慮上下游影響

---

## #2 — Core Execution Workflows（執行工作流程）

### 端到端工作流概覽

| 步驟 | 目標 | 主要產出 |
|---|---|---|
| 1. Research | 理解問題與約束 | 結構化需求摘要 |
| 2. PRD + UI + Docs | 想法 → 產品定義 | PRD（Git 版控）、UI mockups |
| 3. Development | 從 PRD 實作功能 | Feature branch + PR |
| 4. Testing | 確保正確性 | 測試覆蓋率報告、驗證後的 PR |
| 5. Code Review | 確保生產就緒 | 核准 PR + 改進 |
| 6. Release & Monitor | 安全部署 + 觀察 | 生產發佈 + 回饋迴圈 |

### 開發工具選擇指南（VSCode）

| 工具 | 適合任務 | 強項 |
|---|---|---|
| Copilot | 簡單、重複任務 | 最快的 inline 補全 |
| Codex | 中輕度任務（小功能、快速修正） | 比 autocomplete 更結構化 |
| Continue | 中等任務（多檔編輯、重構） | 良好的 codebase context |
| Claude | 重型、複雜任務（架構、深度重構） | 強推理，大 context |

### 重要資源

- LocalCodeSearch: https://github.com/nam-jarvis/LocalCodeSearch
- EveryStepAI: https://github.com/nam-jarvis/EveryStepAI
- Git Flow Guide: https://github.com/nam-jarvis/EveryStepAI/blob/main/dev/git/developer-gitflow.md
- Test Generation: https://github.com/nam-jarvis/EveryStepAI/blob/main/test/README.md
- Release Guide: https://github.com/nam-jarvis/EveryStepAI/blob/main/dev/release/README.md

---

## 待辦

- [ ] 下週一（2026-04-27）回覆 Nam 關於此文件的意見
