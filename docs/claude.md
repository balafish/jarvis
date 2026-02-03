# Claude 寫作模式設定

> 讀取此文件後，說「執行寫作模式」即可啟動所有設定

---

## 寫作模式

用於制定策略、撰寫文檔的協作模式。

### 啟動方式

```
用戶：讀取 claude.md，執行寫作模式
```

### 核心流程

```
討論 → 確認 → 產出 → 審核 → 推送
```

---

## 討論階段（省錢模式）

討論時自動啟用，節省 token：

| 原則 | 說明 |
|------|------|
| 簡潔回覆 | 重點列表，不需完整句子 |
| 確認優先 | 先確認理解，再行動 |
| 不主動產出 | 討論時不執行文件撰寫 |
| 編號選項 | 提供選項用數字，方便快速回覆 |

### 快速回覆方式

- 數字選擇：「1」「2」「3」
- 簡短確認：「是」「對」「正確」「確認」
- 指令式：「推送」「繼續」「產出」

---

## 產出階段

當用戶說「開始產出」或「確認」後：

| 原則 | 說明 |
|------|------|
| 完整內容 | 不精簡，完整撰寫 |
| 優化語句 | 適合對外發表的品質 |
| 多語言 | 先中文，確認後再翻譯 |

---

## 記憶持久化

### 機制

使用 `discussion-notes.md` 保存進度，搭配 Git 推送。

### 「我要離開」觸發

當用戶說「我要離開」，自動執行：

1. 更新 `discussion-notes.md`
   - 目前進度
   - 已確認事項
   - 待辦事項
   - 下次繼續方向
2. Git commit & push
3. 輸出簡短摘要

### 「我回來了」接續

讀取 `discussion-notes.md`，回報：
- 上次進度
- 待辦事項
- 建議下一步

---

## 文件規範

### 多語言結構

```
docs/
├── zh/    # 中文（優先產出）
├── en/    # English
└── vi/    # Tiếng Việt
```

### 產出順序

1. 先產出中文版
2. 用戶確認後再翻譯
3. 節省修改成本

---

## 常用指令

| 指令 | 效果 |
|------|------|
| 執行寫作模式 | 啟動本文件所有設定 |
| 省錢模式 | 進入精簡討論（預設） |
| 開始產出 | 進入完整產出階段 |
| 推送 | Git add + commit + push |
| 我要離開 | 更新筆記 + 推送 + 摘要 |
| 我回來了 | 讀取筆記 + 回報進度 |
| 檢查校正 | 全面檢查文件品質 |
| 執行摘要圖模式 | 啟動圖片生成設定（Imagen Ultra） |
| 產生投影片 | 使用 2slides 生成 PPT 簡報 |

---

## 檢查校正

當用戶說「檢查校正」時，執行以下檢查：

### 檢查項目

1. **語句通順**：檢查是否有不通順、語意不清的句子
2. **拼字正確**：檢查是否有錯字、漏字
3. **內容完整**：檢查是否有未完成的段落、缺失的內容
4. **格式一致**：檢查標題層級、表格格式是否一致
5. **連結有效**：檢查內部連結是否正確

### 輸出格式

產生分析報告，包含：

```
## 檢查校正報告

### 總覽
- 檢查文件數：X
- 發現問題數：X
- 嚴重程度：高/中/低

### 問題清單

| 文件 | 位置 | 問題類型 | 問題描述 | 建議修正 |
|------|------|----------|----------|----------|
| ... | ... | ... | ... | ... |

### 建議
- ...
```

### 自動修正

報告產生後，詢問用戶是否自動修正

---

## 協作原則

1. **不猜測**：資訊不足時詢問
2. **先確認**：重要事項確認後再執行
3. **保持簡潔**：討論時精簡回覆
4. **及時儲存**：重要進度推送 Git
5. **尊重決策**：用戶說不改就不改

---

## 產生摘要圖模式

用於生成投影片風格的摘要圖片，包含完整文字內容。

### 啟動方式

```
用戶：執行摘要圖模式
```

### 工具與模型設定

| 設定項目 | 值 |
|---------|-----|
| API | Google Gemini Imagen |
| 模型 | `imagen-4.0-ultra-generate-001` |
| 環境變數 | `GOOGLE_API_KEY` |
| SDK | `google-genai` |
| 輸出目錄 | `~/jarvis/images/` |

### 圖片生成參數

```python
client.models.generate_images(
    model="imagen-4.0-ultra-generate-001",
    prompt=prompt,
    config=types.GenerateImagesConfig(
        number_of_images=4,      # 每張生成 4 個變體供選擇
        aspect_ratio="16:9",     # 投影片比例
    )
)
```

### Prompt 結構模板

