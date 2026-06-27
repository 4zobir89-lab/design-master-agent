# 🎨 Design Master Agent

> **نظام وكيل تصميم كامل** يحوّل أي LLM (Claude / Cursor / Codex / Gemini) إلى Senior Creative Director.
> مستخلص من 3 مستودعات: `open-design` + `impeccable` + `gsap-animated-frontend`.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Audit Rules: 41](https://img.shields.io/badge/Audit_Rules-41_(21_P0_+12_P1_+8_P2)-red)](#-quality-audit)
[![Themes: 12](https://img.shields.io/badge/Themes-12_ready-blue)](#-theme-library)
[![Recipes: 23+](https://img.shields.io/badge/GSAP_Recipes-23+-orange)](#-animation-recipes)

---

## 🎯 ما هذا؟

بدلاً من بناء "موقع جميل واحد"، هذا النظام يجعل أي وكيل AI **يتبع منهجية صارمة** عند تلقي طلب موقع:

```
User: "أريد موقع شخصي لشاعر عربي معاصر"
         ↓
Agent reads SKILL.md → executes 7 phases:
  0. Discovery (silent — auto-detects intent)
  1. Contract (writes PRODUCT.md + DESIGN.md)
  2. Plan (phases + recipes)
  3. Seed selection (chooses theme + base template)
  4. Implementation (one phase at a time)
  5. Self-Audit (41 deterministic rules)
  6. Delivery (self-contained HTML + artifacts)
         ↓
Output: stunning website + full design contract + audit report
```

## 📦 محتويات النظام

```
design-master-agent/
├── AGENTS.md              ← العقد الأساسي (يقرأه الوكيل أولاً)
├── SKILL.md               ← مهارة الوكيل القابلة للاستدعاء
├── README.md              ← هذا الملف
├── INSTALL.md             ← دليل التثبيت المفصّل لكل منصة
├── LICENSE                ← MIT
├── .gitignore
│
├── references/            ← كنوز المعرفة (يقرأها الوكيل قبل أي كود)
│   ├── anti-ai-slop.md    ← الـ 7 خطايا الكاردينالية (P0)
│   ├── craft-rules.md     ← الـ 36 قاعدة الذهبية (P0+P1)
│   ├── animation-recipes.md  ← 23+ وصفة GSAP جاهزة للّصق
│   ├── scroll-patterns.md ← 10 أنماط ScrollTrigger
│   ├── performance.md     ← 10 قواعد أداء
│   └── themes.md          ← 12 ثيم جاهز
│
├── seeds/
│   └── template.html      ← بذرة HTML/CSS/JS كاملة كنقطة انطلاق
│
├── scripts/
│   ├── discover.py        ← Phase 0: auto-discovery من طلب المستخدم
│   ├── audit.py           ← Phase 5: فحص آلي للقواعد الـ 41
│   └── install.sh         ← سكريبت تثبيت سريع
│
├── templates/             ← قوالب artifacts
│   ├── discovery.md
│   ├── plan.md
│   └── phase.md
│
├── examples/              ← أمثلة جاهزة
│   └── README.md          ← قائمة بأمثلة المشاريع المولّدة
│
└── .github/
    └── workflows/
        └── audit.yml      ← CI: يفحص كل PR بالـ audit.py
```

## 🚀 التثبيت السريع (30 ثانية)

### الطريقة 1: سكريبت آلي (موصى به)

```bash
# Claude Code
curl -fsSL https://raw.githubusercontent.com/4zobir89-lab/design-master-agent/main/scripts/install.sh | bash -s -- --target claude

# Cursor
curl -fsSL https://raw.githubusercontent.com/4zobir89-lab/design-master-agent/main/scripts/install.sh | bash -s -- --target cursor

# Codex CLI
curl -fsSL https://raw.githubusercontent.com/4zobir89-lab/design-master-agent/main/scripts/install.sh | bash -s -- --target codex
```

### الطريقة 2: تثبيت يدوي

```bash
# استنساخ
git clone https://github.com/4zobir89-lab/design-master-agent.git

# نسخ إلى skills directory
cp -r design-master-agent ~/.claude/skills/design-master
# أو في Cursor:
cp -r design-master-agent ~/.cursor/skills/design-master
```

### الطريقة 3: استخدام في سياق المحادثة فقط

أضف محتوى `AGENTS.md` إلى system prompt، أو اطلب من الوكيل:

```
اقرأ https://github.com/4zobir89-lab/design-master-agent/blob/main/AGENTS.md
واطبّق منهجية design-master لبناء موقع لـ X
```

📖 **دليل التثبيت الكامل لكل منصة**: [`INSTALL.md`](INSTALL.md)

## 🎬 كيف يعمل (مثال كامل)

### الطلب
```
User: "أريد موقع شخصي لشاعر عربي معاصر، يكون سينمائي وراقٍ"
```

### ما يحدث تلقائياً (دون سؤال المستخدم)

**Phase 0 — Discovery** (الوكيل يفكّر داخلياً):
```bash
python scripts/discover.py "أريد موقع شخصي لشاعر عربي معاصر، سينمائي"
```
الناتج:
- Archetype: `portfolio`
- Register: `brand` (التميّز معيار)
- Tone: `noir-cinema`
- Theme: `Noir Cinema (Dark Cinematic)`
- Sections: hero, manifesto, works, lab, quotes, timeline, articles, contact
- يكتب `.design/discovery.md`

**Phase 1 — Contract** (الوكيل يكتب ملفّين):
- `PRODUCT.md` — Identity, Register, Anti-references, Tone, Soul
- `DESIGN.md` — Palette, Typography, Motion rules, Anti-patterns

**Phase 2 — Plan** (الوكيل يكتب الخطة):
- لكل قسم: recipe, objective, motion, mobile downgrade
- يكتب `.design/plan.md` + `.design/phases/p0X-*.md`

**Phase 3 — Seed Selection**:
- يقرأ `seeds/template.html` (لا يكتب CSS من الصفر!)
- يطبّق Noir Cinema theme tokens
- يختار recipes من `references/animation-recipes.md`

**Phase 4 — Implementation** (phase واحدة في كل مرة):
- يكتب HTML دلالي
- يكتب CSS باستخدام tokens فقط
- يكتب JS باستخدام recipes فقط
- يضيف ARIA

**Phase 5 — Self-Audit**:
```bash
python scripts/audit.py ./my-website
```
- يفحص 21 قاعدة P0 + 12 قاعدة P1 + 8 قاعدة P2
- إن فشل أي P0 → يُصلح ويُعيد الفحص
- يكتب `.design/audit.md`

**Phase 6 — Delivery**:
- `index.html` (self-contained, ~2000-3000 lines)
- `PRODUCT.md` + `DESIGN.md`
- `.design/` artifacts (للاستئناف الآمن)
- ملخص تنفيذي في الـ chat

## 🔍 لماذا هذا النظام يُنتج "WOW"؟

### 1. القيود، لا الحرّية المطلقة
> **"الإبهار يأتي من القيود، لا من الحرّية المطلقة."**

الوكيل لا يُبتكر من الصفر. يُركّب من:
- **Tokens** (theme .css) — 12 ثيم جاهز
- **Components** (`seeds/template.html`) — بذرة بكل defaults الذكية
- **Recipes** (`references/animation-recipes.md`) — 23+ وصفة مُختبرة
- **Constraints** (`references/anti-ai-slop.md` + `craft-rules.md`) — حدود صارمة

### 2. الـ 7 خطايا الكاردينالية مُتفاداة تلقائياً
- ❌ لا indigo (`#6366f1`, `#8b5cf6`, `#7c3aed`)
- ❌ لا تدرّجات بنفسجية على hero
- ❌ لا إيموجي كأيقونات
- ❌ لا Inter كافتراضي وحيد (Brand register)
- ❌ لا بطاقة مستديرة بحدود يسرى ملوّنة
- ❌ لا أرقام مُختلقة بلا مصدر
- ❌ لا lorem ipsum أو "feature one/two/three"

### 3. الفحص الآلي يضمن الجودة
سكريبت `audit.py` يفحص 41 قاعدة بلا LLM — كل فشل P0 = إعادة بناء.

### 4. الـ "Soul" إجباري
الـ 20% المميّزة المطلوبة:
- خط نادر يعطي شخصية (وليس Inter/DM Sans)
- microcopy دقيق ("ابدأ القراءة" بدل "Get started")
- تفصيلة مستخدم-منتج حقيقية
- انتقال سينمائي غير متوقع
- نسيج/texture خفيف

### 5. الـ artifacts تحل محل chat memory
`.design/` يحفظ كل القرارات — يمكن لأي وكيل آخر استئناف العمل دون سؤال المستخدم.

## 📊 Quality Audit

النظام يفحص كل مشروع بـ **41 قاعدة حتمية** (بلا LLM):

### P0 — Must Pass (21 قاعدة)
- Color bans (indigo, purple, gradient hero)
- Card anti-patterns (rounded + left stripe)
- Code hygiene (no hex outside :root, no margin-left, no text-align: left)
- GSAP performance (no width/height/top/left animation)
- Accessibility (no div role=button, has lang+dir)
- Anti-template (no hero-metric, no gradient-text, no glassmorphism default)
- Filler (no lorem ipsum, no feature-one-two-three)

### P1 — Should Pass (12 قاعدة)
- `prefers-reduced-motion` محترم
- `:focus-visible` معرّف
- ARIA labels + aria-selected
- `ScrollTrigger.batch` للـ grids
- `gsap.matchMedia` للـ responsive
- logical properties (`margin-inline-*`)
- `var(--accent)` مستخدم (ليس hex مباشر)
- ALL CAPS `letter-spacing ≥ 0.06em`
- `max-width: 65ch` للجسم
- touch targets ≥ 24×24
- accent usage ≤ 2 per screen
- لا `letter-spacing` على عربي

### P2 — Bonus (8 قواعد)
- custom cursor (desktop only)
- magnetic buttons
- Lenis smooth scroll
- background color transitions
- texture overlay (paper/noise)
- section numbers (Arabic-Indic)
- microcopy بلغة المستخدم
- parallax layers

### تشغيل الفحص
```bash
python scripts/audit.py ./my-project
```

الناتج:
```
🔴 P0 — Must Pass
  ✓ PASS  [no-indigo] لا ألوان indigo/violet/purple كـ accent
  ✓ PASS  [no-emoji-as-icons] لا إيموجي كأيقونات
  ...
🟡 P1 — Should Pass
  ✓ PASS  [has-prefers-reduced-motion] prefers-reduced-motion محترم
  ...
🟢 P2 — Bonus
  ✓ PASS  [has-custom-cursor] custom cursor على desktop فقط
  ...

📊 SUMMARY
  P0: 21/21 passed
  P1: 11/12 passed
  P2: 8/8 achieved
  Overall: ✅ PASS
```

## 🎨 Theme Library

12 ثيم جاهز، كل واحد 15-25 سطر CSS فقط:

| الثيم | الاستخدام | الـ Accent |
|---|---|---|
| 🌑 **Noir Cinema** | أدب، فن، سينما، تصوير | `#B58E63` brass |
| 📜 **Paper Warm** | أدب، مدونات، مجلات | `#7C2D12` ink red |
| 🔵 **Swiss Grid** | شركات تقنية، SaaS B2B | `#D6001C` Swiss red |
| 🌌 **Aurora Tech** | dev tools، AI، Web3 | `#00D9FF` electric cyan |
| 🍃 **Forest Calm** | صحة، طبيعة، استدامة | `#3F6212` moss |
| 🌅 **Sunset Warm** | مطاعم، ضيافة، سفر | `#C2410C` amber |
| ⚫ **Brutalist Mono** | portfolios تجريبية، فن | `#FF3D00` bolt |
| 🌙 **Midnight Luxury** | فنادق، مجوهرات، عقارات | `#C9A876` gold |
| 🍦 **Soft Pastel** | أطفال، تعليم، تطبيقات لطيفة | `#F472B6` pink |
| 🟤 **Bauhaus Bold** | studios، galleries | `#E63946` red |
| 💎 **Glass Light** | SaaS، dashboards | `#0EA5E9` sky |
| 🎭 **Studio Editorial** | مجلات، صحف | `#1E40AF` editorial blue |

📖 **التفاصيل الكاملة**: [`references/themes.md`](references/themes.md)

## 🎬 Animation Recipes

23+ وصفة GSAP جاهزة للّصق:

### Hero (3)
- Text Reveal Hero — stagger كلمات
- Cinematic Zoom Hero — تكبير سينمائي
- Floating Shapes — خلفية تطفو

### Cards (3)
- Staggered Reveal (ScrollTrigger.batch)
- Hover Lift Effect
- 3D Tilt on Mouse Move

### Numbers (2)
- Count Up — أرقام تتعدّ
- Stats Card with Trend Arrow

### Text (2)
- Word-by-Word Reveal (بدون SplitText)
- Typewriter Effect

### Scroll (4)
- Reveal on Scroll
- Pinned Scene Transitions
- Horizontal Scroll
- Background Color Transition

### Navigation (2)
- Navbar Shrink on Scroll
- Mobile Menu Reveal

### Special Effects (4)
- Magnetic Button (`gsap.quickTo`)
- Custom Cursor (dual-speed)
- Reveal Mask (clip-path)
- SVG Line Draw

### Utilities (3)
- Smooth Scroll (Lenis)
- Page Transition (Next.js)
- Progress Bar

📖 **التفاصيل**: [`references/animation-recipes.md`](references/animation-recipes.md)

## 🎭 السجلّان (Registers)

كل موقع ينتمي لأحد سجلّين (من `impeccable`):

### Brand Register (التميّز معيار)
- التصميم *هو* المنتج
- 适用: portfolio, personal, marketing, magazine, event
- يسمح: full palette, drenched accents, experimental type
- يمنع: Inter كافتراضي، cream/sand/beige default

### Product Register (الإتقان معيار)
- التصميم *يخدم* المنتج
- 适用: dashboard, saas, ecommerce, docs, settings
- يسمح: restrained palette, Inter (مسموح هنا فقط)
- يمنع: experimental type، spectacle يأخر الإنجاز

## 📋 أمثلة طلب → ناتج

### مثال 1: SaaS لـ AI
**الطلب**: "أريد موقع لشركة تقنية ناشئة في مجال الـ AI، عصري وجريء، يستهدف مطورين ومستثمرين"

**ما يكتشف الوكيل تلقائياً**:
- Archetype: `saas-landing`
- Register: `product`
- Tone: `aurora-tech`
- Theme: **Aurora Tech (Cyberpunk Light)**
- Sections: hero, features, how-it-works, integrations, pricing, testimonials, faq, cta
- Fonts: Space Grotesk + Inter (Product register OK) + JetBrains Mono
- Accent: `#00D9FF` electric cyan (لا indigo!)
- Motion: snappy reveals (300-500ms)، magnetic CTAs، code-snippet animations

### مثال 2: مطعم فاخر
**الطلب**: "أريد موقع لمطعم فاخر يقدم مأكولات يابانية، دافئ وأنيق"

**ما يكتشف الوكيل تلقائياً**:
- Archetype: `marketing-site`
- Register: `brand`
- Tone: `sunset-warm` (مع لمسة midnight-luxury)
- Theme: **Sunset Warm**
- Sections: hero, story, menu, chef, gallery, reservation, contact
- Fonts: Playfair Display + Inter + JetBrains Mono
- Accent: `#C2410C` deep amber (لا indigo!)
- Motion: slow reveals (700-1200ms)، parallax images، ken-burns on hero

### مثال 3: متجر قهوة
**الطلب**: "أريد موقع متجر قهوة مختصة، دافئ وفاخر"

**ما يكتشف الوكيل**:
- Archetype: `ecommerce` · Register: `product` · Tone: `midnight-luxury`
- 8 sections: hero, featured-products, categories, bestsellers, story, testimonials, newsletter, footer-cta

## 🛠️ السكريبتات

### `discover.py` — Phase 0: Auto-Discovery
```bash
python scripts/discover.py "أريد موقع شخصي لشاعر عربي معاصر، سينمائي"

# Output:
# Archetype:  portfolio
# Register:   brand
# Tone:       noir-cinema
# Theme:      Noir Cinema (Dark Cinematic)
# Sections:   hero, manifesto, works, lab, quotes, timeline, articles, contact
```

يدعم:
- 10 archetypes (portfolio, marketing, saas, ecommerce, editorial, dashboard, event, nonprofit, education, docs)
- 12 tones (noir-cinema, paper-warm, swiss-grid, aurora-tech, ...)
- كشف audience + constraints تلقائياً
- اقتراح sections حسب archetype

### `audit.py` — Phase 5: Quality Audit
```bash
python scripts/audit.py ./my-website

# Output: تقرير ملوّن + .design/audit.md
# 21 P0 (must pass) + 12 P1 (should pass) + 8 P2 (bonus)
```

### `install.sh` — سكريبت التثبيت
```bash
./scripts/install.sh --target claude    # Claude Code
./scripts/install.sh --target cursor    # Cursor
./scripts/install.sh --target codex     # Codex CLI
./scripts/install.sh --target gemini    # Gemini CLI
./scripts/install.sh --target all       # كل ما سبق
```

## 🧪 اختبار الثواني الثلاث

قبل التسليم، الوكيل يسأل نفسه:

1. هل يبدو كأي موقع AI startup؟ → إن نعم، أعد البناء
2. هل أستطيع تخمين الـ category وحدها؟ → إن نعم، trap one tier deeper
3. هل يبدو كـ Linear/Vercel/Cursor ripoff؟ → إن نعم، أعد البناء
4. هل يحتوي على "feature row" (icon + heading + 3 lines vague benefit)؟ → أزل

## 📚 الفلسفة (من المستودعات الثلاثة)

### من `open-design/craft/`
- فصل الـ tokens عن الـ components عن الـ effects
- القواعد الكونية للأناقة (typography, color, motion, a11y)
- "Compose, don't author from scratch"
- 80% proven + 20% "soul"

### من `impeccable/SKILL.src.md`
- Brand register vs Product register
- Reflex-reject fonts (Inter as default, DM Sans, Outfit, Plus Jakarta, ...)
- Absolute bans (gradient-text, glassmorphism, hero-metric template)
- "Practice what you preach" — النظام يجتاز فحوصاته

### من `gsap-animated-frontend/`
- Spec-driven over prompt-driven
- Phased execution (لا صفحة كاملة في محاولة واحدة)
- `.gsap/` artifacts تحل محل chat memory
- Discover before ask
- Reduced-motion + mobile downgrade non-negotiable
- 20+ animation recipes جاهزة للّصق

## 🤝 المساهمة

المساهمات مرحّب بها! اقرأ [CONTRIBUTING.md](CONTRIBUTING.md) (قريباً).

### أفكار للمساهمة
- إضافة themes جديدة (Y2K, Memphis, Vaporwave, ...)
- إضافة recipes جديدة (Three.js, Canvas particles, WebGL shaders)
- تحسين `discover.py` (كشف أكثر دقة)
- تحسين `audit.py` (قواعد P0/P1/P2 إضافية)
- إضافة دعم لـ Vue/Svelte (غير React فقط)
- دعم CMS headless (Sanity, Contentful, Strapi)

## 📄 الترخيص

MIT — استخدمه، عدّله، وزّعه بحرّية.

النظام مستخلص من 3 مستودعات (مراخيصهم الأصلية محفوظة):
- [`open-design`](https://github.com/nexu-io/open-design) — Apache-2.0
- [`impeccable`](https://github.com/pbakaus/impeccable) — MIT
- [`gsap-animated-frontend`](https://github.com/yousefabdullah171/gsap-animated-frontend) — MIT

## 🙏 شكر خاص

- **Anthropic** — Claude Design الذي ألهم الـ open-design
- **Paul Bakaus** — مؤلف impeccable الذي علّمنا anti-AI-slop
- **nexu-io** — فريق open-design الذي جمع 70 سنة من craft
- **yousefabdullah171** — مؤلف gsap-animated-frontend

---

> **"الإبهار يأتي من القيود، لا من الحرّية المطلقة."**
> هذا النظام يجعل القيود صريحة، فيُنتج الإبهار تلقائياً.

---

## 📞 روابط

- 📦 **المستودع**: https://github.com/4zobir89-lab/design-master-agent
- 🐛 **Issues**: https://github.com/4zobir89-lab/design-master-agent/issues
- 💬 **Discussions**: https://github.com/4zobir89-lab/design-master-agent/discussions
- 📖 **دليل التثبيت**: [`INSTALL.md`](INSTALL.md)
- 🎨 **الثيمات**: [`references/themes.md`](references/themes.md)
- 🎬 **الوصفات**: [`references/animation-recipes.md`](references/animation-recipes.md)

## ⭐ إذا أعجبك النظام

اضغط ⭐ Star على المستودع — هذا يُساعد الآخرين على اكتشافه.

---

**صُنع بـ ❤️ لكل وكيل AI يستحق أن يكون مصمّماً محترفاً.**
