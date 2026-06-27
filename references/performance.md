# Performance Guide — 10 Golden Rules

> مستخلص من `gsap-animated-frontend/references/performance-guide.md`.

## 1. ✅ animate فقط `transform` و `opacity` (GPU-accelerated)

```js
// ALWAYS — GPU-accelerated
gsap.to(el, { x, y, scale, rotation, opacity });

// NEVER — triggers layout reflow
gsap.to(el, { width, height, top, left, margin, padding, fontSize, lineHeight });
```

## 2. ✅ `will-change` بإحكام
```css
.will-animate-on-hover:hover { will-change: transform, opacity; }
/* لا تضف will-change globally — GSAP يضيفها تلقائياً */
```

## 3. ✅ `ScrollTrigger.batch()` للـ grids
```js
// BAD — 50 individual ScrollTriggers
cards.forEach(card => gsap.from(card, { scrollTrigger: { trigger: card, ... } }));

// GOOD — 1 batched ScrollTrigger
ScrollTrigger.batch(".card", { onEnter: (els) => gsap.from(els, { ... }) });
```

## 4. ✅ < 20 ScrollTrigger نشط لكل صفحة
- `once: true` للعناصر التي تُحرّك مرة واحدة
- اقتل ScrollTriggers للأقسام خارج الشاشة في SPAs

## 5. ✅ Mobile downgrade
1. ❌ No parallax on touch
2. ❌ No pinned sections
3. ✅ Reduce stagger counts
4. ✅ Shorter durations
5. ❌ No custom cursor
6. ❌ Avoid `scrub`

## 6. ✅ `prefers-reduced-motion` إجباري
```js
const mm = gsap.matchMedia();
mm.add("(prefers-reduced-motion: reduce)", () => {
  gsap.set(".animated", { clearProps: "all" });
  ScrollTrigger.getAll().forEach(t => t.kill());
});
```

## 7. ✅ منع FOUC
```css
.animate-in { opacity: 0; transform: translateY(30px); }
.js-loaded .animate-in { /* GSAP will handle */ }
@media (prefers-reduced-motion: reduce) {
  .animate-in { opacity: 1 !important; transform: none !important; }
}
```

## 8. ✅ استراتيجية التحميل
- **Above the fold**: animate على page load (بدون ScrollTrigger)
- **Below the fold**: animate على scroll
- **Heavy animations**: lazy-load عند `start: "top 200%"` (2 viewports away)

## 9. ✅ Bundle size
```
gsap core     ~24 KB
ScrollTrigger ~10 KB
@gsap/react   ~2 KB
Lenis         ~5 KB
─────────────────────
Total typical ~41 KB
```
Tree-shake unused plugins (لا تستورد Draggable/Flip إن لم تُستخدم).

## 10. ✅ Performance Checklist
```
[ ] Only animate `transform` and `opacity`
[ ] Use `ScrollTrigger.batch()` for repeated elements
[ ] < 20 active ScrollTriggers per page
[ ] Mobile: no parallax, no pinning, simplified animations
[ ] `prefers-reduced-motion` respected
[ ] CSS initial states prevent FOUC
[ ] Above-fold animates on load, below-fold on scroll
[ ] Unused GSAP plugins not imported
[ ] `ScrollTrigger.refresh()` called after dynamic content
[ ] Animations cleaned up on component unmount
```

## Core Web Vitals Targets
- **LCP** < 2.2s
- **CLS** < 0.03
- **INP** < 150ms
- **Lighthouse** 95+
