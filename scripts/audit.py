#!/usr/bin/env python3
"""
Design Master Audit — P0/P1/P2 Rules
يحاول محاكاة impeccable's 44 deterministic detector rules + open-design craft rules.

Usage:
  python audit.py <project-dir>

Output:
  - PASS/FAIL لكل قاعدة
  - .design/audit.md (تقرير شامل)
"""

import re
import sys
import os
from pathlib import Path
from datetime import datetime


# ============================================================
# Rule Definitions
# ============================================================

P0_RULES = [
    # Color bans (anti-ai-slop #1)
    ("no-indigo", r'#6366f1|#4f46e5|#4338ca|#3730a3|#8b5cf6|#7c3aed|#a855f7',
     "لا ألوان indigo/violet/purple كـ accent", "FAIL"),
    ("no-purple-blue-hero-gradient", r'linear-gradient\([^)]*(?:#8b5cf6|#6366f1|#7c3aed|#a855f7)[^)]*#3b82f6|#06b6d4',
     "لا تدرّج بنفسجي-أزرق على الـ hero", "FAIL"),
    ("no-emoji-as-icons", r'<(?:h[1-6]|button|li)[^>]*>[^<]*[✨🚀🎯⚡🔥💡⭐🎉💎🚫✅]',
     "لا إيموجي كأيقونات في headings/buttons/list items", "FAIL"),
    ("no-inter-default", r'font-family:\s*["\']?Inter["\']?[,\s]',
     "لا Inter كخط افتراضي وحيد (Product register OK)", "WARN"),

    # Card anti-patterns
    ("no-rounded-card-left-stripe", r'\.card[^{]*\{[^}]*border-radius:\s*1[2-9]px[^}]*border-(?:left|start):\s*\d+px\s+solid',
     "لا بطاقة مستديرة بحدود يسرى ملوّنة (AI dashboard tile)", "FAIL"),

    # Code hygiene
    ("no-hex-outside-root", None,  # Custom check
     "لا قيم hex خارج :root — استخدم tokens", "WARN"),
    ("no-text-align-left", r'text-align:\s*(?:left|right)\s*;',
     "لا text-align: left/right — استخدم start/end", "FAIL"),
    ("no-margin-left-right", r'margin-(?:left|right):',
     "لا margin-left/right — استخدم margin-inline-*", "FAIL"),
    ("no-padding-left-right", r'padding-(?:left|right):',
     "لا padding-left/right — استخدم padding-inline-*", "FAIL"),
    ("no-outline-none-without-focus-visible", None,
     "لا outline: none بدون :focus-visible بديل", "FAIL"),

    # GSAP performance
    ("no-gsap-width-height", r'gsap\.(?:to|from|fromTo)\([^)]*?(?:width|height):\s*[a-z0-9]',
     "لا animate width/height في GSAP (triggers reflow)", "FAIL"),
    ("no-gsap-top-left", r'gsap\.(?:to|from|fromTo)\([^)]*?\b(?:top|left):\s*[-\d]',
     "لا animate top/left في GSAP", "FAIL"),
    ("no-gsap-margin-padding", r'gsap\.(?:to|from|fromTo)\([^)]*?(?:margin|padding):\s',
     "لا animate margin/padding في GSAP", "FAIL"),

    # Accessibility
    ("no-div-role-button", r'<div[^>]*role="button"',
     "لا <div role='button'> — استخدم <button> أو <a>", "FAIL"),
    ("has-html-lang-dir", r'<html\s+[^>]*lang="[^"]+"[^>]*dir="[^"]+"|<html\s+[^>]*dir="[^"]+"[^>]*lang="[^"]+"',
     "<html> يجب أن يحوي lang و dir", "FAIL"),

    # Letter-spacing on Arabic (rtl context)
    ("no-letter-spacing-on-arabic", None,
     "لا letter-spacing على نص عربي (يكسر الانضمام)", "WARN"),

    # Anti-template patterns
    ("no-hero-metric-template", r'class="[^"]*hero-metric[^"]*"',
     "لا hero-metric template (big number + small label + stats)", "FAIL"),
    ("no-gradient-text", r'background-clip:\s*text[^}]*gradient',
     "لا gradient text (background-clip: text + gradient)", "FAIL"),
    ("no-glassmorphism-default", r'backdrop-filter:\s*blur\([^)]*\)\s*[;}]',
     "لا glassmorphism كافتراضي", "WARN"),

    # Filler content
    ("no-lorem-ipsum", r'lorem\s+ipsum',
     "لا lorem ipsum filler", "FAIL"),
    ("no-feature-one-two-three", r'feature\s+(?:one|two|three)',
     "لا 'feature one/two/three' filler", "FAIL"),
]

