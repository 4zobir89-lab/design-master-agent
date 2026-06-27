# Animation Recipes — 20+ GSAP Recipes

> مستخلص من `gsap-animated-frontend/references/animation-recipes.md` + `gsap-core-patterns.md`.
> وصفات جاهزة للّصق — انسخ وعدّل فقط.

---

## ⚙️ الإعداد الأساسي

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollToPlugin.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@studio-freight/lenis@1.0.42/dist/lenis.min.js"></script>
<script>
gsap.registerPlugin(ScrollTrigger, ScrollToPlugin);

const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
const isTouch = window.matchMedia("(hover: none)").matches;
const isMobile = window.innerWidth < 768;
</script>
```

---

## 🟢 Hero Recipes (3)

### 1. Text Reveal Hero
**الاستخدام**: عنوان hero — كلمة بكلمة بـ stagger.

```js
if (!reduceMotion) {
  const tl = gsap.timeline({ delay: 0.3, defaults: { ease: "expo.out" } });
  tl.from(".hero__meta > *", { opacity: 0, y: 20, stagger: 0.1, duration: 0.8 })
    .from(".hero__title-word", { opacity: 0, y: 80, stagger: 0.15, duration: 1.2 }, "-=0.4")
    .from(".hero__role", { opacity: 0, y: 30, duration: 1 }, "-=0.6")
    .from(".hero__cta > *", { opacity: 0, y: 20, stagger: 0.1, duration: 0.7 }, "-=0.5");
}
```

### 2. Cinematic Zoom Hero
**الاستخدام**: hero بخلفية صورة/فيديو — تكبير سينمائي.

```js
if (!reduceMotion) {
  const tl = gsap.timeline({ defaults: { ease: "power3.out" } });
  tl.from(".hero-bg", { scale: 1.3, duration: 2, ease: "power2.out" })
    .from(".hero-overlay", { opacity: 0, duration: 0.8 }, 0.3)
    .from(".hero-text", { y: 60, opacity: 0, duration: 1 }, 0.6);
}
```

### 3. Floating Shapes Background
**الاستخدام**: أشكال خلفية تطفو بلا نهاية.

```js
if (!reduceMotion) {
  shapes.forEach((shape, i) => {
    gsap.to(shape, {
      y: "random(-30, 30)", x: "random(-20, 20)",
      rotation: "random(-15, 15)",
      duration: "random(3, 6)", ease: "sine.inOut",
      repeat: -1, yoyo: true, delay: i * 0.3,
    });
  });
}
```

---

## 🟡 Card Recipes (3)

### 4. Staggered Card Reveal (with ScrollTrigger.batch)
**الاستخدام**: شبكة بطاقات — ScrollTrigger واحد بدل 50.

```js
if (!reduceMotion) {
  ScrollTrigger.batch(".card", {
    start: "top 88%",
    onEnter: (elements) => {
      gsap.from(elements, {
        opacity: 0, y: 60, scale: 0.96,
        stagger: 0.1, duration: 0.9, ease: "power3.out",
      });
    },
    once: true,
  });
}
```

### 5. Card Hover Lift Effect
**الاستخدام**: بطاقة ترتفع قليلاً عند hover.

```js
card.addEventListener("mouseenter", () => {
  gsap.to(card, { y: -8, boxShadow: "0 20px 40px rgba(0,0,0,0.3)", duration: 0.3 });
});
card.addEventListener("mouseleave", () => {
  gsap.to(card, { y: 0, boxShadow: "0 0 0 rgba(0,0,0,0)", duration: 0.3 });
});
```

### 6. 3D Card Tilt on Mouse Move
**الاستخدام**: بطاقة تميل تتبع الماوس (3D depth).

```js
card.addEventListener("mousemove", (e) => {
  const rect = card.getBoundingClientRect();
  const x = e.clientX - rect.left;
  const y = e.clientY - rect.top;
  const centerX = rect.width / 2;
  const centerY = rect.height / 2;
  const rotateX = ((y - centerY) / centerY) * -8;
  const rotateY = ((x - centerX) / centerX) * 8;
  gsap.to(card, { rotateX, rotateY, transformPerspective: 800, duration: 0.3 });
});
card.addEventListener("mouseleave", () => {
  gsap.to(card, { rotateX: 0, rotateY: 0, duration: 0.5 });
});
```

---

## 🔵 Number Recipes (2)

### 7. Count Up Numbers
**الاستخدام**: أرقام تتعدّ من 0 للقيمة عند scroll.

```js
const obj = { value: 0 };
gsap.to(obj, {
  value: target, duration: 2, ease: "power2.out",
  snap: { value: 1 },
  scrollTrigger: { trigger: counter, start: "top 80%", toggleActions: "play none none none" },
  onUpdate: () => { counter.textContent = obj.value.toLocaleString(); },
});
```

### 8. Stats Card with Trend Arrow
**الاستخدام**: بطاقة إحصائية مع سهم اتجاه.

```js
const tl = gsap.timeline({
  scrollTrigger: { trigger: ".stat-card", start: "top 80%" }
});
tl.from(".stat-num", { y: 30, opacity: 0, duration: 0.6 })
  .from(".stat-arrow", { scale: 0, opacity: 0, duration: 0.4, ease: "back.out(1.7)" }, "-=0.2")
  .from(".stat-label", { opacity: 0, duration: 0.4 }, "-=0.2");
