# Theme Library — 12 Ready-to-Use Themes

> مستوحى من `open-design/design-templates/html-ppt/assets/themes/` (36 ثيم)،
> مركّز إلى 12 ثيم عالي الجودة جاهز للّصق.
> كل ثيم = 15-25 سطر فقط يُعيد تعريف `:root`.

---

## كيف تستخدم

1. اختر theme واحداً من الـ 12
2. انسخ محتواه إلى `:root` في ملف CSS
3. استبدل القيم بأخرى تناسب العلامة إن أردت
4. كل theme يحترم: 80% neutral · 8% accent · 2% semantic

---

## 1. 🌑 Noir Cinema (Dark Cinematic)
**للأدب، الفن، السينما، التصوير الفوتوغرافي**

```css
:root {
  --bg: #0D0D0D;
  --bg-soft: #141414;
  --surface: #1A1A1A;
  --fg: #F4F0EA;
  --fg-muted: #8A8A8A;
  --border: rgba(244, 240, 234, 0.08);
  --border-strong: rgba(244, 240, 234, 0.16);
  --accent: #B58E63;
  --accent-2: #D9B98C;
  --accent-soft: rgba(181, 142, 99, 0.12);
  --font-display-ar: "Aref Ruqaa", "Amiri", serif;
  --font-body-ar: "Noto Naskh Arabic", serif;
  --font-mono-en: "JetBrains Mono", monospace;
}
[data-theme="light"] {
  --bg: #F4F0EA; --bg-soft: #EDE7DC; --surface: #FFFFFF;
  --fg: #0D0D0D; --fg-muted: #6B6B6B;
  --accent: #8B6B43; --accent-2: #B58E63;
  --border: rgba(13, 13, 13, 0.08); --border-strong: rgba(13, 13, 13, 0.16);
}
```

## 2. 📜 Paper Warm (Editorial Literary)
**للأدب، المدونات، المجلات، الكتابة التحريرية**

```css
:root {
  --bg: #F7F3ED;
  --bg-soft: #EFE9DD;
  --surface: #FFFFFF;
  --fg: #1A1612;
  --fg-muted: #6B6358;
  --border: rgba(26, 22, 18, 0.08);
  --border-strong: rgba(26, 22, 18, 0.16);
  --accent: #7C2D12;
  --accent-2: #9A3F1F;
  --accent-soft: rgba(124, 45, 18, 0.08);
  --font-display-ar: "Amiri", "Aref Ruqaa", serif;
  --font-body-ar: "Noto Naskh Arabic", serif;
  --font-display-en: "Cormorant Garamond", serif;
  --font-body-en: "EB Garamond", Georgia, serif;
}
```

## 3. 🔵 Swiss Grid (International Style)
**للشركات التقنية، SaaS B2B، المنتجات الجادة**

```css
:root {
  --bg: #FAFAFA;
  --bg-soft: #F0F0F0;
  --surface: #FFFFFF;
  --fg: #0A0A0A;
  --fg-muted: #6B6B6B;
  --border: rgba(10, 10, 10, 0.08);
  --border-strong: rgba(10, 10, 10, 0.16);
  --accent: #D6001C;  /* Swiss red */
  --accent-2: #FF1F3D;
  --accent-soft: rgba(214, 0, 28, 0.08);
  --radius: 0;
  --font-display-en: "Inter", sans-serif;  /* Product register OK */
  --font-body-en: "Inter", sans-serif;
  --font-mono-en: "JetBrains Mono", monospace;
}
```

## 4. 🌌 Aurora Tech (Cyberpunk Light)
**للـ dev tools، منصات AI، Web3**

```css
:root {
  --bg: #0A0E1A;
  --bg-soft: #131829;
  --surface: #1A1F35;
  --fg: #E8EBF5;
  --fg-muted: #7A8299;
  --border: rgba(232, 235, 245, 0.08);
  --border-strong: rgba(232, 235, 245, 0.16);
  --accent: #00D9FF;
  --accent-2: #4DEEEA;
  --accent-soft: rgba(0, 217, 255, 0.12);
  --font-display-en: "Space Grotesk", sans-serif;
  --font-body-en: "Inter", sans-serif;
  --font-mono-en: "JetBrains Mono", monospace;
}
```

## 5. 🍃 Forest Calm (Nature Wellness)
**للصحة، الطبيعة، الاستدامة، الـ wellness**

```css
:root {
  --bg: #F8FAF6;
  --bg-soft: #EEF2EA;
  --surface: #FFFFFF;
  --fg: #1A2818;
  --fg-muted: #5C6B58;
  --border: rgba(26, 40, 24, 0.08);
  --border-strong: rgba(26, 40, 24, 0.16);
  --accent: #3F6212;
  --accent-2: #65A30D;
  --accent-soft: rgba(63, 98, 18, 0.08);
  --font-display-en: "Fraunces", serif;
  --font-body-en: "Inter", sans-serif;
}
```

## 6. 🌅 Sunset Warm (Restaurant Lifestyle)
**للمطاعم، الفنادق، السفر، نمط الحياة**

```css
:root {
  --bg: #FDF8F2;
  --bg-soft: #F5EDE0;
  --surface: #FFFFFF;
  --fg: #2A1810;
  --fg-muted: #7A5C45;
  --border: rgba(42, 24, 16, 0.08);
  --border-strong: rgba(42, 24, 16, 0.16);
  --accent: #C2410C;
  --accent-2: #EA580C;
  --accent-soft: rgba(194, 65, 12, 0.08);
  --font-display-en: "Playfair Display", serif;  /* use sparingly */
  --font-body-en: "Inter", sans-serif;
}
```

