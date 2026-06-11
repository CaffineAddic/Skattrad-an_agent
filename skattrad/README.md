# Skattråd 🇸🇪

> **The AI compliance coworker for Swedish small business owners.**
> Grounded answers on tax, VAT, corporate law, and labor regulations — always sourced from Skatteverket, Bolagsverket, and verksamt.se.

Built with [Google ADK](https://google.github.io/adk-docs/) for **Vorker Intern Tryouts — Phase 1** (June 11, 2026).

---

## The problem

Swedish SME owners can't trust generic AI for compliance questions. A wrong answer about VAT, karensavdrag, or an aktieägaravtal isn't just unhelpful — it's a legal and financial liability.

**Skattråd closes the Compliance Gap.** It combines Gemini's reasoning with live, grounded searches of authoritative Swedish sources so every answer is traceable, current, and specific to Swedish law.

---

## Architecture

```
User query
    │
    ▼
┌─────────────────────────────────────────────┐
│  skattrad_agent  (gemini-2.0-flash)          │
│                                             │
│  System prompt: Swedish compliance expert   │
│  Mandatory process: search → fetch → cite   │
│                                             │
│  Tools:                                     │
│  ├── google_search  (ADK built-in)          │
│  │   Finds relevant pages on:               │
│  │   skatteverket.se / bolagsverket.se /    │
│  │   verksamt.se / riksdagen.se             │
│  │                                          │
│  └── fetch_page_content  (custom)           │
│      Reads full text from trusted Swedish   │
│      authority domains for deep grounding   │
└─────────────────────────────────────────────┘
    │
    ▼
Cited, sourced, actionable compliance answer
```

The agent is instructed to **never answer from memory alone** on regulatory questions. It always searches → fetches full page content → synthesises → cites sources.

---

## Demo — test cases from the brief

### VAT cross-border SaaS
```
User: What are the VAT implications for a Swedish company selling SaaS to
      a B2B customer in Norway vs a B2C customer in Germany?

Skattråd: [searches skatteverket.se for OSS/MOSS rules, fetches the relevant page]

Short answer: For B2B Norway: reverse charge applies, no Swedish VAT charged —
the Norwegian company self-assesses. For B2C Germany: EU OSS rules apply,
you must charge German VAT (19%) and report via the Swedish OSS registration.

[...full sourced explanation with URLs...]
Source: skatteverket.se/foretag/moms/salja-till-utlandet
```

### Karensavdrag for part-time employee
```
User: How do I calculate karensavdrag for a part-time employee?

Skattråd: [searches skatteverket.se for sjuklön, fetches Sjuklönelagen article]

Key formula: karensavdrag = 20% of weekly sick pay entitlement
For part-time: based on the employee's actual contracted hours, not full-time equivalent.
[...with exact calculation example and source citation...]
```

### Aktieägaravtal / hembudsförbehåll
```
User: Explain the requirements for an aktieägaravtal regarding hembudsförbehåll in a Swedish AB.

Skattråd: [searches bolagsverket.se + riksdagen.se for ABL chapter 4]

A hembudsförbehåll (right of first refusal clause) in an AB must be registered in
the bolagsordning to be enforceable against third parties (ABL 4:27)...
[...full sourced explanation...]
```

---

## How to run

```bash
# 1. Clone
git clone https://github.com/YOUR_USERNAME/skattrad.git
cd skattrad

# 2. Install
pip install -r requirements.txt

# 3. Configure
cp .env.example .env
# Add your GOOGLE_API_KEY from aistudio.google.com

# 4. Run — web UI (recommended for demo)
adk web
# → Open http://localhost:8000

# 5. Or run in terminal
adk run agent
```

---

## Project structure

```
skattrad/
├── agent/
│   ├── __init__.py          # ADK package entry point
│   ├── agent.py             # Root agent + system instruction
│   └── tools.py             # fetch_page_content tool
├── landing.html             # Product landing page
├── pitch_notes.md           # Investor pitch outline
├── gtm.md                   # Go-to-market plan
├── requirements.txt
├── .env.example
└── README.md
```

---

## Business case

See [`pitch_notes.md`](./pitch_notes.md) and [`gtm.md`](./gtm.md).

**One-liner:** *Skattråd is the AI compliance coworker that gives Swedish SME owners the confidence of a revisor — at a fraction of the cost.*

---

_Built solo at Vorker Intern Tryouts · Phase 1 · June 11, 2026_
