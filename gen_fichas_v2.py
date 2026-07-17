import re

with open('Ficha_Campana_SAN_NICOLAS.html') as f:
    sn = f.read()
css_match = re.search(r'<style>(.*?)</style>', sn, re.DOTALL)
CSS = css_match.group(1)

# ═══════════════════════════════════════════════════════════════════
# LOBOS
# ═══════════════════════════════════════════════════════════════════
LOBOS_HTML = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>LOBOS — Ficha de Campaña · PBA 2026</title>
<style>{CSS}</style>
</head>
<body>

<!-- HEADER -->
<div class="header" style="background: linear-gradient(135deg, #1F6E4E 0%, #16A34A 100%);">
  <div class="header-left">
    <h1>📍 LOBOS</h1>
    <div class="sub">Ficha de Campaña · Polo Turístico y Cuenca Lechera · 2026</div>
    <div class="tag">3ª Sección Electoral · Centro Bonaerense · 1.726 km² · 110 km de CABA</div>
  </div>
  <div class="header-right">
    <div><strong>Intendente:</strong> Jorge Etcheverry <span class="badge-rival">JxC · 3er mandato</span></div>
    <div><strong>Voto LLA (gral 2023):</strong> 52,8% — Alarma roja</div>
    <div><strong>Población:</strong> 41.760 hab. (Censo 2022)</div>
    <div><strong>Vocación:</strong> Turismo laguna · Cuenca lechera · Agro</div>
    <div style="margin-top:5px;font-size:10px;opacity:0.55;">Datos 2026 · PBA Analytics · MatrizPBA + fuentes verificadas</div>
  </div>
</div>

<!-- BANNER -->
<div class="banner">
  <div class="b-label">⚠️ DISTRITO A RECUPERAR · LLA GANÓ CON 52,8% EN GRAL 2023</div>
  <div class="b-title">La laguna que atrae turistas y vota libertad</div>
  <div class="b-grid">
    <div class="b-col">
      <p><strong>¿Por qué visitar Lobos?</strong> Porque en 2023 La Libertad Avanza se llevó el 52,8% de los votos en un municipio que el PJ había ganado apenas dos años antes. Ese movimiento de 20 puntos en 24 meses no fue ideológico: fue emocional. El electorado de Lobos — turístico, tambero, de clase media rural — sintió que el Estado los ignoraba y se fue con quien prometía sacudirlo. Esa narrativa tiene que romperse con hechos concretos.</p>
      <p><strong>¿Cuál es el activo central?</strong> La Laguna de Lobos. Un espejo de agua de 3.000 hectáreas a 110 km de Buenos Aires que mueve más de 15.000 turistas por fin de semana largo. Pesca deportiva, náutica, paracaidismo, cabañas, gastronomía. Es el motor del municipio. Y ese motor depende de decisiones que el intendente Etcheverry no puede tomar solo: el manejo hídrico, la Ruta 205, el plan turístico provincial.</p>
    </div>
    <div class="b-col">
      <p><strong>¿Qué ve la perspectiva provincial que la gestión local no alcanza?</strong> La Laguna de Lobos como recurso hídrico provincial, no solo como atractivo turístico municipal. El manejo integral del espejo de agua, el control de efluentes, el dragado, la conectividad vial — todo eso excede la escala del municipio. Hay una demanda insatisfecha que solo la Provincia puede cubrir, y LLA no puede ofrecer porque no gobierna PBA.</p>
      <p><strong>¿Cuál es el riesgo de no ir?</strong> Que el voto LLA del 52,8% se consolide como identidad y no como protesta. La diferencia importa: el voto protesta es recuperable, la identidad no lo es. La ventana es ahora, antes de que ese electorado se convenza de que el libertarismo es lo que los representa. Lobos es un ejemplo de lo que la Provincia puede perder si no trabaja el interior.</p>
    </div>
  </div>
  <div class="b-nums">
    <div class="b-num"><div class="n">41.760</div><div class="l">Habitantes (Censo 2022)<br>Municipio intermedio</div></div>
    <div class="b-num"><div class="n">52,8%</div><div class="l">LLA en Gral 2023<br>Desde 16,3% en PASO</div></div>
    <div class="b-num"><div class="n">15.000+</div><div class="l">Turistas por fin de semana<br>largo · Ruta 205</div></div>
    <div class="b-num"><div class="n">3er</div><div class="l">Mandato de Etcheverry<br>JxC · Estructura rival</div></div>
  </div>
</div>

<div class="main">

<!-- KPIs -->
<div class="card full">
  <div class="ch" style="background:#1F6E4E;color:white;">📊 Datos Clave · Lobos</div>
  <div class="cb" style="padding:16px 18px;">
    <div class="kpis">
      <div class="kpi" style="background:#F0FDF4;border-color:#86EFAC;">
        <div class="kl">Población (Censo 2022)</div>
        <div class="kv" style="color:#15803D;">41.760</div>
        <div class="ks">Municipio intermedio · Interior PBA · Centro bonaerense</div>
      </div>
      <div class="kpi" style="background:#FEF2F2;border-color:#FCA5A5;">
        <div class="kl">LLA Gral 2023</div>
        <div class="kv" style="color:#DC2626;">52,8%</div>
        <div class="ks">UxP 31,3% · Diferencia de 21,5 pp · Alarma máxima</div>
      </div>
      <div class="kpi" style="background:#FFFBEB;border-color:#FCD34D;">
        <div class="kl">Dinámica Turística</div>
        <div class="kv" style="color:#92400E;">15.000+</div>
        <div class="ks">Turistas por fin de semana largo · Principal motor económico</div>
      </div>
      <div class="kpi" style="background:#EFF6FF;border-color:#93C5FD;">
        <div class="kl">Partido del intendente</div>
        <div class="kv" style="color:#1D4ED8;font-size:16px;">JxC Rival</div>
        <div class="ks">Etcheverry · 3 mandatos consecutivos · Estructura hostil</div>
      </div>
    </div>
  </div>
</div>

<!-- IDENTIDAD TERRITORIAL -->
<div class="card one">
  <div class="ch" style="background:#ECFDF5;color:#065F46;">🗺️ Identidad Territorial</div>
  <div class="cb">
    <div class="chips">
      <span class="chip cg">🌊 Polo Turístico</span>
      <span class="chip cb">🐄 Cuenca Lechera</span>
      <span class="chip cg">🌾 Agro Pampeano</span>
      <span class="chip co">🚗 Turismo de Weekend</span>
      <span class="chip cr">🗳️ LLA 52,8% 2023</span>
    </div>
    <table class="t">
      <tr><th>Indicador</th><th>Lobos</th><th>Ref. Pcia.</th></tr>
      <tr><td>Superficie</td><td class="bld">1.726 km²</td><td>—</td></tr>
      <tr><td>Distancia a CABA</td><td class="inf">110 km · Ruta 205</td><td>—</td></tr>
      <tr><td>Atractivo principal</td><td class="ok">Laguna · 3.000 ha</td><td>Único en radio</td></tr>
      <tr><td>Saldo migratorio</td><td class="warn">Estable-negativo</td><td>Mixto</td></tr>
      <tr><td>Red vial rural</td><td class="ok">Alta inversión municipal</td><td>—</td></tr>
      <tr><td>Educación superior</td><td class="ok">Centro Univ. · UNLZ</td><td>Bien posicionado</td></tr>
    </table>
    <div class="nt">
      <strong>📌 Posición en el mapa provincial</strong>
      Centro bonaerense, entre la 3ª y la cuenca del Salado. Lobos es el municipio turístico de mayor tracción del interior sin contar Mar del Plata. La Laguna actúa como imán para el AMBA en busca de esparcimiento de bajo costo a corta distancia.
    </div>
    <div class="hist">
      <strong>📜 Historia que sostiene el relato</strong>
      <p>La Laguna de Lobos existía antes que el municipio. La identidad del partido se construyó alrededor del agua: pesca, veraneo, campo. Cuando la Ruta 205 se asfaltó, el turismo explotó. Hoy la economía local y la laguna son indisociables. <strong style="color:#78350F;">El peronismo no construyó Lobos, pero puede construirle el futuro que la laguna necesita.</strong></p>
    </div>
  </div>
</div>

