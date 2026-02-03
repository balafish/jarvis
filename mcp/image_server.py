#!/usr/bin/env python3
"""
MCP Server for Image Generation using Google Gemini Imagen
"""

import os
import sys
import asyncio
from datetime import datetime
from pathlib import Path

# MCP SDK
try:
    from mcp.server import Server
    from mcp.server.stdio import stdio_server
    from mcp.types import Tool, TextContent
except ImportError:
    print("請安裝 MCP SDK: pip install mcp", file=sys.stderr)
    sys.exit(1)

try:
    from google import genai
    from google.genai import types
except ImportError:
    print("請安裝 Google GenAI SDK: pip install google-genai", file=sys.stderr)
    sys.exit(1)

# 設定
IMAGES_DIR = Path.home() / "jarvis" / "images"
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

# 初始化
server = Server("image-generator")
client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))


@server.list_tools()
async def list_tools():
    """列出可用工具"""
    return [
        Tool(
            name="generate_image",
            description="使用 Google Imagen 3 生成圖片。輸入描述文字，產生對應圖片並儲存。",
            inputSchema={
                "type": "object",
                "properties": {
                    "prompt": {
                        "type": "string",
                        "description": "圖片描述（英文效果較佳）"
                    },
                    "aspect_ratio": {
                        "type": "string",
                        "description": "圖片比例",
                        "enum": ["1:1", "3:4", "4:3", "9:16", "16:9"],
                        "default": "1:1"
                    },
                    "filename": {
                        "type": "string",
                        "description": "檔案名稱（不含副檔名），預設使用時間戳記"
                    }
                },
                "required": ["prompt"]
            }
        ),
        Tool(
            name="list_images",
            description="列出已生成的圖片",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict):
    """執行工具"""
    
    if name == "generate_image":
        prompt = arguments.get("prompt", "")
        aspect_ratio = arguments.get("aspect_ratio", "1:1")
        filename = arguments.get("filename", "")
        
        if not prompt:
            return [TextContent(type="text", text="❌ 請提供圖片描述")]
        
        try:
            # 呼叫 Imagen API
            response = client.models.generate_images(
                model="imagen-4.0-generate-001",
                prompt=prompt,
                config=types.GenerateImagesConfig(
                    number_of_images=1,
                    aspect_ratio=aspect_ratio,
                )
            )
            
            if not response.generated_images:
                return [TextContent(type="text", text="❌ 圖片生成失敗，請嘗試其他描述")]
            
            # 產生檔名
            if not filename:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"image_{timestamp}"
            
            # 儲存圖片
            filepath = IMAGES_DIR / f"{filename}.png"
            image = response.generated_images[0].image
            image.save(str(filepath))
            
            result = f"""✅ 圖片生成成功！

📁 儲存位置：{filepath}
📐 比例：{aspect_ratio}

📝 描述：{prompt}
"""
            return [TextContent(type="text", text=result)]
            
        except Exception as e:
            return [TextContent(type="text", text=f"❌ 生成失敗：{str(e)}")]
    
    elif name == "list_images":
        try:
            images = list(IMAGES_DIR.glob("*.png"))
            if not images:
                return [TextContent(type="text", text="📂 尚無圖片")]
            
            result = f"📂 圖片列表（{IMAGES_DIR}）：\n\n"
            for img in sorted(images, key=lambda x: x.stat().st_mtime, reverse=True):
                mtime = datetime.fromtimestamp(img.stat().st_mtime).strftime("%Y-%m-%d %H:%M")
                size_kb = img.stat().st_size / 1024
                result += f"• {img.name} ({size_kb:.1f} KB) - {mtime}\n"
            
            return [TextContent(type="text", text=result)]
            
        except Exception as e:
            return [TextContent(type="text", text=f"❌ 錯誤：{str(e)}")]
    
    return [TextContent(type="text", text=f"❌ 未知工具：{name}")]


async def main():
    """啟動 MCP Server"""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
