# 📚 Examples

أمثلة لمواقع مولّدة بواسطة نظام design-master.

## قائمة الأمثلة

| المثال | الطلب | الـ Theme | الحالة |
|---|---|---|---|
| `personal-poet/` | "موقع شخصي لشاعر عربي معاصر، سينمائي" | Noir Cinema | ✅ Available |
| `saas-ai-landing/` | "صفحة هبوط SaaS لشركة AI" | Aurora Tech | 🔜 Coming soon |
| `coffee-shop/` | "موقع متجر قهوة مختصة، فاخر" | Midnight Luxury | 🔜 Coming soon |
| `restaurant-japanese/` | "موقع مطعم ياباني فاخر، دافئ" | Sunset Warm | 🔜 Coming soon |
| `dev-portfolio/` | "بورتفوليو مطور، تقني وعصري" | Aurora Tech | 🔜 Coming soon |
| `nonprofit-ngo/` | "موقع جمعية خيرية، إنساني" | Paper Warm | 🔜 Coming soon |

## كيف تضيف مثالاً

1. أنشئ مجلداً باسم وصفي: `examples/your-example-name/`
2. ضع الملفات التالية:
   - `index.html` — الموقع المولّد
   - `PRODUCT.md` — عقد المنتج
   - `DESIGN.md` — نظام التصميم
   - `.design/discovery.md` — نتيجة Phase 0
   - `.design/plan.md` — الخطة
   - `.design/audit.md` — تقرير الفحص
   - `README.md` — وصف المثال والطلب الأصلي
3. تأكد أن الموقع يجتاز `audit.py` (P0 = 21/21)
4. افتح PR

## مثال على README للمثال

```markdown
# Example: Personal Poet Website

## Original Request
"أريد موقع شخصي لشاعر عربي معاصر، يكون سينمائي وراقٍ"

## Discovery Output
- Archetype: portfolio
- Register: brand
- Tone: noir-cinema
- Theme: Noir Cinema (Dark Cinematic)
- Sections: 8 (hero, manifesto, works, lab, quotes, timeline, articles, contact)

## Audit Result
- P0: 21/21 ✅
- P1: 11/12 ✅
- P2: 8/8 ✅

## Files
- index.html (78 KB)
- PRODUCT.md
- DESIGN.md
- .design/ artifacts
```

## اختبر بنفسك

```bash
# استنساخ المستودع
git clone https://github.com/4zobir89-lab/design-master-agent.git
cd design-master-agent

# فحص أي مثال
python scripts/audit.py examples/personal-poet
```
