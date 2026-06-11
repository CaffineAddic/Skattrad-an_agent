"""Curated authoritative URLs for common Swedish SME compliance topics."""

CURATED_SOURCES = {
    "aktieägaravtal": {
        "topic": "Aktieägaravtal and hembudsförbehåll in Swedish AB",
        "urls": [
            "https://www.bolagsverket.se/foretag/aktiebolag/aktieagare/aktieagaravtal",
            "https://www.riksdagen.se/sv/dokument-lagar/dokument/svensk-forfattningssamling/aktiebolagslag-2005551_sfs-2005-551",
        ],
        "hint": "Check ABL chapter 4 (bolagsordning) for hembudsförbehåll registration requirements.",
    },
    "hembudsförbehåll": {
        "topic": "Hembudsförbehåll (right of first refusal) in Swedish AB",
        "urls": [
            "https://www.bolagsverket.se/foretag/aktiebolag/aktieagare/aktieagaravtal",
            "https://www.riksdagen.se/sv/dokument-lagar/dokument/svensk-forfattningssamling/aktiebolagslag-2005551_sfs-2005-551",
        ],
        "hint": "Hembudsförbehåll in aktieägaravtal must often be reflected in bolagsordning (ABL 4:27).",
    },
    "karensavdrag": {
        "topic": "Karensavdrag and sick pay for employees",
        "urls": [
            "https://www.skatteverket.se/foretag/arbetsgivare/sjuklon/sjuklonochsjukavdrag.4.8e1f7a3f17a64bc2a1400017941.html",
            "https://www.verksamt.se/anstalla/sjuklon",
        ],
        "hint": "Karensavdrag is 20% of average weekly sick pay; pro-rate for part-time by contracted hours.",
    },
    "vat_cross_border": {
        "topic": "VAT for cross-border SaaS (EU B2B vs B2C)",
        "urls": [
            "https://www.skatteverket.se/foretag/moms/saljatillutlandet/euservice.4.8e1f7a3f17a64bc2a1400017941.html",
            "https://www.skatteverket.se/foretag/moms/saljatillutlandet/oss.4.8e1f7a3f17a64bc2a1400017941.html",
            "https://www.verksamt.se/driva/moms/salja-till-utlandet",
        ],
        "hint": "Compare B2B Norway (often reverse charge / no Swedish VAT) vs B2C Germany (German VAT via OSS).",
    },
    "moms_utlandet": {
        "topic": "Moms when selling services abroad",
        "urls": [
            "https://www.skatteverket.se/foretag/moms/saljatillutlandet/euservice.4.8e1f7a3f17a64bc2a1400017941.html",
            "https://www.skatteverket.se/foretag/moms/saljatillutlandet/oss.4.8e1f7a3f17a64bc2a1400017941.html",
        ],
        "hint": "Digital services to EU consumers use OSS; B2B may use reverse charge.",
    },
}
