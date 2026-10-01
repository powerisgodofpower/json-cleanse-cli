#!/usr/bin/env python3
"""
Tool Name: JSON Cleanse CLI
Description: 複雑に入り組んだJSONデータから余計な構造エラーを防ぎ、美しくパースするための超軽量スクリプト。
License: MIT (完全無料・クリーンなオープンソース)
"""

import sys
import json

def cleanse_json(raw_text):
    try:
        parsed = json.loads(raw_text)
        return json.dumps(parsed, ensure_ascii=False, indent=2)
    except Exception as e:
        return f"Error parsing JSON: {e}"

if __name__ == "__main__":
    print("--- JSON Cleanse CLI initialized ---")
    sample_data = '{"user": "global_developer", "status": "active", "target": "success"}'
    print("Original:", sample_data)
    print("Cleaned :", cleanse_json(sample_data))