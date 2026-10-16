#!/usr/bin/env python3
"""Generate social-preview.png (1200x630) for the MOFA docs site.

Reproduces the site's own hero faithfully: the project's actual logo asset
(logo_Mofa_NoBackground.png — the teal office-chair-with-apple mark) on a
light background, with the real tagline from the site's meta description and
the real domain. No machine-specific paths; fonts resolve via
MOFA_FONT_DIR -> ./fonts -> ~/.fonts -> system font dirs.
"""
import os
from PIL import Image, ImageDraw, ImageFont
Image.MAX_IMAGE_PIXELS = None

W, H = 1200, 630
HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
LOGO = os.path.join(REPO_ROOT, "docs", "public", "images", "logo_Mofa_NoBackground.png")

# MOFA brand palette (from the logo asset + site)
TEAL = (3, 127, 140)        # #037F8C — the logo's teal squares
TEXT_DARK = (15, 23, 42)    # slate-900
TEXT_MUTED = (100, 116, 139)  # slate-500
DOMAIN_GREY = (148, 163, 184)  # slate-400


def find_font(name, size):
    env_dir = os.environ.get("MOFA_FONT_DIR")
    candidates = []
    if env_dir:
        candidates.append(os.path.join(env_dir, name))
    candidates += [
        os.path.join("fonts", name),
        os.path.join(os.path.expanduser("~"), ".fonts", name),
        os.path.join("/usr/share/fonts/truetype/dejavu", name),
        os.path.join("/usr/share/fonts/truetype/liberation", name),
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ]
    for c in candidates:
        if os.path.exists(c):
            try:
                return ImageFont.truetype(c, size)
            except Exception:
                pass
    return ImageFont.load_default()


def main():
    img = Image.new("RGB", (W, H), (255, 255, 255))
    draw = ImageDraw.Draw(img, "RGBA")

    # soft top accent band in the site's teal
    draw.rectangle([0, 0, W, 8], fill=TEAL)

    # the project's actual logo asset, centered upper area
    logo = Image.open(LOGO).convert("RGBA")
    logo_w = 300
    logo_h = int(logo.size[1] * logo_w / logo.size[0])
    logo = logo.resize((logo_w, logo_h), Image.LANCZOS)
    img.paste(logo, (int((W - logo_w) / 2), 60), logo)

    # wordmark
    f_word = find_font("DejaVuSans-Bold.ttf", 64)
    word = "MOFA"
    ww = draw.textlength(word, font=f_word)
    draw.text(((W - ww) / 2, 400), word, font=f_word, fill=TEXT_DARK)

    # tagline from the site's meta description
    f_tag = find_font("DejaVuSans.ttf", 30)
    tag = "Empowering Apple Devices with Microsoft Solutions"
    tw = draw.textlength(tag, font=f_tag)
    draw.text(((W - tw) / 2, 490), tag, font=f_tag, fill=TEXT_MUTED)

    # domain in muted grey (plain text, not a button)
    f_dom = find_font("DejaVuSans.ttf", 24)
    dom = "mofa.cocolabs.dev"
    dw = draw.textlength(dom, font=f_dom)
    draw.text(((W - dw) / 2, 548), dom, font=f_dom, fill=DOMAIN_GREY)

    out = os.path.join(REPO_ROOT, "docs", "public", "social-preview.png")
    img.save(out, optimize=True)
    print("wrote", out, img.size)


if __name__ == "__main__":
    main()
