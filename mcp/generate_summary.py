#!/usr/bin/env python3
"""
Summary Slide Generator - Full content with key points
Based on English documentation
"""

import subprocess
from pathlib import Path
from datetime import datetime

result = subprocess.run(['zsh', '-c', 'source ~/.zshrc && echo $GOOGLE_API_KEY'], capture_output=True, text=True)
api_key = result.stdout.strip()

from google import genai
from google.genai import types

client = genai.Client(api_key=api_key)
IMAGES_DIR = Path.home() / "jarvis" / "images"
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

# Common style
STYLE = """Professional business presentation slide with clean modern design.
Dark blue (#1a365d) to teal (#0d9488) gradient background.
Flat-style icons and visual elements. High contrast, white text.
Corporate tech startup aesthetic. 16:9 aspect ratio layout.
Clear visual hierarchy with title, key points, and supporting graphics."""

slides = [
    # === Theme 1: 2026 Company Plan ===
    {
        "filename": "plan_01_vision",
        "prompt": f"""{STYLE}
Title slide for company annual plan.

Title: "JARVIS 2026"
Subtitle: "AGI Application Pioneer"

Key message displayed:
"Small but Mighty R&D Company
Aligned with World-Leading Technology"

Visual elements: AI robot icon, globe, rocket, circuit patterns.
Futuristic tech company vibe."""
    },
    {
        "filename": "plan_02_philosophy",
        "prompt": f"""{STYLE}
Core philosophy slide with 4 key principles.

Title: "Core Philosophy"

Four boxes/quadrants with icons and text:
1. "AI Governance" - Brain icon - Replace traditional management with AI
2. "Lean Team" - People icon - Small headcount, maximized capability  
3. "AI-Native Talent" - Human+Robot icon - Collaborate with AI
4. "Full AI Integration" - Gears icon - AI in every aspect

Clean 2x2 grid layout with icons above text."""
    },
    {
        "filename": "plan_03_financial",
        "prompt": f"""{STYLE}
Financial goals slide with key metrics.

Title: "2026 Financial Goals"

Key metrics prominently displayed:
• Revenue Target: "$220,000 USD"
• Growth: "2X vs 2025"
• Break-even: "2027 Q2"

Revenue sources listed:
• Siraya Service Fee
• Anti-Hijacking Commission 5-10%
• Product Maintenance Fee
• TOMO AI HR Project
• Sky-Net GC Project

Include upward chart, dollar icons, target icon."""
    },
    {
        "filename": "plan_04_team",
        "prompt": f"""{STYLE}
Team expansion slide with growth plan.

Title: "Team Expansion Plan"

Current vs Target: "8 → 15 People"

Quarterly breakdown:
• Q1: +3 (Tech Lead + Devs) → 11
• Q2: +2 (Developers) → 13
• Q3: +1 (Developer) → 14
• Q4: +1 (Developer) → 15

Key Hire highlight box:
"Tech Lead - Entrepreneurial Mindset
• Hands-on Expertise
• Leadership & Integration
• Forward Thinking"

People icons showing growth, org chart visual."""
    },
    {
        "filename": "plan_05_products",
        "prompt": f"""{STYLE}
Product goals slide with three main products.

Title: "2026 Product Goals"

Three product cards:

1. Shield icon - "Anti-Hijacking Product"
   • Continuous optimization
   • New features
   • Generate revenue

2. Dashboard icon - "Customer Portal"
   • Serve Siraya
   • Continuous development

3. Robot icon - "TOMO AI HR"
   • Q2: Localization
   • Q3: External sales

Clean card layout with icons and bullet points."""
    },
    {
        "filename": "plan_06_tech",
        "prompt": f"""{STYLE}
Technical goals slide with development roadmap.

Title: "Technical Goals"

Q1 Deliverables:
• Git Flow & Code Review
• CI/CD Automation
• Sprint Planning System

Q2 Deliverables:
• Vibe Coding Training (Cursor/Copilot)
• Prompt Engineering
• Automated Testing
• Quality Control

Goal statement:
"Build Professional, AI-Driven Development Team"

Include code icon, automation gear, testing checkmark icons."""
    },
    {
        "filename": "plan_07_timeline",
        "prompt": f"""{STYLE}
Annual timeline slide with quarterly milestones.

Title: "2026 Roadmap"

Horizontal timeline with 4 quarters:

Q1 - "Foundation"
• Tech Lead hired
• Dev process setup
• Vibe Coding start
• 1st Exchange

Q2 - "Capability"  
• Auto testing
• AI HR kickoff
• Team: 13
• Commission talk

Q3 - "Explosion"
• AI HR sales
• Sky-Net GC
• Team R&D
• 2nd Exchange

Q4 - "Harvest"
• Team: 15
• Year-end party
• 2027 planning

Arrow timeline with milestone markers."""
    },
    {
        "filename": "plan_08_international",
        "prompt": f"""{STYLE}
International goals slide.

Title: "Internationalization Goals"

3 Cross-Border Projects:
1. TOMO AI HR - Q2 Start → Q3 Sales
2. Sky-Net GC - 100+ Game Integration  
3. Team R&D - Vietnam Market Product

3 Cross-Border Exchanges:
• Q1: Kickoff Exchange
• Q3: Project Collaboration
• Q4: Year-end Celebration 🎉

Globe icon, handshake icon, airplane icon.
Connected world visualization."""
    },
    
    # === Theme 2: Group Overview ===
    {
        "filename": "group_01_structure",
        "prompt": f"""{STYLE}
Group structure overview slide.

Title: "Unicorn International Investment"
Subtitle: "Group Structure - 27+ Companies"

Organization chart showing:
[Holding Company] at top
↓
8 subsidiaries below:
• Siraya - Cloud/CDN/Security
• Jarvis - Software Development ★
• Katsumitec - iGaming R&D
• Tomo - AI Startup
• Sky-Net - IT Solutions
• Ariel - Game Publishing
• Yu Yang - FinTech
• Kaiyin - Point Cards

Jarvis highlighted with star or "You are here" marker.
Corporate hierarchy tree visual."""
    },
    {
        "filename": "group_02_siraya",
        "prompt": f"""{STYLE}
Siraya company profile slide.

Title: "Siraya Technologies"
Tagline: "Built for the Cloud, Secure with AI"

Service Categories:
• Compute - Cloud, VPS, AI Services
• Edge Delivery - CDN, Edge Compute
• Streaming - Live, Low Latency
• Cloud Security - DDoS, WAF, Bot Management
• Professional Services - DevOps, SOC

Locations: Singapore, Vietnam, Malaysia, Shenzhen

Partners: AWS, Azure, Google Cloud, Cloudflare...

Cloud icon, security shield, global network visual."""
    },
    {
        "filename": "group_03_jarvis",
        "prompt": f"""{STYLE}
Jarvis company profile slide.

Title: "Jarvis"
Subtitle: "Software Development Company"

Key Info:
• Founded: 2023
• Location: Hanoi, Vietnam
• Current: ~8 people
• Target: 15-20 people (2026)

Main Products:
1. Customer Portal System
   - Cloud services integration
   - CDN, monitoring, account management
   
2. Anti-Hijacking Product
   - Security solution for Siraya

Vietnam map icon, code brackets icon, growth arrow."""
    },
    {
        "filename": "group_04_tomo",
        "prompt": f"""{STYLE}
Tomo AI company profile slide.

Title: "Tomo - AI Solutions"
Vision: "Market-Leading AI Solutions Provider"

Product Portfolio:

AI HR (MVP)
• Auto sourcing, 7-dimension scoring
• 16x faster resume review
• 2.66x faster recruitment

AI SRE (PoC)
• Multi-agent framework
• Root cause analysis
• Reduce MTTR

AI Dealer (Prototype)
• Digital dealer for gaming
• Real-time customization

AI brain icon, automation icons, efficiency metrics."""
    },
    {
        "filename": "group_05_relationships",
        "prompt": f"""{STYLE}
Jarvis business relationships slide.

Title: "Jarvis Business Relationships"

Relationship diagram with Jarvis in center:

→ Siraya (Main Client)
  Customer Portal + Anti-Hijacking
  Service Fee: Salary + 10%

← Katsumitec (Investor)
  Covers losses
  Past: Telegram, ClickHouse, Payment

↔ Sky-Net (Current Partner)
  GC Project - 100+ games

↔ Tomo (Future Partner)
  AI HR Vietnam market

Connection arrows and flow diagram style."""
    },
    {
        "filename": "group_06_funding",
        "prompt": f"""{STYLE}
Funding structure slide.

Title: "Funding & Growth Path"

Current Structure:
Katsumitec (Investor)
    ↓ Investment + Loss Coverage
Jarvis (R&D)
    ↓ Development Services  
Siraya (Client)
    ↓ Service Fee (Salary + 10%)

Growth Timeline:
2023 Founded → 2026 Growth → 2027 Q2 Break-even

Target State:
• Independent R&D Company
• 15-person Team
• Multiple Revenue Streams
• Product Income Capability

Money flow arrows, timeline, growth chart."""
    },
]

