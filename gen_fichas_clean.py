# CSS limpio y sin conflictos, diseñado para A4 vertical desde cero

CLEAN_CSS = """
/* ─── PAGE SETUP ─────────────────────────────────────── */
@page { size: A4 portrait; margin: 0; }
@page :first { margin: 0; }
* { -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; box-sizing: border-box; margin: 0; padding: 0; }

/* ─── BASE ────────────────────────────────────────────── */
body { font-family: 'Segoe UI', Arial, sans-serif; background: #eef2f7; color: #1a1a2e; font-size: 12px; line-height: 1.5; }

/* ─── HEADER ─────────────────────────────────────────── */
.header { color: white; padding: 22px 28px; display: flex; justify-content: space-between; align-items: flex-start; }
.header h1 { font-size: 28px; font-weight: 900; letter-spacing: 2px; }
.header .sub { font-size: 11px; opacity: 0.85; margin-top: 5px; }
.header .tag { font-size: 10px; opacity: 0.55; margin-top: 3px; }
.header .hright { text-align: right; font-size: 11px; opacity: 0.85; line-height: 2; }
.badge { display: inline-block; padding: 2px 10px; border-radius: 20px; font-size: 10px; font-weight: 700; margin-left: 6px; }
.badge-rival { background: rgba(220,38,38,0.65); }
.badge-aliado { background: rgba(34,197,94,0.65); }

/* ─── BANNER ─────────────────────────────────────────── */
.banner { background: #0f2944; color: white; padding: 22px 28px; border-left: 7px solid #FACC15; }
.b-label { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; color: #FACC15; margin-bottom: 7px; }
.b-title { font-size: 17px; font-weight: 800; margin-bottom: 14px; line-height: 1.3; }
.b-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }
.b-col p { font-size: 11.5px; line-height: 1.75; opacity: 0.9; margin-bottom: 9px; }
.b-col p strong { color: #FACC15; }
.b-nums { display: flex; gap: 10px; margin-top: 18px; }
.b-num { background: rgba(255,255,255,0.07); border: 1px solid rgba(255,255,255,0.15); border-radius: 8px; padding: 11px 14px; flex: 1; }
.b-num .n { font-size: 20px; font-weight: 900; color: #FACC15; line-height: 1; }
.b-num .l { font-size: 9.5px; opacity: 0.7; margin-top: 4px; line-height: 1.45; }

/* ─── MAIN GRID ──────────────────────────────────────── */
.main { padding: 18px 22px; display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
.full { grid-column: 1 / -1; }
.two  { grid-column: span 2; }
.one  { grid-column: span 1; }

/* ─── CARDS ──────────────────────────────────────────── */
.card { background: white; border-radius: 10px; box-shadow: 0 1px 5px rgba(0,0,0,0.08); overflow: hidden; }
.ch   { padding: 10px 15px; font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.9px; }
.cbody { padding: 16px; }

/* ─── SECTION TITLES ─────────────────────────────────── */
.st { font-size: 9.5px; font-weight: 700; color: #1F4E79; padding: 4px 0 5px; border-bottom: 2px solid #1F4E79; margin-bottom: 12px; text-transform: uppercase; letter-spacing: 0.6px; }

/* ─── CHIPS ──────────────────────────────────────────── */
.chips { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 12px; }
.chip { padding: 3px 11px; border-radius: 16px; font-size: 11px; font-weight: 600; }
.chip-b { background: #DBEAFE; border: 1px solid #93C5FD; color: #1E40AF; }
.chip-g { background: #D1FAE5; border: 1px solid #6EE7B7; color: #065F46; }
.chip-o { background: #FEF3C7; border: 1px solid #FCD34D; color: #92400E; }
.chip-r { background: #FEE2E2; border: 1px solid #FCA5A5; color: #7F1D1D; }
.chip-p { background: #EDE9FE; border: 1px solid #C4B5FD; color: #4C1D95; }
.chip-z { background: #F3F4F6; border: 1px solid #D1D5DB; color: #374151; }

/* ─── TABLA ──────────────────────────────────────────── */
.t { width: 100%; border-collapse: collapse; font-size: 11.5px; }
.t th { background: #f5f6f8; color: #555; padding: 6px 9px; text-align: left; font-size: 9.5px; text-transform: uppercase; letter-spacing: 0.4px; border-bottom: 2px solid #e5e7eb; }
.t td { padding: 6px 9px; border-bottom: 1px solid #f3f4f6; vertical-align: top; }
.t tr:last-child td { border-bottom: none; }
.tok   { background: #F0FDF4; color: #14532D; font-weight: 700; }
.twarn { background: #FEF3C7; color: #92400E; font-weight: 700; }
.tbad  { background: #FEF2F2; color: #7F1D1D; font-weight: 700; }
.tinf  { background: #EFF6FF; color: #1E40AF; font-weight: 700; }
.tbld  { font-weight: 700; }

/* ─── KPI ────────────────────────────────────────────── */
.kpis { display: grid; grid-template-columns: repeat(4, 1fr); gap: 11px; }
.kpi  { border-radius: 9px; padding: 13px 14px; border: 1px solid #e5e7eb; }
.kl   { font-size: 9.5px; color: #777; text-transform: uppercase; letter-spacing: 0.4px; margin-bottom: 4px; }
.kv   { font-size: 22px; font-weight: 800; line-height: 1.1; }
.ks   { font-size: 9.5px; color: #999; margin-top: 3px; line-height: 1.4; }

/* ─── SECTORES ───────────────────────────────────────── */
.sgrid { display: grid; grid-template-columns: 1fr 1fr; gap: 11px; margin-bottom: 16px; }
.sc   { border-radius: 7px; padding: 13px; border-left: 4px solid; }
.sc-p { border-color: #2563EB; background: #EFF6FF; }
.sc-s { border-color: #059669; background: #ECFDF5; }
.sc-t { border-color: #D97706; background: #FFFBEB; }
.sc-e { border-color: #7C3AED; background: #F5F3FF; }
.sl   { font-size: 9.5px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.7px; opacity: 0.65; margin-bottom: 3px; }
.sn   { font-size: 13px; font-weight: 800; margin-bottom: 3px; }
.sp   { font-size: 20px; font-weight: 900; margin: 3px 0 7px; }
.sd   { font-size: 10.5px; line-height: 1.65; color: #444; }

/* ─── BARRAS PBG ─────────────────────────────────────── */
.pbr  { display: flex; align-items: center; gap: 7px; margin-bottom: 6px; }
.pbl  { width: 120px; font-size: 10.5px; color: #666; text-align: right; flex-shrink: 0; }
.pbo  { flex: 1; height: 18px; background: #f0f0f0; border-radius: 4px; overflow: hidden; }
.pbi  { height: 100%; border-radius: 4px; display: flex; align-items: center; padding-left: 7px; }
.pbt  { font-size: 9.5px; font-weight: 700; color: white; white-space: nowrap; }
.pbp  { width: 35px; font-size: 10.5px; font-weight: 700; text-align: right; }

/* ─── PALANCAS ───────────────────────────────────────── */
.pgrid { display: grid; grid-template-columns: 1fr 1fr; gap: 11px; }
.pi   { border-radius: 7px; padding: 13px 15px; border-left: 4px solid; }
.pi-o { background: #F0FDF4; border-color: #22C55E; }
.pi-r { background: #FFF7ED; border-color: #F97316; }
.pi-d { background: #EFF6FF; border-color: #3B82F6; }
.pi-x { background: #FEF2F2; border-color: #EF4444; }
.pt   { font-size: 9.5px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.7px; opacity: 0.65; margin-bottom: 4px; }
.pti  { font-size: 11.5px; font-weight: 700; margin-bottom: 5px; }
.pd   { font-size: 10.5px; line-height: 1.65; color: #444; }

/* ─── ACTORES ────────────────────────────────────────── */
.ar  { display: flex; gap: 11px; padding: 11px 0; border-bottom: 1px solid #f0f0f0; }
.ar:last-child { border-bottom: none; }
.ai  { font-size: 20px; min-width: 28px; margin-top: 1px; }
.ain { flex: 1; }
.an  { font-size: 11.5px; font-weight: 700; color: #1F4E79; margin-bottom: 3px; }
.ad  { font-size: 10.5px; color: #555; line-height: 1.6; }
.ats { display: flex; gap: 4px; flex-wrap: wrap; margin-top: 5px; }
.at  { font-size: 9.5px; font-weight: 700; padding: 2px 8px; border-radius: 7px; }

/* ─── AGENDA ─────────────────────────────────────────── */
.ag  { display: flex; gap: 11px; padding: 12px 0; border-bottom: 1px dashed #e8e8e8; }
.ag:last-child { border-bottom: none; }
.agi { font-size: 18px; min-width: 24px; margin-top: 1px; }
.agt strong { font-size: 11.5px; display: block; margin-bottom: 3px; color: #1F4E79; font-weight: 700; }
.agt p { font-size: 10.5px; color: #666; line-height: 1.6; }

/* ─── ALERTAS ────────────────────────────────────────── */
.al  { border-radius: 7px; padding: 12px 14px; margin-top: 11px; font-size: 10.5px; line-height: 1.6; }
.al-v { background: #F0FDF4; border: 1px solid #86EFAC; color: #14532D; }
.al-a { background: #FFFBEB; border: 1px solid #FCD34D; color: #78350F; }
.al-b { background: #EFF6FF; border: 1px solid #93C5FD; color: #1E3A5F; }
.al-k { background: #1e3a5f; color: white; }
.al strong { display: block; margin-bottom: 3px; font-size: 11.5px; }
.al-k strong { color: #FACC15; }

/* ─── NOTA ───────────────────────────────────────────── */
.nt { background: #EFF6FF; border: 1px solid #BFDBFE; border-radius: 7px; padding: 11px 14px; font-size: 10.5px; color: #1E3A5F; margin-top: 11px; line-height: 1.6; }
.nt strong { display: block; font-size: 11.5px; margin-bottom: 3px; color: #1E40AF; }

/* ─── HISTORIA ───────────────────────────────────────── */
.hist { background: #FEF3C7; border: 1px solid #FCD34D; border-radius: 7px; padding: 12px 14px; margin-top: 11px; }
.hist strong { font-size: 11.5px; font-weight: 700; color: #78350F; display: block; margin-bottom: 4px; }
.hist p { font-size: 10.5px; color: #78350F; line-height: 1.65; }

/* ─── CORREDOR ───────────────────────────────────────── */
.corr { background: linear-gradient(135deg, #1e3a5f 0%, #2563EB 100%); color: white; border-radius: 9px; padding: 16px 18px; margin-top: 14px; }
.corr h3 { font-size: 12px; font-weight: 800; margin-bottom: 7px; color: #FACC15; }
.corr p  { font-size: 10.5px; line-height: 1.65; opacity: 0.9; }
.cms { display: flex; gap: 8px; margin-top: 12px; flex-wrap: wrap; }
.cm  { background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); border-radius: 5px; padding: 8px 10px; flex: 1; text-align: center; font-size: 10.5px; font-weight: 700; min-width: 90px; }
.cm span { display: block; font-size: 9.5px; font-weight: 400; opacity: 0.65; margin-top: 2px; }

/* ─── FOOTER ─────────────────────────────────────────── */
.footer { text-align: center; padding: 12px; font-size: 10px; color: #aaa; border-top: 1px solid #e5e7eb; margin-top: 10px; background: white; }

/* ─── PRINT ──────────────────────────────────────────── */
@media print {
  @page { size: A4 portrait; margin: 0; }
  body  { background: #eef2f7 !important; font-size: 8.5pt; line-height: 1.5; }

  .main { grid-template-columns: 1fr 1fr !important; padding: 12px 16px !important; gap: 11px !important; }
  .card { box-shadow: none !important; page-break-inside: avoid; break-inside: avoid; }
  .ch   { font-size: 7.5pt !important; padding: 7px 12px !important; page-break-after: avoid; break-after: avoid; }
  .cbody{ padding: 12px !important; }
  .st   { font-size: 7.5pt !important; }

  /* KPIs: 4 col → 2 col en portrait */
  .kpis { grid-template-columns: 1fr 1fr !important; }

  /* Tablas */
  .t    { font-size: 8pt !important; }
  .t th { font-size: 7pt !important; padding: 4px 7px !important; }
  .t td { padding: 4px 7px !important; }
  thead { display: table-header-group; }
  tr    { page-break-inside: avoid; break-inside: avoid; }

  /* Banner */
  .banner { page-break-inside: avoid; break-inside: avoid; }
  .b-col p { font-size: 8.5pt !important; }
  .b-num .n { font-size: 16pt !important; }
  .b-num .l { font-size: 7.5pt !important; }
  .header { page-break-after: avoid; break-after: avoid; }
  .header h1 { font-size: 20pt !important; }

  /* KPIs values */
  .kl { font-size: 7.5pt !important; }
  .kv { font-size: 16pt !important; }
  .ks { font-size: 7.5pt !important; }

  /* Sectores */
  .sl { font-size: 7.5pt !important; }
  .sn { font-size: 10pt !important; }
  .sp { font-size: 14pt !important; }
  .sd { font-size: 8pt !important; }

  /* Barras */
  .pbl { font-size: 8pt !important; }
  .pbt { font-size: 7.5pt !important; }
  .pbp { font-size: 8pt !important; }

  /* Palancas */
  .pt  { font-size: 7.5pt !important; }
  .pti { font-size: 9pt !important; }
  .pd  { font-size: 8pt !important; }

  /* Actores */
  .an  { font-size: 9pt !important; }
  .ad  { font-size: 8pt !important; }
  .at  { font-size: 7.5pt !important; }

  /* Agenda */
  .agt strong { font-size: 9pt !important; }
  .agt p      { font-size: 8pt !important; }

  /* Alertas / notas */
  .al        { font-size: 8pt !important; page-break-inside: avoid; break-inside: avoid; }
  .al strong { font-size: 9pt !important; }
  .nt        { font-size: 8pt !important; }
  .nt strong { font-size: 9pt !important; }
  .hist      { page-break-inside: avoid; break-inside: avoid; }
  .hist strong { font-size: 9pt !important; }
  .hist p    { font-size: 8pt !important; }

  /* Chips */
  .chip { font-size: 8pt !important; }

  /* Corredor */
  .corr { page-break-inside: avoid; break-inside: avoid; }
  .cm   { font-size: 8pt !important; min-width: 70px !important; }
  .cm span { font-size: 7pt !important; }

  /* Grillas internas en portrait */
  .sgrid { grid-template-columns: 1fr 1fr !important; }
  .pgrid { grid-template-columns: 1fr 1fr !important; }
  div[style*="grid-template-columns:1fr 1fr 1fr"] { grid-template-columns: 1fr 1fr !important; gap: 9px !important; }
  div[style*="grid-template-columns:1fr 1fr"]     { gap: 9px !important; }

  /* Saltos de página */
  div[style*="page-break-before:always"] { margin-top: 0 !important; }
  .footer { page-break-before: avoid; break-before: avoid; font-size: 7.5pt; }
  p, li { orphans: 3; widows: 3; }
}
"""

print(f"CSS: {len(CLEAN_CSS)} chars")