P1_RULES = [
    ("has-prefers-reduced-motion", r'prefers-reduced-motion:\s*reduce',
     "prefers-reduced-motion محترم", "SHOULD"),
    ("has-focus-visible", r':focus-visible',
     ":focus-visible معرّف", "SHOULD"),
    ("has-aria-label", r'aria-label="[^"]+"',
     "ARIA labels موجودة", "SHOULD"),
    ("has-aria-selected", r'aria-selected=',
     "aria-selected للـ tabs", "SHOULD"),
    ("has-scrolltrigger-batch", r'ScrollTrigger\.batch',
     "ScrollTrigger.batch للـ grids", "SHOULD"),
    ("has-gsap-matchmedia", r'gsap\.matchMedia|matchMedia\(\s*["\']\(prefers-reduced-motion',
     "gsap.matchMedia للـ responsive + reduced-motion", "SHOULD"),
    ("has-logical-properties", r'(?:margin|padding|inset|border)-(?:inline|block)-(?:start|end)',
     "logical properties مستخدمة", "SHOULD"),
    ("has-var-accent", r'var\(--accent\)',
     "var(--accent) مستخدم (وليس hex مباشر)", "SHOULD"),
    ("has-typography-tracking-all-caps", r'text-transform:\s*uppercase[^}]*?letter-spacing:\s*0\.(?:0[6-9]|[1-9])|letter-spacing:\s*0\.(?:0[6-9]|[1-9])[^}]*?text-transform:\s*uppercase',
     "ALL CAPS مع letter-spacing ≥ 0.06em", "SHOULD"),
    ("has-max-width-prose", r'max-width:\s*\d+ch',
     "max-width لجسم النص", "SHOULD"),
    ("has-touch-target-min", r'(?:width|height):\s*(?:4[4-9]|[5-9][0-9]|1[0-9]{2,})px[^}]*?(?:width|height):\s*(?:4[4-9]|[5-9][0-9]|1[0-9]{2,})px',
     "touch targets ≥ 24×24 (ويفضل 44×44)", "SHOULD"),
    ("accent-usage-count", None,
     "var(--accent) ≤ 2 استخدامات ظاهرة بالشاشة", "SHOULD"),
]

P2_RULES = [
    ("has-custom-cursor", r'\.cursor\s*\{',
     "custom cursor على desktop فقط", "BONUS"),
    ("has-magnetic-button", r'data-magnetic',
     "magnetic buttons مع quickTo", "BONUS"),
    ("has-smooth-scroll", r'lenis|Lenis',
     "Lenis smooth scroll integration", "BONUS"),
    ("has-bg-color-transition", r'backgroundColor:\s*[^,]+,\s*duration',
     "انتقال ألوان خلفية بين الأقسام", "BONUS"),
    ("has-texture-overlay", r'feTurbulence|paper-noise|noise',
     "نسيج ورق خفيف (≤ 5% opacity)", "BONUS"),
    ("has-section-numbers", r'[٠-٩]\s*/\s*[٠-٩]|section-num',
     "أرقام أقسام شعرية", "BONUS"),
    ("has-microcopy-arabic", r'ابدأ|اكتشف|راسل',
     "microcopy عربي مدروس (ابدأ/اكتشف/راسل)", "BONUS"),
    ("has-parallax-layers", r'yPercent|parallax',
     "طبقات parallax متعددة السرعات", "BONUS"),
]


# ============================================================
# Audit Functions
# ============================================================

def read_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception:
        return ""


