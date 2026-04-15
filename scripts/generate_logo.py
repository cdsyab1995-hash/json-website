#!/usr/bin/env python3
"""Generate professional logo, favicon and OG image for aijsons.com"""
import os, math
from PIL import Image, ImageDraw

OUTPUT_DIR = r"d:\网站开发-json\images"
ROOT_DIR = r"d:\网站开发-json"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Color palette
BG_DARK   = (13, 24, 41)
BG_CARD   = (30, 45, 74)
GREEN     = (34, 197, 94)
GREEN_LT  = (74, 222, 128)
GREEN_DK  = (22, 163, 74)
WHITE     = (255, 255, 255)
GRAY      = (148, 163, 184)

def lerp(a, b, t):
    return int(a + (b - a) * t)

def lerp_color(c1, c2, t):
    return (lerp(c1[0],c2[0],t), lerp(c1[1],c2[1],t), lerp(c1[2],c2[2],t))

def draw_rounded_rect_filled(draw, x0, y0, x1, y1, r, fill):
    draw.rectangle([x0+r, y0, x1-r, y1], fill=fill)
    draw.rectangle([x0, y0+r, x1, y1-r], fill=fill)
    draw.ellipse([x0, y0, x0+2*r, y0+2*r], fill=fill)
    draw.ellipse([x1-2*r, y0, x1, y0+2*r], fill=fill)
    draw.ellipse([x0, y1-2*r, x0+2*r, y1], fill=fill)
    draw.ellipse([x1-2*r, y1-2*r, x1, y1], fill=fill)

def gradient_circle(img, cx, cy, radius, color, alpha_start=200, alpha_end=0):
    """Draw a radial glow"""
    draw = ImageDraw.Draw(img)
    for r in range(radius, 0, -1):
        t = 1 - r / radius
        a = int(alpha_start * (1 - t) + alpha_end * t)
        if a <= 0: continue
        c = color + (a,)
        draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=c)

