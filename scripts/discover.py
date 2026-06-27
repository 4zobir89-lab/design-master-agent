#!/usr/bin/env python3
"""
Design Master Discovery — Phase 0
يكشف الـ intent من طلب المستخدم، يصنّف الـ archetype + register، يختار theme.

Usage:
  python discover.py "أريد موقع شخصي لشاعر عربي معاصر، سينمائي وراقٍ"

Output:
  - stdout: discovery summary
  - .design/discovery.md (if run inside project)
"""

import re
import sys
import json
from pathlib import Path


# ============================================================
# Archetype Detection
# ============================================================

ARCHETYPE_KEYWORDS = {
    "portfolio": ["شخصي", "personal", "portfolio", "بورتفوليو", "سيرة ذاتية", "cv", "اعمالي"],
    "marketing-site": ["شركة", "company", "business", "agency", "وكالة", "مؤسسة"],
    "saas-landing": ["منتج", "product", "saas", "app", "تطبيق", "اشتراك", "subscription"],
    "ecommerce": ["متجر", "shop", "store", "بيع", "منتجات", "ecommerce", "تجاري"],
    "editorial": ["مدونة", "blog", "magazine", "مجلة", "صحيفة", "مقالات", "كتابة"],
    "dashboard": ["لوحة", "dashboard", "تحكم", "ادارة", "analytics"],
    "event": ["فعالية", "event", "مؤتمر", "conference", "مهرجان"],
    "nonprofit": ["جمعية", "nonprofit", "خيري", "إنساني"],
    "education": ["تعليم", "education", "أكاديمية", "مدرسة", "دورات", "course"],
    "docs": ["وثائق", "docs", "documentation", "دليل"],
}


# ============================================================
# Register Detection
# ============================================================

BRAND_REGISTER_KEYWORDS = [
    "شخصي", "personal", "portfolio", "أدب", "literature", "شعر", "poetry",
    "فن", "art", "تصميم", "design", "مجلة", "magazine", "editorial",
    "event", "فعالية", "luxury", "فاخر",
]

PRODUCT_REGISTER_KEYWORDS = [
    "تطبيق", "app", "saas", "dashboard", "متجر", "ecommerce", "shop",
    "settings", "إعدادات", "admin", "لوحة", "ادارة",
]


# ============================================================
# Tone Detection
# ============================================================

TONE_KEYWORDS = {
    "noir-cinema": ["سينمائي", "cinematic", "داكن", "dark", "أدب", "شعر", "literary"],
    "paper-warm": ["ورقي", "paper", "أدب", "editorial", "تحريري", "مجلة", "كتابة"],
    "swiss-grid": ["تقني", "technical", "B2B", "شركة", "corporate", "minimal", "بسيط"],
    "aurora-tech": ["تقنية", "tech", "ai", "dev", "web3", "سايبر", "cyber", "مستقبل"],
    "forest-calm": ["طبيعة", "nature", "صحة", "health", "wellness", "استدامة"],
    "sunset-warm": ["مطعم", "restaurant", "طعام", "food", "ضيافة", "hospitality", "سفر"],
    "brutalist-mono": ["تجريبي", "experimental", "جرئي", "bold", "فن", "art"],
    "midnight-luxury": ["فاخر", "luxury", "مجوهرات", "jewelry", "عقارات", "real estate"],
    "soft-pastel": ["أطفال", "kids", "تعليم", "education", "لطيف", "friendly"],
    "bauhaus-bold": ["استوديو", "studio", "هندسي", "geometric", "فن", "art"],
    "glass-light": ["saas", "modern", "نظيف", "clean", "dashboard"],
    "studio-editorial": ["مجلة", "magazine", "صحيفة", "publication", "news"],
}


# ============================================================
# Section Suggestions by Archetype
# ============================================================

