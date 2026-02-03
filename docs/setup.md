# Jarvis 專案設定

## 1. 圖片產生 MCP（Cursor 內用 AI 產圖）

使用 **Google Imagen**，需先設定 API Key，再註冊 MCP。

### 步驟一：設定 Google API Key

```bash
# 專案根目錄
./setup-google-key.sh
# 或直接帶入 key：./setup-google-key.sh '你的_GOOGLE_API_KEY'
source ~/.zshrc
```

### 步驟二：註冊 Cursor MCP

```bash
./setup-mcp.sh
```

會寫入 `~/.cursor/mcp.json`，讓 Cursor 啟動 `mcp/image_server.py`（需已存在 `mcp/.venv` 且裝好依賴）。

### 步驟三：重開 Cursor

完全關閉 Cursor 後再開啟，或在設定中重新載入 MCP。之後在對話中即可使用「產生圖片」相關工具。

---

## 2. 依賴（mcp 目錄）

```bash
cd mcp
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

---

## 3. 批量產圖（指令列）

不透過 Cursor，直接在終端機跑腳本：

```bash
source ~/.zshrc   # 載入 GOOGLE_API_KEY
cd mcp
.venv/bin/python generate_images_gemini.py
```

圖片會存到專案的 `images/` 目錄。

---

## 快速檢查

- **GOOGLE_API_KEY 是否生效**：`echo $GOOGLE_API_KEY`（應有輸出）
- **MCP 是否註冊**：查看 `~/.cursor/mcp.json` 內是否有 `image-generator`，且 `command` 指向 `mcp/.venv/bin/python`、`args` 指向 `mcp/image_server.py`