def draw_thick_line(draw, pts, width, color):
    """Draw a thick polyline"""
    for i in range(len(pts)-1):
        x0,y0 = pts[i]
        x1,y1 = pts[i+1]
        draw.line([(x0,y0),(x1,y1)], fill=color, width=width)
        draw.ellipse([x0-width//2, y0-width//2, x0+width//2, y0+width//2], fill=color)
    x1,y1 = pts[-1]
    draw.ellipse([x1-width//2, y1-width//2, x1+width//2, y1+width//2], fill=color)

def brace_points_left(cx, cy, h, arm, notch, steps=32):
    """Generate left brace { curve points"""
    top_y = cy - h//2
    bot_y = cy + h//2
    inner_x = cx - arm
    outer_x = cx - arm - notch

    pts_top = []
    for i in range(steps+1):
        t = i / steps
        angle = t * math.pi / 2
        x = inner_x - int(notch * math.sin(angle))
        y = top_y + int(arm * (1 - math.cos(angle)))
        pts_top.append((x, y))

    pts_top_v = [(inner_x, top_y + arm + i) for i in range(0, cy - arm - top_y - arm + 1, 2)]
    
    pts_mid_top = []
    for i in range(steps+1):
        t = i / steps
        angle = math.pi/2 + t * math.pi/2
        x = inner_x - int(notch * (1 - math.cos(t * math.pi)))
        y = (cy - arm) + int(arm * 2 * t)
        pts_mid_top.append((x, y))
    
    pts_bot_v = [(inner_x, cy + arm + i) for i in range(0, bot_y - arm - cy - arm + 1, 2)]
    
    pts_bot = []
    for i in range(steps+1):
        t = i / steps
        angle = t * math.pi / 2
        x = inner_x - int(notch * math.cos(angle))
        y = bot_y - arm + int(arm * math.sin(angle))
        pts_bot.append((x, y))
    
    return pts_top + pts_top_v + pts_mid_top + pts_bot_v + pts_bot

def create_logo(size=512):
    s = size
    scale = s / 512.0
    
    img = Image.new('RGBA', (s, s), (0,0,0,0))
    
    # -- Background with rounded corners --
    bg = Image.new('RGBA', (s, s), BG_DARK + (255,))
    # Add subtle gradient overlay (top-right lighter)
    grad = Image.new('RGBA', (s, s), (0,0,0,0))
    gpix = grad.load()
    for y in range(s):
        for x in range(s):
            t = (x*0.3 + (s-y)*0.7) / (s * 1.0)
            t = min(max(t, 0), 1)
            r,g,b = lerp_color(BG_DARK, BG_CARD, t * 0.6)
            gpix[x,y] = (r,g,b,255)
    bg = Image.alpha_composite(bg, grad)
    
    # Rounded rect mask
    mask = Image.new('L', (s, s), 0)
    md = ImageDraw.Draw(mask)
    r = int(88 * scale)
    draw_rounded_rect_filled(md, 0, 0, s, s, r, 255)
    img.paste(bg, mask=mask)
    
    draw = ImageDraw.Draw(img)
    
    cx = s // 2
    cy = s // 2
    lw = max(3, int(22 * scale))
    
    # Brace geometry
    brace_h = int(256 * scale)
    arm = int(52 * scale)
    notch = int(28 * scale)
    
    top_y = cy - brace_h // 2
    bot_y = cy + brace_h // 2
    
    # === LEFT BRACE { ===
    lx = int(136 * scale)  # inner x of left brace
    
    # Draw using thick arcs/lines
    # Top horizontal cap
    cap_w = int(44 * scale)
    draw.ellipse([lx, top_y-lw//2, lx+cap_w, top_y+lw//2+lw], fill=GREEN_LT)
    draw.rectangle([lx+lw//2, top_y-lw//2, lx+cap_w-lw//2, top_y+lw//2], fill=GREEN_LT)
    
    # Top vertical segment
    draw.rectangle([lx+lw//2, top_y+lw//2, lx+lw//2+lw, cy-arm], fill=GREEN)
    
    # Top curve (top to center-left)
    steps = 24
    pts = []
    for i in range(steps+1):
        t = i/steps
        angle = (math.pi/2) * t
        px = int(lx + lw//2 - notch*math.sin(angle))
        py = int(cy - arm + arm * (math.cos(angle) - 1) * -1 - arm * (1-math.cos(angle)))
        # Simplified: arc from (lx+lw, cy-arm) curving left to (lx+lw-notch, cy)
        px = int((lx+lw) - notch * math.sin(angle))
        py = int((cy - arm) + arm * (1 - math.cos(angle)))
        pts.append((px, py))
    draw_thick_line(draw, pts, lw, GREEN)
    
    # Center dot
    dot_r = int(18 * scale)
    draw.ellipse([lx+lw-notch-dot_r, cy-dot_r, lx+lw-notch+dot_r, cy+dot_r], fill=GREEN_LT)
    
    # Bottom curve (center-left to bottom)
    pts2 = []
    for i in range(steps+1):
        t = i/steps
        angle = (math.pi/2) * t
        px = int((lx+lw) - notch * math.cos(angle))
        py = int(cy + arm * math.sin(angle))
        pts2.append((px, py))
    draw_thick_line(draw, pts2, lw, GREEN)
    
    # Bottom vertical segment
    draw.rectangle([lx+lw//2, cy+arm, lx+lw//2+lw, bot_y-lw//2], fill=GREEN)
    
    # Bottom horizontal cap
    draw.ellipse([lx, bot_y-lw//2-lw, lx+cap_w, bot_y+lw//2], fill=GREEN_LT)
    draw.rectangle([lx+lw//2, bot_y-lw//2, lx+cap_w-lw//2, bot_y+lw//2], fill=GREEN_LT)
    
    # === RIGHT BRACE } (mirror of left) ===
    rx = s - int(136 * scale)
    
    # Top cap
    draw.ellipse([rx-cap_w, top_y-lw//2, rx, top_y+lw//2+lw], fill=GREEN_LT)
    draw.rectangle([rx-cap_w+lw//2, top_y-lw//2, rx-lw//2, top_y+lw//2], fill=GREEN_LT)
    
    # Top vertical
    draw.rectangle([rx-lw//2-lw, top_y+lw//2, rx-lw//2, cy-arm], fill=GREEN)
    
    # Top curve
    pts3 = []
    for i in range(steps+1):
        t = i/steps
        angle = (math.pi/2) * t
        px = int((rx-lw) + notch * math.sin(angle))
        py = int((cy - arm) + arm * (1 - math.cos(angle)))
        pts3.append((px, py))
    draw_thick_line(draw, pts3, lw, GREEN)
    
    # Center dot
    draw.ellipse([rx-lw+notch-dot_r, cy-dot_r, rx-lw+notch+dot_r, cy+dot_r], fill=GREEN_LT)
    
    # Bottom curve
    pts4 = []
    for i in range(steps+1):
        t = i/steps
        angle = (math.pi/2) * t
        px = int((rx-lw) + notch * math.cos(angle))
        py = int(cy + arm * math.sin(angle))
        pts4.append((px, py))
    draw_thick_line(draw, pts4, lw, GREEN)
    
    # Bottom vertical
    draw.rectangle([rx-lw//2-lw, cy+arm, rx-lw//2, bot_y-lw//2], fill=GREEN)
    
    # Bottom cap
    draw.ellipse([rx-cap_w, bot_y-lw//2-lw, rx, bot_y+lw//2], fill=GREEN_LT)
    draw.rectangle([rx-cap_w+lw//2, bot_y-lw//2, rx-lw//2, bot_y+lw//2], fill=GREEN_LT)
    
    # === Letter "J" in center ===
    jw = int(32 * scale)
    jh = int(170 * scale)
    jx = cx - jw // 2
    j_top = cy - jh // 2
    j_bot = cy + jh // 2
    jr = int(44 * scale)
    j_serif = int(36 * scale)
    
    # J vertical
    draw.rectangle([jx, j_top, jx+jw, j_bot-jr//2], fill=GREEN_LT)
    
    # J serif top
    draw.ellipse([jx-j_serif, j_top-jw//2, jx+jw+j_serif, j_top+jw+jw//2], fill=GREEN_LT)
    
    # J bottom curve
    curve_cx = jx - jr//2
    for thickness in range(jw, 0, -1):
        t = 1 - thickness / jw
        col = lerp_color(GREEN_LT, GREEN, t)
        draw.arc([curve_cx, j_bot-jr*2, curve_cx+jr*2, j_bot], 
                  start=180, end=360, fill=col, width=thickness)
    
    # Erase inner part of J curve
    inner_bg = lerp_color(BG_DARK, BG_CARD, 0.3)
    draw.arc([curve_cx+jw, j_bot-jr*2+jw, curve_cx+jr*2-jw, j_bot-jw], 
              start=180, end=360, fill=inner_bg, width=jw)
    
    # Decorative bottom lines
    dl_y1 = int(415 * scale)
    dl_y2 = int(430 * scale)
    dl_alpha = int(60)
    line_col = GREEN + (dl_alpha,)
    limg = Image.new('RGBA', (s, s), (0,0,0,0))
    ld = ImageDraw.Draw(limg)
    ld.rectangle([int(168*scale), dl_y1, int(220*scale), dl_y1+4], fill=GREEN+(50,))
    ld.rectangle([int(230*scale), dl_y1, int(264*scale), dl_y1+4], fill=GREEN+(50,))
    ld.rectangle([int(274*scale), dl_y1, int(344*scale), dl_y1+4], fill=GREEN+(50,))
    ld.rectangle([int(188*scale), dl_y2, int(240*scale), dl_y2+4], fill=GREEN+(35,))
    ld.rectangle([int(250*scale), dl_y2, int(322*scale), dl_y2+4], fill=GREEN+(35,))
    img = Image.alpha_composite(img, limg)
    
    return img


# === Generate all sizes ===
print("Generating logo-512.png...")
logo512 = create_logo(512)
logo512.save(os.path.join(OUTPUT_DIR, "logo-512.png"))

print("Generating logo-192.png...")
logo192 = create_logo(192)
logo192.save(os.path.join(OUTPUT_DIR, "logo-192.png"))

print("Generating apple-touch-icon.png (180x180)...")
logo180 = create_logo(256).resize((180,180), Image.LANCZOS)
logo180.save(os.path.join(OUTPUT_DIR, "apple-touch-icon.png"))

print("Generating favicon-32x32.png...")
logo64 = create_logo(128)
logo32 = logo64.resize((32,32), Image.LANCZOS)
logo32.save(os.path.join(OUTPUT_DIR, "favicon-32x32.png"))

print("Generating favicon-16x16.png...")
logo16 = logo32.resize((16,16), Image.LANCZOS)
logo16.save(os.path.join(OUTPUT_DIR, "favicon-16x16.png"))

print("Generating favicon.ico...")
ico_16 = logo32.resize((16,16), Image.LANCZOS)
ico_32 = logo32
ico_48 = create_logo(96).resize((48,48), Image.LANCZOS)
def to_rgb(img):
    bg = Image.new('RGB', img.size, BG_DARK)
    if img.mode == 'RGBA':
        bg.paste(img, mask=img.split()[3])
    else:
        bg.paste(img)
    return bg

to_rgb(ico_16).save(
    os.path.join(OUTPUT_DIR, "favicon.ico"),
    format='ICO', sizes=[(16,16),(32,32),(48,48)],
    append_images=[to_rgb(ico_32), to_rgb(ico_48)]
)

# === Generate OG image (1200x630) ===
print("Generating og-image.png (1200x630)...")
OG_W, OG_H = 1200, 630

og = Image.new('RGBA', (OG_W, OG_H), BG_DARK + (255,))
og_draw = ImageDraw.Draw(og)

# Gradient background
for y in range(OG_H):
    t = y / OG_H
    r,g,b = lerp_color(BG_CARD, BG_DARK, t)
    og_draw.line([(0,y),(OG_W,y)], fill=(r,g,b,255))

# Left accent bar
og_draw.rectangle([0, 0, 6, OG_H], fill=GREEN+(200,))

# Logo icon on left
logo_og = create_logo(200)
og.paste(logo_og, (80, OG_H//2 - 100), logo_og.split()[3])

# Title text area (using rectangles as text placeholders, then fill with PIL if font available)
tx = 320
# Title block
og_draw.rectangle([tx, 180, tx+680, 220], fill=GREEN_LT+(220,))
og_draw.rectangle([tx, 180, tx+480, 270], fill=GREEN+(255,))

# Subtitle block
og_draw.rectangle([tx, 290, tx+580, 310], fill=WHITE+(160,))
og_draw.rectangle([tx, 322, tx+500, 342], fill=WHITE+(110,))
og_draw.rectangle([tx, 354, tx+420, 370], fill=WHITE+(80,))

# Feature badges
badge_colors = [(GREEN+(180,)), ((59,130,246,180)), ((168,85,247,180))]
bx = tx
for i, label_w in enumerate([140, 130, 145]):
    bc = badge_colors[i % len(badge_colors)]
    og_draw.rounded_rectangle([bx, 410, bx+label_w, 444], radius=8, fill=bc)
    bx += label_w + 14

# Try to use a font
try:
    from PIL import ImageFont
    # Try system fonts
    for font_path in [
        r"C:\Windows\Fonts\arialbd.ttf",
        r"C:\Windows\Fonts\calibrib.ttf",
        r"C:\Windows\Fonts\verdanab.ttf",
        r"C:\Windows\Fonts\segoeui.ttf",
    ]:
        if os.path.exists(font_path):
            font_title = ImageFont.truetype(font_path, 52)
            font_sub = ImageFont.truetype(font_path, 22)
            font_small = ImageFont.truetype(font_path, 18)
            
            # Redraw with actual text
            og_draw.rectangle([tx-4, 170, tx+700, 290], fill=BG_DARK+(220,))  # clear area
            # Title
            og_draw.text((tx, 178), "AI JSON Tools", fill=WHITE+(255,), font=font_title)
            og_draw.text((tx, 244), "aijsons.com", fill=GREEN+(230,), font=font_sub)
            # Subtitle
            og_draw.text((tx, 294), "Free JSON Formatter, Validator & Converter", fill=GRAY+(220,), font=font_sub)
            og_draw.text((tx, 326), "for US & Canada Developers", fill=GRAY+(180,), font=font_sub)
            # Badges
            bx2 = tx
            for badge_text, badge_col in [("Format & Validate", GREEN+(200,)), ("JSON to CSV", (59,130,246,200)), ("JSONPath Query", (168,85,247,200))]:
                bg2 = Image.new('RGBA', (OG_W, OG_H), (0,0,0,0))
                bd = ImageDraw.Draw(bg2)
                tw = font_small.getlength(badge_text) if hasattr(font_small, 'getlength') else 120
                bd.rounded_rectangle([bx2, 410, bx2+int(tw)+24, 444], radius=8, fill=badge_col)
                bd.text((bx2+12, 416), badge_text, fill=WHITE+(230,), font=font_small)
                og = Image.alpha_composite(og, bg2)
                bx2 += int(tw) + 38
            break
except Exception as e:
    print(f"Font not found, using shapes: {e}")

og_rgb = og.convert('RGB')
og_rgb.save(os.path.join(ROOT_DIR, "og-image.png"), quality=95)

# Also save to images dir
og_rgb.save(os.path.join(OUTPUT_DIR, "og-image.png"), quality=95)

print("\nAll files generated:")
for f in ["images/logo-512.png","images/logo-192.png","images/apple-touch-icon.png",
          "images/favicon-32x32.png","images/favicon-16x16.png","images/favicon.ico","og-image.png"]:
    p = os.path.join(ROOT_DIR, f)
    if os.path.exists(p):
        print(f"  OK: {f} ({os.path.getsize(p)//1024}KB)")