```

---

## 🟣 Text Recipes (2)

### 9. Word-by-Word Reveal (No SplitText Plugin)
**الاستخدام**: نص يظهر كلمة بكلمة بلا plugin.

```jsx
// React
text.split(" ").map((word, i) => (
  <span key={i} className="split-word inline-block opacity-0 mr-[0.3em]">{word}</span>
))
// JS
gsap.to(".split-word", { opacity: 1, y: 0, stagger: 0.05, duration: 0.6, ease: "power2.out" });
```

### 10. Typewriter Effect
**الاستخدام**: نص يُكتب حرفاً حرفاً مع cursor يطرف.

```js
const text = "Hello, world.";
let i = 0;
const typeInterval = setInterval(() => {
  if (i < text.length) {
    target.textContent += text.charAt(i);
    i++;
  } else {
    clearInterval(typeInterval);
  }
}, 50);
```

---

## 🟠 Scroll Section Recipes (4)

### 11. Reveal on Scroll (الأكثر استخداماً)
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

### 12. Pinned Scene Transitions
**الاستخدام**: قسم مثبّت يتحرك عبر scenes.

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
  .from(".step-2", { opacity: 0, y: 50 })
  .to(".step-2", { opacity: 0 })
  .from(".step-3", { opacity: 0, y: 50 });
```

### 13. Horizontal Scroll
**الاستخدام**: panels تتحرك أفقياً مع scroll.

```js
gsap.to(panels, {
  xPercent: -100 * (panels.length - 1), ease: "none",
  scrollTrigger: {
    trigger: wrapperRef.current, pin: true, scrub: 1,
    snap: 1 / (panels.length - 1),
    end: () => "+=" + wrapperRef.current.offsetWidth,
  }
});
```

### 14. Background Color Transition on Scroll
**الاستخدام**: خلفية الصفحة تتغير لونها بين الأقسام.

```js
gsap.utils.toArray("[data-bg]").forEach((section) => {
  const bg = section.dataset.bg;
  ScrollTrigger.create({
    trigger: section,
    start: "top 50%", end: "bottom 50%",
    onEnter: () => gsap.to("body", { backgroundColor: bg, duration: 0.8 }),
    onEnterBack: () => gsap.to("body", { backgroundColor: bg, duration: 0.8 }),
  });
});
```

---

## 🟤 Navigation Recipes (2)

### 15. Navbar Shrink on Scroll
```js
ScrollTrigger.create({
  start: "top -80", end: 99999,
  onToggle: (self) => nav.classList.toggle("is-scrolled", self.isActive),
});

// Hide on scroll down, show on scroll up
let lastScroll = 0;
ScrollTrigger.create({
  start: 0, end: 99999,
  onUpdate: (self) => {
    const dir = self.direction;
    if (dir === 1 && self.scroll() > 200) {
      gsap.to(nav, { y: -100, duration: 0.3 });
    } else {
      gsap.to(nav, { y: 0, duration: 0.3 });
    }
  },
});
```

### 16. Mobile Menu Reveal
```js
const tl = gsap.timeline({ paused: true });
tl.from(".mobile-menu", { xPercent: 100, duration: 0.4, ease: "power3.out" })
  .from(".mobile-menu li", { x: 30, opacity: 0, stagger: 0.08, duration: 0.3 }, "-=0.2");

menuBtn.addEventListener("click", () => tl.play());
closeBtn.addEventListener("click", () => tl.reverse());
```

---

## 🟢 Special Effects (4)

### 17. Magnetic Button (مع gsap.quickTo)
```js
if (!isTouch && !isMobile) {
  document.querySelectorAll("[data-magnetic]").forEach((btn) => {
    const xTo = gsap.quickTo(btn, "x", { duration: 0.4, ease: "power3.out" });
    const yTo = gsap.quickTo(btn, "y", { duration: 0.4, ease: "power3.out" });
    btn.addEventListener("mousemove", (e) => {
      const rect = btn.getBoundingClientRect();
      const x = e.clientX - rect.left - rect.width / 2;
      const y = e.clientY - rect.top - rect.height / 2;
      xTo(x * 0.3);  // 0.3 = magnetic strength
      yTo(y * 0.3);
    });
    btn.addEventListener("mouseleave", () => { xTo(0); yTo(0); });
  });
}
```

