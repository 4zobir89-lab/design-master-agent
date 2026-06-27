# Craft Rules — 36 Golden Rules

> مستخلص من `open-design/craft/` (10 ملفات) + `impeccable/SKILL.src.md`.
> مرجع مركّز للقواعد الكونية لأناقة التصميم.

---

## الطباعة (Typography) — 6 قواعد

### 1. ALL CAPS دائماً يحتاج `letter-spacing ≥ 0.06em`
```css
.eyebrow { letter-spacing: 0.18em; text-transform: uppercase; }  /* ✅ */
.label   { letter-spacing: 0.08em; text-transform: uppercase; }  /* ✅ */
.bad     { text-transform: uppercase; }                          /* ❌ cramped */
```

### 2. Display ≥ 48px يحتاج tracking سالب
```css
.display { letter-spacing: -0.02em; }   /* 48-72px */
.hero    { letter-spacing: -0.03em; }   /* 96px+ */
```

### 3. لا `letter-spacing` على نص عربي (يكسر الانضمام)
```css
.display-ar { letter-spacing: 0; }              /* ✅ */
.display-ar { letter-spacing: -0.02em; }        /* ❌ breaks joining */
```

### 4. 3 أوزان فقط ظاهرة
- Read: 400 (regular) أو 450
- Emphasize: 500 (medium) أو 550
- Announce: 600 (semibold) — نادراً
- لا 700+ إلا للشعارات

### 5. `max-width: 65ch` لجسم النص
```css
.prose { max-width: 65ch; }  /* 50-75 chars per line */
```

### 6. لا `text-align: justify` للجسم (يصنع أنهاراً)

---

## الهرمية (Hierarchy) — 4 قواعد

### 7. نقطة دخول مهيمنة واحدة فقط لكل منطقة بصرية
لا تتنافس العناصر. واحد فقط primary.

### 8. فعّل متجهين على الأقل للعنصر المهيمن
5 متجهات: scale, weight, spacing, tracking, alignment.

### 9. لا "graduated weight ladder" (regular→medium→semibold→bold→extrabold)
الوزن يقفز لا يتنقل. 400 → 600، لا 400 → 500 → 600.

### 10. لا uniform section spacing — اكسر الإيقاع
dense → spacious → medium. التماثل = template.

---

## اللون (Color) — 5 قواعد

### 11. 80% محايد، 8% accent، 2% semantic
```css
/* distribution by pixels */
80% --bg, --surface, --fg, --muted
8%  --accent
2%  --success, --warn, --danger
<1% gradients, glows
```

### 12. `var(--accent)` ≤ 2 استخدامات ظاهرة بالشاشة
زوج نموذجي: eyebrow/chip + CTA. الروابط تحسب accent — أخفضها للـ --fg underline إن كان لديك CTA.

### 13. تسمية دلالية لا لونية
```css
--accent: #2f6feb;   /* ✅ */
--blue-500: #2f6feb; /* ❌ locks you out of theming */
```

### 14. لا أسود/أبيض نقي
```css
--bg:        #0f0f0f;   /* ✅ not #000 */
--fg:        #f0f0f0;   /* ✅ not #fff */
--bg-dark:   #000;      /* ❌ */
--fg-light:  #fff;      /* ❌ */
```

### 15. حدود شفافة شبه بيضاء/سوداء
```css
--border: rgba(255, 255, 255, 0.08);  /* dark theme */
--border: rgba(0, 0, 0, 0.08);         /* light theme */
```

---

## الحركة (Motion) — 5 قواعد

### 16. 150ms افتراضي للحالات
```js
{ duration: 0.15, ease: "power2.out" }   /* hover, focus */
{ duration: 0.3, ease: "power2.out" }    /* state confirm */
{ duration: 0.7-0.9, ease: "power3.out" } /* scroll reveal */
{ duration: 1.2-1.8, ease: "expo.out" }  /* hero entrance */
```

