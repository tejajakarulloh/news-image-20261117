import sys
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
img = Image.new("RGB", (W, H), color="#0F172A") # Deep Slate Navy
draw = ImageDraw.Draw(img)

# Fonts
font_sans_bold = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
font_sans_reg = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
font_serif_bold = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"

f_masthead = ImageFont.truetype(font_serif_bold, 54)
f_dateline = ImageFont.truetype(font_sans_bold, 18)
f_subbanner = ImageFont.truetype(font_sans_reg, 15)

f_tag = ImageFont.truetype(font_sans_bold, 13)
f_title = ImageFont.truetype(font_sans_bold, 22)
f_body = ImageFont.truetype(font_sans_reg, 15)
f_stat_num = ImageFont.truetype(font_sans_bold, 28)
f_stat_lbl = ImageFont.truetype(font_sans_reg, 12)
f_footer = ImageFont.truetype(font_sans_bold, 14)

# Top Bar
draw.rectangle([0, 0, W, 8], fill="#38BDF8") # Cyan top stripe

# Masthead Box
draw.text((W//2, 50), "THE WORLD CHRONICLE", fill="#F8FAFC", font=f_masthead, anchor="mm")
draw.line([(60, 85), (W - 60, 85)], fill="#334155", width=2)
draw.text((W//2, 105), "GLOBAL NEWS DIGEST  •  TUESDAY, 17 NOVEMBER 2026  •  FINAL GLOBAL EDITION", fill="#38BDF8", font=f_dateline, anchor="mm")
draw.line([(60, 125), (W - 60, 125)], fill="#334155", width=2)

# Grid Layout: 2x2 cards
# Margins
left = 50
right = W - 50
gap = 30
card_w = (right - left - gap) // 2
card_h = 370
y_top = 145
y_bot = y_top + card_h + gap

cards = [
    {
        "x": left, "y": y_top,
        "tag": "DIPLOMACY & GLOBAL SECURITY", "tag_bg": "#1E3A8A", "tag_fg": "#93C5FD",
        "title": "G20 Accord Finalizes Global Peace & Security Corridor",
        "stat_val": "19 NATIONS", "stat_lbl": "Ratify Joint Accord",
        "bullets": [
            "• Multilateral summit reaches consensus on permanent de-escalation framework.",
            "• UN-backed humanitarian supply corridors guaranteed across 4 critical regions.",
            "• International reconstruction & stabilization fund approved with initial $45B pledge."
        ]
    },
    {
        "x": left + card_w + gap, "y": y_top,
        "tag": "TECHNOLOGY & ARTIFICIAL INTELLIGENCE", "tag_bg": "#065F46", "tag_fg": "#6EE7B7",
        "title": "International Frontier AI Safety Treaty Enters Into Force",
        "stat_val": "45 STATES", "stat_lbl": "Enforce Shared Safety",
        "bullets": [
            "• First binding multinational treaty standardizing frontier AI risk assessments.",
            "• Global open registry established for frontier compute training clusters (>10^26 FLOPs).",
            "• Universal mandate passed guaranteeing open scientific access for climate and health AI."
        ]
    },
    {
        "x": left, "y": y_bot,
        "tag": "ENERGY & GLOBAL ECONOMY", "tag_bg": "#831843", "tag_fg": "#F472B6",
        "title": "Clean Energy Surpasses 40% of Global Electricity Generation",
        "stat_val": "40.4%", "stat_lbl": "Global Renewable Share",
        "bullets": [
            "• Global renewable generation reaches historic high driven by offshore wind & utility solar.",
            "• Inflation across OECD economies stabilizes to 2.1%, easing global monetary pressures.",
            "• Landmark cross-continental clean power interconnector begins active commercial transmission."
        ]
    },
    {
        "x": left + card_w + gap, "y": y_bot,
        "tag": "SCIENCE & DEEP SPACE EXPLORATION", "tag_bg": "#581C87", "tag_fg": "#D8B4FE",
        "title": "Lunar Far-Side Scientific Observatory Transmits First Data",
        "stat_val": "30 DISHES", "stat_lbl": "Deep-Space Array Live",
        "bullets": [
            "• International lunar science array captures unprecedented radio quiet cosmic signals.",
            "• High-resolution mapping of the early universe cosmic microwave background initiates.",
            "• Automated solar storm warning telemetry operational for orbital communications."
        ]
    }
]

for c in cards:
    cx, cy = c["x"], c["y"]
    # Card Background
    draw.rounded_rectangle([cx, cy, cx + card_w, cy + card_h], radius=12, fill="#1E293B", outline="#334155", width=2)
    
    # Tag
    tag_w = draw.textlength(c["tag"], font=f_tag) + 20
    draw.rounded_rectangle([cx + 20, cy + 20, cx + 20 + tag_w, cy + 45], radius=6, fill=c["tag_bg"])
    draw.text((cx + 30, cy + 32), c["tag"], fill=c["tag_fg"], font=f_tag, anchor="lm")
    
    # Title (wrap if needed)
    words = c["title"].split()
    line1, line2 = "", ""
    for w in words:
        test = (line1 + " " + w).strip()
        if draw.textlength(test, font=f_title) < card_w - 40:
            line1 = test
        else:
            line2 = (line2 + " " + w).strip()
            
    draw.text((cx + 20, cy + 70), line1, fill="#F8FAFC", font=f_title)
    if line2:
        draw.text((cx + 20, cy + 98), line2, fill="#F8FAFC", font=f_title)
    
    # Stat box
    stat_box_y = cy + 135
    draw.rounded_rectangle([cx + 20, stat_box_y, cx + card_w - 20, stat_box_y + 55], radius=8, fill="#0F172A", outline="#475569", width=1)
    draw.text((cx + 35, stat_box_y + 27), c["stat_val"], fill="#38BDF8", font=f_stat_num, anchor="lm")
    draw.text((cx + card_w - 35, stat_box_y + 27), c["stat_lbl"], fill="#94A3B8", font=f_stat_lbl, anchor="rm")
    
    # Bullets
    by = stat_box_y + 70
    for bullet in c["bullets"]:
        # word wrap bullet
        b_words = bullet.split()
        b_l1, b_l2 = "", ""
        for bw in b_words:
            t = (b_l1 + " " + bw).strip()
            if draw.textlength(t, font=f_body) < card_w - 40:
                b_l1 = t
            else:
                b_l2 = (b_l2 + " " + bw).strip()
        draw.text((cx + 20, by), b_l1, fill="#CBD5E1", font=f_body)
        by += 22
        if b_l2:
            draw.text((cx + 32, by), b_l2, fill="#CBD5E1", font=f_body)
            by += 22
        by += 6

# Footer Bar
footer_y = H - 65
draw.rectangle([0, footer_y, W, H], fill="#020617")
draw.line([(0, footer_y), (W, footer_y)], fill="#334155", width=2)
draw.text((W//2, footer_y + 32), "GLOBAL COVERAGE VERIFIED • TUESDAY, 17 NOVEMBER 2026 • PUBLISHED FOR MAKE.FUN WORLD NEWS COMPETITION", fill="#94A3B8", font=f_footer, anchor="mm")

img.save("/home/ubuntu/makefun-work/repos/news-image-17/entry.png", "PNG", optimize=True)
print("Saved entry.png successfully! Size:", os.path.getsize("/home/ubuntu/makefun-work/repos/news-image-17/entry.png"), "bytes")