<!-- MATRIZ PRODUCTIVA -->
<div class="card two">
  <div class="ch" style="background:#1F6E4E;color:white;">⚙️ Matriz Productiva · En qué se destaca Lobos</div>
  <div class="cb">
    <div class="st">Sectores Productivos</div>
    <div class="sgrid">
      <div class="sc t">
        <div class="sl">🥇 Motor económico actual</div>
        <div class="sn">Turismo · Laguna de Lobos</div>
        <div class="sp" style="color:#D97706;">~30% actividad</div>
        <div class="sd">La Laguna tracciona gastronomía, hotelería, cabañas, alquiler de equipos náuticos, campings y comercio de insumos de pesca. Picos de más de 15.000 visitantes en fines de semana largos. Sensible a la calidad del agua y la conectividad vial — ambas dependen de la Provincia.</div>
      </div>
      <div class="sc s">
        <div class="sl">🔹 Base económica histórica</div>
        <div class="sn">Cuenca Lechera y Agro</div>
        <div class="sp" style="color:#059669;">~25% actividad</div>
        <div class="sd">Tambos de primera línea y producción agrícola (soja, maíz, girasol). La cuenca lechera de la 3ª sección tiene escala y calidad. Los productores tamberos son los principales empleadores rurales del partido. Su voto: PJ en 2021, LLA en 2023.</div>
      </div>
      <div class="sc p">
        <div class="sl">🔸 Derivada del turismo y el campo</div>
        <div class="sn">Comercio y Servicios Locales</div>
        <div class="sp" style="color:#1D4ED8;">~35% actividad</div>
        <div class="sd">El comercio del casco urbano vive del turismo estacional y del salario rural. Alta sensibilidad al ciclo agrícola y a los fines de semana. El 2023 post-pandemia fue bueno para el comercio, pero la inflación y la recesión 2024-25 golpearon al pequeño comerciante.</div>
      </div>
      <div class="sc e">
        <div class="sl">🔸 Sector emergente</div>
        <div class="sn">Educación y Servicios Universitarios</div>
        <div class="sp" style="color:#6D28D9;">Crecimiento</div>
        <div class="sd">El Centro Universitario de Lobos (convenio UNLZ) ofrece tecnicaturas en turismo sustentable y administración agraria. Un activo de largo plazo que la Provincia puede ampliar con nuevas carreras técnicas ligadas al perfil productivo local.</div>
      </div>
    </div>

    <div class="st">Estructura de Actividad Estimada</div>
    <div class="pbr"><div class="pbl">Comercio y Servicios</div><div class="pbo"><div class="pbi" style="width:70%;background:#2563EB"><div class="pbt">~35%</div></div></div><div class="pbp" style="color:#2563EB;">35%</div></div>
    <div class="pbr"><div class="pbl">Turismo · Laguna</div><div class="pbo"><div class="pbi" style="width:60%;background:#D97706"><div class="pbt">~30%</div></div></div><div class="pbp" style="color:#D97706;">30%</div></div>
    <div class="pbr"><div class="pbl">Agropecuario · Tambo</div><div class="pbo"><div class="pbi" style="width:50%;background:#059669"><div class="pbt">~25%</div></div></div><div class="pbp" style="color:#059669;">25%</div></div>
    <div class="pbr"><div class="pbl">Construcción / Otros</div><div class="pbo"><div class="pbi" style="width:20%;background:#7C3AED"><div class="pbt">~10%</div></div></div><div class="pbp" style="color:#7C3AED;">10%</div></div>

    <div class="st" style="margin-top:18px;">Actores Clave del Territorio</div>
    <div class="ar">
      <div class="ai">🌊</div>
      <div class="ain">
        <div class="an">Asociación de Turismo y Pesca · Laguna de Lobos</div>
        <div class="ad">Organiza y regula las actividades turísticas en la laguna: pesca deportiva, náutica, paracaidismo, campings. Su aval es indispensable para cualquier anuncio de plan de manejo. Interlocutores naturales para la visita. Son el puente entre el discurso provincial y el comercio turístico local.</div>
        <div class="ats">
          <span class="at" style="background:#D1FAE5;color:#065F46;">Aliado potencial</span>
          <span class="at" style="background:#DBEAFE;color:#1E40AF;">Contacto previo recomendado</span>
        </div>
      </div>
    </div>
    <div class="ar">
      <div class="ai">🐄</div>
      <div class="ain">
        <div class="an">Cooperativas y Tambos · Cuenca Lechera 3ª Sección</div>
        <div class="ad">Los productores tamberos del partido son quizás el grupo que más se alejó del PJ hacia LLA. Votan campo. Sensibles a crédito, costo de flete, estado de las rutas rurales y política de precios de leche. Una reunión con referentes del sector, más un anuncio de crédito Banco Provincia, tiene efecto inmediato.</div>
        <div class="ats">
          <span class="at" style="background:#FEF3C7;color:#92400E;">Recuperación clave</span>
          <span class="at" style="background:#FEE2E2;color:#7F1D1D;">Voto LLA 2023</span>
        </div>
      </div>
    </div>
    <div class="ar">
      <div class="ai">🏪</div>
      <div class="ain">
        <div class="an">Cámara de Comercio de Lobos</div>
        <div class="ad">El comercio minorista y gastronómico vive del turismo de la laguna. En 2023 votaron mayoritariamente LLA. Son recuperables con propuestas concretas: financiamiento para equipamiento gastronómico, posicionamiento de Lobos en el circuito bonaerense oficial. No son ideológicos — son pragmáticos.</div>
        <div class="ats">
          <span class="at" style="background:#FEF3C7;color:#92400E;">A cultivar</span>
          <span class="at" style="background:#F3F4F6;color:#374151;">Voto volátil</span>
        </div>
      </div>
    </div>
    <div class="ar">
      <div class="ai">🎓</div>
      <div class="ain">
        <div class="an">Centro Universitario de Lobos · Convenio UNLZ</div>
        <div class="ad">Tecnicaturas en turismo sustentable y administración agraria. Vínculo con jóvenes del municipio que no migran al Gran Buenos Aires. La Provincia puede ampliar la oferta educativa y financiar nuevas tecnicaturas ligadas al manejo de recursos naturales y a la logística agropecuaria.</div>
        <div class="ats">
          <span class="at" style="background:#EDE9FE;color:#4C1D95;">Multiplicador generacional</span>
          <span class="at" style="background:#D1FAE5;color:#065F46;">Inversión provincia posible</span>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- PERSPECTIVA PROVINCIAL -->
<div class="card full">
  <div class="ch" style="background:#0f2944;color:#FACC15;">👁️ Perspectiva Provincial · Palancas que solo el nivel provincial puede activar</div>
  <div class="cb">
    <p style="font-size:12px;color:#666;margin-bottom:16px;line-height:1.7;">Etcheverry puede gestionar el municipio — el alumbrado, la costanera, el SAME. Lo que no puede hacer es manejar el recurso hídrico de la laguna, sostener las rutas provinciales o posicionar a Lobos en el circuito turístico oficial de Buenos Aires. Esas son palancas de otro nivel.</p>
    <div class="pgrid">
      <div class="pi o">
        <div class="pt">✅ Inversión con impacto inmediato</div>
        <div class="pti">Plan Integral de Manejo de la Laguna de Lobos</div>
        <div class="pd">La laguna es un recurso hídrico provincial que requiere intervención sistemática: dragado, control de efluentes de campos y urbanizaciones cercanas, monitoreo de calidad de agua, modernización de la costanera. Comprometerse con el plan de manejo transforma la visita en un hito. "La Provincia va a ser socia permanente de la Laguna de Lobos."</div>
      </div>
      <div class="pi d">
        <div class="pt">🔵 Decisión de infraestructura vial</div>
        <div class="pti">Ruta 205 y Ruta 41: la conectividad que hace posible el turismo y la lechería</div>
        <div class="pd">Ambas rutas son provinciales y son la columna vertebral de la economía de Lobos. Sin Ruta 205 en buen estado no hay turismo de fin de semana. Sin Ruta 41 la lechería pierde competitividad. Un plan diferenciado de mantenimiento para las rutas de acceso turístico y agroindustrial tiene efecto directo sobre los dos sectores que definen el voto local.</div>
      </div>
      <div class="pi d">
        <div class="pt">🔵 Política agroalimentaria provincial</div>
        <div class="pti">Banco Provincia + MAGYP: apoyo a los productores tamberos de la 3ª sección</div>
        <div class="pd">La cuenca lechera de la 3ª sección tiene potencial productivo subutilizado por falta de crédito accesible y asistencia técnica. Articular el Banco Provincia con el Ministerio de Agroindustria provincial para ofrecer líneas específicas para pequeños y medianos tamberos de la zona. "La leche que produce Lobos alimenta al país. La Provincia lo sabe y va a acompañar."</div>
      </div>
      <div class="pi o">
        <div class="pt">✅ Agenda de turismo provincial</div>
        <div class="pti">Lobos en el circuito bonaerense oficial: de destino informal a polo turístico de la Provincia</div>
        <div class="pd">Lobos recibe 15.000 turistas por fin de semana largo pero no aparece en ningún circuito turístico oficial de la Provincia. Incluirlo en el plan de turismo bonaerense, la señalética en rutas nacionales y provinciales, el apoyo a eventos de pesca deportiva de escala: todo suma visibilidad sin costo municipal y genera aliados entre el sector gastronómico y hotelero.</div>
      </div>
      <div class="pi r">
        <div class="pt">⚠️ Riesgo ambiental · Urgencia</div>
        <div class="pti">Calidad del agua de la laguna: el activo en riesgo</div>
        <div class="pd">La laguna tiene historial de floraciones de algas (cianobacterias) en veranos de calor extremo, agravadas por efluentes rurales y aguas residuales no tratadas. Un episodio grave en temporada alta puede destruir una temporada turística. El monitoreo y las obras de saneamiento son competencia provincial. Si la laguna se enferma, Lobos se queda sin turismo y sin argumento.</div>
      </div>
      <div class="pi x">
        <div class="pt">🔴 Tensión política · Navegar con cuidado</div>
        <div class="pti">Presencia provincial sin confrontar al intendente JxC</div>
        <div class="pd">Etcheverry tiene tres mandatos y control territorial. El error sería ir a Lobos a disputarle su gestión. La estrategia: hablar desde la Provincia hacia arriba — la laguna, las rutas, la cuenca lechera — sin tocar lo municipal. La gente percibe la diferencia entre quien viene a sumar y quien viene a competir.</div>
      </div>
    </div>
    <div class="corr">
      <h3>🌊 Corredor Turístico Interior 3ª Sección · La dimensión regional</h3>
      <p>Lobos no está solo. Es el nodo más fuerte de un corredor de turismo de fin de semana y agroturismo en la 3ª sección que incluye municipios con recursos naturales y gastronómicos complementarios. Una política provincial que integre este corredor multiplica el impacto de cada peso invertido.</p>
      <div class="cms">
        <div class="cm">📍 LOBOS<span>Laguna · pesca · náutica</span></div>
        <div class="cm">↔ ROQUE PÉREZ<span>Reserva Natural · rural</span></div>
        <div class="cm">↔ SALADILLO<span>Turismo rural · agro</span></div>
        <div class="cm">↔ MONTE<span>Cuenca lechera · campo</span></div>
        <div class="cm">↔ CAÑUELAS<span>Caballos · agro · polo</span></div>
      </div>
    </div>
  </div>
