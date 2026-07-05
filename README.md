# Skattråd 🇸🇪

> **The AI compliance coworker for Swedish small business owners.**
> Grounded answers on tax, VAT, corporate law, and labor regulations — always sourced from Skatteverket, Bolagsverket, and verksamt.se.

Built with [Google ADK](https://google.github.io/adk-docs/) + [NVIDIA NIM](https://build.nvidia.com/) for **Vorker Intern Tryouts — Phase 1** (June 11, 2026).

**Status:** ✅ All 3 test cases working. Agent grounds answers in live Swedish authority sources.

---

## The Problem — The Compliance Gap

Swedish SME owners can't trust generic AI for compliance questions. A wrong answer about VAT, karensavdrag, or an aktieägaravtal isn't just unhelpful — it's a legal and financial liability.

**Skattråd closes the Compliance Gap.** It combines LLM reasoning with live, grounded fetches of authoritative Swedish sources so every answer is traceable, current, and specific to Swedish law.

---

## Architecture

```
User query
    │
    ▼
┌──────────────────────────────────────────────┐
│  skattrad_agent                              │
│  Model: NVIDIA NIM — Llama 4 Maverick 17B   │
│  Framework: Google ADK 2.2.0 (via LiteLLM)  │
│                                              │
│  Tool: fetch_page_content (custom)           │
│  Fetches full text from trusted Swedish      │
│  authority domains only:                     │
│  • skatteverket.se (tax, VAT, moms)          │
│  • bolagsverket.se (corporate law)           │
│  • verksamt.se (SME guides)                  │
│  • riksdagen.se (law text)                   │
└──────────────────────────────────────────────┘
    │
    ▼
Cited, sourced, actionable compliance answer
```

---

## Demo — Test Cases from the Brief

All three high-fidelity test cases from the assignment, answered with correct source fetches:

### 1. VAT Cross-Border SaaS (B2B Norway vs B2C Germany)

Agent fetches from **skatteverket.se** and correctly distinguishes:
- B2B Norway → reverse charge, no Swedish VAT
- B2C Germany → EU OSS rules, charge German VAT (19%)

### 2. Karensavdrag for Part-Time Employee

Agent fetches from **riksdagen.se** (Förordning 2020:400) and explains:
- Karensavdrag = 20% of weekly sick pay entitlement
- Pro-rated to contracted hours for part-time

### 3. Aktieägaravtal & Hembudsförbehåll

Agent fetches from **bolagsverket.se** and explains:
- Hembudsförbehåll must be in bolagsordningen to bind third parties (ABL 4:27)

📄 **See [SKATTRAD_FULL_REPORT.pdf](./SKATTRAD_FULL_REPORT.pdf) for full demo with screenshots.**

---

## How to Run

```bash
# 1. Clone
git clone https://github.com/CaffineAddic/Vorker.git
cd Vorker/skattrad

# 2. Install
pip install -r requirements.txt
pip install google-adk[extensions] litellm

# 3. Configure
export NVIDIA_NIM_API_KEY="your-nvidia-api-key"

# 4. Run (web UI)
cd ..
adk web
# Open http://localhost:8000 — select skattrad from dropdown
```

---

## Project Structure

```
Vorker/
├── skattrad/                    # Agent package
│   ├── agent/
│   │   ├── __init__.py          # ADK entry point
│   │   ├── agent.py             # Root agent + system instruction
│   │   └── tools.py             # fetch_page_content tool
│   ├── landing.html             # Product landing page (Swedish)
│   ├── pitch_notes.md           # 6-slide investor pitch
│   ├── gtm.md                   # Go-to-market strategy
│   ├── requirements.txt
│   └── .env.example
├── SKATTRAD_FULL_REPORT.pdf     # Complete project report (6 pages)
├── SKATTRAD_DEMO.pdf            # Demo screenshots
├── landing_page.png             # Landing page screenshot
├── VIT.pdf                      # Original assignment brief
└── README.md
```

---

## Business Case

| Document | Description |
|----------|-------------|
| [SKATTRAD_FULL_REPORT.pdf](./SKATTRAD_FULL_REPORT.pdf) | Complete report: demo, landing page, GTM, pitch, architecture |
| [skattrad/pitch_notes.md](./skattrad/pitch_notes.md) | 6-slide pitch: problem, solution, market, GTM, Vorker fit |
| [skattrad/gtm.md](./skattrad/gtm.md) | Full GTM: target segments, channels, pricing, partnerships, 90-day targets |
| [skattrad/landing.html](./skattrad/landing.html) | Swedish-language landing page with pricing and demo |

**One-liner:** *Skattråd is the AI compliance coworker that gives Swedish SME owners the confidence of a revisor — at a fraction of the cost.*


---

_June 11, 2026 · [Vorker.ai](https://vorker.ai)_