### 17. حرك فقط لإعادة توجيه
- ✅ انتقال صفحات، تمدد حاويات، مؤشرات تقدم، reveal على scroll
- ❌ تعليم نظام معقد، تزيين، إشارة "premium"

### 18. curve للـ opacity/color، spring للـ position/scale
```js
opacity:    { ease: "power2.out" }  /* between two known points */
x, y:       { ease: "power3.out" }  /* or spring for physical feel */
```

### 19. `prefers-reduced-motion` إجباري
```js
const mm = gsap.matchMedia();
mm.add("(prefers-reduced-motion: reduce)", () => {
  gsap.set("*", { clearProps: "all" });
  ScrollTrigger.getAll().forEach(t => t.kill());
});
```

### 20. لا View Transitions API بدون override explicit
الـ API لا يطبّق reduced-motion تلقائياً.

---

## الوصول (Accessibility) — 6 قواعد

### 21. WCAG 2.2 AA كسقف عمل

### 22. تباين 4.5:1 للنص العادي، 3:1 للكبير

### 23. touch target ≥ 24×24 CSS px (AA)، 44×44 (AAA)

### 24. `:focus-visible` دائماً
```css
:focus-visible { outline: 2px solid var(--accent); outline-offset: 4px; }
/* لا outline: none بدون هذا البديل */
```

### 25. `<button>` و `<a href>` فقط — لا `<div role="button">`

### 26. `<label for>` + `aria-describedby` + `aria-invalid` للحقول
```html
<label for="email">Email</label>
<input id="email" type="email" required
       aria-describedby="email-hint email-error"
       aria-invalid="true">
<span id="email-error" role="alert">Email must include @.</span>
```

---

## RTL/Bidi — 4 قواعد

### 27. logical properties أولاً
```css
margin-inline-start;   /* لا margin-left */
padding-inline-end;    /* لا padding-right */
text-align: start;     /* لا text-align: left */
inset-inline-start;    /* لا left */
border-start-start-radius;  /* لا border-top-left-radius */
```

### 28. `<html dir="rtl" lang="ar">` للصفحة العربية الكاملة

### 29. `dir="ltr"` إجباري على حقول intrinsically-LTR
email, URL, phone, IBAN, credit-card.

### 30. خط الجسم العربي 14-18px مع `line-height: 1.5-1.75`
لافتراضات اللاتيني ضيقة جداً على harakat.

---

## الحالات (State Coverage) — 4 قواعد

### 31. 5 حالات لكل سطح بيانات
loading (skeleton + timeout 15s) · empty (headline + CTA) · error (3 questions) · populated · edge (نصوص طويلة/RTL).

### 32. تحقق على blur، لا على keystroke
```js
input.addEventListener("blur", validate);  /* ✅ */
input.addEventListener("input", validate); /* ❌ too early */
```

### 33. أخطاء تكيفية (4-7 رسائل لكل حقل معقد)
```js
// ❌ generic
"Invalid email"
// ✅ specific
"Email needs @ and a domain"
"Did you mean .com instead of .co?"
"This looks like a phone number, not an email"
```

### 34. ملخص الأخطاء في الأعلى على submit فقط
```html
<div tabindex="-1" role="group" aria-label="Form errors">
  <h2>2 problems found</h2>
  <ul>...</ul>
</div>
```

---

## الأداء (Performance) — 2 قواعد

### 35. animate فقط `transform` و `opacity` (GPU)
```js
gsap.to(el, { x: 100, opacity: 0.5 });          /* ✅ */
gsap.to(el, { width: 200, height: 100 });        /* ❌ triggers reflow */
gsap.to(el, { top: 50, left: 50 });              /* ❌ triggers reflow */
gsap.to(el, { fontSize: 24 });                   /* ❌ triggers reflow */
```

### 36. < 20 ScrollTrigger نشط لكل صفحة
- استخدم `ScrollTrigger.batch()` للـ grids (ScrollTrigger واحد بدل 50)
- استخدم `once: true` للعناصر التي تُحرّك مرة واحدة
- اقتل ScrollTriggers للأقسام خارج الشاشة في SPAs
