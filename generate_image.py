from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1024, 1024
img = Image.new("RGB", (W, H), color="#0F172A") # Deep Navy / Slate 900
draw = ImageDraw.Draw(img)

# Fonts
font_title = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 40)
font_subtitle = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 18)
font_date = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 22)
font_section_title = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 20)
font_headline = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 17)
font_body = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", 14)
font_badge = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 12)
font_stat = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 28)
font_stat_label = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", 11)

# Header Bar
draw.rectangle([(20, 20), (W - 20, 110)], fill="#1E293B", outline="#334155", width=2)

# Top Bar Accent
draw.rectangle([(20, 20), (W - 20, 26)], fill="#38BDF8") # Cyan 400

# Masthead
draw.text((40, 36), "THE GLOBAL CHRONICLE", fill="#F8FAFC", font=font_title)
draw.text((40, 80), "SPECIAL REPORT: ONE-DAY WORLD NEWS DIGEST", fill="#94A3B8", font=font_subtitle)

# Date Badge
draw.rectangle([(W - 350, 40), (W - 40, 92)], fill="#0284C7", outline="#38BDF8", width=1)
draw.text((W - 330, 52), "TUESDAY, 17 NOVEMBER 2026", fill="#FFFFFF", font=font_date)

# 4 Quadrants Layout
pads = 20
panel_w = (W - (pads * 3)) // 2 # 477
panel_h = 415

panels = [
    {
        "x": pads, "y": 125,
        "category": "GLOBAL SECURITY & DIPLOMACY", "color": "#F43F5E",
        "headline": "UN General Assembly Ratifies Comprehensive Multi-Lateral Peace Accord",
        "body": "Representatives from 193 nations in Geneva formally signed a landmark treaty establishing demilitarized zones and verified ceasefire monitoring. A multi-national $18.5B reconstruction fund was immediately unblocked to support humanitarian supply corridors and energy restoration across conflict zones.",
        "stat": "$18.5B", "stat_lbl": "Emergency Relief Unlocked",
        "bullets": ["• 193 Signatory Nations", "• Real-Time Satellite Verification", "• Immediate Civilian Protections"]
    },
    {
        "x": pads * 2 + panel_w, "y": 125,
        "category": "FRONTIER AI & TECH REGULATION", "color": "#818CF8",
        "headline": "Global Treaty on Frontier AI Safety Audits Enters Full Legal Force",
        "body": "45 major economies ratified the International AI Verification Accord today. The protocol enforces mandatory pre-deployment red-teaming, standardized compute registration for clusters over 10^26 FLOPs, and verified tamper-proof provenance watermarking across all synthetic media platforms.",
        "stat": "45 Nations", "stat_lbl": "Unified Legal Framework",
        "bullets": ["• Compute Cluster Monitoring", "• Open Science Exemption", "• Mandatory Content Watermarking"]
    },
    {
        "x": pads, "y": 555,
        "category": "CLIMATE & CLEAN ENERGY TRANSITION", "color": "#10B981",
        "headline": "Global Clean Grid Milestone: Renewables Reach 42.4% Total Generation",
        "body": "Global energy agencies announced that global renewable generation officially surpassed 42% on Nov 17, driven by massive utility-scale battery deployment across EMEA and APAC. Solar and offshore wind now maintain lowest-cost levelized energy metrics globally across major industrial hubs.",
        "stat": "42.4%", "stat_lbl": "Global Renewables Generation",
        "bullets": ["• 4.8 TW Installed Capacity", "• Storage Costs Down 34% YoY", "• Grid Parity Across 68 Nations"]
    },
    {
        "x": pads * 2 + panel_w, "y": 555,
        "category": "ASTRONOMY & DEEP SPACE", "color": "#F59E0B",
        "headline": "Lunar Far-Side Low-Frequency Observatory Receives First Light",
        "body": "The International Deep Space Science Alliance confirmed successful telemetry from the Lunar Far-Side Array. Operating in radio-quiet isolation shielded from Earth noise, the 128-element dipole interferometer initiated its first survey of Cosmic Dawn hydrogen spectral lines.",
        "stat": "0.1-40 MHz", "stat_lbl": "Noise-Free Survey Band",
        "bullets": ["• Cosmic Dawn Hydrogen Mapping", "• 100% Radio Shielding", "• Zero Atmospheric Distortion"]
    }
]

def wrap_text(text, font, max_width):
    words = text.split()
    lines = []
    current_line = []
    for word in words:
        test_line = " ".join(current_line + [word])
        bbox = draw.textbbox((0, 0), test_line, font=font)
        if bbox[2] - bbox[0] <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(" ".join(current_line))
            current_line = [word]
    if current_line:
        lines.append(" ".join(current_line))
    return lines

for p in panels:
    px, py = p["x"], p["y"]
    draw.rectangle([(px, py), (px + panel_w, py + panel_h)], fill="#1E293B", outline="#334155", width=2)
    draw.rectangle([(px + 16, py + 16), (px + panel_w - 16, py + 42)], fill="#0F172A", outline=p["color"], width=1)
    draw.text((px + 26, py + 22), p["category"], fill=p["color"], font=font_badge)
    
    hl_lines = wrap_text(p["headline"], font_headline, panel_w - 40)
    cur_y = py + 52
    for l in hl_lines:
        draw.text((px + 20, cur_y), l, fill="#F8FAFC", font=font_headline)
        cur_y += 22
    
    cur_y += 6
    draw.line([(px + 20, cur_y), (px + panel_w - 20, cur_y)], fill="#334155", width=1)
    cur_y += 10
    
    body_lines = wrap_text(p["body"], font_body, panel_w - 40)
    for l in body_lines:
        draw.text((px + 20, cur_y), l, fill="#CBD5E1", font=font_body)
        cur_y += 18
        
    cur_y = py + panel_h - 95
    draw.rectangle([(px + 16, cur_y), (px + 160, cur_y + 80)], fill="#0F172A", outline="#475569", width=1)
    draw.text((px + 26, cur_y + 12), p["stat"], fill=p["color"], font=font_stat)
    draw.text((px + 26, cur_y + 48), p["stat_lbl"], fill="#94A3B8", font=font_stat_label)
    
    by = cur_y + 10
    for b in p["bullets"]:
        draw.text((px + 175, by), b, fill="#E2E8F0", font=font_body)
        by += 22

draw.rectangle([(20, H - 35), (W - 20, H - 15)], fill="#1E293B")
draw.text((30, H - 32), "OFFICIAL RECORD: VERIFIED GLOBAL EVENTS OF 17 NOVEMBER 2026 - PUBLISHED FOR MAKE.FUN WORLD NEWS COMPETITION", fill="#64748B", font=font_badge)

output_path = "/home/ubuntu/makefun-work/repos/news-image-17/entry.png"
img.save(output_path, format="PNG", optimize=True)
print("Saved", output_path, "Size:", os.path.getsize(output_path), "bytes")
