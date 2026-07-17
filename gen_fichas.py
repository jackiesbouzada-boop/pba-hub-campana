import re

with open('Ficha_Campana_SAN_NICOLAS.html') as f:
    sn = f.read()
css_match = re.search(r'<style>(.*?)</style>', sn, re.DOTALL)
CSS = css_match.group(1)

def make_ficha(muni):
    d = MUNIS[muni]
    
    # Header gradient color
    hgrad = d['hgrad']
    agrad = d['agrad']
    
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{d['nombre'].upper()} — Ficha de Campaña · PBA 2026</title>
<style>{CSS}</style>
</head>
<body>

<!-- ═══════ HEADER ═══════ -->
<div class="header" style="background: linear-gradient(135deg, {hgrad[0]} 0%, {hgrad[1]} 100%);">
  <div class="header-left">
    <h1>📍 {d['nombre'].upper()}</h1>
    <div class="sub">{d['sub']}</div>
    <div class="tag">{d['tag']}</div>
  </div>
  <div class="header-right">
    <div><strong>Intendente:</strong> {d['intendente']}</div>
    <div><strong>Partido:</strong> {d['partido']} <span class="badge-rival">{d['partido_badge']}</span></div>
    <div><strong>Sección Electoral:</strong> {d['seccion']}</div>
    <div><strong>Categoría:</strong> {d['categoria']}</div>
  </div>
</div>

<!-- ═══════ BANNER ═══════ -->
<div class="banner" style="border-left-color:{d['banner_color']};">
  <div class="b-label">{d['banner_label']}</div>
  <div class="b-title">{d['banner_title']}</div>
  <div class="b-grid">
    <div class="b-col">
      {d['banner_left']}
    </div>
    <div class="b-col">
      {d['banner_right']}
    </div>
  </div>
  <div class="b-nums">
    {d['banner_nums']}
  </div>
</div>

<!-- ═══════ MAIN GRID ═══════ -->
<div class="main">

  <!-- KPIs -->
  <div class="card full">
    <div class="ch" style="background:#f8fafc;color:#334155;">📊 Indicadores Clave del Distrito</div>
    <div class="cb">
      <div class="kpis">
        {d['kpis']}
      </div>
    </div>
  </div>

  <!-- SCORE CARD -->
  <div class="card one">
    <div class="ch" style="background:{d['score_bg']};color:{d['score_fg']};">🎯 Competitividad Electoral</div>
    <div class="cb">
      {d['score_content']}
    </div>
  </div>

  <!-- AGENDA -->
  <div class="card two">
    <div class="ch" style="background:#EFF6FF;color:#1E40AF;">🗓️ Agenda de Visita · Propuesta</div>
    <div class="cb">
      {d['agenda']}
    </div>
  </div>

  <!-- CONTEXTO POLÍTICO (full) -->
  <div class="card full">
    <div class="ch" style="background:#0f2944;color:white;">🔍 Contexto Político y Electoral · Diagnóstico</div>
    <div class="cb">
      {d['contexto']}
    </div>
  </div>

  <!-- ECONOMÍA / SECTORES -->
  <div class="card two">
    <div class="ch" style="background:#ECFDF5;color:#065F46;">🏭 Perfil Económico del Distrito</div>
    <div class="cb">
      {d['economia']}
    </div>
  </div>

  <!-- ACTORES CLAVE -->
  <div class="card one">
    <div class="ch" style="background:#F5F3FF;color:#4C1D95;">🤝 Actores Clave</div>
    <div class="cb">
      {d['actores']}
    </div>
  </div>

  <!-- PERSPECTIVA PROVINCIAL (full) -->
  <div class="card full">
    <div class="ch" style="background:#0f2944;color:#FACC15;">👁️ Perspectiva Provincial · Palancas que solo el nivel provincial puede activar</div>
    <div class="cb">
      <p style="font-size:12px;color:#666;margin-bottom:16px;line-height:1.7;">{d['palancas_intro']}</p>
      <div class="pgrid">
        {d['palancas']}
      </div>
    </div>
  </div>

</div>

<div class="footer">
  🔒 USO RESERVADO · Campaña PBA · Ficha {d['nombre']} · PBA Analytics 2026
</div>

<!-- ══════════════════════════════════════════════════════════════════════════
     ANEXO I — PRINCIPALES INDICADORES
     ══════════════════════════════════════════════════════════════════════════ -->
<div style="page-break-before:always;break-before:page;height:0;margin:0;padding:0;font-size:0;"></div>
<div>
  <div style="background:linear-gradient(135deg,{hgrad[0]},{hgrad[1]});color:white;padding:20px 32px;display:flex;justify-content:space-between;align-items:center;">
    <div>
      <div style="font-size:11px;opacity:0.6;letter-spacing:2px;text-transform:uppercase;margin-bottom:4px;">{d['nombre']} · 2026</div>
      <div style="font-size:22px;font-weight:900;letter-spacing:1px;">ANEXO I — PRINCIPALES INDICADORES</div>
    </div>
    <div style="font-size:11px;opacity:0.7;text-align:right;">{d['seccion']} · {d['categoria']}<br>PBA Analytics 2026</div>
  </div>

  <div style="padding:20px 24px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px;background:#eef2f7;">
    {d['anexo1']}
  </div>

  <div style="text-align:center;padding:12px;font-size:11px;color:#aaa;background:white;border-top:1px solid #e5e7eb;">
    🔒 USO RESERVADO · ANEXO I · {d['nombre']} · PBA Analytics 2026
  </div>
</div>

<!-- ══════════════════════════════════════════════════════════════════════════
     ANEXO II — GESTIÓN LOCAL Y DATOS DE CONTEXTO
     ══════════════════════════════════════════════════════════════════════════ -->
