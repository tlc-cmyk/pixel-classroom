#!/usr/bin/env python3
"""Rebuild school-uniform student sprites into assets/atlas.{png,json}.

Keeps existing Pixel Office furniture / desk_unit tiles intact.
Appends male (student0) + female (student1) uniform frames in a new strip:
  - male: short black hair, white shirt, school crest, charcoal trousers, belt
  - female: black ponytail, white shirt, plaid tie + navy/green/yellow skirt

Run from repo root:
  python3 tools/build_atlas.py
"""
from __future__ import annotations

import json
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
ATLAS_PNG = ROOT / "assets" / "atlas.png"
ATLAS_JSON = ROOT / "assets" / "atlas.json"

OUTLINE = (26, 28, 44, 255)
SKIN = (255, 205, 117, 255)
SKIN_SH = (239, 125, 87, 255)
HAIR = (30, 32, 48, 255)
HAIR_HI = (60, 64, 90, 255)
WHITE = (248, 248, 252, 255)
WHITE_SH = (180, 198, 214, 255)
CREST_Y = (240, 200, 60, 255)
CREST_G = (56, 160, 90, 255)
CREST_B = (40, 70, 120, 255)
TROUSER = (45, 48, 58, 255)
TROUSER_SH = (28, 30, 38, 255)
BELT = (20, 20, 28, 255)
BUCKLE = (200, 200, 210, 255)
SHOE = (50, 55, 70, 255)
PLAID_N = (28, 48, 78, 255)
PLAID_G = (36, 90, 70, 255)
PLAID_Y = (200, 180, 70, 255)
TIE = (32, 70, 60, 255)
MOUTH = (177, 62, 83, 255)
EYE = (26, 28, 44, 255)
TRANSP = (0, 0, 0, 0)


def blank(w: int = 40, h: int = 64) -> Image.Image:
    return Image.new("RGBA", (w, h), TRANSP)


def px(im: Image.Image, x: int, y: int, c) -> None:
    if 0 <= x < im.width and 0 <= y < im.height:
        im.putpixel((x, y), c)


def fill_rect(im: Image.Image, x0: int, y0: int, x1: int, y1: int, c) -> None:
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            px(im, x, y, c)


def draw_outline(src: Image.Image) -> Image.Image:
    w, h = src.size
    out = Image.new("RGBA", (w, h), TRANSP)
    sp = src.load()
    for y in range(h):
        for x in range(w):
            if sp[x, y][3] < 128:
                continue
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < w and 0 <= ny < h and sp[nx, ny][3] < 128:
                    out.putpixel((nx, ny), OUTLINE)
    out.alpha_composite(src)
    return out