### 18. Custom Cursor (Dual-Speed)
```js
if (!isTouch && !isMobile) {
  const cursor = document.getElementById("cursor");
  const dot = document.getElementById("cursor-dot");
  const xTo = gsap.quickTo(cursor, "x", { duration: 0.5, ease: "power3.out" });
  const yTo = gsap.quickTo(cursor, "y", { duration: 0.5, ease: "power3.out" });
  const xToDot = gsap.quickTo(dot, "x", { duration: 0.1, ease: "power3.out" });
  const yToDot = gsap.quickTo(dot, "y", { duration: 0.1, ease: "power3.out" });

  window.addEventListener("mousemove", (e) => {
    xTo(e.clientX); yTo(e.clientY);
    xToDot(e.clientX); yToDot(e.clientY);
  });

  // Hover effect on interactive elements
  document.querySelectorAll("a, button, [data-magnetic]").forEach((el) => {
    el.addEventListener("mouseenter", () => cursor.classList.add("is-hovering"));
    el.addEventListener("mouseleave", () => cursor.classList.remove("is-hovering"));
  });
}
```

### 19. Reveal Mask (Clip-Path)
```js
gsap.from(".masked-image", {
  clipPath: "inset(100% 0 0 0)",  // hidden from bottom
  duration: 1.2, ease: "power3.inOut",
});
```

### 20. SVG Line Draw
```js
const length = path.getTotalLength();
gsap.set(path, { strokeDasharray: length, strokeDashoffset: length });
gsap.to(path, {
  strokeDashoffset: 0, duration: 2, ease: "power2.inOut",
  scrollTrigger: { trigger: path, start: "top 80%" },
});
```

---

## 🟦 Page Utilities (3)

### 21. Smooth Scroll (Lenis Integration)
```js
let lenis = null;
if (!reduceMotion && !isTouch && window.Lenis) {
  lenis = new Lenis({
    duration: 1.2,
    easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
    smoothWheel: true, smoothTouch: false,
  });
  lenis.on("scroll", ScrollTrigger.update);
  gsap.ticker.add((time) => lenis.raf(time * 1000));
  gsap.ticker.lagSmoothing(0);
}
```

### 22. Page Transition (Next.js App Router)
```tsx
function PageTransition({ children }) {
  const ref = useRef(null);
  useEffect(() => {
    gsap.fromTo(ref.current,
      { opacity: 0, y: 20 },
      { opacity: 1, y: 0, duration: 0.5, ease: "power2.out" }
    );
  }, []);
  return <div ref={ref}>{children}</div>;
}
```

### 23. Progress Bar (Scroll-Linked)
```js
ScrollTrigger.create({
  trigger: document.body, start: "top top", end: "bottom bottom",
  onUpdate: (self) => {
    gsap.to(".progress-bar", { scaleX: self.progress, duration: 0.1, overwrite: true });
  },
});
```

---

## 🎯 Position Parameters (Advanced)

```js
const tl = gsap.timeline({ defaults: { duration: 0.6 } });
tl.from(".title", { y: 40 })
  .from(".subtitle", { y: 30 }, "-=0.3")  // 0.3s overlap with previous
  .from(".cta", { scale: 0.8 }, "<")       // same start as previous
  .from(".badge", { x: -20 }, "<0.2");     // 0.2s after previous starts

// Position markers:
// "-=0.3" → 0.3s before previous ends (overlap)
// "+=0.5" → 0.5s after previous ends (gap)
// "<"     → same start as previous tween
// "<0.2"  → 0.2s after previous starts
// 2       → absolute 2s from timeline start
```

---

## 🎯 Easing Reference

| Easing | الاستخدام |
|---|---|
| `power1.out` | gentle fade |
| `power2.out` | standard ease-out |
| `power3.out` | dramatic ease-out (90% of reveals) |
| `power4.out` | very dramatic |
| `back.out(1.4)` | slight overshoot (CTAs only) |
| `back.out(1.7)` | more overshoot (rare) |
| `elastic.out(1, 0.3)` | spring/bounce (avoid in luxury) |
| `expo.out` | Apple-style premium entrance |
| `sine.inOut` | ambient/looping animations |
| `"none"` | scrub/linear scroll-linked |

> **القاعدة الذهبية**: استخدم `.out` 90% من الوقت (عناصر تصل). استخدم `.inOut` للانتقالات بين الحالات. نادراً `.in` وحدها.