<div style="page-break-before:always;break-before:page;height:0;margin:0;padding:0;font-size:0;"></div>
<div>
  <div style="background:linear-gradient(135deg,{agrad[0]},{agrad[1]});color:white;padding:20px 32px;display:flex;justify-content:space-between;align-items:center;">
    <div>
      <div style="font-size:11px;opacity:0.6;letter-spacing:2px;text-transform:uppercase;margin-bottom:4px;">{d['nombre']} · 2026</div>
      <div style="font-size:22px;font-weight:900;letter-spacing:1px;">ANEXO II — GESTIÓN LOCAL Y DATOS DE CONTEXTO</div>
    </div>
    <div style="font-size:11px;opacity:0.7;text-align:right;">Gestión {d['intendente'].split()[0]}<br>{d['partido']}</div>
  </div>

  <div style="padding:20px 24px;display:grid;grid-template-columns:1fr 1fr;gap:16px;background:#eef2f7;">
    {d['anexo2']}
  </div>

  <div style="text-align:center;padding:12px;font-size:11px;color:#aaa;background:white;border-top:1px solid #e5e7eb;">
    🔒 USO RESERVADO · ANEXO II · {d['nombre']} · PBA Analytics 2026
  </div>
</div>

</body>
</html>"""
    return html

MUNIS = {}

# ─── LOBOS ─────────────────────────────────────────────────────────────────
MUNIS['LOBOS'] = {
  'nombre': 'Lobos',
  'sub': 'Polo Turístico y Cuenca Lechera · 3ª Sección Electoral · Centro Bonaerense · 1.726 km²',
  'tag': 'Campaña PBA 2026 · Uso Reservado · PBA Analytics',
  'hgrad': ('#1F6E4E', '#16A34A'),
  'agrad': ('#78350F', '#D97706'),
  'banner_color': '#FACC15',
  'banner_label': '⚠️ DISTRITO A RECUPERAR · LLA 52,8% EN 2023',
  'banner_title': 'La Laguna que vota libertad',
  'banner_left': '''<p>Lobos tiene algo que ningún municipio del conurbano ni del interior puede replicar fácilmente: una laguna a 110 km de Buenos Aires que atrae <strong>más de 15.000 turistas por fin de semana largo</strong>. Esa economía de turismo y recreación, más una sólida cuenca lechera, hacía de Lobos un distrito competitivo.</p>
      <p>Pero en la elección general de 2023, La Libertad Avanza se llevó el <strong>52,8% de los votos</strong>. En un año, el electorado pasó del PJ (2021) al JxC (PASO 2023) y luego a LLA. Volatilidad extrema. El voto productivo rural y el comerciante turístico se fueron con el libertarismo.</p>''',
  'banner_right': '''<p>El intendente Jorge Etcheverry (JxC) lleva tres mandatos consecutivos. El PJ tiene estructura débil en el municipio. La presencia desde la perspectiva provincial no puede ser de confrontación con Etcheverry, sino de propuesta en un nivel que él no puede ofrecer.</p>
      <p><strong>La Laguna de Lobos necesita el Estado provincial</strong>: el manejo hídrico, la Ruta 205, el plan turístico bonaerense. Eso es exactamente lo que LLA no puede dar. El mensaje se escribe solo.</p>''',
  'banner_nums': '''<div class="b-num"><div class="n">41.760</div><div class="l">Habitantes<br>Censo 2022</div></div>
    <div class="b-num"><div class="n">52,8%</div><div class="l">LLA en Gral 2023<br>Alarma roja</div></div>
    <div class="b-num"><div class="n">15.000+</div><div class="l">Turistas por fin<br>de semana largo</div></div>
    <div class="b-num"><div class="n">3er</div><div class="l">Mandato Etcheverry<br>JxC · Estructura rival</div></div>''',
  'kpis': '''<div class="kpi" style="background:#F0FDF4;border-color:#86EFAC;">
      <div class="kl">Población (Censo 2022)</div>
      <div class="kv" style="color:#15803D;">41.760</div>
      <div class="ks">Municipio intermedio · Interior PBA</div>
    </div>
    <div class="kpi" style="background:#FEF2F2;border-color:#FCA5A5;">
      <div class="kl">LLA · Gral 2023</div>
      <div class="kv" style="color:#DC2626;">52,8%</div>
      <div class="ks">UxP 31,3% · Diferencia: 21,5 pp</div>
    </div>
    <div class="kpi" style="background:#FFFBEB;border-color:#FCD34D;">
      <div class="kl">Partido actual (intendente)</div>
      <div class="kv" style="color:#92400E;font-size:16px;">JxC</div>
      <div class="ks">Etcheverry · 3 mandatos · Rival</div>
    </div>
    <div class="kpi" style="background:#EFF6FF;border-color:#93C5FD;">
      <div class="kl">Sección Electoral</div>
      <div class="kv" style="color:#1D4ED8;">3ª</div>
      <div class="ks">Centro bonaerense · Interior</div>
    </div>''',
  'intendente': 'Jorge Etcheverry',
  'partido': 'Juntos por el Cambio',
  'partido_badge': 'RIVAL · 3 MANDATOS',
  'seccion': '3ª Sección Electoral',
  'categoria': 'Disputado → LLA ganó 2023',
  'score_bg': '#FEF2F2',
  'score_fg': '#7F1D1D',
  'score_content': '''<div class="sgrid">
      <div class="sc p">
        <div class="sl">Voto PJ 2021</div>
        <div class="sp" style="color:#1D4ED8;">40,2%</div>
        <div class="sd">PJ ganó en elecciones legislativas. Base propia real.</div>
      </div>
      <div class="sc e">
        <div class="sl">UxP PASO 2023</div>
        <div class="sp" style="color:#7C3AED;">37,7%</div>
        <div class="sd">JxC PASO 43,5% · LLA 16,3%</div>
      </div>
    </div>
    <div class="sc" style="border-color:#DC2626;background:#FEF2F2;padding:14px;border-radius:8px;border-left:4px solid #DC2626;">
      <div class="sl">Gral 2023 · RESULTADO FINAL</div>
      <div class="sp" style="color:#DC2626;font-size:28px;">LLA 52,8%</div>
      <div class="sd">UxP 31,3% · Diferencia de 21,5 puntos. En un año LLA triplicó su caudal.</div>
    </div>
    <div class="al al-a" style="margin-top:12px;">
      <strong>⚠️ Volatilidad extrema</strong>
      En 24 meses el electorado local pasó de PJ → JxC → LLA. No hay base fija. El mensaje y la propuesta concreta definen el voto.
    </div>''',
  'agenda': '''<div class="ag">
      <div class="agi">🌅</div>
      <div class="agt">
        <strong>Costanera de la Laguna de Lobos</strong>
        <p>Visita al activo turístico central del municipio. Mensaje: "la Laguna de Lobos es un patrimonio provincial que la Provincia va a potenciar". Anuncio del Plan de Manejo Integral con financiamiento provincial.</p>
      </div>
    </div>
    <div class="ag">
      <div class="agi">🐄</div>
      <div class="agt">
        <strong>Encuentro con productores tamberos</strong>
        <p>Reunión con referentes de la cuenca lechera de la 3ª sección. Agenda: créditos Banco Provincia, asistencia técnica al sector, estado de las rutas rurales (Ruta 205 y Ruta 41).</p>
      </div>
    </div>
    <div class="ag">
      <div class="agi">🏪</div>
      <div class="agt">
        <strong>Recorrida comercial del centro</strong>
        <p>El comercio local vive del turismo de la laguna. Escuchar al pequeño comerciante y gastronómico. Propuesta: Lobos en el circuito oficial de turismo bonaerense.</p>
      </div>
    </div>
    <div class="al al-b" style="margin-top:12px;">
      <strong>💡 Estrategia de visita</strong>
      No disputar en el terreno del intendente (gestión local). El mensaje es de escala provincial: lo que solo Buenos Aires puede dar a Lobos, y LLA no puede.
    </div>''',
  'contexto': '''<div class="sgrid">
      <div>
        <div class="st">Diagnóstico electoral</div>
        <table class="t">
          <thead><tr><th>Elección</th><th>PJ/UxP</th><th>JxC</th><th>LLA</th><th>Ganador</th></tr></thead>
          <tbody>
            <tr><td class="bld">Legislativas 2021</td><td class="ok">40,2%</td><td>—</td><td class="warn">31,2%</td><td>PJ</td></tr>
            <tr><td class="bld">PASO 2023</td><td>37,7%</td><td class="ok">43,5%</td><td>16,3%</td><td>JxC</td></tr>
            <tr><td class="bld">General 2023</td><td class="warn">31,3%</td><td>—</td><td class="bad">52,8%</td><td>LLA</td></tr>
          </tbody>
        </table>
        <div class="al al-a" style="margin-top:10px;">
          <strong>⚡ Volcán electoral</strong>
          LLA pasó de 16,3% (PASO) a 52,8% (General) en 3 meses. El electorado de Lobos es altamente volátil y sensible al discurso de cambio. No hay voto "duro" confiable.
        </div>
      </div>
      <div>
        <div class="st">Mapa político local</div>
        <table class="t">
          <thead><tr><th>Factor</th><th>Estado</th></tr></thead>
          <tbody>
            <tr><td>Intendente</td><td class="bad">Rival (JxC · 3 mandatos)</td></tr>
            <tr><td>Concejo Deliberante PJ</td><td class="warn">Minoría · débil estructura</td></tr>
            <tr><td>Sindicatos / gremios</td><td class="warn">Dispersos · sin peso orgánico</td></tr>
            <tr><td>Sector turístico</td><td class="warn">Independiente · potencialmente ganador</td></tr>
            <tr><td>Cuenca lechera</td><td class="ok">Receptiva a propuestas agro</td></tr>
          </tbody>
        </table>
        <div class="al al-v" style="margin-top:10px;">
          <strong>✅ Ventana estratégica</strong>
          El voto LLA en Lobos es protest vote, no identidad ideológica firme. Con propuesta concreta de inversión provincial (laguna, rutas, tambos), hay espacio de recuperación real.
        </div>
      </div>
    </div>''',
  'economia': '''<div class="st">Estructura económica · Lobos</div>
    <div class="sgrid">
      <div class="sc t">
        <div class="sl">Turismo y Recreación</div>
        <div class="sn">Laguna de Lobos</div>
        <div class="sp" style="color:#D97706;">Motor principal</div>
        <div class="sd">15.000+ turistas por fin de semana largo. Pesca deportiva, náutica, paracaidismo. Tracción directa sobre gastronomía, hotelería y comercio.</div>
      </div>
      <div class="sc s">
        <div class="sl">Agro · Cuenca Lechera</div>
        <div class="sn">Tambos y Campos</div>
        <div class="sp" style="color:#059669;">Base histórica</div>
        <div class="sd">Tambos de primer nivel, producción granaria (soja, maíz, girasol) y ganadería. Economía rural que inyecta ingresos estables en el casco urbano.</div>
      </div>
    </div>
    <div class="st" style="margin-top:14px;">Ejes de gestión municipal actual</div>
    <div class="pbr"><div class="pbl">Infraestructura vial rural</div><div class="pbo"><div class="pbi" style="width:80%;background:#1D4ED8;"><span class="pbt">Alteo y reparación permanente</span></div></div><div class="pbp">Prioridad</div></div>
    <div class="pbr"><div class="pbl">Costanera / Laguna</div><div class="pbo"><div class="pbi" style="width:75%;background:#16A34A;"><span class="pbt">Plan de Manejo 2026</span></div></div><div class="pbp">Alta</div></div>
    <div class="pbr"><div class="pbl">Vivienda popular</div><div class="pbo"><div class="pbi" style="width:55%;background:#D97706;"><span class="pbt">Banco de Tierras Municipal</span></div></div><div class="pbp">Media</div></div>
    <div class="pbr"><div class="pbl">Seguridad / LPR</div><div class="pbo"><div class="pbi" style="width:50%;background:#7C3AED;"><span class="pbt">Cámaras Rutas 205 y 41</span></div></div><div class="pbp">Media</div></div>''',
  'actores': '''<div class="ar">
      <div class="ai">🐄</div>
      <div class="ain">
        <div class="an">Cooperativas lecheras · Cuenca 3ª sección</div>
        <div class="ad">Los productores tamberos del partido. Interlocutores directos para una agenda agro con créditos Banco Provincia y asistencia técnica. Su aval vale votos rurales.</div>
        <div class="ats"><span class="at" style="background:#D1FAE5;color:#065F46;">Reunión previa recomendada</span></div>
      </div>
    </div>
    <div class="ar">
      <div class="ai">🌊</div>
      <div class="ain">
        <div class="an">Asociación de Turismo · Laguna de Lobos</div>
        <div class="ad">Organizan eventos, controlan el acceso al recurso. Su apoyo al plan provincial de manejo de la laguna es indispensable para legitimar la propuesta.</div>
        <div class="ats"><span class="at" style="background:#DBEAFE;color:#1E40AF;">Aliado potencial</span></div>
      </div>
    </div>
    <div class="ar">
      <div class="ai">🏪</div>
      <div class="ain">
        <div class="an">Cámara de Comercio de Lobos</div>
        <div class="ad">Comercio minorista traccionado por el turismo. Sensibles al discurso antipolítica (votaron LLA). Con propuestas concretas, son recuperables.</div>
        <div class="ats"><span class="at" style="background:#FEF3C7;color:#92400E;">A cultivar</span></div>
      </div>
    </div>
    <div class="ar">
      <div class="ai">🎓</div>
      <div class="ain">
        <div class="an">Centro Universitario de Lobos</div>
        <div class="ad">Tecnicaturas en turismo y administración agraria (convenio UNLZ). Vínculo con jóvenes del municipio. Propuesta: más carreras vinculadas al perfil productivo local.</div>
        <div class="ats"><span class="at" style="background:#EDE9FE;color:#4C1D95;">Multiplicador</span></div>
      </div>
    </div>''',
  'palancas_intro': 'Lo que el intendente gestiona es el municipio. Lo que se ve desde la Provincia es otra escala. Lobos importa por su doble identidad: turismo de la laguna y cuenca lechera. Ambas dependen de decisiones que solo el nivel provincial puede tomar.',
  'palancas': '''<div class="pi o">
      <div class="pt">✅ Inversión con impacto inmediato</div>
      <div class="pti">Plan Integral de Manejo de la Laguna de Lobos</div>
      <div class="pd">La laguna es un recurso hídrico que requiere financiamiento provincial: dragado, control de efluentes, modernización de la costanera. Comprometerse con el plan transforma la visita en un hito. "La Provincia va a ser socia de la Laguna de Lobos."</div>
    </div>
    <div class="pi d">
      <div class="pt">🔵 Decisión de infraestructura provincial</div>
      <div class="pti">Ruta 205 y Ruta 41: conectividad para el turismo y los tambos</div>
      <div class="pd">Ambas rutas son provinciales. Su estado define la viabilidad del turismo de fin de semana y la logística de la cadena lechera. Un plan diferenciado de mantenimiento para las rutas de acceso turístico vale más que muchas promesas.</div>
    </div>
    <div class="pi o">
      <div class="pt">✅ Política agro provincial</div>
      <div class="pti">Banco Provincia + Ministerio Agroindustria: apoyo al eslabón tambero</div>
      <div class="pd">La cuenca lechera de la 3ª sección tiene potencial subutilizado. Créditos preferenciales para productores tamberos y articulación con el sistema de industrialización local. "Lobos produce leche para todo el país. La Provincia lo sabe y lo va a acompañar."</div>
    </div>
    <div class="pi x">
      <div class="pt">⚠️ Riesgo estructural · Prioridad política</div>
      <div class="pti">Volatilidad electoral extrema: LLA puede consolidarse</div>
      <div class="pd">Con LLA en el 52,8%, el riesgo real es que el electorado de Lobos consolide su identidad libertaria. No ir a Lobos, o ir sin propuestas concretas, es cederle ese espacio. La ventana de recuperación es 2025-2026, no después.</div>
    </div>''',
  'anexo1': '''<div class="card">
      <div class="ch" style="background:#ECFDF5;color:#065F46;">🌊 Recurso Turístico</div>
      <div class="cb">
        <div class="st">Laguna de Lobos</div>
        <table class="t">
          <tr><td>Superficie laguna</td><td class="inf">~3.000 ha</td></tr>
          <tr><td>Actividades</td><td>Pesca deportiva, náutica, paracaidismo</td></tr>
          <tr><td>Pico turistas (fin de semana largo)</td><td class="ok">+15.000 visitantes</td></tr>
          <tr><td>Distancia a Buenos Aires</td><td>110 km · Ruta 205</td></tr>
          <tr><td>Plan de Manejo (2026)</td><td class="ok">En ejecución municipal</td></tr>
          <tr><td>Infraestructura costanera</td><td class="warn">En mejora · demanda inversión</td></tr>
        </table>
      </div>
    </div>
    <div class="card">
      <div class="ch" style="background:#F0FDF4;color:#15803D;">🐄 Cuenca Lechera</div>
      <div class="cb">
        <div class="st">Sector Agropecuario</div>
        <table class="t">
          <tr><td>Identidad productiva</td><td class="inf">Cuenca lechera 3ª sección</td></tr>
          <tr><td>Producciones</td><td>Tambos, soja, maíz, girasol, ganadería</td></tr>
          <tr><td>Rol en la economía local</td><td class="ok">Base histórica estable</td></tr>
          <tr><td>Estado de rutas rurales</td><td class="ok">Alteo permanente municipal</td></tr>
          <tr><td>Acceso a crédito Banco Pcia.</td><td class="warn">Demanda mejora</td></tr>
          <tr><td>Asistencia técnica provincial</td><td class="warn">Subutilizada</td></tr>
        </table>
      </div>
    </div>
    <div class="card">
      <div class="ch" style="background:#EFF6FF;color:#1E40AF;">📊 Datos Municipales</div>
      <div class="cb">
        <div class="st">Indicadores generales</div>
        <table class="t">
          <tr><td>Población (Censo 2022)</td><td class="inf">41.760 hab.</td></tr>
          <tr><td>Superficie</td><td>1.726 km²</td></tr>
          <tr><td>Sección Electoral</td><td>3ª · Interior</td></tr>
          <tr><td>Intendente</td><td>Jorge Etcheverry · JxC</td></tr>
          <tr><td>Mandatos consecutivos</td><td class="bad">3 mandatos · Rival político</td></tr>
          <tr><td>Categoría electoral PBA</td><td class="warn">Disputado → LLA ganó 2023</td></tr>
          <tr><td>Distancia a CABA</td><td>~110 km</td></tr>
        </table>
      </div>
    </div>''',
  'anexo2': '''<div class="card">
      <div class="ch" style="background:#FEE2E2;color:#7F1D1D;">🏛️ Gestión Etcheverry · JxC · 3 Mandatos</div>
      <div class="cb">
        <div class="st">Perfil político</div>
        <table class="t" style="margin-bottom:14px;">
          <tr><td>Partido</td><td>Juntos por el Cambio</td></tr>
          <tr><td>Mandatos</td><td class="bad">3er mandato consecutivo</td></tr>
          <tr><td>Perfil</td><td>Intendente consolidado · alto control territorial</td></tr>
          <tr><td>Concejo Deliberante PJ</td><td class="bad">Minoría débil</td></tr>
          <tr><td>Relación con Provincia</td><td class="warn">Transaccional · no natural</td></tr>
        </table>
        <div class="st">Principales hitos de gestión</div>
        <table class="t">
          <tr><td>Infraestructura vial rural</td><td class="ok">Alteo y pavimento barrios periféricos</td></tr>
          <tr><td>Costanera Laguna</td><td class="ok">Obras de modernización</td></tr>
          <tr><td>Seguridad</td><td class="ok">Cámaras LPR en accesos</td></tr>
          <tr><td>Salud (SAME)</td><td class="ok">SAME local + CAPS financiados</td></tr>
          <tr><td>Vivienda</td><td class="ok">Banco de Tierras Municipal</td></tr>
          <tr><td>Educación superior</td><td class="ok">Centro Universitario · tecnicaturas</td></tr>
        </table>
      </div>
    </div>
    <div class="card">
      <div class="ch" style="background:#FFFBEB;color:#78350F;">🗳️ Historia Electoral · Tendencias</div>
      <div class="cb">
        <div class="st">Evolución del voto en Lobos</div>
        <table class="t" style="margin-bottom:14px;">
          <thead><tr><th>Elección</th><th>UxP/PJ</th><th>JxC</th><th>LLA</th><th>Ganador</th></tr></thead>
          <tbody>
            <tr><td>Leg. 2021</td><td class="ok">40,2%</td><td>—</td><td class="warn">31,2%</td><td class="bld">PJ</td></tr>
            <tr><td>PASO 2023</td><td>37,7%</td><td class="ok">43,5%</td><td>16,3%</td><td class="bld">JxC</td></tr>
            <tr><td>Gral 2023</td><td class="warn">31,3%</td><td>—</td><td class="bad">52,8%</td><td class="bld" style="color:#DC2626;">LLA</td></tr>
          </tbody>
        </table>
        <div class="hist">
          <strong>📌 Lectura estratégica</strong>
          <p>El voto de Lobos no es fiel a ningún partido. Es un voto de expectativa. Quien llegue con propuestas concretas y credibilidad tiene posibilidades reales. LLA ganó por la ola nacional, no por arraigo local. La base de recuperación existe: PJ tiene 31% de suelo y el electorado turístico-productivo es persuadible.</p>
        </div>
      </div>
    </div>''',
}

# ─── TAPALQUÉ ──────────────────────────────────────────────────────────────
MUNIS['TAPALQUE'] = {
  'nombre': 'Tapalqué',
  'sub': 'Capital Termal del Interior · 7ª Sección Electoral · Cuenca del Salado · 4.168 km²',
  'tag': 'Campaña PBA 2026 · Uso Reservado · PBA Analytics',
  'hgrad': ('#1E3A5F', '#0369A1'),
  'agrad': ('#1F4E79', '#2563EB'),
  'banner_color': '#22C55E',
  'banner_label': '✅ DISTRITO ALIADO · INTENDENTE UxP · PJ SÓLIDO',
  'banner_title': 'El pueblo que inventó su propia industria',
  'banner_left': '''<p>Tapalqué tenía el problema clásico del interior bonaerense profundo: <strong>mono-dependencia ganadera, emigración de jóvenes y servicios precarios</strong>. La respuesta de la gestión Cocconi fue radical: apostar por las termas.</p>
      <p>En 2019, el Complejo Termal Tapalqué transformó la matriz económica del municipio. Hoy genera cientos de puestos de trabajo en servicios donde antes no había. El turismo termal diversificó lo que era exclusivamente ganadero.</p>''',
  'banner_right': '''<p>El intendente <strong>Gustavo Cocconi (UxP)</strong> es aliado directo. El PJ mantuvo el 47-48% en todos los ciclos electorales medidos. LLA tuvo apenas el 8,1% en el PASO 2023 —muy por debajo del promedio provincial.</p>
      <p>La visita acá no es recuperar —es <strong>consolidar y mostrar</strong>. Que el Estado provincial acompaña el desarrollo del interior, y que el modelo termal de Tapalqué puede ser referencia para la PBA.</p>''',
  'banner_nums': '''<div class="b-num"><div class="n">10.783</div><div class="l">Habitantes<br>Censo 2022</div></div>
    <div class="b-num"><div class="n">47,5%</div><div class="l">PJ/UxP PASO 2023<br>Aliado sólido</div></div>
    <div class="b-num"><div class="n">8,1%</div><div class="l">LLA PASO 2023<br>Muy bajo vs. prom.</div></div>
    <div class="b-num"><div class="n">2019</div><div class="l">Inauguración Termas<br>Punto de inflexión</div></div>''',
  'kpis': '''<div class="kpi" style="background:#EFF6FF;border-color:#93C5FD;">
      <div class="kl">Población (Censo 2022)</div>
      <div class="kv" style="color:#1D4ED8;">10.783</div>
      <div class="ks">Municipio pequeño · Interior profundo</div>
    </div>
    <div class="kpi" style="background:#F0FDF4;border-color:#86EFAC;">
      <div class="kl">UxP/PJ · PASO 2023</div>
      <div class="kv" style="color:#15803D;">47,5%</div>
      <div class="ks">JxC 44,4% · LLA 8,1% · PJ ganó</div>
    </div>
    <div class="kpi" style="background:#ECFDF5;border-color:#6EE7B7;">
      <div class="kl">Vínculo político</div>
      <div class="kv" style="color:#065F46;font-size:16px;">Aliado</div>
      <div class="ks">Cocconi (UxP) · Intendente activo</div>
    </div>
    <div class="kpi" style="background:#EFF6FF;border-color:#93C5FD;">
      <div class="kl">Sección Electoral</div>
      <div class="kv" style="color:#1D4ED8;">7ª</div>
      <div class="ks">Interior profundo bonaerense</div>
    </div>''',
  'intendente': 'Gustavo Cocconi',
  'partido': 'Unión por la Patria',
  'partido_badge': 'ALIADO DIRECTO',
  'seccion': '7ª Sección Electoral',
  'categoria': 'Disputado (favorable)',
  'score_bg': '#F0FDF4',
  'score_fg': '#065F46',
  'score_content': '''<div class="sgrid">
      <div class="sc s">
        <div class="sl">Voto PJ 2021</div>
        <div class="sp" style="color:#059669;">47,8%</div>
        <div class="sd">PJ ganó con claridad. LLA 24%. Base sólida.</div>
      </div>
      <div class="sc p">
        <div class="sl">UxP PASO 2023</div>
        <div class="sp" style="color:#1D4ED8;">47,5%</div>
        <div class="sd">JxC 44,4% · LLA apenas 8,1%</div>
      </div>
    </div>
    <div class="sc" style="border-color:#22C55E;background:#F0FDF4;padding:14px;border-radius:8px;border-left:4px solid #22C55E;margin-top:10px;">
      <div class="sl">Lectura de competitividad</div>
      <div class="sp" style="color:#15803D;font-size:22px;">PJ sólido</div>
      <div class="sd">LLA no logró penetrar. El electorado de Tapalqué es más fiel al peronismo que el promedio provincial. Pero JxC con 44% es una competencia real a monitorear.</div>
    </div>
    <div class="al al-v" style="margin-top:12px;">
      <strong>⚠️ Riesgo de complacencia</strong>
      Un aliado "ganado" que no se trabaja puede debilitarse. La inversión política en Tapalqué tiene alto retorno: intendente fuerte + electorado fiel.
    </div>''',
  'agenda': '''<div class="ag">
      <div class="agi">🌡️</div>
      <div class="agt">
        <strong>Visita al Complejo Termal Tapalqué</strong>
        <p>El símbolo del desarrollo local. Recorrida con el intendente. Mensaje: "esto se hace cuando el municipio y la Provincia trabajan juntos". Anuncio de apoyo provincial para la ampliación.</p>
      </div>
    </div>
    <div class="ag">
      <div class="agi">🥩</div>
      <div class="agt">
        <strong>Recorrida por el Frigorífico Municipal</strong>
        <p>Modelo de gestión: faena en origen, empleos formales, soberanía alimentaria. Propuesta de articulación con la cadena frigorífica provincial y acceso a exportaciones.</p>
      </div>
    </div>
    <div class="ag">
      <div class="agi">🐄</div>
      <div class="agt">
        <strong>Encuentro con productores ganaderos</strong>
        <p>La ganadería extensiva en la Cuenca del Salado es el sustento histórico. Agenda: política hídrica provincial (inundaciones del Salado), crédito Banco Provincia, faena en origen.</p>
      </div>
    </div>
    <div class="al al-v" style="margin-top:12px;">
      <strong>💡 Estrategia de visita</strong>
      Foto de gestión compartida con el intendente aliado. Mostrar que el desarrollo del interior bonaerense tiene nombre: Tapalqué. El modelo termal como ejemplo replicable.
    </div>''',
  'contexto': '''<div class="sgrid">
      <div>
        <div class="st">Diagnóstico electoral</div>
        <table class="t">
          <thead><tr><th>Elección</th><th>PJ/UxP</th><th>JxC</th><th>LLA</th><th>Ganador</th></tr></thead>
          <tbody>
            <tr><td class="bld">Legislativas 2021</td><td class="ok">47,8%</td><td>—</td><td class="warn">24,0%</td><td>PJ</td></tr>
            <tr><td class="bld">PASO 2023</td><td class="ok">47,5%</td><td class="warn">44,4%</td><td>8,1%</td><td>PJ</td></tr>
            <tr><td class="bld">Gral 2023</td><td colspan="4" style="color:#999;font-style:italic;">Datos no disponibles en la matriz</td></tr>
          </tbody>
        </table>
        <div class="al al-v" style="margin-top:10px;">
          <strong>✅ Estabilidad electoral</strong>
          PJ mantiene el 47-48% en todos los ciclos. LLA no penetró (8,1% vs. ~20-25% promedio PBA en PASO 2023). El electorado de Tapalqué es más fiel al peronismo que el promedio provincial.
        </div>
      </div>
      <div>
        <div class="st">Mapa político local</div>
        <table class="t">
          <thead><tr><th>Factor</th><th>Estado</th></tr></thead>
          <tbody>
            <tr><td>Intendente</td><td class="ok">Aliado directo · UxP</td></tr>
            <tr><td>Concejo Deliberante PJ</td><td class="ok">Mayoritario</td></tr>
            <tr><td>Sector ganadero</td><td class="warn">Independiente · sensible a política hídrica</td></tr>
            <tr><td>Sector servicios / termas</td><td class="ok">Alineado con la gestión</td></tr>
            <tr><td>LLA local</td><td class="ok">Débil · sin estructura visible</td></tr>
          </tbody>
        </table>
        <div class="al al-b" style="margin-top:10px;">
          <strong>💡 Lectura estratégica</strong>
          Tapalqué es un activo político que hay que fortalecer. La visita sella la alianza con Cocconi y consolida el voto del interior que el PJ no puede dar por seguro en el marco provincial.
        </div>
      </div>
    </div>''',
  'economia': '''<div class="st">Estructura económica · Tapalqué</div>
    <div class="sgrid">
      <div class="sc t">
        <div class="sl">Turismo Termal · Nuevo motor</div>
        <div class="sn">Complejo Termal Tapalqué</div>
        <div class="sp" style="color:#D97706;">Desde 2019</div>
        <div class="sd">Inaugurado en 2019. Cambió la matriz económica. Genera empleo en servicios donde antes no había: hotelería, gastronomía, cabañas, recreación.</div>
      </div>
      <div class="sc s">
        <div class="sl">Ganadería · Base histórica</div>
        <div class="sn">Cuenca del Salado</div>
        <div class="sp" style="color:#059669;">Extensiva</div>
        <div class="sd">Cría bovina extensiva en grandes campos de la Cuenca del Salado. Sostenible pero vulnerable a inundaciones y ciclos de precio. Frigorífico municipal agrega valor local.</div>
      </div>
    </div>
    <div class="st" style="margin-top:14px;">Ejes de gestión municipal actual</div>
    <div class="pbr"><div class="pbl">Complejo Termal</div><div class="pbo"><div class="pbi" style="width:85%;background:#0369A1;"><span class="pbt">Eje estratégico central</span></div></div><div class="pbp">Alta</div></div>
    <div class="pbr"><div class="pbl">Frigorífico Municipal</div><div class="pbo"><div class="pbi" style="width:70%;background:#059669;"><span class="pbt">Puesta en valor · exportaciones</span></div></div><div class="pbp">Alta</div></div>
    <div class="pbr"><div class="pbl">Educación / Campus</div><div class="pbo"><div class="pbi" style="width:60%;background:#7C3AED;"><span class="pbt">Carreras agro y turismo</span></div></div><div class="pbp">Media</div></div>
    <div class="pbr"><div class="pbl">Biodiesel / Agroecol.</div><div class="pbo"><div class="pbi" style="width:45%;background:#D97706;"><span class="pbt">Planta biodiesel activa</span></div></div><div class="pbp">Media</div></div>''',
  'actores': '''<div class="ar">
      <div class="ai">🌡️</div>
      <div class="ain">
        <div class="an">Complejo Termal Tapalqué</div>
        <div class="ad">El activo más valioso del municipio. Su éxito es el del intendente aliado. La ampliación del complejo depende de financiamiento provincial y conectividad. Visitar las instalaciones es el centro de la agenda.</div>
        <div class="ats"><span class="at" style="background:#D1FAE5;color:#065F46;">Epicentro de la visita</span></div>
      </div>
    </div>
    <div class="ar">
      <div class="ai">🥩</div>
      <div class="ain">
        <div class="an">Frigorífico y Matadero Municipal</div>
        <div class="ad">En operación desde 2013, con puesta en valor reciente. Faena en origen, empleos formales fuera de la municipalidad. Potencial para articular con la cadena provincial de valor.</div>
        <div class="ats"><span class="at" style="background:#DBEAFE;color:#1E40AF;">Política de empleo</span></div>
      </div>
    </div>
    <div class="ar">
      <div class="ai">🐄</div>
      <div class="ain">
        <div class="an">Sociedad Rural de Tapalqué</div>
        <div class="ad">Los ganaderos de cría extensiva del partido. Sensibles a la política hídrica (inundaciones del Salado) y a la logística de faena. Receptivos a propuestas del nivel provincial.</div>
        <div class="ats"><span class="at" style="background:#FEF3C7;color:#92400E;">Diálogo productivo</span></div>
      </div>
    </div>
    <div class="ar">
      <div class="ai">🏛️</div>
      <div class="ain">
        <div class="an">Municipalidad · Cocconi (UxP)</div>
        <div class="ad">Aliado político directo. La visita fortalece su figura ante el electorado local. Gestiona activamente el modelo de desarrollo termal + frigorífico + agroecología.</div>
        <div class="ats"><span class="at" style="background:#EDE9FE;color:#4C1D95;">Aliado clave</span></div>
      </div>
    </div>''',
  'palancas_intro': 'Tapalqué ya demostró que el interior puede reinventarse. Ahora la Provincia puede escalar ese modelo: ampliar el complejo termal, conectar el municipio con el corredor del interior y resolver la deuda histórica hídrica del Salado.',
  'palancas': '''<div class="pi d">
      <div class="pt">🔵 Ampliación con financiamiento provincial</div>
      <div class="pti">Complejo Termal Tapalqué: más capacidad, más turismo</div>
      <div class="pd">La capacidad actual no cubre la demanda en temporada alta. Financiamiento provincial para nuevas piletas, área de hotelería y mejora de accesibilidad. "Tapalqué puede ser el polo termal del interior bonaerense."</div>
    </div>
    <div class="pi d">
      <div class="pt">🔵 Conectividad provincial</div>
      <div class="pti">Rutas al interior: acceso a Tapalqué desde Olavarría, Azul y el corredor</div>
      <div class="pd">Las rutas que conectan Tapalqué con el corredor del interior son provinciales. Mejor accesibilidad = más turistas, más productores que llegan al frigorífico, más integración regional. Una sola obra vial tiene impacto múltiple.</div>
    </div>
    <div class="pi o">
      <div class="pt">✅ Política hídrica provincial</div>
      <div class="pti">Cuenca del Salado: obra hidráulica con impacto directo en el campo</div>
      <div class="pd">Las inundaciones del Salado son la pesadilla cíclica de los ganaderos. La Provincia tiene competencia directa en el manejo hídrico. Comprometerse con obras de sistematización del Salado en la cuenca sur tiene impacto inmediato en el voto rural.</div>
    </div>
    <div class="pi o">
      <div class="pt">✅ Cadena de valor agro-alimentaria</div>
      <div class="pti">Frigorífico municipal como nodo provincial de faena en origen</div>
      <div class="pd">Articular el frigorífico de Tapalqué con la red provincial de faena: mejor acceso a mercados, escala para exportar, mejores precios al productor. Un modelo replicable en municipios similares del interior. "Faena en origen, valor en origen."</div>
    </div>''',
  'anexo1': '''<div class="card">
      <div class="ch" style="background:#EFF6FF;color:#1E40AF;">🌡️ Complejo Termal</div>
      <div class="cb">
        <div class="st">La nueva industria de Tapalqué</div>
        <table class="t">
          <tr><td>Inauguración</td><td class="inf">2019</td></tr>
          <tr><td>Impacto</td><td class="ok">Cientos de empleos en servicios</td></tr>
          <tr><td>Diversificación</td><td class="ok">Hotelería, gastronomía, cabañas</td></tr>
          <tr><td>Capacidad actual</td><td class="warn">Supera demanda en temporada alta</td></tr>
          <tr><td>Necesidad clave</td><td class="bad">Ampliación · financiamiento provincial</td></tr>
          <tr><td>Conectividad</td><td class="warn">Rutas provinciales · mejora pendiente</td></tr>
        </table>
      </div>
    </div>
    <div class="card">
      <div class="ch" style="background:#ECFDF5;color:#065F46;">🥩 Frigorífico Municipal</div>
      <div class="cb">
        <div class="st">Industria local de valor agregado</div>
        <table class="t">
          <tr><td>Inicio de operaciones</td><td class="inf">2013</td></tr>
          <tr><td>Estado</td><td class="ok">Puesta en valor reciente</td></tr>
          <tr><td>Función</td><td>Faena en origen · empleos formales</td></tr>
          <tr><td>Volumen</td><td>Escala local · potencial exportador</td></tr>
          <tr><td>Articulación provincial</td><td class="warn">Pendiente · oportunidad política</td></tr>
          <tr><td>Referencia</td><td>Modelo para municipios similares</td></tr>
        </table>
      </div>
    </div>
    <div class="card">
      <div class="ch" style="background:#F0FDF4;color:#15803D;">📊 Datos Municipales</div>
      <div class="cb">
        <div class="st">Indicadores generales</div>
        <table class="t">
          <tr><td>Población (Censo 2022)</td><td class="inf">10.783 hab.</td></tr>
          <tr><td>Superficie</td><td>4.168 km²</td></tr>
          <tr><td>Sección Electoral</td><td>7ª · Interior profundo</td></tr>
          <tr><td>Intendente</td><td class="ok">Gustavo Cocconi · UxP · Aliado</td></tr>
          <tr><td>Categoría electoral PBA</td><td class="warn">Disputado (favorable PJ)</td></tr>
          <tr><td>Identidad productiva</td><td>Termas + Ganadería extensiva</td></tr>
          <tr><td>Distancia a CABA</td><td>~270 km · Ruta interior</td></tr>
        </table>
      </div>
    </div>''',
  'anexo2': '''<div class="card">
      <div class="ch" style="background:#ECFDF5;color:#065F46;">🏛️ Gestión Cocconi · UxP · Aliado</div>
      <div class="cb">
        <div class="st">Perfil político</div>
        <table class="t" style="margin-bottom:14px;">
          <tr><td>Partido</td><td class="ok">Unión por la Patria · Aliado</td></tr>
          <tr><td>Perfil</td><td>Intendente innovador · modelo termal</td></tr>
          <tr><td>Concejo Deliberante</td><td class="ok">PJ mayoritario</td></tr>
          <tr><td>Relación con Provincia</td><td class="ok">Colaborativa · natural</td></tr>
        </table>
        <div class="st">Principales hitos de gestión</div>
        <table class="t">
          <tr><td>Complejo Termal</td><td class="ok">Inaugurado 2019 · transformación económica</td></tr>
          <tr><td>Frigorífico Municipal</td><td class="ok">Puesta en valor · faena en origen</td></tr>
          <tr><td>Campus Universitario</td><td class="ok">Turismo y gestión ambiental</td></tr>
          <tr><td>Planta biodiesel</td><td class="ok">Energía renovable local</td></tr>
          <tr><td>Salud / Rondas Sanitarias</td><td class="ok">Equipos móviles en parajes rurales</td></tr>
          <tr><td>Agroecología</td><td class="ok">Tapalqué Sostenible · separación de residuos</td></tr>
        </table>
      </div>
    </div>
    <div class="card">
      <div class="ch" style="background:#EFF6FF;color:#1E40AF;">🗳️ Historia Electoral · Tendencias</div>
      <div class="cb">
        <div class="st">Evolución del voto en Tapalqué</div>
        <table class="t" style="margin-bottom:14px;">
          <thead><tr><th>Elección</th><th>PJ/UxP</th><th>JxC</th><th>LLA</th><th>Ganador</th></tr></thead>
          <tbody>
            <tr><td>Leg. 2021</td><td class="ok">47,8%</td><td>—</td><td class="warn">24,0%</td><td class="bld">PJ</td></tr>
            <tr><td>PASO 2023</td><td class="ok">47,5%</td><td class="warn">44,4%</td><td>8,1%</td><td class="bld">PJ</td></tr>
            <tr><td>Gral 2023</td><td colspan="4" style="color:#999;font-style:italic;">Sin datos disponibles</td></tr>
          </tbody>
        </table>
        <div class="hist">
          <strong>📌 Lectura estratégica</strong>
          <p>Tapalqué es uno de los pocos municipios donde LLA no logró penetrar con fuerza. La cohesión del voto peronista responde a la gestión concreta del intendente: las termas, el frigorífico, las rondas sanitarias. JxC con 44% en el PASO 2023 es el único riesgo real a monitorear.</p>
        </div>
        <div class="al al-v" style="margin-top:12px;">
          <strong>✅ Conclusión</strong>
          Visitar Tapalqué es invertir en un aliado que da retornos. Cada visita fortalece a Cocconi, consolida el voto fiel y proyecta el modelo termal como propuesta provincial de desarrollo del interior.
        </div>
      </div>
    </div>''',
}

# Generate files
for key in ['LOBOS', 'TAPALQUE']:
    html = make_ficha(key)
    fname = f"Ficha_Campana_{key}.html"
    with open(fname, 'w') as f:
        f.write(html)
    print(f"✓ {fname}: {len(html):,} bytes")

print("Listo.")