## 7. ⚫ Brutalist Mono (Bold Statement)
**للـ portfolios التجريبية، الفن، الـ studios الجريئة**

```css
:root {
  --bg: #FFFFFF;
  --bg-soft: #F0F0F0;
  --surface: #FFFFFF;
  --fg: #000000;
  --fg-muted: #595959;
  --border: #000000;
  --border-strong: #000000;
  --accent: #FF3D00;  /* orange-red bolt */
  --accent-2: #FF6E40;
  --accent-soft: rgba(255, 61, 0, 0.08);
  --radius: 0;
  --font-display-en: "Space Grotesk", sans-serif;
  --font-body-en: "Space Mono", monospace;
}
```

## 8. 🌙 Midnight Luxury (Premium Dark)
**للفنادق الفاخرة، المجوهرات، الساعات، العقارات**

```css
:root {
  --bg: #0B0F1A;
  --bg-soft: #131829;
  --surface: #1A1F35;
  --fg: #F5E6CA;
  --fg-muted: #8A7F65;
  --border: rgba(245, 230, 202, 0.08);
  --border-strong: rgba(245, 230, 202, 0.16);
  --accent: #C9A876;
  --accent-2: #E5C896;
  --accent-soft: rgba(201, 168, 118, 0.12);
  --font-display-en: "Cormorant Garamond", serif;
  --font-body-en: "EB Garamond", serif;
  --font-mono-en: "JetBrains Mono", monospace;
}
```

## 9. 🍦 Soft Pastel (Friendly Products)
**للأطفال، التعليم، المنتجات اللطيفة، التطبيقات**

```css
:root {
  --bg: #FEFCF9;
  --bg-soft: #F9F4ED;
  --surface: #FFFFFF;
  --fg: #2D2418;
  --fg-muted: #7B6A52;
  --border: rgba(45, 36, 24, 0.08);
  --border-strong: rgba(45, 36, 24, 0.16);
  --accent: #F472B6;  /* soft pink */
  --accent-2: #FB7185;
  --accent-soft: rgba(244, 114, 182, 0.10);
  --radius: 16px;
  --font-display-en: "Fraunces", serif;
  --font-body-en: "Inter", sans-serif;
}
```

## 10. 🟤 Bauhaus Bold (Geometric)
**للـ design studios، الـ galleries، الفن الحديث**

```css
:root {
  --bg: #F5F1E8;
  --bg-soft: #EDE7D8;
  --surface: #FFFFFF;
  --fg: #1A1A1A;
  --fg-muted: #6B6B6B;
  --border: rgba(26, 26, 26, 0.08);
  --border-strong: rgba(26, 26, 26, 0.16);
  --accent: #E63946;  /* Bauhaus red */
  --accent-2: #F77F00;
  --accent-soft: rgba(230, 57, 70, 0.08);
  --radius: 0;
  --font-display-en: "Space Grotesk", sans-serif;
  --font-body-en: "Inter", sans-serif;
}
```

## 11. 💎 Glass Light (Modern Crisp)
**للـ SaaS، productivity apps، الـ dashboards**

```css
:root {
  --bg: #F8FAFC;
  --bg-soft: #F1F5F9;
  --surface: #FFFFFF;
  --fg: #0F172A;
  --fg-muted: #64748B;
  --border: rgba(15, 23, 42, 0.08);
  --border-strong: rgba(15, 23, 42, 0.16);
  --accent: #0EA5E9;  /* sky blue — not indigo */
  --accent-2: #38BDF8;
  --accent-soft: rgba(14, 165, 233, 0.08);
  --font-display-en: "Inter", sans-serif;
  --font-body-en: "Inter", sans-serif;
}
```

## 12. 🎭 Studio Editorial (Magazine)
**للمجلات، الـ publications، الصحف الرقمية**

```css
:root {
  --bg: #FFFEFC;
  --bg-soft: #F5F2EB;
  --surface: #FFFFFF;
  --fg: #0D0D0D;
  --fg-muted: #6B6B6B;
  --border: rgba(13, 13, 13, 0.08);
  --border-strong: rgba(13, 13, 13, 0.16);
  --accent: #1E40AF;  /* deep editorial blue */
  --accent-2: #3B82F6;
  --accent-soft: rgba(30, 64, 175, 0.06);
  --font-display-en: "Playfair Display", serif;
  --font-body-en: "EB Garamond", serif;
  --font-mono-en: "JetBrains Mono", monospace;
}
```

---

## How to Choose a Theme

| النوع / النبرة | الثيم المقترح |
|---|---|
| أدب / شعر / كتابة | Noir Cinema OR Paper Warm |
| مطعم / طعام / ضيافة | Sunset Warm |
| SaaS / dashboard | Swiss Grid OR Glass Light |
| تقنية / AI / dev tool | Aurora Tech |
| صحة / طبيعة / استدامة | Forest Calm |
| فاخر / مجوهرات / عقارات | Midnight Luxury |
| بورتفوليو تجريبي | Brutalist Mono OR Bauhaus Bold |
| أطفال / تعليم / لطيف | Soft Pastel |
| مجلة / صحيفة | Studio Editorial |
| شخصي راقٍ | Noir Cinema |

## Customization Rules

عند تخصيص ثيم:
1. ❌ لا تتجاوز 6 tokens للون (bg, surface, fg, fg-muted, accent, accent-2)
2. ❌ لا تضف accent ثالث — أعد التفكير
3. ✅ ابدأ من ثيم جاهز وعدّل
4. ✅ اختبر التباين: WCAG 4.5:1 للنص
5. ✅ اختبر الوضعين الداكن والفاتح (أو على الأقل الأنسب)