ARCHETYPE_SECTIONS = {
    "portfolio": [
        "hero", "manifesto", "works", "lab", "quotes", "timeline", "articles", "contact"
    ],
    "marketing-site": [
        "hero", "problem", "solution", "features", "testimonials", "pricing", "faq", "cta"
    ],
    "saas-landing": [
        "hero", "features", "how-it-works", "integrations", "pricing", "testimonials", "faq", "cta"
    ],
    "ecommerce": [
        "hero", "featured-products", "categories", "bestsellers", "story", "testimonials", "newsletter", "footer-cta"
    ],
    "editorial": [
        "hero", "featured-article", "latest-articles", "categories", "authors", "newsletter", "archive"
    ],
    "dashboard": [
        "sidebar", "header", "stats", "main-chart", "recent-activity", "tasks", "settings"
    ],
    "event": [
        "hero", "about-event", "speakers", "schedule", "venue", "sponsors", "register", "faq"
    ],
    "nonprofit": [
        "hero", "mission", "impact", "programs", "stories", "team", "donate", "contact"
    ],
    "education": [
        "hero", "courses", "instructors", "curriculum", "testimonials", "pricing", "enroll", "faq"
    ],
    "docs": [
        "sidebar", "content", "on-this-page", "next-steps", "feedback"
    ],
}


# ============================================================
# Detection Logic
# ============================================================

def detect_archetype(request):
    scores = {}
    request_lower = request.lower()
    for arch, keywords in ARCHETYPE_KEYWORDS.items():
        scores[arch] = sum(1 for kw in keywords if kw in request_lower)
    if not any(scores.values()):
        return "portfolio"  # default
    return max(scores, key=scores.get)


def detect_register(request, archetype):
    # Override: certain archetypes always product register
    if archetype in {"dashboard", "ecommerce", "saas-landing", "docs"}:
        return "product"
    if archetype in {"portfolio", "editorial", "event"}:
        return "brand"

    # Otherwise: detect from keywords
    request_lower = request.lower()
    brand_score = sum(1 for kw in BRAND_REGISTER_KEYWORDS if kw in request_lower)
    product_score = sum(1 for kw in PRODUCT_REGISTER_KEYWORDS if kw in request_lower)
    return "brand" if brand_score >= product_score else "product"


def detect_tone(request):
    scores = {}
    request_lower = request.lower()
    for tone, keywords in TONE_KEYWORDS.items():
        scores[tone] = sum(1 for kw in keywords if kw in request_lower)
    if not any(scores.values()):
        return "noir-cinema"  # default — luxury minimal
    return max(scores, key=scores.get)


def detect_audience(request):
    # Extract audience hints
    audiences = []
    if re.search(r"قارئ|readers|كتاب|writers", request, re.I):
        audiences.append("readers/writers")
    if re.search(r"عميل|clients|customer", request, re.I):
        audiences.append("clients")
    if re.search(r"مستثمر|investor", request, re.I):
        audiences.append("investors")
    if re.search(r"مطور|developer|dev", request, re.I):
        audiences.append("developers")
    if re.search(r"مصمم|designer", request, re.I):
        audiences.append("designers")
    if re.search(r"طالب|student", request, re.I):
        audiences.append("students")
    if not audiences:
        audiences.append("general audience")
    return audiences


def detect_constraints(request):
    constraints = []
    if re.search(r"RTL|عربي|arabic", request, re.I):
        constraints.append("RTL Arabic")
    if re.search(r"mobile|موبايل|هاتف", request, re.I):
        constraints.append("mobile-first")
    if re.search(r"dark|داكن|ليلي", request, re.I):
        constraints.append("dark mode preferred")
    if re.search(r"light|فاتح|نهاري", request, re.I):
        constraints.append("light mode preferred")
    if re.search(r"fast|سريع|performance", request, re.I):
        constraints.append("performance-critical")
    if re.search(r"accessib|وصول|a11y", request, re.I):
        constraints.append("accessibility AA+")
    return constraints if constraints else ["standard web"]


# ============================================================
# Theme Mapping
# ============================================================