def make_male(leg_off: int = 0, sit: bool = False) -> Image.Image:
    im = blank(40, 64)
    cx = 20
    fill_rect(im, cx - 7, 6, cx + 6, 18, SKIN)
    fill_rect(im, cx - 8, 4, cx + 7, 11, HAIR)
    fill_rect(im, cx - 8, 11, cx - 5, 16, HAIR)
    fill_rect(im, cx + 4, 11, cx + 7, 15, HAIR)
    px(im, cx + 5, 5, HAIR_HI)
    px(im, cx - 2, 5, HAIR_HI)
    px(im, cx - 3, 13, EYE)
    px(im, cx + 2, 13, EYE)
    px(im, cx - 1, 16, MOUTH)
    px(im, cx + 4, 15, SKIN_SH)
    fill_rect(im, cx - 2, 19, cx + 1, 21, SKIN)
    fill_rect(im, cx - 8, 21, cx + 7, 36, WHITE)
    fill_rect(im, cx + 5, 22, cx + 7, 35, WHITE_SH)
    fill_rect(im, cx - 11, 22, cx - 8, 30, WHITE)
    fill_rect(im, cx + 7, 22, cx + 10, 30, WHITE_SH)
    fill_rect(im, cx - 11, 30, cx - 9, 33, SKIN)
    fill_rect(im, cx + 8, 30, cx + 10, 33, SKIN)
    fill_rect(im, cx - 5, 26, cx - 2, 29, CREST_B)
    px(im, cx - 5, 26, CREST_Y)
    px(im, cx - 2, 26, CREST_G)
    px(im, cx - 5, 29, CREST_G)
    px(im, cx - 2, 29, CREST_Y)
    fill_rect(im, cx - 8, 36, cx + 7, 38, BELT)
    px(im, cx - 1, 37, BUCKLE)
    px(im, cx, 37, BUCKLE)
    if sit:
        fill_rect(im, cx - 7, 39, cx + 6, 52, TROUSER)
        fill_rect(im, cx + 4, 39, cx + 6, 52, TROUSER_SH)
        fill_rect(im, cx - 6, 52, cx - 2, 55, SHOE)
        fill_rect(im, cx + 1, 52, cx + 5, 55, SHOE)
    else:
        fill_rect(im, cx - 7, 39, cx - 2, 54, TROUSER)
        fill_rect(im, cx + 1, 39, cx + 6, 54, TROUSER)
        fill_rect(im, cx + 4, 39, cx + 6, 54, TROUSER_SH)
        if leg_off == 1:
            fill_rect(im, cx - 8, 48, cx - 3, 55, TROUSER)
            fill_rect(im, cx + 2, 48, cx + 6, 52, TROUSER)
            fill_rect(im, cx - 7, 55, cx - 3, 57, SHOE)
            fill_rect(im, cx + 2, 52, cx + 6, 54, SHOE)
        elif leg_off == -1:
            fill_rect(im, cx - 7, 48, cx - 2, 52, TROUSER)
            fill_rect(im, cx + 2, 48, cx + 7, 55, TROUSER)
            fill_rect(im, cx - 6, 52, cx - 2, 54, SHOE)
            fill_rect(im, cx + 2, 55, cx + 6, 57, SHOE)
        else:
            fill_rect(im, cx - 6, 54, cx - 2, 57, SHOE)
            fill_rect(im, cx + 1, 54, cx + 5, 57, SHOE)
    return draw_outline(im)


def plaid_fill(im: Image.Image, x0: int, y0: int, x1: int, y1: int) -> None:
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            vx = (x - x0) % 4
            hy = (y - y0) % 4
            if vx == 0:
                c = PLAID_Y if hy == 0 else PLAID_G
            elif hy == 0:
                c = PLAID_N
            elif vx == 2:
                c = PLAID_N
            else:
                c = PLAID_G if (vx + hy) % 2 == 0 else PLAID_N
            px(im, x, y, c)


def make_female(leg_off: int = 0, sit: bool = False) -> Image.Image:
    im = blank(48, 64)
    cx = 22
    fill_rect(im, cx - 7, 7, cx + 6, 19, SKIN)
    fill_rect(im, cx - 8, 4, cx + 7, 12, HAIR)
    fill_rect(im, cx - 8, 12, cx - 4, 18, HAIR)
    fill_rect(im, cx + 4, 12, cx + 7, 17, HAIR)
    fill_rect(im, cx + 7, 8, cx + 12, 28, HAIR)
    fill_rect(im, cx + 8, 28, cx + 11, 34, HAIR)
    px(im, cx + 9, 6, HAIR_HI)
    px(im, cx - 3, 5, HAIR_HI)
    px(im, cx - 7, 14, HAIR)
    px(im, cx + 6, 15, HAIR)
    px(im, cx - 3, 14, EYE)
    px(im, cx + 2, 14, EYE)
    px(im, cx - 1, 17, MOUTH)
    px(im, cx + 4, 16, SKIN_SH)
    fill_rect(im, cx - 2, 20, cx + 1, 22, SKIN)
    fill_rect(im, cx - 8, 22, cx + 7, 36, WHITE)
    fill_rect(im, cx + 5, 23, cx + 7, 35, WHITE_SH)
    fill_rect(im, cx - 11, 23, cx - 8, 30, WHITE)
    fill_rect(im, cx + 7, 23, cx + 10, 30, WHITE_SH)
    fill_rect(im, cx - 11, 30, cx - 9, 33, SKIN)
    fill_rect(im, cx + 8, 30, cx + 10, 33, SKIN)
    fill_rect(im, cx - 5, 27, cx - 2, 30, CREST_B)
    px(im, cx - 5, 27, CREST_Y)
    px(im, cx - 2, 27, CREST_G)
    px(im, cx - 5, 30, CREST_G)
    px(im, cx - 2, 30, CREST_Y)
    fill_rect(im, cx - 1, 22, cx + 1, 35, TIE)
    px(im, cx, 24, PLAID_Y)
    px(im, cx, 28, PLAID_Y)
    px(im, cx, 32, PLAID_Y)
    if sit:
        plaid_fill(im, cx - 9, 36, cx + 8, 50)
        fill_rect(im, cx - 5, 50, cx - 1, 54, SKIN)
        fill_rect(im, cx + 1, 50, cx + 5, 54, SKIN)
        fill_rect(im, cx - 5, 54, cx - 1, 56, SHOE)
        fill_rect(im, cx + 1, 54, cx + 5, 56, SHOE)
    else:
        plaid_fill(im, cx - 9, 36, cx + 8, 48)
        if leg_off == 1:
            fill_rect(im, cx - 6, 48, cx - 2, 55, SKIN)
            fill_rect(im, cx + 1, 48, cx + 5, 52, SKIN)
            fill_rect(im, cx - 6, 55, cx - 2, 57, SHOE)
            fill_rect(im, cx + 1, 52, cx + 5, 54, SHOE)
        elif leg_off == -1:
            fill_rect(im, cx - 6, 48, cx - 2, 52, SKIN)
            fill_rect(im, cx + 1, 48, cx + 5, 55, SKIN)
            fill_rect(im, cx - 6, 52, cx - 2, 54, SHOE)
            fill_rect(im, cx + 1, 55, cx + 5, 57, SHOE)
        else:
            fill_rect(im, cx - 5, 48, cx - 1, 55, SKIN)
            fill_rect(im, cx + 1, 48, cx + 5, 55, SKIN)
            fill_rect(im, cx - 5, 55, cx - 1, 57, SHOE)
            fill_rect(im, cx + 1, 55, cx + 5, 57, SHOE)
    return draw_outline(im)