def generate_images(prompt: str, filename: str, count: int = 4):
    """Generate multiple images for selection"""
    print(f"\n{'='*50}")
    print(f"Generating: {filename} ({count} variations)")
    print(f"{'='*50}")
    
    try:
        response = client.models.generate_images(
            model="imagen-4.0-ultra-generate-001",
            prompt=prompt,
            config=types.GenerateImagesConfig(
                number_of_images=count,
                aspect_ratio="16:9",
            )
        )
        
        if response.generated_images:
            saved = []
            for i, img in enumerate(response.generated_images):
                suffix = chr(ord('a') + i)
                filepath = IMAGES_DIR / f"{filename}_{suffix}.png"
                img.image.save(filepath)
                saved.append(filepath.name)
                print(f"  ✓ Saved: {filepath.name}")
            return saved
        else:
            print(f"  ✗ No images generated")
            return []
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return []

def main():
    print(f"""
╔══════════════════════════════════════════════════════════════╗
║     Summary Slide Generator - Full Content                   ║
║     Model: imagen-4.0-ultra-generate-001                     ║
║     Output: 4 variations per slide                           ║
╚══════════════════════════════════════════════════════════════╝

Output directory: {IMAGES_DIR}
Total slides: {len(slides)}
Total images: {len(slides) * 4}

Started at: {datetime.now().strftime('%H:%M:%S')}
""")
    
    results = {"success": 0, "failed": 0}
    
    for i, slide in enumerate(slides, 1):
        print(f"\n[{i}/{len(slides)}] ", end="")
        saved = generate_images(slide["prompt"], slide["filename"], count=4)
        if saved:
            results["success"] += len(saved)
        else:
            results["failed"] += 1
    
    print(f"""

╔══════════════════════════════════════════════════════════════╗
║     COMPLETE                                                 ║
║     Success: {results['success']} images                                      ║
║     Failed: {results['failed']} slides                                        ║
║     Finished at: {datetime.now().strftime('%H:%M:%S')}                               ║
╚══════════════════════════════════════════════════════════════╝
""")

if __name__ == "__main__":
    main()