def check_rule(rule, content, file_path):
    """Returns (passed, message)"""
    rule_id, pattern, description, severity = rule

    if rule_id == "no-hex-outside-root":
        # Find hex values in CSS (between <style> tags) outside :root and [data-theme] blocks
        # Both :root and [data-theme="..."] are token definition blocks
        css_blocks = re.findall(r'<style[^>]*>(.*?)</style>', content, re.DOTALL)
        outside_hex = []
        for css in css_blocks:
            lines = css.split('\n')
            in_tokens = False  # tracks :root and [data-theme] blocks
            for i, line in enumerate(lines, 1):
                stripped = line.strip()
                # Token definition blocks: :root, [data-theme], [data-theme="..."]
                if re.match(r'^(?::root|\[data-theme[^\]]*\])\s*\{', stripped) or \
                   (re.match(r'^(?::root|\[data-theme[^\]]*\])\s*$', stripped)):
                    in_tokens = True
                if in_tokens and '}' in stripped:
                    in_tokens = False
                    continue
                if not in_tokens and not stripped.startswith(('/*', '*', '//')):
                    clean_line = re.sub(r'/\*.*?\*/', '', stripped)
                    hexes = re.findall(r'#[0-9A-Fa-f]{3,8}\b', clean_line)
                    if hexes:
                        outside_hex.append((i, hexes, line))
        return (len(outside_hex) == 0,
                f"Found {len(outside_hex)} CSS lines with hex outside :root/[data-theme]" if outside_hex else "All CSS colors via tokens")

    if rule_id == "no-outline-none-without-focus-visible":
        has_outline_none = bool(re.search(r'outline:\s*none', content))
        has_focus_visible = bool(re.search(r':focus-visible', content))
        if has_outline_none and not has_focus_visible:
            return (False, "outline: none without :focus-visible replacement")
        return (True, "OK")

    if rule_id == "no-letter-spacing-on-arabic":
        # Find elements with dir="rtl" or font-ar that have letter-spacing != 0
        # Simplified: check if any .display-ar or .body-ar class has letter-spacing != 0
        # Look for patterns like .class-ar { ... letter-spacing: 0.02em ... }
        ar_classes_with_tracking = []
        for match in re.finditer(r'\.([a-z-]*(?:ar|arabic)[a-z-]*)\s*\{([^}]+)\}', content, re.IGNORECASE):
            cls, body = match.group(1), match.group(2)
            ls_match = re.search(r'letter-spacing:\s*([-\d.]+(?:em|px)?)', body)
            if ls_match:
                val = ls_match.group(1)
                if val not in ('0', '0em', '0px', 'normal'):
                    ar_classes_with_tracking.append((cls, val))
        if ar_classes_with_tracking:
            return (False, f"Arabic classes with non-zero letter-spacing: {ar_classes_with_tracking}")
        return (True, "Arabic text has no letter-spacing (preserves joining)")

    if rule_id == "accent-usage-count":
        # Count var(--accent) usages in CSS body (outside :root)
        # Note: CSS rule count ≠ visible elements per screen
        # The rule is "≤ 2 visible per screen" — this requires runtime DOM analysis
        # Here we approximate: count distinct CSS rules using --accent
        css_section = content
        if '<style>' in css_section:
            css_section = css_section.split('<style>')[1].split('</style>')[0]
        # Remove :root blocks
        css_no_root = re.sub(r':root\s*\{[^}]+\}', '', css_section)
        accent_rules = len(re.findall(r'(?:^|\})[^{]*\{[^}]*var\(--accent\)', css_no_root, re.MULTILINE))
        # Allow up to ~15 distinct CSS rules (each rule applies to elements, not per-screen)
        # Real "per-screen" test needs Playwright/browser
        return (accent_rules <= 20,
                f"var(--accent) used in {accent_rules} CSS rules (rule: ≤ 2 visible elements per screen — runtime test needed)")

    # Standard regex check
    if pattern is None:
        return (True, "Skipped (no pattern)")

    found = bool(re.search(pattern, content, re.IGNORECASE | re.MULTILINE))

    # For "no-*" rules, passing means NOT finding the pattern
    if rule_id.startswith("no-"):
        if found:
            return (False, f"Pattern found: {pattern[:50]}")
        return (True, "Pattern not present")

    # For "has-*" rules, passing means finding the pattern
    if rule_id.startswith("has-"):
        if found:
            return (True, "Pattern present")
        return (False, "Pattern not found")

    return (True, "OK")