def gen_set(maker, prefix: str, pad_w: int) -> dict:
    frames = {}

    def pad(im: Image.Image) -> Image.Image:
        if im.width == pad_w and im.height == 64:
            return im
        out = blank(pad_w, 64)
        out.paste(im, ((pad_w - im.width) // 2, 0), im)
        return out

    walk = [pad(maker(leg_off=o, sit=False)) for o in (0, 1, 0, -1)]
    sit = pad(maker(leg_off=0, sit=True))
    for d in range(4):
        for fi, fr in enumerate(walk):
            img = fr.transpose(Image.FLIP_LEFT_RIGHT) if d == 1 else fr
            frames[f"{prefix}_{d}_{fi}"] = img
    frames[f"{prefix}_sit"] = sit
    return frames


def main() -> None:
    male = gen_set(make_male, "student0", 40)
    female = gen_set(make_female, "student1", 48)

    atlas = Image.open(ATLAS_PNG).convert("RGBA")
    SPR = json.loads(ATLAS_JSON.read_text())

    # Drop previous uniform strip if re-run (keys already point into strip below original height)
    base_h = 530  # original HQ atlas height before uniform strip
    if atlas.height > base_h:
        atlas = atlas.crop((0, 0, atlas.width, base_h))

    aw, ah = atlas.size
    row_h = 68
    new_atlas = Image.new("RGBA", (max(aw, 1600), ah + row_h * 2 + 8), TRANSP)
    new_atlas.paste(atlas, (0, 0))

    def pack_row(frames_dict: dict, y0: int) -> None:
        x = 2
        for name in sorted(frames_dict.keys()):
            im = frames_dict[name]
            new_atlas.paste(im, (x, y0), im)
            SPR[name] = {"x": x, "y": y0, "w": im.width, "h": im.height}
            x += im.width + 2

    pack_row(male, ah + 2)
    pack_row(female, ah + 2 + row_h)

    new_atlas.save(ATLAS_PNG)
    ATLAS_JSON.write_text(json.dumps(SPR, indent=2) + "\n")
    print(f"Wrote {ATLAS_PNG.relative_to(ROOT)} ({new_atlas.size[0]}x{new_atlas.size[1]})")
    print(f"student0_sit={SPR['student0_sit']} student1_sit={SPR['student1_sit']}")


if __name__ == "__main__":
    main()
