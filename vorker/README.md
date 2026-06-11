# Vorker Compliance

> **The AI compliance coworker for Swedish small business owners.**
> Grounded answers on tax, VAT, corporate law, and labor regulations — always sourced from Skatteverket, Bolagsverket, and verksamt.se.

Built with [Google ADK](https://google.github.io/adk-docs/) for **Vorker Intern Tryouts — Phase 1** (June 11, 2026).

Repository: [github.com/CaffineAddic/Vorker](https://github.com/CaffineAddic/Vorker)

---

## The problem

Swedish SME owners can't trust generic AI for compliance questions. A wrong answer about VAT, karensavdrag, or an aktieägaravtal isn't just unhelpful — it's a legal and financial liability.

**Vorker Compliance closes the Compliance Gap.** It combines Gemini's reasoning with live searches and fetches from authoritative Swedish sources so every answer is traceable, current, and specific to Swedish law.

---

## Architecture

```
User query
    │
    ▼
┌─────────────────────────────────────────────┐
│  vorker_compliance_agent  (gemini-2.0-flash) │
│                                             │
│  System prompt: Swedish compliance expert   │
│  Mandatory process: search → fetch → cite   │
│                                             │
│  Tools:                                     │
│  ├── google_search  (ADK built-in)          │
│  ├── get_recommended_sources  (curated)     │
│  └── fetch_page_content  (custom)           │
└─────────────────────────────────────────────┘
    │
    ▼
Cited, sourced, actionable compliance answer
```

---

## Demo — VIT test cases

### 1. Aktieägaravtal / hembudsförbehåll
```
User: Explain the requirements for an aktieägaravtal regarding hembudsförbehåll in a Swedish AB.

Agent: [get_recommended_sources → fetch bolagsverket.se + riksdagen.se → cited answer]
```

### 2. Karensavdrag (part-time)
```
User: How do I calculate karensavdrag for a part-time employee?

Agent: [get_recommended_sources → fetch skatteverket.se → 20% rule + pro-rating example]
```

### 3. VAT cross-border SaaS
```
User: VAT implications for SaaS to B2B Norway vs B2C Germany?

Agent: [get_recommended_sources → fetch Skatteverket OSS pages → side-by-side comparison]
```

---

## How to run

```bash
git clone https://github.com/CaffineAddic/Vorker.git
cd Vorker/vorker

pip install -r requirements.txt

cp .env.example .env
# Add your GOOGLE_API_KEY from https://aistudio.google.com/

adk web
# → Open http://localhost:8000
```

---

## Project structure

```
vorker/
├── __init__.py
├── agent.py             # Root agent + system instruction
├── tools.py             # fetch_page_content, get_recommended_sources
├── sources.py           # Curated URLs for VIT test cases
├── landing.html
├── pitch_notes.md
├── gtm.md
├── requirements.txt
├── .env.example
└── README.md
```

---

## Business case

See [`pitch_notes.md`](./pitch_notes.md) and [`gtm.md`](./gtm.md).

**One-liner:** *Vorker Compliance is the AI coworker that gives Swedish SME owners the confidence of a revisor — at a fraction of the cost.*

---

_Built at Vorker Intern Tryouts · Phase 1 · June 11, 2026_