```
[風格定義]
Professional business presentation slide, clean modern design.
Dark blue (#1a365d) to teal (#0d9488) gradient background.
Flat-style icons and visual elements. High contrast, white accents.
Corporate tech startup aesthetic. 16:9 aspect ratio layout.

[內容描述]
Title: "標題文字"
描述要呈現的內容重點、文字、數據...
搭配相關 icon 和視覺元素
```

### 內容規劃原則

| 原則 | 說明 |
|------|------|
| 優先英文 | 英文內容生成品質較佳 |
| 完整摘要 | 可包含標題、重點、數據 |
| 搭配視覺 | 文字內容搭配 icon、圖表、流程圖 |
| 多版選擇 | 每張生成 4 個變體，選最佳版本 |

### 檔案命名規則

```
{主題}_{序號}_{名稱}_{變體}.png

範例：
plan_01_vision_a.png
plan_01_vision_b.png
group_03_jarvis_c.png
```

### 執行流程

```
1. 讀取來源文檔（優先英文版）
2. 規劃圖片內容（標題 + 重點 + 視覺元素）
3. 確認規劃後執行生成
4. 每張生成 4 個變體
5. 用戶選擇最佳版本
```

### MCP Server 設定

配置 `~/.cursor/mcp.json`：

```json
{
  "mcpServers": {
    "image-generator": {
      "command": "/bin/zsh",
      "args": ["-c", "source ~/.zshrc && /Users/max/jarvis/mcp/.venv/bin/python /Users/max/jarvis/mcp/image_server.py"]
    },
    "2slides": {
      "url": "https://2slides.com/api/mcp?apikey=YOUR_API_KEY"
    }
  }
}
```

### 2slides MCP 工具

用於生成專業 PPT/投影片，文字 100% 準確。

| 工具 | 用途 |
|------|------|
| `slides_generate` | 根據內容生成投影片 |
| `slides_create_like_this` | 根據參考圖片生成類似風格 |
| `themes_search` | 搜尋投影片模板 |
| `jobs_get` | 查詢生成進度 |

**使用範例：**
```json
{
  "themeId": "st-xxx",
  "userInput": "2026 Company Plan summary",
  "responseLanguage": "English",
  "mode": "async"
}
```

### 常見問題處理

| 問題 | 解決方案 |
|------|---------|
| 文字拼寫錯誤 | 生成多版本選擇，或後製修正 |
| 模型找不到 | 用 `client.models.list()` 查詢可用模型 |
| API Key 無效 | 確認 `GOOGLE_API_KEY` 環境變數 |
| 排版不如預期 | 調整 prompt 描述，多生成幾版 |

---

## 產生投影片模式

用於生成專業 PPT 投影片，文字 100% 準確，適合正式簡報。

### 啟動方式

```
用戶：產生投影片
用戶：幫我做一份 XXX 的簡報
```

### 工具與設定

| 設定項目 | 值 |
|---------|-----|
| MCP 工具 | `2slides` |
| 執行方式 | `npx -y 2slides-mcp` |
| 環境變數 | `API_KEY`（已在 mcp.json 配置） |

### 可用工具

| 工具 | 用途 |
|------|------|
| `slides_generate` | 根據內容生成投影片 |
| `slides_create_like_this` | 根據參考圖片生成類似風格 |
| `themes_search` | 搜尋投影片模板風格 |
| `jobs_get` | 查詢生成進度（async 模式） |

### 執行流程

```
1. 確認簡報主題與內容來源
2. 搜尋合適的模板風格（themes_search）
3. 規劃投影片架構（頁數、每頁重點）
4. 確認後執行生成（slides_generate）
5. 等待生成完成，提供下載連結
```

### slides_generate 參數

```json
{
  "themeId": "st-xxx",           // 模板 ID（從 themes_search 取得）
  "userInput": "簡報內容描述",    // 內容需求
  "responseLanguage": "English", // 輸出語言
  "mode": "async"                // async=背景生成, sync=即時等待
}
```

### 最佳實踐

| 原則 | 說明 |
|------|------|
| 先搜模板 | 用 `themes_search` 找合適風格 |
| 英文生成 | 英文內容品質較佳，可後續翻譯 |
| 明確架構 | 提供清晰的大綱和重點 |
| Async 模式 | 複雜簡報用 async，避免超時 |

### 與摘要圖模式的差異

| 面向 | 產生投影片 | 摘要圖模式 |
|------|-----------|-----------|
| 工具 | 2slides MCP | Imagen API |
| 輸出 | PPT 檔案 | PNG 圖片 |
| 文字準確度 | 100% 準確 | AI 生成，可能有誤 |
| 適用場景 | 正式簡報 | 視覺素材、社群圖 |

---

*啟動寫作模式後，以上設定自動生效*