</div>

<!-- ANÁLISIS POLÍTICO DEL MOMENTO -->
<div class="card two">
  <div class="ch" style="background:#FFFBEB;color:#78350F;">📈 Análisis del Momento · LLA 52,8% y lo que revela</div>
  <div class="cb">
    <div class="st">Diagnóstico electoral · Evolución del voto</div>
    <table class="t" style="margin-bottom:16px;">
      <thead><tr><th>Elección</th><th>PJ / UxP</th><th>JxC</th><th>LLA</th><th>Ganador</th></tr></thead>
      <tbody>
        <tr><td class="bld">Legislativas 2021</td><td class="ok">40,2%</td><td>—</td><td class="warn">31,2%</td><td>PJ</td></tr>
        <tr><td class="bld">PASO 2023</td><td>37,7%</td><td class="ok">43,5%</td><td>16,3%</td><td>JxC</td></tr>
        <tr><td class="bld">General 2023</td><td class="warn">31,3%</td><td>—</td><td class="bad">52,8%</td><td style="color:#DC2626;font-weight:700;">LLA</td></tr>
      </tbody>
    </table>
    <div class="ag">
      <div class="agi">🔴</div>
      <div class="agt">
        <strong>Causa: volatilidad del electorado rural y turístico</strong>
        <p>El electorado de Lobos no tiene identidad partidaria fija. El tambero, el comerciante gastronómico, el propietario de cabañas — son votantes de resultado, no de lealtad. En 2021 votaron PJ porque "había que darle una chance". En el PASO 2023 probaron JxC. En la general 2023 se fueron con LLA porque el discurso de cambio radical era el más fuerte. Cada elección es una nueva partida.</p>
      </div>
    </div>
    <div class="ag">
      <div class="agi">🟡</div>
      <div class="agt">
        <strong>Señal: LLA creció del 16% al 52% en tres meses</strong>
        <p>Ese salto de 36 puntos entre el PASO y la general indica que no es un voto de convicción: es de ola. Los votantes de JxC migran masivamente a LLA en la general. El suelo LLA propio en Lobos probablemente es 20-25%. El resto es ola trasvasada. Eso es recuperable con trabajo territorial y propuesta concreta.</p>
      </div>
    </div>
    <div class="ag" style="border-bottom:none;">
      <div class="agi">🟢</div>
      <div class="agt">
        <strong>Apertura: el electorado de Lobos es pragmático — responde a propuestas</strong>
        <p>El 31,3% de UxP en la general 2023 es el suelo propio. Sobre ese piso hay espacio real de crecimiento si la propuesta es concreta (la laguna, las rutas, el crédito tambero) y si hay presencia física. Lobos no está perdido — está esperando que alguien llegue con algo tangible.</p>
      </div>
    </div>
    <div class="al al-a">
      <strong>⚠️ El riesgo que no puede ignorarse</strong>
      Si LLA logra consolidar estructura local y candidatos propios en las elecciones de 2025-2027, el 52,8% puede transformarse en mayoría estable. La ventana de recuperación es ahora, cuando ese voto sigue siendo protest y no identidad. Después puede ser tarde.
    </div>
  </div>
</div>

<!-- AGENDA DE DISCURSO -->
<div class="card one">
  <div class="ch" style="background:#1F6E4E;color:white;">🎤 Agenda de Discurso · Perspectiva Provincial</div>
  <div class="cb">
    <div class="st">Ejes · Por prioridad de impacto</div>
    <div class="ag">
      <div class="agi">🌊</div>
      <div class="agt">
        <strong>1. La laguna como responsabilidad provincial</strong>
        <p>"La Laguna de Lobos no es solo del municipio — es de toda la Provincia. Y la Provincia va a asumir esa responsabilidad."</p>
      </div>
    </div>
    <div class="ag">
      <div class="agi">🛣️</div>
      <div class="agt">
        <strong>2. Rutas que conectan el campo con el mercado</strong>
        <p>"El tambero de Lobos produce leche todos los días. La Ruta 205 tiene que estar en condiciones todos los días."</p>
      </div>
    </div>
    <div class="ag">
      <div class="agi">🐄</div>
      <div class="agt">
        <strong>3. Crédito para quien produce</strong>
        <p>Banco Provincia con líneas específicas para tamberos y pequeños productores agropecuarios. Anuncio tangible de resultado inmediato.</p>
      </div>
    </div>
    <div class="ag">
      <div class="agi">🎓</div>
      <div class="agt">
        <strong>4. Educación con perfil productivo</strong>
        <p>Ampliación del Centro Universitario con nuevas tecnicaturas ligadas al manejo del agua y a la logística agroindustrial. Para que los jóvenes de Lobos puedan quedarse.</p>
      </div>
    </div>
    <div class="ag" style="border-bottom:none;">
      <div class="agi">🚫</div>
      <div class="agt">
        <strong>Qué evitar</strong>
        <p>Hablar de asistencialismo social. Atacar a Etcheverry. Prometer obras de escala municipal. Hablar de política nacional. Lo que mueve a Lobos es la laguna y el campo — el resto no conecta.</p>
      </div>
    </div>
    <div class="al al-k">
      <strong>⚡ La frase que sintetiza la visita</strong>
      "Lobos tiene el activo. La Provincia tiene la escala. Juntos podemos hacer de esta laguna el polo turístico más importante del interior bonaerense."
    </div>
  </div>
</div>

</div>

<div class="footer">
  🔒 USO RESERVADO · Campaña PBA · Ficha Lobos · PBA Analytics 2026
</div>

