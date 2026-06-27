---
name: design-master
description: >
  Senior design agent that transforms vague requests ("build me a website for X")
  into stunning, soul-bearing digital presences. Applies 70 years of design craft
  (typography, color, motion, accessibility) with strict anti-AI-slop discipline.
  Auto-discovers intent, writes contract, plans phases, builds with seeds+recipes,
  self-audits with 44 deterministic rules, delivers as self-contained HTML.
triggers:
  - "موقع"
  - "صفحة"
  - "landing"
  - "portfolio"
  - "website"
  - "site"
  - "design"
  - "صمم"
  - "ابن"
  - "اعمل موقع"
  - "أريد موقع"
  - "صفحة هبوط"
  - "build a website"
  - "design a page"
  - "create a landing"
  - "make me a site"
od:
  mode: prototype
  craft_requires:
    - anti-ai-slop
    - typography
    - color
    - animation-discipline
    - accessibility-baseline
    - state-coverage
  capabilities_required:
    - file_write
    - file_read
outputs:
  - "<out>/index.html"
  - "<out>/PRODUCT.md"
  - "<out>/DESIGN.md"
  - "<out>/.design/discovery.md"
  - "<out>/.design/plan.md"
  - "<out>/.design/audit.md"
example_prompt: "أريد موقع شخصي لشاعر عربي معاصر، يكون سينمائي وراقٍ"
---

# design-master — Skill

## When to Use
أي طلب لبناء موقع أو صفحة ويب كاملة، سواء:
- موقع شخصي / portfolio
- صفحة هبوط لمنتج (SaaS landing)
- موقع شركة
- مدونة / موقع تحريري
- متجر (ecommerce single-page)
- موقع فعالية / حدث
- صفحة تواصل

## When NOT to Use
- تعديل صفحة موجودة → استخدم refactor mode
- صفحة واحدة بسيطة (about/contact) → اكتبها مباشرة
- API/backend → مهارة أخرى

## Pre-flight Reading (إلزامي قبل أي كود)

اقرأ بهذا الترتيب:

1. `AGENTS.md` — العقد الكامل (Section 2: 7 Phases)
2. `references/anti-ai-slop.md` — الـ 7 خطايا الكاردينالية
3. `references/craft-rules.md` — القواعد الذهبية الـ 36
4. `references/animation-recipes.md` — 20+ وصفة GSAP
5. `references/scroll-patterns.md` — أنماط ScrollTrigger
6. `references/performance.md` — قواعد الأداء الـ 10
7. `references/themes.md` — الثيمات الـ 12 الجاهزة
8. `seeds/template.html` — البذرة الأساسية (CSS tokens + classes)
9. `templates/` — قوالب artifacts الجاهزة

## The 7 Phases (Non-Negotiable)

### Phase 0 — Discovery (silent, no user questions)
```
INPUT: user request + optional PRD
PROCESS:
  1. Parse intent: type, audience, tone, constraints
  2. Classify: archetype (10 options) + register (brand vs product)
  3. Infer tone: luxury-minimalism | editorial | brutalist | swiss | cyber | paper
  4. Choose default theme from themes/
  5. Identify "hero moment" candidate
OUTPUT: .design/discovery.md
TIME: 30 seconds
```

### Phase 1 — Contract
```
INPUT: discovery.md
PROCESS:
  1. Write PRODUCT.md (identity, register, audience, anti-refs, tone, soul)
  2. Write DESIGN.md (palette, typography, spacing, motion, anti-patterns)
  3. All decisions auto-taken — explain inside files, not in chat
OUTPUT: PRODUCT.md + DESIGN.md
```

### Phase 2 — Plan
```
INPUT: DESIGN.md
PROCESS:
  1. List sections (5-8 typical)
  2. For each section: assign recipe from animation-recipes.md
  3. Assign motion direction per section
  4. Define mobile downgrade per section
  5. Write .design/plan.md (table)
  6. Write .design/phases/p0X-<section>.md for each
OUTPUT: .design/plan.md + .design/phases/*.md
```

### Phase 3 — Seed Selection
```
INPUT: DESIGN.md + theme
PROCESS:
  1. Read seeds/template.html (DO NOT MODIFY — use as base)
  2. Apply theme tokens (override :root variables)
  3. Read recipes applicable to plan
OUTPUT: chosen recipes + theme ready in mind
```

### Phase 4 — Implementation (one phase at a time)
```
FOR each section in plan:
  1. Read phase file
  2. Write semantic HTML using seed classes
  3. Write section-specific CSS (only additions, no overrides of tokens)
  4. Write section JS using recipe
  5. Add ARIA
  6. Verify mobile downgrade
  7. Update phase status: In Progress → Done
  8. Update .design/plan.md
```

### Phase 5 — Self-Audit (must pass before delivery)
```
RUN audit script: python scripts/audit.py <output-dir>
CHECKS:
  P0 (must pass, 21 rules):
    - no forbidden colors (indigo family)
    - no forbidden fonts (Inter as default, DM Sans, etc.)
    - no emoji as icons
    - no hex outside :root
    - no text-align: left/right
    - no margin-left/right
    - no letter-spacing on Arabic
    - no animating width/height/top/left in GSAP
    - no <div role="button">
    - <html lang/dir> correct
    - var(--accent) ≤ 2 visible uses per screen
    - ... (see AGENTS.md Section 2 Phase 5)

  P1 (should pass, 12 rules):
    - ALL CAPS letter-spacing
    - Display negative tracking
    - max-width: 65ch
    - line-height ≥ 1.6 Arabic
    - 5 states for data surfaces
    - prefers-reduced-motion
    - :focus-visible
    - touch targets ≥ 24×24
    - contrast ≥ 4.5:1
    - < 20 ScrollTriggers
    - ScrollTrigger.batch for grids

  P2 (bonus, 8 rules):
    - 80/20 soul
    - microcopy
    - texture
    - bg color transitions
    - custom cursor desktop-only

IF any P0 fails → fix and re-audit
IF any P1 fails → warn but allow delivery with explanation
OUTPUT: .design/audit.md
```

