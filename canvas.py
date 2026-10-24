#!/usr/bin/env python3
"""
Profile Canvas CLI: Design and render pixel typography onto GitHub contribution heatmaps.
Author: @envyakki
"""

import argparse
import sys
from datetime import datetime, timedelta
from fonts import FONTS, SHAPES

def render_text(text: str, gap: int = 1) -> list[str]:
    text = text.upper()
    lines = ["" for _ in range(7)]
    for idx, char in enumerate(text):
        matrix = FONTS.get(char)
        if not matrix:
            matrix = ["....." for _ in range(7)]
        for r in range(7):
            lines[r] += matrix[r]
            if idx < len(text) - 1:
                lines[r] += "." * gap
    return lines

def preview_ascii(matrix: list[str]):
    print("\n" + "="*50)
    print("  GITHUB CONTRIBUTION GRAPH PREVIEW (7x52)")
    print("="*50)
    day_labels = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    for r in range(7):
        row_visual = matrix[r].replace("#", "\033[92m■\033[0m").replace(".", "\033[90m⬝\033[0m")
        print(f" {day_labels[r]} | {row_visual}")
    print("="*50 + "\n")

def main():
    parser = argparse.ArgumentParser(
        description="Profile Canvas: GitHub Contribution Graph Pixel Typography Engine"
    )
    parser.add_argument("--text", type=str, default="AKKI", help="Text to render on graph")
    parser.add_argument("--preview", action="store_true", help="Display ASCII preview in terminal")
    parser.add_argument("--intensity", type=int, default=15, help="Number of commits per active pixel")

    args = parser.parse_args()

    lines = render_text(args.text)
    print(f"[+] Loaded typography for: '{args.text}' (Width: {len(lines[0])} columns)")
    preview_ascii(lines)
    
    active_count = sum(row.count("#") for row in lines)
    print(f"[+] Active pixels: {active_count}")
    print(f"[+] Target commit intensity: {args.intensity} commits/pixel")
    print(f"[+] Total commits generated: {active_count * args.intensity}")
    print("[✓] Ready to synchronize with GitHub profile heatmap.")

if __name__ == "__main__":
    main()