<!-- ANEXO I -->
<div style="page-break-before:always;break-before:page;height:0;margin:0;padding:0;font-size:0;"></div>
<div>
  <div style="background:linear-gradient(135deg,#1F6E4E,#16A34A);color:white;padding:20px 32px;display:flex;justify-content:space-between;align-items:center;">
    <div>
      <div style="font-size:11px;opacity:0.6;letter-spacing:2px;text-transform:uppercase;margin-bottom:4px;">Lobos · Campaña PBA 2026</div>
      <div style="font-size:22px;font-weight:900;letter-spacing:1px;">ANEXO I — PRINCIPALES INDICADORES</div>
    </div>
    <div style="font-size:11px;opacity:0.7;text-align:right;">3ª Sección Electoral · Interior<br>PBA Analytics 2026</div>
  </div>
  <div style="padding:20px 24px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px;background:#eef2f7;">

    <div class="card">
      <div class="ch" style="background:#ECFDF5;color:#065F46;">🌊 Recurso Turístico · Laguna</div>
      <div class="cb">
        <div class="st">La Laguna de Lobos</div>
        <table class="t">
          <tr><td>Superficie</td><td class="inf">~3.000 hectáreas</td></tr>
          <tr><td>Actividades</td><td>Pesca deportiva, náutica, paracaidismo, camping</td></tr>
          <tr><td>Turistas (fin de semana largo)</td><td class="ok">+15.000 visitantes</td></tr>
          <tr><td>Distancia a CABA</td><td>110 km · Ruta 205</td></tr>
          <tr><td>Estado del agua</td><td class="warn">Riesgo estacional cianobacterias</td></tr>
          <tr><td>Plan de Manejo Municipal</td><td class="ok">En curso desde 2025</td></tr>
          <tr><td>Intervención provincial</td><td class="bad">Pendiente · demanda urgente</td></tr>
        </table>
      </div>
    </div>

    <div class="card">
      <div class="ch" style="background:#F0FDF4;color:#15803D;">🐄 Sector Agropecuario</div>
      <div class="cb">
        <div class="st">Cuenca lechera y agro</div>
        <table class="t">
          <tr><td>Perfil productivo</td><td class="inf">Tambo + soja/maíz/girasol</td></tr>
          <tr><td>Cuenca lechera</td><td class="ok">3ª sección · primera línea</td></tr>
          <tr><td>Acceso vial rural</td><td class="ok">Alta inversión municipal (alteo)</td></tr>
          <tr><td>Crédito Banco Provincia</td><td class="warn">Subutilizado · oportunidad</td></tr>
          <tr><td>Asistencia técnica MAGYP</td><td class="warn">Escasa presencia en campo</td></tr>
          <tr><td>Exportación granaria</td><td>Vía mercados de la región</td></tr>
          <tr><td>Voto productores 2023</td><td class="bad">LLA · recuperación clave</td></tr>
        </table>
      </div>
    </div>

    <div class="card">
      <div class="ch" style="background:#EFF6FF;color:#1E40AF;">📊 Datos Municipales Generales</div>
      <div class="cb">
        <div class="st">Indicadores de base</div>
        <table class="t">
          <tr><td>Población (Censo 2022)</td><td class="inf">41.760 hab.</td></tr>
          <tr><td>Superficie</td><td>1.726 km²</td></tr>
          <tr><td>Sección Electoral</td><td>3ª · Interior bonaerense</td></tr>
          <tr><td>Intendente</td><td class="bad">Jorge Etcheverry · JxC · Rival</td></tr>
          <tr><td>Mandatos consecutivos</td><td class="bad">3er mandato</td></tr>
          <tr><td>Categoría electoral</td><td class="warn">Disputado → LLA ganó 2023</td></tr>
          <tr><td>Distancia a CABA</td><td>~110 km · Ruta 205</td></tr>
          <tr><td>Seguridad vial</td><td class="ok">Cámaras LPR Rutas 205 y 41</td></tr>
        </table>
      </div>
    </div>

    <div class="card">
      <div class="ch" style="background:#FFFBEB;color:#78350F;">🏛️ Gestión Municipal Actual</div>
      <div class="cb">
        <div class="st">Etcheverry · JxC · Hitos 2023-2026</div>
        <table class="t">
          <tr><td>Vial rural</td><td class="ok">Alteo permanente · presupuesto prioritario</td></tr>
          <tr><td>Pavimentación urbana</td><td class="ok">Barrios periféricos · Empalme Lobos</td></tr>
          <tr><td>Costanera Laguna</td><td class="ok">Nuevos espacios recreativos</td></tr>
          <tr><td>Turismo</td><td class="ok">Plan de Manejo 2026 activo</td></tr>
          <tr><td>Seguridad</td><td class="ok">Centro de Monitoreo · cámaras LPR</td></tr>
          <tr><td>Salud</td><td class="ok">SAME local + CAPS barrios</td></tr>
          <tr><td>Vivienda</td><td class="ok">Banco de Tierras Municipal</td></tr>
          <tr><td>Educación superior</td><td class="ok">Centro Univ. · tecnicaturas</td></tr>
        </table>
      </div>
    </div>

    <div class="card">
      <div class="ch" style="background:#FEE2E2;color:#7F1D1D;">🗳️ Historial Electoral</div>
      <div class="cb">
        <div class="st">Evolución del voto · Lobos</div>
        <table class="t">
          <thead><tr><th>Elección</th><th>PJ/UxP</th><th>JxC</th><th>LLA</th><th>Resultado</th></tr></thead>
          <tbody>
            <tr><td>Leg. 2021</td><td class="ok">40,2%</td><td>—</td><td class="warn">31,2%</td><td class="bld">PJ</td></tr>
            <tr><td>PASO 2023</td><td>37,7%</td><td class="ok">43,5%</td><td>16,3%</td><td class="bld">JxC</td></tr>
            <tr><td>Gral 2023</td><td class="warn">31,3%</td><td>—</td><td class="bad">52,8%</td><td class="bld" style="color:#DC2626;">LLA</td></tr>
          </tbody>
        </table>
        <div class="hist" style="margin-top:10px;">
          <strong>📌 Tendencia</strong>
          <p>Volatilidad estructural. LLA pasó de 16% a 52% en 3 meses. El suelo PJ propio es ~31%. La recuperación requiere propuesta concreta y presencia territorial. Lobos no es peronista ni liberal — es pragmático.</p>
        </div>
      </div>
    </div>

    <div class="card">
      <div class="ch" style="background:#F5F3FF;color:#4C1D95;">🎯 Prioridad Estratégica</div>
      <div class="cb">
        <div class="st">Posición en el mapa de campaña</div>
        <table class="t">
          <tr><td>Clasificación PBA</td><td class="warn">Disputado</td></tr>
          <tr><td>Urgencia política</td><td class="bad">Alta · LLA ganó</td></tr>
          <tr><td>Potencial de recuperación</td><td class="ok">Alto · voto no fidelizado</td></tr>
          <tr><td>Palanca principal</td><td class="inf">Laguna + Rutas + Crédito</td></tr>
          <tr><td>Vínculo con intendente</td><td class="bad">Rival · no confrontar</td></tr>
          <tr><td>Perfil electorado</td><td>Rural / turístico / clase media</td></tr>
          <tr><td>Tipo de voto LLA</td><td class="warn">Protest vote · recuperable</td></tr>
        </table>
      </div>
    </div>

  </div>
  <div style="text-align:center;padding:12px;font-size:11px;color:#aaa;background:white;border-top:1px solid #e5e7eb;">
    🔒 USO RESERVADO · ANEXO I · Lobos · PBA Analytics 2026
  </div>
</div>

<!-- ANEXO II -->
<div style="page-break-before:always;break-before:page;height:0;margin:0;padding:0;font-size:0;"></div>
<div>
  <div style="background:linear-gradient(135deg,#78350F,#D97706);color:white;padding:20px 32px;display:flex;justify-content:space-between;align-items:center;">
    <div>
      <div style="font-size:11px;opacity:0.6;letter-spacing:2px;text-transform:uppercase;margin-bottom:4px;">Lobos · 2026</div>
      <div style="font-size:22px;font-weight:900;letter-spacing:1px;">ANEXO II — GESTIÓN LOCAL Y DATOS DE CONTEXTO</div>
    </div>
    <div style="font-size:11px;opacity:0.7;text-align:right;">Gestión Etcheverry · JxC<br>3er mandato · Rival</div>
  </div>
  <div style="padding:20px 24px;display:grid;grid-template-columns:1fr 1fr;gap:16px;background:#eef2f7;">

    <div class="card">
      <div class="ch" style="background:#FEE2E2;color:#7F1D1D;">🏛️ Gestión Etcheverry · JxC · Diagnóstico</div>
      <div class="cb">
        <div class="st">Fortalezas y debilidades desde la mirada provincial</div>
        <table class="t" style="margin-bottom:14px;">
          <tr><td>Perfil político</td><td>Intendente consolidado · bajo perfil ideológico · pragmático</td></tr>
          <tr><td>Legitimidad local</td><td class="bad">Alta · 3 mandatos consecutivos</td></tr>
          <tr><td>Estructura opositora PJ</td><td class="bad">Débil · Concejo en minoría</td></tr>
          <tr><td>Relación con la Provincia</td><td class="warn">Transaccional · no natural</td></tr>
          <tr><td>Agenda turística</td><td class="ok">Activa · centrada en la laguna</td></tr>
          <tr><td>Agenda agropecuaria</td><td class="ok">Fuerte en vial rural</td></tr>
          <tr><td>Agenda social</td><td class="warn">Moderada · CAPS y SAME</td></tr>
        </table>
        <div class="al al-b">
          <strong>💡 Estrategia de convivencia</strong>
          No disputar el terreno municipal. Llegar con propuestas que Etcheverry no puede vetar porque exceden su jurisdicción: manejo de la laguna, rutas provinciales, circuito turístico oficial. La agenda provincial no compite con la municipal — la complementa.
        </div>
      </div>
    </div>

    <div class="card">
      <div class="ch" style="background:#F0FDF4;color:#15803D;">🌊 Programa Municipal · Laguna y Desarrollo</div>
      <div class="cb">
        <div class="st">Principales programas en ejecución</div>
        <table class="t" style="margin-bottom:14px;">
          <tr><td>Plan de Manejo Laguna</td><td class="ok">Dragado + control efluentes en proceso</td></tr>
          <tr><td>Costanera</td><td class="ok">Nuevos espacios recreativos 2025-26</td></tr>
          <tr><td>Ruta 205 (tramo urbano)</td><td class="ok">Mantenimiento municipal</td></tr>
          <tr><td>Puesta en Valor Laguna</td><td class="ok">Campings regulados · infraestructura</td></tr>
          <tr><td>LPR (seguridad vial)</td><td class="ok">Cámaras en accesos Rtas 205 y 41</td></tr>
          <tr><td>SAME local</td><td class="ok">Base operativa municipal activa</td></tr>
          <tr><td>Banco de Tierras</td><td class="ok">Lotes para familias jóvenes</td></tr>
        </table>
        <div class="al al-v">
          <strong>✅ Señal</strong>
          La gestión municipal tiene razonable nivel de obra concreta. Lo que falta es la escala provincial: el recurso hídrico de la laguna no puede manejarse solo desde el municipio. Ahí está el espacio político disponible.
        </div>
      </div>
    </div>

  </div>
  <div style="text-align:center;padding:12px;font-size:11px;color:#aaa;background:white;border-top:1px solid #e5e7eb;">
    🔒 USO RESERVADO · ANEXO II · Lobos · PBA Analytics 2026
  </div>
</div>

