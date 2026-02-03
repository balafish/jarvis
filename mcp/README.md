# MCP 與圖片產生

## 環境

- Python 3.12 + 虛擬環境 `.venv`
- 依賴：`pip install -r requirements.txt`

## Google 批量產圖（Gemini Imagen）

1. **設定 API Key**（專案根目錄）：
   ```bash
   ./setup-google-key.sh
   # 或：./setup-google-key.sh '你的_GOOGLE_API_KEY'
   ```
2. **讓終端機載入 key**：
   ```bash
   source ~/.zshrc
   ```
3. **執行**：
   ```bash
   cd mcp
   .venv/bin/python generate_images_gemini.py
   ```
   圖片會存到專案的 `images/` 目錄。

## Cursor 圖片 MCP（DALL-E）

由 `setup-python-mcp.sh` 設定，使用 `OPENAI_API_KEY`，見專案根目錄說明。