THEME_MAP = {
    "noir-cinema": "Noir Cinema (Dark Cinematic)",
    "paper-warm": "Paper Warm (Editorial Literary)",
    "swiss-grid": "Swiss Grid (International Style)",
    "aurora-tech": "Aurora Tech (Cyberpunk Light)",
    "forest-calm": "Forest Calm (Nature Wellness)",
    "sunset-warm": "Sunset Warm (Restaurant Lifestyle)",
    "brutalist-mono": "Brutalist Mono (Bold Statement)",
    "midnight-luxury": "Midnight Luxury (Premium Dark)",
    "soft-pastel": "Soft Pastel (Friendly Products)",
    "bauhaus-bold": "Bauhaus Bold (Geometric)",
    "glass-light": "Glass Light (Modern Crisp)",
    "studio-editorial": "Studio Editorial (Magazine)",
}


# ============================================================
# Main
# ============================================================

def discover(request):
    archetype = detect_archetype(request)
    register = detect_register(request, archetype)
    tone = detect_tone(request)
    theme = THEME_MAP[tone]
    audience = detect_audience(request)
    constraints = detect_constraints(request)
    sections = ARCHETYPE_SECTIONS.get(archetype, ["hero", "about", "contact"])

    result = {
        "request": request,
        "archetype": archetype,
        "register": register,
        "tone": tone,
        "theme": theme,
        "audience": audience,
        "constraints": constraints,
        "sections_suggested": sections,
        "hero_moment_hint": "Create a 'I want to explore' first impression — not a banner",
    }
    return result


def write_discovery_md(result, output_dir="."):
    """Write .design/discovery.md"""
    design_dir = Path(output_dir) / ".design"
    design_dir.mkdir(parents=True, exist_ok=True)
    path = design_dir / "discovery.md"

    with open(path, 'w', encoding='utf-8') as f:
        f.write("# Phase 0 — Discovery\n\n")
        f.write(f"**Request**: {result['request']}\n\n")
        f.write("## Detected Signals\n\n")
        f.write(f"- **Archetype**: `{result['archetype']}`\n")
        f.write(f"- **Register**: `{result['register']}` (Brand=distinctiveness, Product=earned familiarity)\n")
        f.write(f"- **Tone**: `{result['tone']}`\n")
        f.write(f"- **Suggested Theme**: {result['theme']}\n")
        f.write(f"- **Audience**: {', '.join(result['audience'])}\n")
        f.write(f"- **Constraints**: {', '.join(result['constraints'])}\n\n")
        f.write("## Suggested Sections\n\n")
        for i, s in enumerate(result['sections_suggested'], 1):
            f.write(f"{i}. {s}\n")
        f.write(f"\n## Hero Moment Hint\n\n{result['hero_moment_hint']}\n\n")
        f.write("## Next Phase\n\n")
        f.write("Write PRODUCT.md + DESIGN.md based on this discovery.\n")

    return path


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python discover.py \"<user request>\" [output-dir]")
        sys.exit(1)

    request = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "."

    result = discover(request)

    print("=" * 70)
    print("🔍 Design Master Discovery — Phase 0")
    print("=" * 70)
    print(f"\n📝 Request: {result['request']}\n")
    print("Detected Signals:")
    print(f"  • Archetype:  {result['archetype']}")
    print(f"  • Register:   {result['register']}")
    print(f"  • Tone:       {result['tone']}")
    print(f"  • Theme:      {result['theme']}")
    print(f"  • Audience:   {', '.join(result['audience'])}")
    print(f"  • Constraints: {', '.join(result['constraints'])}")
    print("\nSuggested Sections:")
    for i, s in enumerate(result['sections_suggested'], 1):
        print(f"  {i}. {s}")

    if output_dir != ".":
        path = write_discovery_md(result, output_dir)
        print(f"\n📝 Discovery written to: {path}")

    print("\n" + "=" * 70)
    print("✅ Discovery complete. Next: write PRODUCT.md + DESIGN.md")
    print("=" * 70)
