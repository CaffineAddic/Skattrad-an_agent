# Skattråd — Pitch

_Vorker Intern Tryouts, Phase 1 · June 11, 2026_

---

## Slide 1 — The problem (The Compliance Gap)

**Sweden has 650,000+ small businesses.** Most can't afford a revisor on retainer.

When they Google tax questions, they get generic answers. When they ask ChatGPT,
they get plausible-sounding answers that may not reflect Swedish law.

A wrong answer about VAT costs 5–20% in penalties. A missed F-skatt registration
freezes business activity. An incorrectly structured aktieägaravtal can invalidate
shareholder rights.

**The Compliance Gap:** the space between "I need an answer" and "I can trust this answer."

---

## Slide 2 — The solution

**Skattråd** is a specialized AI compliance coworker for Swedish SME owners.

It doesn't guess. It searches. It fetches the actual page from Skatteverket or
Bolagsverket. It cites the source. It tells you when to call a human.

Built on Google ADK + Gemini 2.0 Flash. Every answer is grounded in:
- **skatteverket.se** — tax, VAT, employer contributions
- **bolagsverket.se** — corporate law, share agreements
- **verksamt.se** — practical business guides
- **riksdagen.se** — actual law text when needed

**One-liner:** *"The confidence of a revisor, available 24/7, at 1% of the cost."*

---

## Slide 3 — Live demo

Three test cases from the brief, all answered correctly with source citations:

1. **VAT cross-border SaaS:** B2B Norway (reverse charge, no Swedish VAT) vs
   B2C Germany (OSS rules, charge German VAT 19%) — sourced from skatteverket.se

2. **Karensavdrag part-time:** 20% of weekly sick pay entitlement, pro-rated
   to contracted hours — sourced from Sjuklönelagen via skatteverket.se

3. **Aktieägaravtal hembudsförbehåll:** Must be in bolagsordning to bind third
   parties (ABL 4:27) — sourced from bolagsverket.se + riksdagen.se

*See README.md for full example conversations.*

---

## Slide 4 — Market

- **TAM:** 650,000 Swedish small businesses
- **SAM:** ~330,000 solo/micro businesses with active compliance needs
- **ICP:** Solo founders and micro-AB, 1–3 years in business, no dedicated revisor

**Why now:** Swedish regulations change frequently (LAS reform 2022, moms OSS 2021,
new F-skatt rules). Even revisors struggle to stay current. AI that self-updates
via live search has a structural advantage.

---

## Slide 5 — GTM *(full detail in gtm.md)*

- **Phase 1:** Direct outreach to Frilansare Sverige community (FB group: 40k members)
- **Phase 2:** Integration partnership with Bokio / Fortnox (200k+ Swedish SME users)
- **Phase 3:** White-label for revisorsbyråer (B2B revenue stream)

**Pricing:** 0 kr free tier → 149 kr/mo Solo → 499 kr/mo Företag

---

## Slide 6 — Why Vorker

Vorker is building the AI coworker stack for small business. Skattråd is the
compliance module that every Swedish business coworker needs.

The integration is natural: when a Vorker user asks their AI coworker "can I
hire a consultant on F-skatt?" — Skattråd handles it with a sourced, accurate answer.

**The ask:** Build Skattråd into Vorker as the Swedish compliance layer, with
a path to expanding to other Nordic regulatory markets (Norway, Finland, Denmark).
