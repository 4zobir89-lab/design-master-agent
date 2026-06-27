# 📦 INSTALL.md — دليل التثبيت الكامل

دليل تفصيلي لتثبيت نظام design-master على كل منصة وكيل AI.

---

## 🚀 التثبيت السريع (سكريبت آلي)

```bash
# Claude Code
curl -fsSL https://raw.githubusercontent.com/4zobir89-lab/design-master-agent/main/scripts/install.sh | bash -s -- --target claude

# Cursor
curl -fsSL https://raw.githubusercontent.com/4zobir89-lab/design-master-agent/main/scripts/install.sh | bash -s -- --target cursor

# Codex CLI
curl -fsSL https://raw.githubusercontent.com/4zobir89-lab/design-master-agent/main/scripts/install.sh | bash -s -- --target codex

# Gemini CLI
curl -fsSL https://raw.githubusercontent.com/4zobir89-lab/design-master-agent/main/scripts/install.sh | bash -s -- --target gemini

# الكل
curl -fsSL https://raw.githubusercontent.com/4zobir89-lab/design-master-agent/main/scripts/install.sh | bash -s -- --target all
```

---

## 📋 التثبيت اليدوي لكل منصة

### 1. Claude Code

#### المتطلبات
- Claude Code CLI مُثبّت ([التثبيت](https://claude.com/claude-code))
- Python 3.9+ (لـ `audit.py` و `discover.py`)
- git

#### الخطوات

```bash
# 1. استنساخ المستودع
git clone https://github.com/4zobir89-lab/design-master-agent.git

# 2. نسخ إلى skills directory
mkdir -p ~/.claude/skills
cp -r design-master-agent ~/.claude/skills/design-master

# 3. جعل السكريبتات قابلة للتنفيذ
chmod +x ~/.claude/skills/design-master/scripts/*.py
chmod +x ~/.claude/skills/design-master/scripts/install.sh

# 4. التحقق
ls ~/.claude/skills/design-master/
# يجب أن ترى: AGENTS.md SKILL.md references/ scripts/ seeds/ templates/
```

#### التفعيل
في أي محادثة Claude Code، قل:
```
Use the design-master skill to build me a website for X
```

أو بشكل صريح:
```
اقرأ ~/.claude/skills/design-master/AGENTS.md واطبّق منهجية design-master
لبناء موقع لـ X
```

---

### 2. Cursor

#### المتطلبات
- Cursor IDE مُثبّت ([التثبيت](https://cursor.com))
- Python 3.9+
- git

#### الخطوات

```bash
# 1. استنساخ
git clone https://github.com/4zobir89-lab/design-master-agent.git

# 2. نسخ إلى Cursor skills directory
mkdir -p ~/.cursor/skills
cp -r design-master-agent ~/.cursor/skills/design-master

# 3. الصلاحيات
chmod +x ~/.cursor/skills/design-master/scripts/*.py
```

#### التفعيل في Cursor
1. افتح Cursor Settings → AI → Skills
2. اضغط "Add Skill"
3. اختر المسار: `~/.cursor/skills/design-master`
4. فعّل الـ skill

أو في الـ chat:
```
@design-master build me a website for X
```

---

### 3. Codex CLI (OpenAI)

#### المتطلبات
- Codex CLI مُثبّت ([التثبيت](https://developers.openai.com/codex))
- Python 3.9+
- git

#### الخطوات

```bash
git clone https://github.com/4zobir89-lab/design-master-agent.git

mkdir -p ~/.codex/skills
cp -r design-master-agent ~/.codex/skills/design-master

chmod +x ~/.codex/skills/design-master/scripts/*.py
```

#### التفعيل
```
codex --skill design-master "build me a website for X"
```

---

### 4. Gemini CLI

#### المتطلبات
- Gemini CLI مُثبّت ([التثبيت](https://geminicli.com))
- Python 3.9+
- git

#### الخطوات

```bash
git clone https://github.com/4zobir89-lab/design-master-agent.git

mkdir -p ~/.gemini/skills
cp -r design-master-agent ~/.gemini/skills/design-master

chmod +x ~/.gemini/skills/design-master/scripts/*.py
```

#### التفعيل
```
gemini --skill design-master "build me a website for X"
```

---

### 5. GitHub Copilot (VS Code)

#### المتطلبات
- VS Code + GitHub Copilot Chat
- Python 3.9+
- git

#### الخطوات

```bash
git clone https://github.com/4zobir89-lab/design-master-agent.git

# نسخ إلى workspace
mkdir -p .vscode/copilot-skills
cp -r design-master-agent .vscode/copilot-skills/design-master
```

أضف إلى `.vscode/settings.json`:
```json
{
  "github.copilot.chat.codeGeneration.instructions": [
    "When user asks for a website, read .vscode/copilot-skills/design-master/AGENTS.md and follow the 7-phase methodology"
  ]
}
```

---

### 6. استخدام في أي LLM (دون تثبيت محلي)

إن لم ترد تثبيت محلي، أضف محتوى `AGENTS.md` إلى system prompt:

#### ChatGPT / Claude.ai / Gemini Web
انسخ محتوى [`AGENTS.md`](https://raw.githubusercontent.com/4zobir89-lab/design-master-agent/main/AGENTS.md) والصقه في system prompt أو في أول رسالة.

ثم اطلب:
```
اتبع هذا العقد لبناء موقع لـ X
```

#### API (Custom Application)
```python
import requests

agents_md = requests.get(
    "https://raw.githubusercontent.com/4zobir89-lab/design-master-agent/main/AGENTS.md"
).text

system_prompt = f"""
You are a design-master agent. Follow this contract strictly:

{agents_md}

When user asks for a website, execute the 7 phases.
"""
```

---

## 🔧 التحقق من التثبيت

بعد التثبيت، تحقّق:

```bash
# 1. الملفات موجودة
ls ~/.claude/skills/design-master/
# Expected: AGENTS.md SKILL.md README.md references/ scripts/ seeds/ templates/

# 2. السكريبتات تعمل
python ~/.claude/skills/design-master/scripts/discover.py "test"
# Expected: اكتشاف archetype + tone + theme

# 3. audit script يعمل
echo "<html><body>test</body></html>" > /tmp/test.html
python ~/.claude/skills/design-master/scripts/audit.py /tmp
```

---

## 🎯 كيف يستخدم الوكيل النظام

### تدفّق العمل (Workflow)

```
User Request: "أريد موقع لـ X"
         ↓
┌─────────────────────────────────────┐
│ 1. الوكيل يقرأ SKILL.md             │
│    - يفهم أنه skill "design-master" │
│    - يقرأ Pre-flight Reading List   │
└─────────────────────────────────────┘
         ↓
┌─────────────────────────────────────┐
│ 2. Phase 0 — Discovery              │
│    - يقرأ AGENTS.md (العقد)         │
│    - يطبّق Discovery logic           │
│    - أو يشغّل discover.py            │
│    - يكتب .design/discovery.md      │
└─────────────────────────────────────┘
         ↓
┌─────────────────────────────────────┐
│ 3. Phase 1 — Contract               │
│    - يكتب PRODUCT.md                │
│    - يكتب DESIGN.md                 │
└─────────────────────────────────────┘
         ↓
┌─────────────────────────────────────┐
│ 4. Phase 2 — Plan                   │
│    - يكتب .design/plan.md           │
│    - يكتب .design/phases/*.md       │
└─────────────────────────────────────┘
         ↓
┌─────────────────────────────────────┐
│ 5. Phase 3 — Seed Selection         │
│    - يقرأ seeds/template.html       │
│    - يختار theme من references/     │
│    - يختار recipes من references/   │
└─────────────────────────────────────┘
         ↓
┌─────────────────────────────────────┐
│ 6. Phase 4 — Implementation         │
│    - يكتب index.html (phase واحدة)  │
│    - يستخدم tokens من theme         │
│    - يستخدم recipes من references   │
│    - يحترم anti-ai-slop rules       │
└─────────────────────────────────────┘
         ↓
┌─────────────────────────────────────┐
│ 7. Phase 5 — Self-Audit             │
│    - يشغّل audit.py                 │
│    - يفحص 41 قاعدة                  │
│    - إن فشل P0 → يُصلح ويُعيد       │
│    - يكتب .design/audit.md          │
└─────────────────────────────────────┘
         ↓
┌─────────────────────────────────────┐
│ 8. Phase 6 — Delivery               │
│    - index.html (self-contained)    │
│    - PRODUCT.md + DESIGN.md         │
│    - .design/ artifacts             │
│    - ملخص تنفيذي في الـ chat        │
└─────────────────────────────────────┘
```

### الصلاحيات المطلوبة

الوكيل يحتاج صلاحيات:

| الصلاحية | الاستخدام |
|---|---|
| `file_write` | كتابة index.html, PRODUCT.md, DESIGN.md, .design/ |
| `file_read` | قراءة references/, seeds/, AGENTS.md |
| `shell_exec` | تشغيل python scripts/audit.py, discover.py |
| `http_fetch` | تحميل خطوط Google Fonts، GSAP CDN |

في Claude Code:
```json
{
  "permissions": {
    "file_write": true,
    "file_read": true,
    "shell_exec": ["python3", "git", "ls", "cat"],
    "http_fetch": ["fonts.googleapis.com", "cdnjs.cloudflare.com", "cdn.jsdelivr.net"]
  }
}
```

---

## 🧪 تجربة سريعة بعد التثبيت

بعد التثبيت، جرّب:

```
User: "أريد موقع شخصي لشاعر عربي معاصر، يكون سينمائي وراقٍ"
```

يجب أن يحدث:

1. ✅ الوكيل يقرأ AGENTS.md
2. ✅ يشغّل Phase 0 (Discovery)
3. ✅ يكتب PRODUCT.md + DESIGN.md
4. ✅ يكتب .design/plan.md
5. ✅ يقرأ seeds/template.html
6. ✅ يكتب index.html (phase واحدة في كل مرة)
7. ✅ يشغّل audit.py
8. ✅ يسلم: index.html + PRODUCT.md + DESIGN.md + .design/ + ملخص

---

## ❓ استكشاف الأخطاء

### المشكلة: الوكيل لا يقرأ SKILL.md
**الحل**: اطلب صراحةً:
```
اقرأ ~/.claude/skills/design-master/AGENTS.md ثم اتبع منهجيته لبناء موقع لـ X
```

### المشكلة: `python scripts/audit.py` لا يعمل
**الحل**: تأكد أن Python 3.9+ مُثبّت:
```bash
python3 --version
# أو
python --version
```

### المشكلة: الوكيل يتخطّى phases
**الحل**: اطلب صراحة:
```
اتبع الـ 7 phases بصرامة. اكتب PRODUCT.md و DESIGN.md أولاً، ثم .design/plan.md،
ثم ابدأ implementation. لا تتخطّى أي phase.
```

### المشكلة: الموقع يبدو كـ AI slop
**الحل**: اطلب:
```
شغّل audit.py على الموقع. إن فشل أي P0، أعد بناء الجزء الفاشل.
```

### المشكلة: التثبيت فشل على Mac
**الحل**: تأكد من صلاحيات المجلد:
```bash
sudo chown -R $(whoami) ~/.claude/skills/
```

---

## 📞 الدعم

- 🐛 [Issue Tracker](https://github.com/4zobir89-lab/design-master-agent/issues)
- 💬 [Discussions](https://github.com/4zobir89-lab/design-master-agent/discussions)
- 📖 [README](README.md)