</body>
</html>"""

with open('Ficha_Campana_LOBOS.html', 'w') as f:
    f.write(LOBOS_HTML)
print(f"✓ LOBOS: {len(LOBOS_HTML):,} bytes")

# ═══════════════════════════════════════════════════════════════════
# TAPALQUÉ
# ═══════════════════════════════════════════════════════════════════
TAPALQUE_HTML = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TAPALQUÉ — Ficha de Campaña · PBA 2026</title>
<style>{CSS}</style>
</head>
<body>

<!-- HEADER -->
<div class="header" style="background: linear-gradient(135deg, #1E3A5F 0%, #0369A1 100%);">
  <div class="header-left">
    <h1>📍 TAPALQUÉ</h1>
    <div class="sub">Ficha de Campaña · Capital Termal del Interior · 2026</div>
    <div class="tag">7ª Sección Electoral · Cuenca del Salado · Interior Profundo · 4.168 km²</div>
  </div>
  <div class="header-right">
    <div><strong>Intendente:</strong> Gustavo Cocconi <span style="display:inline-block;padding:2px 10px;border-radius:20px;font-size:11px;font-weight:700;background:rgba(34,197,94,0.6);margin-left:6px;">UxP · ALIADO</span></div>
    <div><strong>Voto PJ (PASO 2023):</strong> 47,5% — Territorio fiel</div>
    <div><strong>Población:</strong> 10.783 hab. (Censo 2022)</div>
    <div><strong>Vocación:</strong> Termas · Ganadería extensiva · Cuenca del Salado</div>
    <div style="margin-top:5px;font-size:10px;opacity:0.55;">Datos 2026 · PBA Analytics · MatrizPBA + fuentes verificadas</div>
  </div>
</div>

<!-- BANNER -->
<div class="banner" style="border-left-color:#22C55E;">
  <div class="b-label">✅ DISTRITO ALIADO · INTENDENTE UxP · PJ SÓLIDO AL 47-48%</div>
  <div class="b-title">El pueblo que decidió inventar su propia industria</div>
  <div class="b-grid">
    <div class="b-col">
      <p><strong>¿Por qué visitar Tapalqué?</strong> Porque Tapalqué hizo algo que muy pocos municipios del interior bonaerense lograron: salir de la mono-dependencia ganadera a través de una apuesta propia, sin esperar que el Estado nacional o provincial lo rescatara. En 2019, inauguró el Complejo Termal que transformó su matriz económica. Visitar Tapalqué es mostrar que el desarrollo del interior es posible cuando el gobierno municipal y la Provincia trabajan con visión.</p>
      <p><strong>¿Cuál es el momento?</strong> El momento de escala. Las termas ya demostraron que funcionan. El frigorífico municipal ya genera empleo formal. El campus universitario ya forma jóvenes. Lo que falta es el salto de escala que solo puede venir desde la Provincia: ampliación del complejo termal, conectividad vial para el turismo, sistematización hídrica del Salado para los ganaderos. Tapalqué está listo para crecer. La Provincia tiene que aparecer.</p>
    </div>
    <div class="b-col">
      <p><strong>¿Qué ve la perspectiva provincial que la gestión local no alcanza?</strong> La posición de Tapalqué en el corredor del interior bonaerense. No es solo un municipio con termas: es el nodo que puede articular turismo termal, ganadería de calidad y agroindustria sustentable en la 7ª sección. Desde la Provincia se puede proponer una agenda regional de desarrollo del interior que Tapalqué puede liderar simbólicamente.</p>
      <p><strong>¿Cuál es el riesgo de no ir?</strong> El riesgo es la complacencia. Un distrito aliado que se da por garantizado tiende a debilitarse. El intendente Cocconi necesita poder mostrarle a su electorado que tener un aliado en la Provincia sirve para algo concreto. Si la visita no viene con anuncios tangibles, la alianza se mantiene pero la narrativa se debilita. Y JxC con 44% en el PASO 2023 es una competencia real que no puede ignorarse.</p>
    </div>
  </div>
  <div class="b-nums">
    <div class="b-num"><div class="n">10.783</div><div class="l">Habitantes (Censo 2022)<br>Interior profundo PBA</div></div>
    <div class="b-num"><div class="n">47,5%</div><div class="l">PJ/UxP · PASO 2023<br>Territorio fiel al peronismo</div></div>
    <div class="b-num"><div class="n">2019</div><div class="l">Inauguración Complejo Termal<br>Punto de inflexión económica</div></div>
    <div class="b-num"><div class="n">8,1%</div><div class="l">LLA en PASO 2023<br>Muy bajo vs promedio PBA</div></div>
  </div>
</div>

<div class="main">

<!-- KPIs -->
<div class="card full">
  <div class="ch" style="background:#1E3A5F;color:white;">📊 Datos Clave · Tapalqué</div>
  <div class="cb" style="padding:16px 18px;">
    <div class="kpis">
      <div class="kpi" style="background:#EFF6FF;border-color:#93C5FD;">
        <div class="kl">Población (Censo 2022)</div>
        <div class="kv" style="color:#1D4ED8;">10.783</div>
        <div class="ks">Municipio pequeño · Interior profundo bonaerense</div>
      </div>
      <div class="kpi" style="background:#F0FDF4;border-color:#86EFAC;">
        <div class="kl">UxP/PJ · PASO 2023</div>
        <div class="kv" style="color:#15803D;">47,5%</div>
        <div class="ks">JxC 44,4% · LLA solo 8,1% · PJ ganó</div>
      </div>
      <div class="kpi" style="background:#ECFDF5;border-color:#6EE7B7;">
        <div class="kl">Vínculo con candidato</div>
        <div class="kv" style="color:#065F46;font-size:15px;">Aliado</div>
        <div class="ks">Cocconi (UxP) · Activo · Gestión modelo</div>
      </div>
      <div class="kpi" style="background:#FFFBEB;border-color:#FCD34D;">
        <div class="kl">Superficie · Extensión</div>
        <div class="kv" style="color:#92400E;font-size:18px;">4.168 km²</div>
        <div class="ks">Gran municipio rural · Interior 7ª sección</div>
      </div>
    </div>
  </div>
</div>

<!-- IDENTIDAD TERRITORIAL -->
<div class="card one">
  <div class="ch" style="background:#EFF6FF;color:#1E40AF;">🗺️ Identidad Territorial</div>
  <div class="cb">
    <div class="chips">
      <span class="chip cb">🌡️ Polo Termal</span>
      <span class="chip cg">🐄 Ganadería Extensiva</span>
      <span class="chip co">🥩 Frigorífico Municipal</span>
      <span class="chip cg">🌿 Agroecología</span>
      <span class="chip cp">✅ Aliado UxP</span>
    </div>
    <table class="t">
      <tr><th>Indicador</th><th>Tapalqué</th><th>Ref. Pcia.</th></tr>
      <tr><td>Superficie</td><td class="bld">4.168 km²</td><td>—</td></tr>
      <tr><td>Densidad</td><td>2,6 hab/km²</td><td>Interior: ~5</td></tr>
      <tr><td>Motor económico nuevo</td><td class="inf">Termas (2019)</td><td>Innovación</td></tr>
      <tr><td>Motor histórico</td><td class="ok">Ganadería extensiva</td><td>Cuenca Salado</td></tr>
      <tr><td>Frigorífico municipal</td><td class="ok">Operativo desde 2013</td><td>Modelo</td></tr>
      <tr><td>Voto LLA 2023 PASO</td><td class="ok">8,1% — Resistió</td><td>PBA: ~20%</td></tr>
    </table>
    <div class="nt">
      <strong>📌 Posición en el mapa provincial</strong>
      Interior profundo, 7ª sección, cuenca del Salado. A 270 km de Buenos Aires. Municipio rural que innovó con las termas. Forma parte del corredor del interior junto a Olavarría, Azul y Rauch. El Complejo Termal lo posiciona como destino turístico real dentro de la 7ª sección.
    </div>
    <div class="hist">
      <strong>📜 Historia que sostiene el relato</strong>
      <p>Tapalqué era un municipio de campo puro. La ganadería lo sostuvo durante décadas pero no lo hizo crecer. La apuesta de Cocconi por las termas fue arriesgada — nadie estaba seguro de que funcionara. Funcionó. <strong style="color:#78350F;">El relato es el de un municipio que apostó al futuro sin esperar al Estado nacional. La Provincia puede ser el socio que le dé escala a esa apuesta.</strong></p>
    </div>
  </div>
</div>

<!-- MATRIZ PRODUCTIVA -->
<div class="card two">
  <div class="ch" style="background:#1E3A5F;color:white;">⚙️ Matriz Productiva · La transformación económica de Tapalqué</div>
  <div class="cb">
    <div class="st">Sectores Productivos · Antes y después de las termas</div>
    <div class="sgrid">
      <div class="sc s">
        <div class="sl">🥇 Base histórica</div>
        <div class="sn">Ganadería Extensiva · Cuenca del Salado</div>
        <div class="sp" style="color:#059669;">~45% actividad</div>
        <div class="sd">Cría bovina extensiva en grandes campos de la Cuenca del Salado. Productores medianos y grandes con alta vulnerabilidad a inundaciones. El frigorífico municipal agrega valor local. Mercado de Liniers y exportaciones como destino final. La ganadería no creció — pero tampoco cedió.</div>
      </div>
      <div class="sc t">
        <div class="sl">🚀 Motor nuevo (desde 2019)</div>
        <div class="sn">Turismo Termal · Complejo Termal Tapalqué</div>
        <div class="sp" style="color:#D97706;">~30% actividad</div>
        <div class="sd">El Complejo Termal inaugurado en 2019 generó una revolución silenciosa: creó cientos de empleos en servicios donde antes no había. Hotelería, gastronomía, cabañas, recreación — sectores inexistentes en el municipio. En temporada alta la capacidad se satura: hay demanda no atendida.</div>
      </div>
      <div class="sc p">
        <div class="sl">🔸 Industria local</div>
        <div class="sn">Frigorífico y Matadero Municipal</div>
        <div class="sp" style="color:#1D4ED8;">Empleo formal</div>
        <div class="sd">Operativo desde 2013 con puesta en valor reciente. Faena en origen: el productor vende más cerca, el consumidor compra más barato, el municipio retiene el valor. Es un modelo de agroindustria pública que pocas ciudades del interior tienen. Potencial de escala con apoyo provincial.</div>
      </div>
      <div class="sc e">
        <div class="sl">🌿 Diferencial sustentable</div>
        <div class="sn">Agroecología y Energía Renovable</div>
        <div class="sp" style="color:#6D28D9;">Modelo</div>
        <div class="sd">Planta de biodiesel activa. Separación de residuos con alto cumplimiento vecinal. Participación en la RAMCC (Red Argentina de Municipios frente al Cambio Climático). Tapalqué tiene un perfil de sustentabilidad que excede su tamaño. Un activo de narrativa para el nivel provincial.</div>
      </div>
    </div>

    <div class="st">Estructura de Actividad Estimada</div>
    <div class="pbr"><div class="pbl">Ganadería y Agro</div><div class="pbo"><div class="pbi" style="width:90%;background:#059669"><div class="pbt">~45%</div></div></div><div class="pbp" style="color:#059669;">45%</div></div>
    <div class="pbr"><div class="pbl">Turismo Termal</div><div class="pbo"><div class="pbi" style="width:60%;background:#D97706"><div class="pbt">~30%</div></div></div><div class="pbp" style="color:#D97706;">30%</div></div>
    <div class="pbr"><div class="pbl">Comercio y Servicios</div><div class="pbo"><div class="pbi" style="width:30%;background:#2563EB"><div class="pbt">~15%</div></div></div><div class="pbp" style="color:#2563EB;">15%</div></div>
    <div class="pbr"><div class="pbl">Agroindustria / Frigorífico</div><div class="pbo"><div class="pbi" style="width:20%;background:#7C3AED"><div class="pbt">~10%</div></div></div><div class="pbp" style="color:#7C3AED;">10%</div></div>

    <div class="st" style="margin-top:18px;">Actores Clave del Territorio</div>
    <div class="ar">
      <div class="ai">🌡️</div>
      <div class="ain">
        <div class="an">Complejo Termal Tapalqué · Municipalidad</div>
        <div class="ad">El activo más transformador del municipio. Generó cientos de empleos y diversificó la economía ganadera. En temporada alta supera la capacidad. La ampliación (nuevas piletas, área de hotelería, mejora de accesos) depende de financiamiento provincial. Es el epicentro de la visita y el argumento más visible del modelo de desarrollo.</div>
        <div class="ats">
          <span class="at" style="background:#D1FAE5;color:#065F46;">Epicentro de la visita</span>
          <span class="at" style="background:#DBEAFE;color:#1E40AF;">Anuncio provincial aquí</span>
        </div>
      </div>
    </div>
    <div class="ar">
      <div class="ai">🥩</div>
      <div class="ain">
        <div class="an">Frigorífico y Matadero Municipal · Tapalqué</div>
        <div class="ad">En operación desde 2013 con puesta en valor reciente. Faena en origen: genera empleo formal fuera de la municipalidad y abarata la cadena alimentaria local. Con apoyo provincial (habilitaciones, logística, acceso a exportaciones) puede convertirse en un nodo regional de faena para municipios vecinos sin frigorífico propio.</div>
        <div class="ats">
          <span class="at" style="background:#FEF3C7;color:#92400E;">Modelo replicable</span>
          <span class="at" style="background:#EDE9FE;color:#4C1D95;">Escala con Provincia</span>
        </div>
      </div>
    </div>
    <div class="ar">
      <div class="ai">🐄</div>
      <div class="ain">
        <div class="an">Sociedad Rural de Tapalqué · Productores de la Cuenca</div>
        <div class="ad">Los ganaderos de cría extensiva son el sector más tradicional y con mayor superficie. Su demanda central es hídrica: las inundaciones del Salado destruyen pasturas y afectan el stock. La política hídrica del Salado es competencia directa de la Provincia. Un compromiso concreto en esta materia tiene efecto político inmediato en el campo.</div>
        <div class="ats">
          <span class="at" style="background:#F0FDF4;color:#15803D;">Diálogo productivo</span>
          <span class="at" style="background:#FEE2E2;color:#7F1D1D;">Agenda hídrica urgente</span>
        </div>
      </div>
    </div>
    <div class="ar">
      <div class="ai">🏛️</div>
      <div class="ain">
        <div class="an">Municipalidad de Tapalqué · Intendente Cocconi (UxP)</div>
        <div class="ad">Aliado político directo. Gestor de un modelo de desarrollo municipal innovador (termas + frigorífico + agroecología + campus). La visita fortalece su figura localmente y le da los anuncios que necesita para la campaña 2025-2027. Es el interlocutor natural y el amplificador del mensaje provincial en el interior de la 7ª sección.</div>
        <div class="ats">
          <span class="at" style="background:#D1FAE5;color:#065F46;">Aliado clave</span>
          <span class="at" style="background:#DBEAFE;color:#1E40AF;">Coordinación previa total</span>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- PERSPECTIVA PROVINCIAL -->
<div class="card full">
  <div class="ch" style="background:#0f2944;color:#FACC15;">👁️ Perspectiva Provincial · Palancas que solo el nivel provincial puede activar</div>
  <div class="cb">
    <p style="font-size:12px;color:#666;margin-bottom:16px;line-height:1.7;">Cocconi demostró que la escala municipal puede innovar. Pero para que Tapalqué dé el salto siguiente —de municipio con termas a polo de desarrollo del interior de la 7ª sección— se necesitan decisiones que exceden al intendente: financiamiento para ampliar el complejo, rutas para conectarlo, política hídrica para los ganaderos.</p>
    <div class="pgrid">
      <div class="pi d">
        <div class="pt">🔵 Inversión estratégica · Alta visibilidad</div>
        <div class="pti">Ampliación del Complejo Termal: más capacidad, más temporada, más empleo</div>
        <div class="pd">El complejo actual supera su capacidad en temporada alta. Una ampliación con financiamiento provincial (nuevas piletas, área de descanso, zona de hotelería básica) permite atender más turistas, extender la temporada y crear nuevos puestos de trabajo. El anuncio tiene altísima visibilidad local y resonancia regional en toda la 7ª sección.</div>
      </div>
      <div class="pi d">
        <div class="pt">🔵 Infraestructura para el turismo</div>
        <div class="pti">Conectividad vial hacia Tapalqué: la ruta que hace posible el turismo termal</div>
        <div class="pd">La ruta que conecta Tapalqué con Olavarría y el corredor del interior es provincial. Cada fin de semana llegan turistas que sufren el estado del camino. Mejorar la conectividad vial no es solo infraestructura: es hacer más sustentable el modelo turístico que el municipio construyó solo. "La Provincia pone la ruta, Tapalqué pone las termas."</div>
      </div>
      <div class="pi o">
        <div class="pt">✅ Política hídrica · Impacto directo en el campo</div>
        <div class="pti">Cuenca del Salado: sistematización hídrica para los ganaderos</div>
        <div class="pd">Las inundaciones periódicas del Salado y sus afluentes son la principal amenaza para la ganadería extensiva del partido. La Provincia tiene competencia directa y exclusiva sobre el manejo hídrico de la cuenca. Comprometerse con obras de sistematización (canales, esclusas, monitoreo de niveles) tiene efecto político inmediato entre los productores rurales, el sector más independiente del electorado.</pd>
      </div>
      <div class="pi o">
        <div class="pt">✅ Agroindustria provincial</div>
        <div class="pti">Frigorífico de Tapalqué como nodo regional de faena en origen</div>
        <div class="pd">Articular el frigorífico municipal con la red provincial de comercialización y exportación. Que los municipios vecinos sin capacidad propia de faena puedan acceder al frigorífico de Tapalqué bajo convenio provincial. Esto da escala al frigorífico, más empleo al municipio y más valor al productor ganadero que hoy manda la hacienda a Liniers.</div>
      </div>
      <div class="pi r">
        <div class="pt">⚠️ Riesgo a monitorear · Competencia JxC</div>
        <div class="pti">JxC con 44,4% en PASO 2023 — un punto de diferencia real</div>
        <div class="pd">La diferencia entre el PJ (47,5%) y JxC (44,4%) en el PASO 2023 es de apenas 3 puntos. Si el voto de LLA (8,1%) migra a JxC en una general, el resultado puede revertirse. La visita y los anuncios concretos son parte del trabajo de consolidación que el aliado local necesita para mantener esa ventaja.</div>
      </div>
      <div class="pi d">
        <div class="pt">🔵 Educación con perfil productivo</div>
        <div class="pti">Campus Universitario: ampliar la oferta con carreras técnicas provinciales</div>
        <div class="pd">El campus universitario de Tapalqué ofrece carreras vinculadas a gestión ambiental y turismo. La Provincia puede ampliar la oferta con tecnicaturas en manejo ganadero, frigoríficos y energías renovables. Que los jóvenes del interior puedan estudiar sin irse a Olavarría o a Buenos Aires. "La formación que necesita el campo bonaerense tiene que llegar al campo bonaerense."</div>
      </div>
    </div>
    <div class="corr">
      <h3>🌿 Interior Productivo Bonaerense · La 7ª Sección como laboratorio de desarrollo</h3>
      <p>Tapalqué puede ser el caso de éxito que muestre que el interior bonaerense no tiene por qué perder población ni depender de transferencias. Un modelo: termas + frigorífico + campo sustentable + educación técnica. Desde la Provincia, ese modelo puede escalarse a otros municipios de la sección.</p>
      <div class="cms">
        <div class="cm">📍 TAPALQUÉ<span>Termas · Frigorífico · Agro</span></div>
        <div class="cm">↔ OLAVARRÍA<span>Cemento · Universidad</span></div>
        <div class="cm">↔ AZUL<span>Turismo cultural · Agro</span></div>
        <div class="cm">↔ RAUCH<span>Ganadería · Interior</span></div>
        <div class="cm">↔ GENERAL LAMADRID<span>Agro · Interior profundo</span></div>
      </div>
    </div>
  </div>
</div>

<!-- ANÁLISIS DEL MOMENTO -->
<div class="card two">
  <div class="ch" style="background:#FFFBEB;color:#78350F;">📈 Análisis del Momento · La alianza que hay que profundizar</div>
  <div class="cb">
    <div class="st">Diagnóstico político · Tapalqué en el mapa provincial</div>
    <table class="t" style="margin-bottom:16px;">
      <thead><tr><th>Elección</th><th>PJ / UxP</th><th>JxC</th><th>LLA</th><th>Ganador</th></tr></thead>
      <tbody>
        <tr><td class="bld">Legislativas 2021</td><td class="ok">47,8%</td><td>—</td><td class="warn">24,0%</td><td>PJ</td></tr>
        <tr><td class="bld">PASO 2023</td><td class="ok">47,5%</td><td class="warn">44,4%</td><td>8,1%</td><td>PJ</td></tr>
        <tr><td class="bld">Gral 2023</td><td colspan="4" style="color:#999;font-style:italic;">Sin datos disponibles en la matriz</td></tr>
      </tbody>
    </table>
    <div class="ag">
      <div class="agi">🟢</div>
      <div class="agt">
        <strong>Fortaleza: PJ mantuvo el 47% en todos los ciclos</strong>
        <p>A diferencia de la mayoría de los municipios del interior donde LLA se coló con fuerza, en Tapalqué el peronismo se sostuvo en el 47-48% de forma consistente. Eso no es casualidad: es el resultado de una gestión visible (las termas, el frigorífico, las rondas sanitarias) que conecta con el electorado en clave cotidiana, no solo electoral.</p>
      </div>
    </div>
    <div class="ag">
      <div class="agi">🟡</div>
      <div class="agt">
        <strong>Señal a monitorear: JxC con 44,4% en el PASO — competencia real</strong>
        <p>La diferencia entre el PJ y JxC en el PASO 2023 es de apenas 3 puntos. JxC tiene estructura en la 7ª sección y puede crecer si el gobierno provincial no consolida la narrativa de gestión en territorio aliado. La visita y los anuncios concretos son parte del trabajo de consolidación que el candidato necesita.</p>
      </div>
    </div>
    <div class="ag" style="border-bottom:none;">
      <div class="agi">🔵</div>
      <div class="agt">
        <strong>Oportunidad: el modelo Tapalqué como relato de la gestión provincial</strong>
        <p>Tapalqué es el argumento que refuta la narrativa del interior abandonado. Con inversión concreta de la Provincia (rutas, complejo termal ampliado, política hídrica del Salado), el municipio se convierte en caso de éxito que el candidato puede mostrar en toda la 7ª sección como ejemplo de lo que la gestión provincial puede hacer cuando está alineada con el intendente.</p>
      </div>
    </div>
    <div class="al al-v">
      <strong>✅ Conclusión estratégica</strong>
      La alianza con Cocconi es uno de los activos más sólidos del interior profundo. Hay que invertir en ella antes de la elección, no después. Cada peso anunciado en Tapalqué tiene efecto multiplicador en la narrativa del interior de la 7ª sección.
    </div>
  </div>
</div>

<!-- AGENDA DE DISCURSO -->
<div class="card one">
  <div class="ch" style="background:#1E3A5F;color:white;">🎤 Agenda de Discurso · Perspectiva Provincial</div>
  <div class="cb">
    <div class="st">Ejes · Por prioridad de impacto</div>
    <div class="ag">
      <div class="agi">🌡️</div>
      <div class="agt">
        <strong>1. El modelo que funciona merece escala</strong>
        <p>"Tapalqué apostó por las termas cuando nadie creía. Funcionó. La Provincia va a apostar ahora para que esto crezca." Anuncio de financiamiento para la ampliación del complejo.</p>
      </div>
    </div>
    <div class="ag">
      <div class="agi">💧</div>
      <div class="agt">
        <strong>2. La deuda histórica del Salado</strong>
        <p>"El campo de Tapalqué sabe lo que es una inundación. La Provincia va a estar al lado del productor cuando baje el agua — y también cuando sube." Compromiso con la política hídrica de la cuenca.</p>
      </div>
    </div>
    <div class="ag">
      <div class="agi">🥩</div>
      <div class="agt">
        <strong>3. Faena en origen, valor en origen</strong>
        <p>El frigorífico de Tapalqué como modelo provincial. Propuesta de articulación con la red de comercialización de la Provincia. El productor que vende más cerca cobra mejor.</p>
      </div>
    </div>
    <div class="ag">
      <div class="agi">🎓</div>
      <div class="agt">
        <strong>4. Educación que no obliga a emigrar</strong>
        <p>"No podemos seguir aceptando que para estudiar haya que irse. La Provincia va a traer las carreras técnicas al interior." Ampliación del campus con tecnicaturas productivas.</p>
      </div>
    </div>
    <div class="ag" style="border-bottom:none;">
      <div class="agi">🚫</div>
      <div class="agt">
        <strong>Qué evitar</strong>
        <p>No llegar sin anuncios concretos. No hablar de política nacional en un municipio aislado del debate nacional. No ignorar la agenda ganadera: los productores del campo son tan importante como el complejo termal. Un aliado sin anuncios es un aliado debilitado.</p>
      </div>
    </div>
    <div class="al al-k">
      <strong>⚡ La frase que sintetiza la visita</strong>
      "Tapalqué no esperó al Estado para desarrollarse. Ahora el Estado provincial viene a acompañar lo que Tapalqué ya construyó."
    </div>
  </div>
</div>

</div>

<div class="footer">
  🔒 USO RESERVADO · Campaña PBA · Ficha Tapalqué · PBA Analytics 2026
</div>

<!-- ANEXO I -->
<div style="page-break-before:always;break-before:page;height:0;margin:0;padding:0;font-size:0;"></div>
<div>
  <div style="background:linear-gradient(135deg,#1E3A5F,#0369A1);color:white;padding:20px 32px;display:flex;justify-content:space-between;align-items:center;">
    <div>
      <div style="font-size:11px;opacity:0.6;letter-spacing:2px;text-transform:uppercase;margin-bottom:4px;">Tapalqué · Campaña PBA 2026</div>
      <div style="font-size:22px;font-weight:900;letter-spacing:1px;">ANEXO I — PRINCIPALES INDICADORES</div>
    </div>
    <div style="font-size:11px;opacity:0.7;text-align:right;">7ª Sección Electoral · Interior<br>PBA Analytics 2026</div>
  </div>
  <div style="padding:20px 24px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px;background:#eef2f7;">

    <div class="card">
      <div class="ch" style="background:#EFF6FF;color:#1E40AF;">🌡️ Complejo Termal</div>
      <div class="cb">
        <div class="st">La nueva industria de Tapalqué</div>
        <table class="t">
          <tr><td>Inauguración</td><td class="inf">2019 · transformación económica</td></tr>
          <tr><td>Impacto empleo</td><td class="ok">Cientos de puestos en servicios</td></tr>
          <tr><td>Sectores creados</td><td class="ok">Hotelería, gastro, cabañas, recreación</td></tr>
          <tr><td>Capacidad actual</td><td class="warn">Se satura en temporada alta</td></tr>
          <tr><td>Demanda no atendida</td><td class="bad">Alta · requiere ampliación</td></tr>
          <tr><td>Financiamiento ampliación</td><td class="bad">Pendiente · palanca provincial</td></tr>
          <tr><td>Conectividad vial</td><td class="warn">Rutas provinciales · mejora urgente</td></tr>
        </table>
      </div>
    </div>

    <div class="card">
      <div class="ch" style="background:#ECFDF5;color:#065F46;">🐄 Ganadería y Cuenca del Salado</div>
      <div class="cb">
        <div class="st">Base histórica del partido</div>
        <table class="t">
          <tr><td>Perfil productivo</td><td class="inf">Cría extensiva bovina</td></tr>
          <tr><td>Cuenca</td><td>Del Salado · campo grande</td></tr>
          <tr><td>Principal amenaza</td><td class="bad">Inundaciones periódicas del Salado</td></tr>
          <tr><td>Política hídrica</td><td class="bad">Competencia Provincia · pendiente</td></tr>
          <tr><td>Frigorífico municipal</td><td class="ok">Desde 2013 · puesta en valor</td></tr>
          <tr><td>Faena en origen</td><td class="ok">Abarata cadena · genera empleo</td></tr>
          <tr><td>Escala frigorífico</td><td class="warn">Limitada · requiere articulación prov.</td></tr>
        </table>
      </div>
    </div>

    <div class="card">
      <div class="ch" style="background:#F0FDF4;color:#15803D;">📊 Datos Municipales Generales</div>
      <div class="cb">
        <div class="st">Indicadores de base</div>
        <table class="t">
          <tr><td>Población (Censo 2022)</td><td class="inf">10.783 hab.</td></tr>
          <tr><td>Superficie</td><td>4.168 km²</td></tr>
          <tr><td>Sección Electoral</td><td>7ª · Interior profundo</td></tr>
          <tr><td>Intendente</td><td class="ok">Gustavo Cocconi · UxP · Aliado</td></tr>
          <tr><td>Categoría electoral</td><td class="warn">Disputado (favorable PJ)</td></tr>
          <tr><td>Identidad económica</td><td>Termas + Ganadería + Agroindustria</td></tr>
          <tr><td>Voto LLA PASO 2023</td><td class="ok">8,1% — Muy bajo vs PBA</td></tr>
          <tr><td>Distancia a CABA</td><td>~270 km · corredor interior</td></tr>
        </table>
      </div>
    </div>

    <div class="card">
      <div class="ch" style="background:#FFFBEB;color:#78350F;">🌿 Programas de Sustentabilidad</div>
      <div class="cb">
        <div class="st">Tapalqué Sostenible</div>
        <table class="t">
          <tr><td>Planta de biodiesel</td><td class="ok">Activa · energía local</td></tr>
          <tr><td>Separación de residuos</td><td class="ok">Alto cumplimiento vecinal</td></tr>
          <tr><td>RAMCC</td><td class="ok">Red Municipios Cambio Climático</td></tr>
          <tr><td>Agroecología</td><td class="ok">Fomento activo municipal</td></tr>
          <tr><td>Campus ambiental</td><td class="ok">Carreras de gestión ambiental</td></tr>
          <tr><td>Perfil diferencial</td><td class="inf">Municipio verde · referencia PBA</td></tr>
        </table>
        <div class="al al-v" style="margin-top:10px;">
          <strong>✅ Activo narrativo</strong>
          Tapalqué tiene un perfil de sustentabilidad inusual para su tamaño. Puede posicionarse como referencia provincial en agroecología y energías renovables.
        </div>
      </div>
    </div>

    <div class="card">
      <div class="ch" style="background:#FEE2E2;color:#7F1D1D;">🗳️ Historial Electoral</div>
      <div class="cb">
        <div class="st">Evolución del voto · Tapalqué</div>
        <table class="t">
          <thead><tr><th>Elección</th><th>PJ/UxP</th><th>JxC</th><th>LLA</th><th>Resultado</th></tr></thead>
          <tbody>
            <tr><td>Leg. 2021</td><td class="ok">47,8%</td><td>—</td><td class="warn">24,0%</td><td class="bld">PJ</td></tr>
            <tr><td>PASO 2023</td><td class="ok">47,5%</td><td class="warn">44,4%</td><td>8,1%</td><td class="bld">PJ</td></tr>
            <tr><td>Gral 2023</td><td colspan="4" style="color:#999;font-style:italic;">Sin datos en la matriz</td></tr>
          </tbody>
        </table>
        <div class="hist" style="margin-top:10px;">
          <strong>📌 Tendencia</strong>
          <p>PJ sólido y consistente. LLA no penetró (8% vs ~20% PBA). JxC con 44% es el único riesgo real. La fortaleza peronista responde a gestión concreta visible. Consolidar requiere presencia e inversión provincial antes de 2027.</p>
        </div>
      </div>
    </div>

    <div class="card">
      <div class="ch" style="background:#F5F3FF;color:#4C1D95;">🎯 Prioridad Estratégica</div>
      <div class="cb">
        <div class="st">Posición en el mapa de campaña</div>
        <table class="t">
          <tr><td>Clasificación PBA</td><td class="warn">Disputado (favorable)</td></tr>
          <tr><td>Urgencia política</td><td class="ok">Media · Aliado consolidado</td></tr>
          <tr><td>Retorno de la visita</td><td class="ok">Alto · narrativa y votos</td></tr>
          <tr><td>Palanca 1</td><td class="inf">Ampliación Complejo Termal</td></tr>
          <tr><td>Palanca 2</td><td class="inf">Política hídrica Salado</td></tr>
          <tr><td>Palanca 3</td><td class="inf">Frigorífico como nodo regional</td></tr>
          <tr><td>Vínculo con intendente</td><td class="ok">Aliado directo · UxP</td></tr>
        </table>
      </div>
    </div>

  </div>
  <div style="text-align:center;padding:12px;font-size:11px;color:#aaa;background:white;border-top:1px solid #e5e7eb;">
    🔒 USO RESERVADO · ANEXO I · Tapalqué · PBA Analytics 2026
  </div>
</div>

<!-- ANEXO II -->
<div style="page-break-before:always;break-before:page;height:0;margin:0;padding:0;font-size:0;"></div>
<div>
  <div style="background:linear-gradient(135deg,#1F4E79,#2563EB);color:white;padding:20px 32px;display:flex;justify-content:space-between;align-items:center;">
    <div>
      <div style="font-size:11px;opacity:0.6;letter-spacing:2px;text-transform:uppercase;margin-bottom:4px;">Tapalqué · 2026</div>
      <div style="font-size:22px;font-weight:900;letter-spacing:1px;">ANEXO II — GESTIÓN LOCAL Y DATOS DE CONTEXTO</div>
    </div>
    <div style="font-size:11px;opacity:0.7;text-align:right;">Gestión Cocconi · UxP<br>Aliado · Modelo interior</div>
  </div>
  <div style="padding:20px 24px;display:grid;grid-template-columns:1fr 1fr;gap:16px;background:#eef2f7;">

    <div class="card">
      <div class="ch" style="background:#ECFDF5;color:#065F46;">🏛️ Gestión Cocconi · UxP · Diagnóstico</div>
      <div class="cb">
        <div class="st">El intendente aliado: perfil y fortalezas</div>
        <table class="t" style="margin-bottom:14px;">
          <tr><td>Perfil político</td><td class="ok">Innovador · desarrollista · pragmático</td></tr>
          <tr><td>Legitimidad local</td><td class="ok">Alta · gestión visible y tangible</td></tr>
          <tr><td>Concejo Deliberante</td><td class="ok">Mayoría PJ</td></tr>
          <tr><td>Relación con Provincia</td><td class="ok">Colaborativa · natural</td></tr>
          <tr><td>Agenda termal</td><td class="ok">Activa · su obra insignia</td></tr>
          <tr><td>Agenda ganadera</td><td class="ok">Frigorífico como política activa</td></tr>
          <tr><td>Agenda sustentable</td><td class="ok">Biodiesel, residuos, RAMCC</td></tr>
        </table>
        <div class="al al-v">
          <strong>✅ Coordinación total recomendada</strong>
          Cocconi es el organizador natural de la visita. Debe coordinar el recorrido del complejo termal, el encuentro con productores y la recorrida por el frigorífico. Su imagen y la del candidato deben aparecer juntos en todos los anuncios. El fortalecimiento mutuo es el objetivo.
        </div>
      </div>
    </div>

    <div class="card">
      <div class="ch" style="background:#EFF6FF;color:#1E40AF;">📋 Programas Municipales · Hitos 2019-2026</div>
      <div class="cb">
        <div class="st">Principales logros de gestión</div>
        <table class="t" style="margin-bottom:14px;">
          <tr><td>Complejo Termal</td><td class="ok">Inaugurado 2019 · transformación</td></tr>
          <tr><td>Frigorífico Municipal</td><td class="ok">Puesta en valor 2023-24</td></tr>
          <tr><td>Campus Universitario</td><td class="ok">Gestión ambiental y turismo</td></tr>
          <tr><td>Planta biodiesel</td><td class="ok">En operación</td></tr>
          <tr><td>Separación residuos</td><td class="ok">Alto cumplimiento</td></tr>
          <tr><td>Rondas sanitarias rurales</td><td class="ok">400+ atenciones/mes en parajes</td></tr>
          <tr><td>Programa Producción</td><td class="ok">Apoyo a productores y emprendedores</td></tr>
        </table>
        <div class="hist">
          <strong>📌 Relato para la visita</strong>
          <p>La gestión Cocconi es el mejor argumento que la visita provincial puede usar: un intendente aliado que sin grandes recursos del Estado nacional logró cambiar la economía de su municipio. La Provincia entra a amplificar ese logro, no a reemplazarlo.</p>
        </div>
      </div>
    </div>

  </div>
  <div style="text-align:center;padding:12px;font-size:11px;color:#aaa;background:white;border-top:1px solid #e5e7eb;">
    🔒 USO RESERVADO · ANEXO II · Tapalqué · PBA Analytics 2026
  </div>
</div>

</body>
</html>"""

with open('Ficha_Campana_TAPALQUE.html', 'w') as f:
    f.write(TAPALQUE_HTML)
print(f"✓ TAPALQUÉ: {len(TAPALQUE_HTML):,} bytes")
