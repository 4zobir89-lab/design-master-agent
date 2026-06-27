# ScrollTrigger Patterns — 10 Essential

> مستخلص من `gsap-animated-frontend/references/scroll-trigger-patterns.md`.

## toggleActions Reference
```
"onEnter onLeave onEnterBack onLeaveBack"
```
- Play once: `"play none none none"` ✅ recommended
- Play/reverse: `"play reverse play reverse"`
- Restart: `"restart none none none"`

## start/end Reference
| Value | Meaning |
|---|---|
| `"top top"` | Element top meets viewport top |
| `"top 80%"` | Element top at 80% down viewport (common reveal) |
| `"center center"` | Element center meets viewport center |
| `"top bottom"` | Element top meets viewport bottom (just entering) |
| `"+=2000"` | 2000px of scroll distance (for end with pin) |

## scrub Values
- `true` → instant (1:1 with scroll)
- `1` → 1s smoothing ✅ recommended
- `2` → very floaty

---

## 1. Reveal on Scroll (Most Common)
```js
gsap.from(".section-content", {
  opacity: 0, y: 50, duration: 0.8, ease: "power2.out",
  scrollTrigger: {
    trigger: ".section-content",
    start: "top 80%",
    toggleActions: "play none none none",
  },
});
```

## 2. Scrub (Scroll-Linked Progress)
```js
gsap.to(".parallax-bg", {
  y: -200, ease: "none",
  scrollTrigger: {
    trigger: ".parallax-section",
    start: "top bottom", end: "bottom top",
    scrub: 1,
  },
});
```

## 3. Pin Section
```js
const tl = gsap.timeline({
  scrollTrigger: {
    trigger: ".pinned-section",
    start: "top top", end: "+=2000",
    pin: true, scrub: 1,
  }
});
tl.from(".step-1", { opacity: 0, y: 50 })
  .to(".step-1", { opacity: 0 })
  .from(".step-2", { opacity: 0, y: 50 });
```

## 4. Horizontal Scroll
```js
gsap.to(panels, {
  xPercent: -100 * (panels.length - 1), ease: "none",
  scrollTrigger: {
    trigger: wrapper, pin: true, scrub: 1,
    snap: 1 / (panels.length - 1),
    end: () => "+=" + wrapper.offsetWidth,
  }
});
```

## 5. ScrollTrigger.batch (for grids — performance!)
```js
ScrollTrigger.batch(".card", {
  onEnter: (elements) => {
    gsap.from(elements, { opacity: 0, y: 40, stagger: 0.08, duration: 0.5 });
  },
  start: "top 85%",
});
```

## 6. Parallax Layers (3 layers, different speeds)
```js
gsap.to(".bg-layer", { y: -100, scrollTrigger: { trigger: ".parallax-section", scrub: 1 } });
gsap.to(".mid-layer", { y: -200, scrollTrigger: { ... } });
gsap.to(".fg-layer", { y: -400, scrollTrigger: { ... } });
```

## 7. Progress-Linked (progress bar)
```js
ScrollTrigger.create({
  trigger: ".article", start: "top top", end: "bottom bottom",
  onUpdate: (self) => {
    gsap.set(".progress-bar", { scaleX: self.progress });
  }
});
```

## 8. Class Toggle
```js
ScrollTrigger.create({
  trigger: ".section", start: "top center", end: "bottom center",
  toggleClass: { targets: ".nav-link", className: "active" },
});
```

## 9. Responsive with matchMedia
```js
const mm = gsap.matchMedia();
mm.add({
  isDesktop: "(min-width: 1024px)",
  isTablet: "(min-width: 768px) and (max-width: 1023px)",
  isMobile: "(max-width: 767px)",
  reducedMotion: "(prefers-reduced-motion: reduce)",
}, (context) => {
  const { isDesktop, isMobile, reducedMotion } = context.conditions;
  if (reducedMotion) return;
  if (isDesktop) { /* Full parallax + pinning */ }
  if (isMobile) { /* Simple fade-in only */ }
});
```

## 10. Dynamic Content (with ScrollTrigger.refresh)
```js
useGSAP(() => {
  if (!data) return;
  requestAnimationFrame(() => {
    ScrollTrigger.refresh();
    ScrollTrigger.batch(".dynamic-card", { ... });
  });
}, { dependencies: [data] });
```

---

## Mobile Rules (CRITICAL)
- ❌ No parallax on touch (janky with touch scrolling)
- ❌ No pinned sections (confuses touch scroll)
- ❌ No `scrub` (touch momentum makes scrub feel laggy)
- ✅ Shorter durations (mobile users are impatient)
- ✅ Reduce stagger counts (fewer items visible)