### Phase 6 — Delivery
```
OUTPUT FILES:
  - index.html (self-contained, no external CSS files, CDN OK for fonts/GSAP)
  - PRODUCT.md
  - DESIGN.md
  - .design/discovery.md
  - .design/plan.md
  - .design/phases/*.md
  - .design/audit.md

CHAT RESPONSE:
  - One-paragraph executive summary
  - List of files delivered
  - Key design decisions explained (3-5 bullets)
  - What to do next (suggestions)

DO NOT:
  - Dump full HTML in chat
  - Ask user for decisions mid-build
  - Skip any phase
```

## Auto-Decision Matrix

| Input signal | Auto-decision |
|---|---|
| "شخصي" / "personal" | Brand register + archetype=portfolio |
| "شركة" / "company" | Product register + archetype=marketing-site |
| "متجر" / "shop" | Product register + archetype=ecommerce |
| "مدونة" / "blog" | Brand register + archetype=editorial |
| "سياحة" / "luxury" | Dark theme + brass accent + serif display |
| "تقنية" / "tech" | Dark theme + electric accent + mono accents |
| "أطفال" / "kids" | Light theme + warm palette + playful bounce |
| "صحة" / "medical" | Light theme + green/blue + clean sans |
| "أدب" / "شعر" | Paper theme + ink accent + Arabic serif |
| "مطعم" / "food" | Warm theme + earthy accent + display serif |

## Forbidden (Reflex-Reject)

لا تستخدم هذه الخطوط (reflex-reject fonts from impeccable):
```
Fraunces, Newsreader, Lora, Crimson (any), Playfair Display,
Cormorant (any), Syne, IBM Plex (any), Space Mono, Space Grotesk,
Inter (as default — OK in Product register only),
DM Sans, DM Serif (any), Outfit, Plus Jakarta Sans,
Instrument Sans, Instrument Serif
```

> استثناء: في Brand register، Cormorant Garamond مسموح لأنه ليس Reflex-reject في القائمة الأصلية (ولكن انتبه من Overuse).

لا تستخدم هذه الأنماط (saturated aesthetic lanes):
```
- Editorial-typographic (italic Fraunces + mono labels + ruled separators) — saturated
- Cream/sand/beige body bg as AI default 2026
- Purple-to-blue gradient hero
- Glassmorphism as default
- "AI dashboard tile" (rounded card + left colored border)
- Hero-metric template (big number + small label + supporting stats)
```

## Required Files in Output

```
<project-name>/
├── index.html              ← self-contained, ~1500-3000 lines
├── PRODUCT.md              ← 200-400 words
├── DESIGN.md               ← 500-800 words
└── .design/
    ├── discovery.md        ← Phase 0 output
    ├── plan.md             ← Phase 2 output
    ├── audit.md            ← Phase 5 output
    └── phases/
        ├── p01-<section>.md
        ├── p02-<section>.md
        └── ...
```

## Quality Bar

الموقع يُعتبر "ناجحاً" فقط إذا:

1. ✅ اجتاز كل P0 rules (21 قاعدة)
2. ✅ اجتاز ≥ 90% من P1 rules
3. ✅ يحتوي على ≥ 3 لمسات "soul" مميّزة
4. ✅ اجتاز اختبار الثواني الثلاث (لا يبدو كـ AI)
5. ✅ يحتوي على hero moment واحد قوي
6. ✅ كل قسم له شخصية بصرية مميّزة (لا identical cards)
7. ✅ الأنيميشن هادف (لا استعراضي)
8. ✅ الـ microcopy دقيق ومناسب للعلامة
9. ✅ RTL/LTR مضبوط (حسب اللغة)
10. ✅ mobile downgrade معرّف لكل قسم

## Failure Modes (avoid these)

1. **"Pretty but soulless"** — طبّقت القواعد لكن لا لمسة مميّزة
2. **"Linear/Vercel ripoff"** — استخدمت indigo + Inter + glass + grid
3. **"AI dashboard tile"** — بطاقات مستديرة بحدود يسرى
4. **"Saturated aesthetic"** — اخترت editorial-typographic الـ saturated
5. **"Hero-metric template"** — رقم كبير + label + supporting stats
6. **"Identical card grid"** — 3-4 بطاقات بنفس الشكل
7. **"Eyebrow everywhere"** — `ALL CAPS EYEBROW` على كل قسم
8. **"Feature row trap"** — icon + heading + 3 lines vague benefit
9. **"Gradient text"** — `background-clip: text` + gradient
10. **"Glassmorphism default"** — `backdrop-filter: blur` على كل شيء

## See Also

- `AGENTS.md` — العقد الكامل
- `references/anti-ai-slop.md` — مكافحة بصمات الـ AI
- `references/craft-rules.md` — القواعد الذهبية
- `references/animation-recipes.md` — وصفات GSAP
- `references/scroll-patterns.md` — أنماط ScrollTrigger
- `references/performance.md` — قواعد الأداء
- `references/themes.md` — الثيمات الجاهزة
- `seeds/template.html` — البذرة الأساسية
- `templates/` — قوالب artifacts
- `scripts/audit.py` — سكريبت الفحص الآلي
