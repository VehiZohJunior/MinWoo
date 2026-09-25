"""Extract dominant colors from each reference image using Pillow median-cut quantization.
No external deps beyond Pillow (already installed). Run: python extract_colors.py
"""
import os
from PIL import Image

REF_DIR = os.path.dirname(os.path.abspath(__file__))
# Crop boxes (left, top, right, bottom) targeting fabric/torso regions,
# avoiding faces, skin, sky and background walls/foliage as much as possible.
IMAGES = {
    "indigo-1.webp": (40, 300, 440, 650),
    "indigo-2.png":  (20, 150, 280, 350),
    "indigo-3.png":  (20, 120, 280, 280),
    "indigo-4.png":  (0, 150, 303, 380),
    "mixed-5.png":   (0, 150, 303, 350),
    "kita-6.png":    (20, 150, 283, 400),
    "kita-7.png":    (0, 80, 303, 220),
    "kita-8.png":    (20, 120, 283, 320),
}
N_COLORS = 10
THUMB = 200  # downscale for speed; color distribution is stable at this size

def hex_of(rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)

def analyze(path, box=None):
    im = Image.open(path).convert("RGB")
    if box:
        im = im.crop(box)
    im.thumbnail((THUMB, THUMB))
    total_px = im.width * im.height
    q = im.quantize(colors=N_COLORS, method=Image.MEDIANCUT)
    palette = q.getpalette()[: N_COLORS * 3]
    counts = q.getcolors()  # list of (count, palette_index)
    counts.sort(reverse=True, key=lambda x: x[0])
    results = []
    for count, idx in counts:
        r, g, b = palette[idx * 3 : idx * 3 + 3]
        pct = 100 * count / total_px
        results.append((hex_of((r, g, b)), round(pct, 1)))
    return results

if __name__ == "__main__":
    for name, box in IMAGES.items():
        path = os.path.join(REF_DIR, name)
        if not os.path.exists(path):
            print(f"{name}: MISSING")
            continue
        print(f"\n=== {name} (crop {box}) ===")
        for hexcode, pct in analyze(path, box):
            bar = "#" * max(1, int(pct))
            print(f"  {hexcode}  {pct:5.1f}%  {bar}")
