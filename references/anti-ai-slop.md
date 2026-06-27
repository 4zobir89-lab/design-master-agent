# Anti-AI-Slop Rules — The 7 Cardinal Sins

> مستخلص من `open-design/craft/anti-ai-slop.md` + `impeccable/SKILL.src.md`.
> هذه القواعد **P0** — فشل أي منها = إعادة بناء.

---

## السبع الخطايا الكاردينالية (P0 — Must Pass)

### 1. ❌ Tailwind Indigo كلون مميز

**البصمة الأشهر للـ AI**. ممنوع تماماً:

```css
/* FORBIDDEN */
--accent: #6366f1;   /* indigo-500 */
--accent: #4f46e5;   /* indigo-600 */
--accent: #4338ca;   /* indigo-700 */
--accent: #3730a3;   /* indigo-800 */
--accent: #8b5cf6;   /* violet-500 */
--accent: #7c3aed;   /* violet-600 */
--accent: #a855f7;   /* purple-500 */
```

**العلاج**: اختر accent ذا شخصية:
- Luxury → brass/gold (#B58E63, #C9A876)
- Tech → cyan/electric (#06B6D4, #00D9FF)
- Editorial → ink/deep-red (#7C2D12, #1E1B4B but with warm tint)
- Nature → moss/forest (#3F6212, #166534)
- Sunset → coral/amber (#EA580C, #D97706)

### 2. ❌ تدرّج ثنائي اللون على الـ Hero

```css
/* FORBIDDEN — AI slop signature */
background: linear-gradient(135deg, #8b5cf6, #3b82f6);
background: linear-gradient(135deg, #6366f1, #ec4899);
background: linear-gradient(135deg, #06b6d4, #3b82f6);
```

**العلاج**: سطح مسطح + نوع مقصود يتفوق دائماً. أو إن أردت تدرّجاً:
- تدرّج أحادي اللون (lightness فقط)
- تدرّج ذو معنى وظيفي (يفرّق هرميات لا يزين فراغاً)

### 3. ❌ الإيموجي كأيقونات مميزة

```html
<!-- FORBIDDEN -->
<h2>🚀 Quick Start</h2>
<button>✨ Get Started</button>
<li>🎯 Feature one</li>
```

**العلاج**: SVG monoline بسماكة 1.6-1.8px مع `currentColor`:

```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">
  <path d="M5 12h14M12 5l7 7-7 7"/>
</svg>
```

### 4. ❌ Sans-serif على العنوان عندما الـ seed خط serif

```css
/* FORBIDDEN — typeface mismatch */
:root { --font-display: "Playfair Display", serif; }
h1 { font-family: "Inter", sans-serif; }  /* ← AI default */
```

**العلاج**: h1/h2 دائماً `var(--font-display)`. الـ body وحده sans-serif إن أردت.

### 5. ❌ بطاقة مستديرة بحدود يسرى ملوّنة

```css
/* FORBIDDEN — "AI dashboard tile" */
.card {
  border-radius: 16px;
  border-left: 4px solid var(--accent);
  background: white;
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
```

**العلاج**: أسقط إما الزاوية (border-radius: 0 or 4px) أو الحد الأيسر.

### 6. ❌ أرقام مُختلقة

```html
<!-- FORBIDDEN -->
<div class="stat">
  <span class="number">10×</span>
  <span class="label">Faster than competitors</span>
</div>
<div class="stat">
  <span class="number">99.9%</span>
  <span class="label">Uptime</span>
</div>
```

**العلاج**: 
- إن لم يوجد مصدر حقيقي → لا تستخدم أرقاماً
- أو استخدم placeholder مُعلَّم: `<span class="number ph-num">[TBD]</span>`
- أو استخدم نصاً نوعياً: "أسرع بكثير" بدل "10× faster"

### 7. ❌ نص حشو (Filler Copy)

```html
<!-- FORBIDDEN -->
<p>Lorem ipsum dolor sit amet...</p>
<ul>
  <li>Feature one — description</li>
  <li>Feature two — description</li>
  <li>Feature three — description</li>
</ul>
```

**العلاج**:
- لا تكتب قسماً فارغاً — التكوين أفضل من اختلاق كلمات
- اكتب نصاً حقيقياً خاصاً بالمنتج، أو اترك القسم

---

## إشارات لطيفة (P1 — Should Pass)

### 8. تسلسل "Hero → Features → Pricing → FAQ → CTA" بلا تباين
لا تتبع الـ template الافتراضي للـ SaaS. اختر ترتيباً يخدم القصة.

### 9. CDN صور placeholder خارجية (unsplash, placehold.co)
استخدم فئة `.ph-img` أو SVG placeholders محلية.

### 10. أكثر من ~12 قيمة hex خارج `:root`
كل لون يجب أن يمرّ عبر token.

### 11. `var(--accent)` مستخدم 6+ مرات في الصفحة
سقف 2 استخدامات ظاهرة لكل شاشة.

---

## وصفة "الروح" (The Soul Recipe)

> **"Aim for ~80% proven patterns + ~20% distinctive choice."**

الـ 20% تعيش في:

1. **حركة بصرية جريئة واحدة** — انتقال غير متوقع، حركة نص مبتكرة
2. **microcopy دقيق** — "Start tracking" بدل "Get started"
3. **تفاعل دقيق واحد** — شيء يتذكره المستخدم (hover effect, magnetic, sound)
4. **تفصيلة مستخدم-منتج** — تلميح `kbd`، شارة حالة بعبارة خاصة بالمنتج، مرجع داخلي

> **"If a reviewer screenshots the artifact and someone outside the project can identify which product it's from — you have soul. If not, you shipped a template."**

---

## اختبار الثواني الثلاث

قبل التسليم، انظر للموقع 3 ثوانٍ ثم اسأل:

1. هل يبدو كأي موقع AI startup؟ → إن نعم، أعد البناء
2. هل أستطيع تخمين الـ category وحدها؟ → إن نعم، trap one tier deeper
3. هل أستطيع تخمين الـ aesthetic family من category+anti-references؟ → إن نعم، فشل
4. هل يبدو كـ Linear/Vercel/Cursor ripoff؟ → إن نعم، أعد البناء
5. هل يحتوي على "feature row" (icon + heading + 3 lines vague benefit)؟ → أزل

---

## Absolute Bans (من impeccable — match-and-refuse)

- Side-stripe borders (الخطأ #5 أعلاه)
- Gradient text (`background-clip: text` + gradient)
- Glassmorphism كافتراضي
- Hero-metric template (رقم كبير + label + supporting stats)
- Identical card grids
- Eyebrow على كل قسم
- Numbered section markers (01/02/03) كـ scaffolding وحده
- Text overflow (clip دائماً)

## Reflex-Reject Fonts (لا تستخدمها كافتراضي)

```
Fraunces · Newsreader · Lora · Crimson (any) · Playfair Display ·
Cormorant (any) · Syne · IBM Plex (any) · Space Mono · Space Grotesk ·
Inter (as default — OK in Product register only) ·
DM Sans · DM Serif (any) · Outfit · Plus Jakarta Sans ·
Instrument Sans · Instrument Serif
```

**بدائل مسموحة**:
- Display: Aref Ruqaa, Amiri (Arabic), Cormorant Garamond, EB Garamond, Fraunces (use sparingly)
- Body: Noto Naskh Arabic, Reem Kufi (Arabic), EB Garamond, Georgia
- Mono: JetBrains Mono, IBM Plex Mono (only for code, not display)