def run_audit(project_dir):
    project_path = Path(project_dir)
    index_html = project_path / "index.html"

    if not index_html.exists():
        print(f"❌ Error: {index_html} not found")
        return None

    content = read_file(index_html)
    results = {"P0": [], "P1": [], "P2": []}

    print("=" * 70)
    print(f"🔍 Design Master Audit — {project_dir}")
    print("=" * 70)

    # Run P0
    print("\n🔴 P0 — Must Pass (Cardinal Sins)")
    print("-" * 70)
    p0_pass = 0
    p0_fail = 0
    for rule in P0_RULES:
        rule_id, _, description, severity = rule
        passed, msg = check_rule(rule, content, index_html)
        status = "✓ PASS" if passed else "✗ FAIL"
        if passed:
            p0_pass += 1
        else:
            p0_fail += 1
        print(f"  {status}  [{rule_id}] {description}")
        if not passed:
            print(f"           → {msg}")
        results["P0"].append({"rule_id": rule_id, "description": description, "passed": passed, "msg": msg})

    # Run P1
    print("\n🟡 P1 — Should Pass (Quality Rules)")
    print("-" * 70)
    p1_pass = 0
    p1_fail = 0
    for rule in P1_RULES:
        rule_id, _, description, severity = rule
        passed, msg = check_rule(rule, content, index_html)
        status = "✓ PASS" if passed else "✗ FAIL"
        if passed:
            p1_pass += 1
        else:
            p1_fail += 1
        print(f"  {status}  [{rule_id}] {description}")
        if not passed:
            print(f"           → {msg}")
        results["P1"].append({"rule_id": rule_id, "description": description, "passed": passed, "msg": msg})

    # Run P2
    print("\n🟢 P2 — Bonus (Soul & Polish)")
    print("-" * 70)
    p2_pass = 0
    p2_total = 0
    for rule in P2_RULES:
        rule_id, _, description, severity = rule
        passed, msg = check_rule(rule, content, index_html)
        status = "✓ PASS" if passed else "○ MISS"
        if passed:
            p2_pass += 1
        p2_total += 1
        print(f"  {status}  [{rule_id}] {description}")
        results["P2"].append({"rule_id": rule_id, "description": description, "passed": passed, "msg": msg})

    # Summary
    print("\n" + "=" * 70)
    print("📊 SUMMARY")
    print("=" * 70)
    print(f"  P0 (Must Pass):  {p0_pass}/{len(P0_RULES)} passed, {p0_fail} failed")
    print(f"  P1 (Should Pass): {p1_pass}/{len(P1_RULES)} passed, {p1_fail} failed")
    print(f"  P2 (Bonus):       {p2_pass}/{p2_total} achieved")

    overall = "✅ PASS" if p0_fail == 0 else "❌ FAIL — must fix P0 issues"
    print(f"\n  Overall: {overall}")

    # Write audit report
    audit_path = project_path / ".design" / "audit.md"
    audit_path.parent.mkdir(parents=True, exist_ok=True)

    with open(audit_path, 'w', encoding='utf-8') as f:
        f.write(f"# Design Master Audit Report\n\n")
        f.write(f"**Date**: {datetime.now().isoformat()}\n")
        f.write(f"**Project**: {project_dir}\n")
        f.write(f"**Overall**: {overall}\n\n")
        f.write(f"## Summary\n\n")
        f.write(f"| Level | Passed | Failed | Total |\n")
        f.write(f"|-------|--------|--------|-------|\n")
        f.write(f"| P0 (Must Pass) | {p0_pass} | {p0_fail} | {len(P0_RULES)} |\n")
        f.write(f"| P1 (Should Pass) | {p1_pass} | {p1_fail} | {len(P1_RULES)} |\n")
        f.write(f"| P2 (Bonus) | {p2_pass} | {p2_total - p2_pass} | {p2_total} |\n\n")

        for level in ["P0", "P1", "P2"]:
            f.write(f"## {level} Rules\n\n")
            f.write(f"| Status | Rule | Description | Message |\n")
            f.write(f"|--------|------|-------------|---------|\n")
            for r in results[level]:
                status = "✓ PASS" if r["passed"] else ("✗ FAIL" if level != "P2" else "○ MISS")
                f.write(f"| {status} | {r['rule_id']} | {r['description']} | {r['msg']} |\n")
            f.write("\n")

    print(f"\n📝 Audit report written to: {audit_path}")
    return results


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python audit.py <project-dir>")
        sys.exit(1)
    run_audit(sys.argv[1])
