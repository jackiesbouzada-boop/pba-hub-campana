#!/usr/bin/env python3
"""
PBA_Maestro_2026.html — v3
4 tabs: Inmersión | Recorrida Territorial (simplificado) | Fichas | Metodología & Estrategia
"""
import re, os, json, unicodedata, importlib.util, hashlib

BASE_HTML = "/sessions/bold-wizardly-edison/mnt/PBA - Analitica/"
BASE_DATA = "/sessions/bold-wizardly-edison/mnt/outputs/"
OUTPUT    = BASE_HTML + "PBA_Maestro_2026.html"

# ── IE lookup ────────────────────────────────────────────────────────────────
with open(BASE_DATA + 'ie_lookup_v2.json') as f:
    IE_LOOKUP = json.load(f)

def norm_muni(s):
    s = unicodedata.normalize('NFD', str(s).upper())
    return ''.join(c for c in s if unicodedata.category(c) != 'Mn').strip()

def get_ie(muni):
    k = norm_muni(muni)
    if k in IE_LOOKUP: return IE_LOOKUP[k]
    for key in IE_LOOKUP:
        if k in key or key in k: return IE_LOOKUP[key]
    return 6

def load_py(path):
    spec = importlib.util.spec_from_file_location('m', path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

ciudades  = load_py(BASE_DATA + 'data_ciudades.py')
conurbano = load_py(BASE_DATA + 'data_conurbano.py')
otros     = load_py(BASE_DATA + 'data_otros.py')
interior  = load_py(BASE_DATA + 'data_interior_salado_sur.py')
sur_m     = load_py(BASE_DATA + 'data_sur.py')

ADJUSTMENTS = {
    'Basílica Nuestra Señora de Luján': dict(pc=7),
    'Casa Museo Eva Perón — Los Toldos': dict(ie_override=10, pc=10, ut=10),
    'Base Naval Puerto Belgrano — Armada Argentina': dict(pc=10, ut=10),
    'TenarisSiderca — Tubos sin costura para YPF y el mundo': dict(pc=10, ut=10),
    'Loma Negra — El cemento que construyó Argentina': dict(pc=9, ut=9, rs=9),
    'La Serenísima / Mastellone Hermanos — La leche de los argentinos': dict(pc=9, ut=9, rs=9),
    'Central Nuclear Atucha I y II — La energía soberana de la Provincia': dict(pc=10, ut=10, rs=9, lv=7),
}

def score(p):
    ie = get_ie(p[1])
    pc, ut, rs, lv = p[3], p[4], p[5], p[6]
    adj = ADJUSTMENTS.get(p[0], {})
    if 'ie_override' in adj: ie = adj['ie_override']
    return round(adj.get('pc',pc)*0.25 + ie*0.25 + adj.get('ut',ut)*0.20 + adj.get('rs',rs)*0.15 + adj.get('lv',lv)*0.15, 2)

def score_detail(p):
    ie = get_ie(p[1])
    pc, ut, rs, lv = p[3], p[4], p[5], p[6]
    adj = ADJUSTMENTS.get(p[0], {})
    if 'ie_override' in adj: ie = adj['ie_override']
    pc2=adj.get('pc',pc); ut2=adj.get('ut',ut); rs2=adj.get('rs',rs); lv2=adj.get('lv',lv)
    return ie, pc2, ut2, rs2, lv2, round(ie*0.25+pc2*0.25+ut2*0.20+rs2*0.15+lv2*0.15, 2)

def top50(lst): return sorted(lst, key=score, reverse=True)[:50]

CLUSTER_META = {
    'CIUDADES':  {'color':'#1a3a5c','icon':'🏙️','desc':'10 municipios · Cabeceras de sección'},
    'CONURBANO': {'color':'#5a2480','icon':'🌆','desc':'29 municipios · Tercer cordón GBA'},
    'CORREDOR':  {'color':'#1d6b3e','icon':'🛤️','desc':'13 municipios · Eje industrial norte'},
    'COSTERO':   {'color':'#0077b6','icon':'🌊','desc':'7 municipios · Mar Argentino'},
    'INTERIOR':  {'color':'#7b5e00','icon':'🌾','desc':'37 municipios · Pampa húmeda'},
    'SALADO':    {'color':'#8b3a3a','icon':'🌿','desc':'19 municipios · Cuenca del Salado'},
    'SUR':       {'color':'#2e4057','icon':'🏔️','desc':'20 municipios · Sierra bonaerense'},
}

PRIVADO_KW  = [
    # Originales
    'toyota','tenaris','loma negra','mccain','mastellone','la serenísima','tambo robot',
    'mundo marino','cristales cattorini','cooperativa','frigorifico','estancia','bodega',
    # Correcciones de clasificación
    'cervecería y maltería','ternium','siderar','profertil',
    'bioceres','san miguel s.a.','semino','molinos juan',
    'conarpesa','pesquera bariloche','pbbpolisur','pbbeolisur',
    'ytec','y-tec','mattievich','astilleros mestrina','rexnord','plantin',
    # Alternativas privadas (el emoji las identifica)
    '🔄',
]
NACIONAL_KW = ['inta ','cnea','atucha','conicet','utn —','unlp','armada argentina','base naval','astilleros río santiago','destilería ypf','ypf la plata','universidad nacional']

ACC_STYLE = {
    'PRIVADO':   ('🏭', '#1b4332', '#d8f3dc', 'Sin protocolo municipal'),
    'NACIONAL':  ('🏛️', '#1d3461', '#dde3f5', 'Coordinar con autoridad nacional'),
    'PROTOCOLAR':('🤝', '#5c3317', '#fef3c7', 'Notificar al intendente local'),
}

# HOOKS — razón específica y única de visitar ESTE lugar y no otro
# ── COORDENADAS MUNICIPALES (aprox.) para el mapa ────────────────────────────
MUNI_COORDS = {
    # CONURBANO
    'Almirante Brown':(-34.8167,-58.4000),'Avellaneda':(-34.6667,-58.3667),
    'Berazategui':(-34.7667,-58.2000),'Esteban Echeverría':(-34.8333,-58.4667),
    'Ezeiza':(-34.8500,-58.5167),'Florencio Varela':(-34.8167,-58.2667),
    'General San Martín':(-34.5750,-58.5333),'Gral. San Martín':(-34.5750,-58.5333),
    'Hurlingham':(-34.5833,-58.6333),'Ituzaingó':(-34.6500,-58.6667),
    'José C. Paz':(-34.5167,-58.7500),'La Matanza':(-34.7667,-58.6333),
    'Lanús':(-34.7083,-58.3833),'Lomas de Zamora':(-34.7583,-58.4000),
    'Malvinas Argentinas':(-34.4833,-58.7000),'Merlo':(-34.6667,-58.7333),
    'Moreno':(-34.6500,-58.7833),'Morón':(-34.6500,-58.6167),
    'Quilmes':(-34.7205,-58.2535),'San Fernando':(-34.4500,-58.5667),
    'San Isidro':(-34.4667,-58.5167),'San Miguel':(-34.5417,-58.7125),
    'Tigre':(-34.4297,-58.5792),'Tres de Febrero':(-34.6083,-58.5583),
    'Vicente López':(-34.5333,-58.4833),'Escobar':(-34.3500,-58.7833),
    'Pilar':(-34.4667,-58.9167),'Presidente Perón':(-34.8833,-58.3667),
    'San Vicente':(-35.0167,-58.4167),'Marcos Paz':(-34.7833,-58.8500),
    # CIUDADES
    'La Plata':(-34.9205,-57.9536),'Mar del Plata':(-38.0023,-57.5575),
    'Gral. Pueyrredón':(-38.0023,-57.5575),'General Pueyrredón':(-38.0023,-57.5575),
    'Bahía Blanca':(-38.7183,-62.2661),'Tandil':(-37.3167,-59.1333),
    'Junín':(-34.5833,-60.9333),'Pergamino':(-33.8833,-60.5667),
    'San Nicolás':(-33.3333,-60.2167),'Olavarría':(-36.8833,-60.3167),
    'Necochea':(-38.5500,-58.7333),'Zárate':(-34.1000,-59.0167),
    'Campana':(-34.1667,-58.9667),'San Pedro':(-33.6833,-59.6667),
    'Ensenada':(-34.8667,-57.9167),'Berisso':(-34.8750,-57.8833),
    # CORREDOR
    'Luján':(-34.5667,-59.1167),'Mercedes':(-34.6500,-59.4333),
    'Chivilcoy':(-34.9000,-60.0167),'Chacabuco':(-34.6333,-60.4667),
    'Salto':(-34.2833,-60.2500),'Ramallo':(-33.4833,-60.0167),
    'San Antonio de Areco':(-34.2500,-59.4667),
    'General Rodríguez':(-34.6000,-58.9500),'Gral. Rodríguez':(-34.6000,-58.9500),
    'Cañuelas':(-35.0500,-58.7500),'Las Heras':(-34.9167,-59.4333),
    'General Las Heras':(-34.9167,-59.4333),'Gral. Las Heras':(-34.9167,-59.4333),
    'Lobos':(-35.1833,-59.1000),'Navarro':(-35.0000,-59.2667),
    'Alberti':(-35.0333,-60.2667),'Arrecifes':(-34.0667,-60.1000),
    'Baradero':(-33.8167,-59.5000),'Colón':(-33.8833,-61.1000),
    'Exaltación de la Cruz':(-34.3000,-59.1000),'Suipacha':(-34.7667,-59.6833),
    'Leandro N. Alem':(-34.0667,-61.0500),'Rojas':(-34.1833,-60.7167),
    # COSTERO
    'La Costa':(-36.6667,-56.7000),'Pinamar':(-37.1167,-56.8667),
    'Villa Gesell':(-37.2667,-57.0000),'Mar Chiquita':(-37.7333,-57.4333),
    'Miramar':(-38.2667,-57.8333),'Balcarce':(-37.8500,-58.2500),
    'Lobería':(-38.1667,-58.8167),'San Cayetano':(-38.3500,-59.6000),
    # INTERIOR
    'Azul':(-36.7833,-59.8667),'Bolívar':(-36.2500,-61.1167),
    'Bragado':(-35.1167,-60.4833),'Carlos Casares':(-35.6167,-61.3667),
    'Carlos Tejedor':(-35.3833,-62.4167),'Daireaux':(-36.6000,-61.7333),
    'Florentino Ameghino':(-34.9833,-62.4667),
    'General Alvear':(-36.0333,-60.0167),'Gral. Alvear':(-36.0333,-60.0167),
    'General Viamonte':(-35.0000,-61.0500),'Gral. Viamonte':(-35.0000,-61.0500),
    'General Villegas':(-35.0333,-63.0167),'Gral. Villegas':(-35.0333,-63.0167),
    'General Pinto':(-34.7667,-61.9000),'Gral. Pinto':(-34.7667,-61.9000),
    '9 de Julio':(-35.4500,-60.8833),'Pehuajó':(-35.8500,-61.9000),
    'Rivadavia':(-35.4833,-62.9833),'Saladillo':(-35.6333,-59.7833),
    'Trenque Lauquen':(-35.9667,-62.7333),'Lincoln':(-34.8667,-61.5333),
    'Roque Pérez':(-35.3833,-59.3333),'San Andrés de Giles':(-34.4333,-59.4333),
    'Tapalqué':(-36.3500,-60.0167),'Veinticinco de Mayo':(-35.4333,-60.1667),
    '25 de Mayo':(-35.4333,-60.1667),'Salliqueló':(-36.7500,-62.9500),
    'Tres Lomas':(-36.4500,-62.8500),'Guaminí':(-37.0167,-62.4167),
    'Hipólito Yrigoyen':(-36.2000,-61.2000),'Henderson':(-36.3000,-61.7167),
    'Brandsen':(-35.1667,-58.2333),
    # SALADO
    'Ayacucho':(-37.1500,-58.4833),'Chascomús':(-35.5667,-58.0167),
    'Dolores':(-36.3167,-57.6833),'General Belgrano':(-35.7667,-58.4833),
    'Gral. Belgrano':(-35.7667,-58.4833),'General Guido':(-36.6500,-57.7833),
    'General Lavalle':(-36.4000,-56.9333),'General Madariaga':(-37.0000,-57.1500),
    'Gral. Madariaga':(-37.0000,-57.1500),'General Paz':(-35.5167,-59.0833),
    'Gral. Paz':(-35.5167,-59.0833),'Las Flores':(-36.0167,-59.1000),
    'Lezama':(-35.9667,-57.9333),'Magdalena':(-35.0833,-57.5167),
    'Maipú':(-36.8667,-57.8833),'Monte':(-35.4333,-58.8000),
    'San Miguel del Monte':(-35.4333,-58.8000),'Pila':(-36.0000,-58.1500),
    'Punta Indio':(-35.2667,-57.2167),'Rauch':(-36.7667,-59.0833),
    'Tordillo':(-36.5000,-57.2333),'Castelli':(-36.0667,-57.8000),
    # SUR
    'Adolfo Alsina':(-37.0667,-62.5833),'Adolfo Gonzales Chaves':(-38.0333,-60.1000),
    'Gonzales Chaves':(-38.0333,-60.1000),'Benito Juárez':(-37.6667,-59.8000),
    'Coronel Dorrego':(-38.7167,-61.2833),'Coronel Pringles':(-37.9833,-61.3500),
    'Coronel Suárez':(-37.4667,-61.9167),'Monte Hermoso':(-38.9833,-61.3000),
    'Patagones':(-40.8000,-62.9667),'Puan':(-37.5333,-62.7667),
    'Saavedra':(-37.7500,-62.3500),'Tornquist':(-38.1000,-62.2333),
    'Tres Arroyos':(-38.3667,-60.2833),'Villarino':(-39.2500,-62.9167),
    'Coronel de Marina Leonardo Rosales':(-38.9167,-62.0167),
    'Rosales':(-38.9167,-62.0167),'Punta Alta':(-38.8833,-62.0833),
}

def _get_coords(muni, name=''):
    """Coordenadas con jitter determinístico para separar múltiples lugares del mismo municipio."""
    coords = MUNI_COORDS.get(muni)
    if not coords:
        ml = muni.lower()
        for k, v in MUNI_COORDS.items():
            if k.lower() == ml or k.lower() in ml or ml in k.lower():
                coords = v; break
    if not coords:
        coords = (-36.8, -60.0)  # centro aproximado de PBA
    lat, lng = coords
    h = int(hashlib.md5(name.encode('utf-8','ignore')).hexdigest()[:8], 16)
    lat += ((h & 0xFF) - 128) / 128.0 * 0.018
    lng += ((h >> 8 & 0xFF) - 128) / 128.0 * 0.018
    return round(lat, 5), round(lng, 5)

HOOKS = {
    # ── Lugares existentes de alto valor ──
    'Toyota': 'Única planta de Toyota en Argentina; exporta el 85% de su producción',
    'TenarisSiderca': '40% de los tubos que usa YPF en todo el país salen de aquí',
    'Loma Negra': '40% del cemento que se consume en Argentina lo produce este municipio',
    'Central Nuclear Atucha': 'La Provincia con dos reactores propios: el 11% de energía eléctrica del país',
    'Tambo robot': 'Uno de los primeros tambos robotizados de PBA; sin operario nocturno desde 2019',
    'Villa Epecuén': 'La única ciudad del mundo inundada 25 años y hoy emergente; visible desde satélite',
    'Casa Museo Eva Perón': 'La única casa donde nació Evita, recuperada por el Estado en 2002',
    'Astilleros Río Santiago': 'Construyeron el Almirante Irizar, único rompehielos antártico de Argentina',
    'Destilería YPF': 'La refinería más antigua en operación continua de Argentina (desde 1925)',
    'La Serenísima': '1 de cada 3 litros de leche que toma la Argentina viene de General Rodríguez',
    'Base Naval Puerto Belgrano': 'La base naval más grande de América del Sur; operativa desde 1898',
    'Complejo Vial Zárate': 'El puente más largo construido con ingeniería 100% argentina (1977)',
    'CNEA': 'Argentina enriquece uranio soberanamente y exporta radiofármacos a 40 países',
    'INTA Castelar': 'Aquí se desarrolló la tecnología de siembra directa que Argentina enseñó al mundo',
    'INTI': 'Asiste a más de 4.000 PyMEs argentinas al año en innovación industrial',
    'Chapadmalal': '4.000 plazas para trabajadores en el mar; fundado por Evita en 1950. Única en Argentina',
    # ── Alternativas privadas ──
    'Conarpesa': '1 de cada 4 cajas de langostino que Argentina exporta sale de aquí',
    'Antares': 'Pionera del craft beer: nació aquí en 1998 cuando nadie creía en la cerveza artesanal',
    'PBBPolisur': 'Única planta en Argentina que produce polietileno y PVC simultáneamente',
    'Mestrina': '3 generaciones construyendo barcos de madera en el Delta; último astillero artesanal',
    'La Juanita': 'Del 40% de desocupación en 2001 al Premio Cartier de Emprendimiento Social',
    'MadyGraf': 'Fábrica recuperada en 2014; hoy imprime para UNICEF y las Naciones Unidas',
    'Plantín': 'Exporta 1M+ plantas al año a Europa; fundado por la comunidad japonesa de Escobar',
    'Bioceres': 'Primera empresa latinoamericana de biotech agrícola en NASDAQ (2019)',
    'San Miguel S.A': 'El primer embarque de mandarina argentina a China salió de aquí (2019)',
    'Cooperativa Apícola del Corredor': '18% de la miel argentina que va a Europa sale del corredor norte',
    'Semino': '4ª generación familiar; único molino con terminal portuaria propia sobre el Quequén',
    'Pesquera Bariloche': 'Pioneer en frío a bordo: procesa la merluza en el barco, no en tierra',
    'La Ballenita': 'Único centro privado de rescate de fauna marina del litoral bonaerense',
    'La Lacteo': 'Ganó medalla de oro en Lyon (Francia): único queso bonaerense premiado en Europa',
    'El Ombú Grande': 'Pioneros en la raza Brangus en Argentina; exportan genética a 3 países',
    'Cumelén': 'Exportan genética bovina (semen y embriones) a 12 países desde Dolores',
    'Y-TEC': 'Único lugar en Argentina donde se fabrican celdas de baterías de litio',
    'Piscicultura Salado': 'Único criadero intensivo de pejerrey del país; la tecnología la usa el INIDEP',
    'Ecoturismo Ventana': 'El Cerro Tres Picos está en campo privado: sin este operador no se sube',
    'Calzados Guante': 'El calzado de seguridad que usa la mitad de los obreros industriales del país',
    'Cooperativa Hortícola del Río Colorado': 'Produce cebollas en el desierto sur bonaerense bajo riego gota a gota',
    # ── Nuevos relatos ──
    'Fric-Rot': 'Única empresa argentina de autopartes con homologación en 40 países; provee a Toyota',
    'CATA': '100 años de historia; factura más por año que el presupuesto municipal de Tres Arroyos',
    'Fuerte del Carmen 1827': 'En 1827, vecinos capturaron 3 buques de guerra brasileños: primera victoria naval argentina',
    'Huanguelén': 'El único caso en PBA de rechazo popular exitoso a una empresa minera (asamblea 2010)',
    'Cooperativa Eléctrica de Necochea': '95 años gestionando energía; el kWh más barato del sur bonaerense',
    # ── Hooks autogenerados desde justificacion ──
    'Puerto Mar del Plata + Flota Pesquera': 'El mayor puerto pesquero del Atlántico Sur argentino.',
    'Ternium Siderar': 'La planta integrada de acero más grande de Argentina con 5.400 empleados directos.',
    'Delta del Paraná': 'El Delta en Tigre: 45 minutos de CABA, ecosistema de humedales único en el mundo.',
    'Puerto Bahía Blanca + Polo Petroquímico': 'Mayor complejo portuario del sur del hemisferio occidental y único polo petroquímico integrado de Argentina: YPF,…',
    'INIDEP': 'El centro científico que regula la pesca del Mar Argentino y determina cuotas de captura.',
    'Casino Central + Playa Bristol': 'El casino más importante de la Provincia y el símbolo del veraneo bonaerense conocido por todos los argentinos.',
    'Basílica Nuestra Señora de Luján': 'La imagen religiosa más venerada de Argentina, con 2+ millones de peregrinos anuales y sede de la Peregrinación…',
    'Puente Zárate-Brazo Largo': 'Los puentes más largos de América Latina al inaugurarse en 1977.',
    'Hub Industrial Zárate': 'El corredor industrial Zárate-Campana concentra plantas de Dow, Givaudan, AGD, VW Parts y decenas de industrias pesadas.',
    'Tandil': 'La única ciudad bonaerense con sierra, chacinados con IGP, industria metalúrgica de precisión y turismo de naturaleza.',
    'AXION Energy / Complejo Petroquímico Campana': 'Refinería de petróleo y plantas petroquímicas que forman parte del hub industrial Zárate-Campana.',
    'Complejo Museográfico Provincial Enrique Udaondo': 'El museo histórico más importante de la Provincia: colección de artefactos desde el siglo XVII, arquitectura colonial…',
    'UNMDP': 'Universidad de 30.000 estudiantes con perfil fuerte en pesca, ingeniería, economía y ciencias del mar.',
    'Teatro Auditorium Mar del Plata': 'Sala cultural icónica del veraneo, sede del Festival Internacional de Cine.',
    'Bahía Blanca': 'Cuna de Pepe Sánchez y generaciones de basquetbolistas que llegaron a la NBA y ligas europeas.',
    'Villa Victoria Ocampo': 'Residencia histórica de Victoria Ocampo, fundadora de la revista Sur.',
    'Central Termoeléctrica San Nicolás': 'Una de las centrales térmicas más grandes del sistema eléctrico argentino.',
    'Parque Independencia y Piedra Movediza': 'La piedra movediza fue la roca más famosa de Argentina: 300 toneladas que oscilaban con el viento.',
    'Astilleros artesanales y náutica menor': 'La industria náutica artesanal de San Fernando: botes, veleros y lanchas construidos por carpinteros navales con…',
    'Universidad Nacional del Sur': 'Principal universidad del sur bonaerense con investigación de excelencia en ingeniería química, materiales y agro.',
    'Reserva Natural Municipal Río Luján': 'Humedales del río Luján con fauna autóctona y vegetación ribereña.',
    'Parque Industrial Campana': 'Zona industrial consolidada con decenas de empresas nacionales e internacionales.',
    'Parque Industrial Mar del Plata': 'Hub de PyMEs industriales: textiles, plástico, metal.',
    'UNICEN': 'Universidad que articula con la industria metalúrgica y agropecuaria.',
    'CINTAN': 'El cluster metalúrgico de Tandil incluye metalurgia de precisión, matrices, moldes y componentes para industria…',
    'Puerto Zárate': 'Puerto fluvial privado que opera en Exporta granos y productos industriales al Mercosur',
    'Puerto San Nicolás': 'Puerto sobre el Paraná que completa la cadena logística siderúrgica: entrada de materia prima y salida de productos…',
    'Puerto Campana': 'Puerto sobre el Paraná integrado al complejo industrial.',
    'Hospital Municipal Dr. Penna': 'Hospital de referencia del sur bonaerense: alta complejidad en un área de influencia de 500km.',
    'UNICEN Olavarría': 'Centro de formación de ingenieros vinculado con la industria cementera y minera local.',
    'Canteras de piedra caliza y mineral': 'Las canteras de piedra caliza que alimentan a las cementeras: extracción minera en plena sierra chica, imagen única…',
    'Santuario Virgen del Aparecido': 'Sitio de devoción religiosa mariana con creciente afluencia de peregrinos bonaerenses.',
    'Universidad Nacional de Luján': 'Universidad que forma a la fuerza laboral del corredor oeste: administración, ciencias agropecuarias, educación.',
    'Estadio Municipal Mundialista 1978': 'Sede del Mundial 78. Historia, deporte y memoria colectiva bonaerense.',
    'Cooperativa Agropecuaria de Junín': 'La cooperativa de primer grado más importante del noroeste bonaerense.',
    'Hospital Presidente Perón': 'Hospital público del norte del conurbano que atiende a la población del delta y la zona continental.',
    'Hipódromo de Luján': 'El hipódromo del corredor oeste: símbolo del turf bonaerense y actividad hípica con tradición centenaria',
    'Laguna de Gómez': 'La laguna más importante del noroeste bonaerense: turismo lacustre, pesca deportiva y esparcimiento para la ciudad…',
    'Parque Industrial Olavarría': 'Zona industrial que alberga PyMEs de la cadena cerámica, refractaria y de la construcción.',
    'El Fortín Cemento / Complejo Cementero': 'Segunda cementera de Olavarría que complementa a Loma Negra.',
    'Complejo Museográfico y Centro Cultural': 'Historia del norte bonaerense, identidad siderúrgica y patrimonio cultural de la ciudad del acero',
    'Centro Histórico y Museo de Zárate': 'Patrimonio fundacional del norte bonaerense.',
    'Complejo Cultural': 'Teatro histórico del sur provincial con 100+ años.',
    'UNNOBA': 'Universidad que forma a los profesionales del noroeste bonaerense: agronomía, ingeniería, informática.',
    'Dique de Vela y Paraje La Cascada': 'Turismo natural serrano en el entorno rural de Tandil.',
    'Hospital Municipal de Junín': 'Hospital de referencia del noroeste bonaerense.',
    'Mercado Central': 'El mayor mercado mayorista de alimentos del país: 540ha, 700+ empresas, conexión con productores de todo el…',
    'Malvinas Argentinas': 'El nombre del municipio es en sí mismo un símbolo patriótico',
    'Escobar': 'Escobar produce el 65% de las flores de corte de Argentina y es el único polo florícola industrial del país.',
    'Hospital Nacional Posadas': 'El hospital público más grande de Argentina por número de camas: 1.200 camas, formación médica y atención de alta…',
    'Hospital El Cruce': 'Modelo de hospital público de alta complejidad en el conurbano profundo: trasplantes, cirugías cardíacas, atención…',
    'Industria del Vidrio': 'Berazategui produce el 80% del vidrio plano de Argentina.',
    'UNLP + Ciudad del Conocimiento': 'Segunda universidad más grande del país con 100.000 estudiantes y sistema CONICET vinculado.',
    'Polo Farmacéutico Nacional': 'El mayor cluster de laboratorios farmacéuticos nacionales del país: Roemmers, Elea, Bagó, Phoenix.',
    'UNLaM': 'Universidad estratégica del municipio más poblado de Argentina.',
    'Cooperativas textiles y economía popular': 'La Matanza concentra el mayor número de cooperativas de trabajo del conurbano: textil, confección, calzado.',
    'CONICET La Plata': 'La mayor concentración de investigadores bonaerenses: IFLP, CIDEPINT, LATU y decenas de centros articulados con la UNLP.',
    'UNQ + Polo Tecnológico Quilmes': 'Universidad Nacional de Quilmes con polo tecnológico e incubadora de empresas tecnológicas.',
    'Puerto Dock Sud / Refinería': 'El complejo portuario e industrial más cercano a la Ciudad de Buenos Aires.',
    'Mercado y Puerto de Frutos de Tigre': 'El Mercado de Frutos es el mercado artesanal y de muebles ratán más conocido del norte bonaerense.',
    'Teatro Argentino de La Plata': 'El segundo teatro lírico más importante de Argentina, sede de ópera, ballet y conciertos de primer nivel.',
    'Centro Textil e Industrial de Avellaneda': 'El mayor cluster textil del Gran Buenos Aires, con miles de talleres y fábricas.',
    'Hospital Paroissien': 'El mayor hospital público del municipio más poblado de Argentina.',
    'UNLaM Extensión + Centro Comercial de Lomas': 'Lomas de Zamora concentra el mayor polo comercial del sur del conurbano.',
    'Aeródromo El Palomar / Hub logístico': 'El ex-Aeródromo El Palomar es estratégico para la conectividad del conurbano oeste.',
    'Hospital San Martín de La Plata': 'Hospital universitario de alta complejidad: formación médica, trasplantes y atención pública de nivel terciario en la…',
    'Hub Industrial y Comercial de Lanús': 'Lanús es el municipio más densamente industrializado del conurbano sur: metalúrgica, textil y comercio popular.',
    'Aeropuerto Internacional Ministro Pistarini': 'El principal aeropuerto del país: conexión de la Argentina con el mundo.',
    'Club Atlético Quilmes': 'El club más antiguo de Argentina (1887).',
    'CONICET Florencio Varela': 'Instituto de Investigaciones Bioquímicas con proyectos de salud y ciencia básica de relevancia nacional.',
    'UNDAV': 'Universidad con perfil de primera generación universitaria del conurbano sur.',
    'Parque Industrial Malvinas Argentinas': 'Uno de los parques industriales más activos del noroeste del conurbano: laboratorios, metalúrgica, plásticos.',
    'Hipódromo de La Plata': 'Hipódromo histórico de la capital provincial: turf, industria hípica y tradición centenaria.',
    'Catedral de San Isidro': 'Una de las catedrales más bellas del país, en el casco histórico colonial de San Isidro.',
    'Puerto San Fernando / Náutica Tigre': 'El complejo náutico más grande del Río de la Plata: clubes de regatas, astilleros, turismo fluvial.',
    'Vicente López': 'El municipio con mayor PBI per cápita del conurbano.',
    'Parque Industrial Escobar': 'Zona industrial en plena expansión sobre el corredor Panamericana.',
    'Universidad de Morón / Centro Universitario': 'Centro de educación superior del conurbano oeste: formación de primera generación universitaria en ingeniería,…',
    'Centro de Innovación y Zona Norte Residencial': 'San Isidro tiene la mayor concentración de empresas tecnológicas y servicios de alto valor del norte del conurbano.',
    'Cooperativa de Trabajo del conurbano sur': 'Florencio Varela concentra cooperativas de trabajo en logística, construcción y servicios.',
    'Parque Industrial Berazategui': 'Zona industrial del sur del conurbano: plástico, metalúrgica y alimentos.',
    'Parque Industrial y Zona Productiva Almirante Brown': 'El mayor municipio del sur del conurbano con parques industriales en expansión y una economía diversificada entre…',
    'Zona Industrial Esteban Echeverría': 'Polo industrial del sur del conurbano con empresas en logística, alimentación y metalurgia.',
    'Cooperativas y Economía Popular de Merlo': 'Merlo concentra una de las redes de cooperativas de trabajo y economía social más activas del conurbano oeste.',
    'Berisso': 'Cuna simbólica del 17 de Octubre de 1945.',
    'Centro Comercial Popular de José C. Paz': 'El corredor comercial de José C. Paz es el mercado popular del noroeste bonaerense: comercio accesible, economía…',
    'Polo Industrial y Comercial de Ituzaingó': 'Municipio industrial del corredor oeste: metalúrgica, servicios y PyMEs de producción.',
    'Hub Industrial General Rodríguez': 'En expansión industrial sobre el corredor Ruta 7.',
    'Centro de Educación Técnica INET / Moreno': 'Moreno tiene uno de los sistemas de educación técnica más activos del conurbano: escuelas técnicas que forman a los…',
    'Hurlingham': 'Hurlingham tiene los clubes deportivos más activos del corredor noroeste.',
    'Puerto de Berisso': 'El puerto histórico donde llegaron los inmigrantes europeos que construyeron la PBA.',
    'San Antonio de Areco': 'El lugar más representativo de la identidad cultural bonaerense: artesanos de plata, talabarteros, la Fiesta Nacional…',
    'AFA': 'La cooperativa agropecuaria de primer grado más grande de Argentina y 22ª del mundo: 33.000 socios, exportaciones a…',
    'San Pedro': 'Principal productor de frutas de clima templado de la Provincia: arándanos, kiwi, ciruelas para Europa.',
    'INTA Pergamino': 'El principal centro de investigación agropecuaria del país: soja, trigo, maíz, semillas y biotecnología.',
    'Complejo Industrial Ramallo': 'La planta de Dow Chemical en Ramallo produce materiales y químicos para toda la industria argentina.',
    'Cámara de Semilleros de Pergamino / Syngenta': 'El ecosistema semillero más denso de Argentina rodea a Pergamino: Syngenta, BASF, Don Mario y decenas de semilleras.',
    'Polo Semillero de Arrecifes / Syngenta-Bayer': 'La mayor concentración de plantas semilleras de Argentina rodea a Arrecifes: Syngenta, Bayer, NIDERA-BASF y…',
    'Cooperativa Frutihortícola del norte bonaerense': 'La cooperativa que organiza a los productores de fruta fresca del norte bonaerense y mejora su poder de negociación…',
    'Plantas de Arándano para Exportación': 'San Pedro es el capital del arándano de exportación de la Provincia: cultivos bajo malla, trazabilidad y…',
    'Capilla del Señor': 'Centro colonial declarado patrimonio',
    'Platería Artesanal': 'La única comunidad de artesanos plateros con técnica centenaria en Argentina.',
    'Estancias Turísticas del Corredor Norte': 'Las estancias turísticas de San Antonio de Areco son el modelo de turismo rural premium bonaerense: gastronomía…',
    'Puerto San Pedro': 'Puerto sobre el Paraná que exporta fruta fresca y manufacturas del norte bonaerense.',
    'INTA Arrecifes': 'Extensión del INTA que trabaja con productores del corredor norte: semillas, plagas y tecnología de aplicación',
    'Museo del Hombre y Transporte': 'Museo histórico sobre movilidad',
    'Zona Franca Metropolitana de Colón': 'La única zona franca de la Provincia de Buenos Aires: régimen aduanero especial, exportaciones e inversión industrial.',
    'Reserva Natural Costanera del Paraná': 'La ribera del Paraná en San Pedro conserva humedales con fauna autóctona: nutrias, carpinchos y aves migratorias.',
    'Estancias boutique del corredor norte': 'Las estancias de lujo del corredor de la Provincia más cercano a CABA: gastronomía, equitación y cultura criolla',
    'Parque Criollo': 'El parque que alberga la Fiesta de la Tradición: rodeo, doma, desfile de gauchos.',
    'Puerto Ramallo': 'Puerto industrial sobre el Paraná que sirve al complejo químico de Ramallo y exporta subproductos de la industria local',
    'San Andrés de Giles': 'Municipio agroproductivo con estancias históricas y campo ganadero.',
    'Pulpería La Blanqueada': 'Pulpería histórica de más de 100 años: la gastronomía criolla auténtica del norte bonaerense.',
    'Río Paraná de las Palmas': 'El Paraná de las Palmas en Baradero: pesca del dorado y surubí, naturaleza ribereña y turismo fluvial accesible',
    'Campo productivo y estancias de Carmen de Areco': 'Municipio agroproductivo del corazón del corredor norte: campo ganadero, estancias de turismo rural y comunidad…',
    'Tambo e industria láctea local': 'Tambos tecnificados del corredor norte que producen leche de calidad para la cuenca láctea bonaerense',
    'Baradero': 'Baradero tiene tradición de construcción naval artesanal sobre el Paraná: botes, canoas y embarcaciones menores.',
    'Turismo rural de la pradera bonaerense': 'Las estancias y el paisaje de Carmen de Areco representan el campo bonaerense auténtico: ceibo, ombú y gaucho',
    'Turismo rural del corredor oeste': 'Las estancias y el paisaje pampeano de Giles como destino de turismo rural accesible',
    'Centro Industrial Pergamino': 'Zona industrial con PyMEs de maquinaria agrícola, metalúrgica y agroalimentaria.',
    'Campo productivo de Salto': 'El municipio de Salto es uno de los más productivos en cereales y oleaginosas del corredor norte.',
    'Cooperativa Agropecuaria de Salto': 'La cooperativa de primer grado que agrupa a los productores cerealeros del norte del corredor y los conecta con el…',
    'INTA Área Salto': 'Centro de transferencia de tecnología agropecuaria para el norte del corredor: cultivos intensivos y manejo de suelos',
    'Campo productivo de Ramallo': 'Agricultura y ganadería intensiva del norte bonaerense.',
    'Campo productivo de Exaltación de la Cruz': 'Agricultura mixta e invernáculos del periurbano norte bonaerense.',
    'Laguna de Arrecifes': 'Turismo lacustre local con pesca deportiva y esparcimiento para las familias del interior norte',
    'Cooperativa agropecuaria de Giles': 'Cooperativa que organiza a los productores del corredor y los conecta con los mercados nacionales',
    'Club Atlético Pergamino / Tejido Social': 'Los grandes clubes de Pergamino son el motor de la vida social del interior norte.',
    'Centro urbano Arrecifes': 'El centro comercial y de servicios rurales del interior del corredor norte.',
    'Campo productivo de Baradero': 'Ganadería y agricultura mixta del norte bonaerense.',
    'Campo productivo de Colón': 'Agricultura mixta y tambo del corredor norte.',
    'Campo productivo de Rojas': 'Rojas es uno de los municipios con mayor productividad por hectárea en soja y trigo del norte bonaerense.',
    'Campo productivo de Capitán Sarmiento': 'Uno de los municipios agroproductivos más eficientes del corredor norte.',
    'Centro histórico de Salto': 'El casco histórico de Salto con arquitectura del siglo XIX y tradición de inmigración europea del norte bonaerense',
    'Cooperativa agropecuaria local': 'La cooperativa que organiza a los productores del sur del interior y los conecta con la comercialización',
    'INTA Área Rojas': 'Extensión del INTA que acompaña la transición tecnológica de los productores del norte del corredor',
    'Centro histórico de Colón': 'Casco histórico del norte bonaerense con arquitectura del siglo XIX y tradición de inmigración europea',
    'Centro histórico y social de Rojas': 'El corazón social del norte bonaerense: clubes, asociaciones y comunidad rural que mantiene vivo el tejido social del…',
    'Centro Comercial y Servicios de Baradero': 'Hub de servicios rurales del norte bonaerense: comercio, salud y educación para los productores del corredor',
    'Centro comunitario de Capitán Sarmiento': 'El tejido social del interior productivo: clubes, asociaciones vecinales y servicios comunitarios del norte bonaerense',
    'Mundo Marino': 'El oceanario y parque marino más grande de América del Sur, en San Clemente del Tuyú.',
    'Puerto Quequén': 'El segundo puerto en exportaciones agropecuarias de la Provincia: millones de toneladas de granos y subproductos del…',
    'Reserva de Biósfera Bahía Samborombón': 'La reserva natural costera más importante de la Provincia: humedal de importancia internacional RAMSAR, nidificación…',
    'Mar Chiquita': 'La única albufera de la Provincia y Reserva de Biósfera UNESCO.',
    'Centro de Rehabilitación de Fauna Marina': 'El único centro de rescate y rehabilitación de fauna marina de la Provincia: lobos marinos, tortugas y aves marinas…',
    'Bosque y Médanos de Gesell': 'El bosque de Villa Gesell fue plantado sobre médanos costeros: único en su tipo en la Argentina.',
    'Cooperativa Pesquera de Necochea': 'La cooperativa pesquera del sur bonaerense que organiza a los marineros y procesa el pescado local',
    'Villa Gesell': 'Villa Gesell es el destino de la clase media bonaerense: fundada sobre médanos como experimento forestal en los años…',
    'Industria de la Harina': 'Los molinos harineros de Necochea procesan el trigo del sur bonaerense: transformación de grano en harina para…',
    'Pinamar': 'Pinamar es el destino de veraneo de la clase media-alta bonaerense: arquitectura pintoresca entre los pinos,…',
    'Pesca Deportiva del Quequén': 'El río Quequén es uno de los mejores ríos para la pesca de dorado y surubí de la Provincia: deportistas de toda la…',
    'Parque Miguel Lillo': 'El parque urbano más grande de Argentina por superficie: más de 400ha de bosque implantado frente al mar.',
    'Laguna de Los Patos': 'Laguna urbana de Necochea con pesca deportiva, kayak y entorno natural a metros del mar.',
    'Centro Histórico de Necochea': 'Necochea combina ciudad productiva y turismo de playa: un equilibrio entre el puerto pesquero y el veraneo familiar',
    'Playa Norte de Necochea': 'La playa más concurrida del sur de la costa bonaerense: turismo familiar de acceso masivo en el corredor sur del litoral',
    'Vivero Florentino Ameghino': 'El mayor vivero público de la Provincia de Buenos Aires: 300ha de producción forestal para repoblar la costa.',
    'Observación de Aves': 'La laguna de Mar Chiquita es uno de los principales sitios de avistaje de aves migratorias de la Provincia:…',
    'San Clemente del Tuyú': 'El primer balneario del litoral atlántico bonaerense al salir de Buenos Aires: punto de entrada de millones de…',
    'Festival Nacional de Danzas Folklóricas': 'El festival folklórico más convocante de la costa bonaerense: danzas de todo el país en el corazón de la temporada de…',
    'Miramar': 'Miramar es el balneario más elegido por las familias bonaerenses con niños: playas calmas, ciudad pequeña y aire puro.',
    'Arquitectura de Pinamar': 'La arquitectura única de Pinamar: casas de diseño integradas al bosque de pinos plantados por Jorge Bunge en los años…',
    'San Bernardo': 'San Bernardo es el destino de playa más accesible para la clase media bonaerense de menores ingresos.',
    'Santa Teresita': 'Santa Teresita concentra el turismo popular en temporada alta: familias de Buenos Aires, jubilados y jóvenes que…',
    'Balneario Municipal y playas públicas': 'Las playas públicas municipales de La Costa: acceso libre y gratuito para todos los bonaerenses.',
    'Ecoturismo de la Reserva de Biósfera': 'Turismo ecológico certificado en la Reserva de Biósfera: recorridas guiadas, kayak en la albufera y avistaje de fauna…',
    'Mar de Ajó': 'El destino más tranquilo de la Costa: pesca artesanal, familias que buscan playa sin masificación.',
    'Gastronomía costera y mariscos de La Costa': 'La oferta gastronómica de mariscos y pescados frescos que representa la identidad culinaria del litoral bonaerense',
    'Artesanías de Villa Gesell': 'La feria de artesanos más conocida de la costa: joyería, cerámica, cuero y arte popular en el corazón turístico de…',
    'Cerveza Artesanal del litoral bonaerense': 'Villa Gesell tiene el mayor número de cervecerías artesanales de la costa bonaerense.',
    'Gastronomía de Gesell': 'La escena gastronómica de Gesell: mariscos, pizzas de molde y la cocina popular de la costa que define el veraneo…',
    'Monte Hermoso': 'Monte Hermoso es el único lugar de la costa argentina donde el sol nace Y se pone sobre el agua del mar.',
    'Cariló': 'Cariló es el barrio más exclusivo de la costa bonaerense: casas de diseño entre pinos centenarios.',
    'Producción hortícola del corredor costero': 'Los productores del periurbano costero de Mar Chiquita abastecen de hortalizas frescas a los balnearios y a Mar del…',
    'Feria de Artesanos de La Costa': 'El circuito de ferias artesanales de la Costa Atlántica: artesanías locales, diseño y producción sustentable en los…',
    'Balneario Parque Atlántico de Mar Chiquita': 'El balneario más exclusivo y tranquilo del litoral norte de la Provincia: playas vírgenes y baja masificación',
    'Club Náutico Gesell': 'Deportes acuáticos, kitesurf y windsurf en las playas de Gesell.',
    'Pesca Artesanal de Miramar': 'La pesca artesanal en la zona de Miramar: una tradición costera de pequeños pescadores que abastece a los…',
    'Frente costero y Balneario Municipal de Miramar': 'Las playas de Miramar: calmas, accesibles y limpias.',
    'Gastronomía premium de Pinamar': 'La oferta gastronómica más sofisticada de la costa bonaerense: restaurantes de calidad que convocan al sector ABC1',
    'Centro de convenciones y turismo de reuniones': 'Pinamar tiene capacidad de alojamiento y reuniones para turismo corporativo: un destino que combina playa y negocios',
    'Parque Municipal de Miramar': 'El parque serrano de Miramar: naturaleza, bañado y biodiversidad en la franja costera.',
    'Festival de Moda y Diseño de Pinamar': 'Los festivales de moda y diseño de Pinamar convocan a diseñadores e influencers nacionales.',
    'Ostende y Valeria del Mar': 'Los balnearios más tranquilos del partido de Pinamar: menos masificados, más naturales y con identidad propia',
    'Playas vírgenes y naturaleza costera': 'Las playas más naturales y menos masificadas de la costa bonaerense: sin edificios de hormigón frente al mar, reserva…',
    'Club Golf Miramar': 'El campo de golf de Miramar atrae al turismo de clase media-alta de Buenos Aires: deporte, tranquilidad y litoral',
    'Pesca artesanal y gastronomía marina': 'La pesca artesanal de Monte Hermoso provee pescado fresco a sus restaurantes.',
    'Polo turístico del litoral sur': 'Monte Hermoso como base del turismo regional del sur: complemento a Bahía Blanca para el visitante que quiere conocer…',
    'Deporte y polo en los courts de Pinamar': 'Los courts de tenis y el polo de Pinamar concentran al turismo deportivo del sector ABC1 en verano',
    'Deportes acuáticos y kitesurf': 'Viento constante y playa extensa hacen de Monte Hermoso el mejor spot de kitesurf del sur bonaerense',
    'Feria de artesanos del litoral sur': 'Artesanías locales en el ambiente tranquilo de Monte Hermoso.',
    'Producción lechera artesanal de Cañuelas': 'Los quesos y dulces de leche artesanales de Cañuelas son conocidos en toda la Provincia.',
    'Hub agropecuario del noroeste': 'Chacabuco es el nodo articulador del noroeste agropecuario: cooperativas cerealeras, acopiadoras y servicios…',
    'Cooperativa láctea': '9 de Julio está en el corazón de la cuenca lechera: cooperativas de primer grado que conectan a pequeños tamberos con…',
    'Feedlot de escala': 'Lincoln concentra uno de los mayores clusters de feedlots del país.',
    'Cabaña ganadera de élite de Azul': 'Azul aloja cabañas ganaderas con genética bovina de primer nivel: reproductores exportados a países vecinos.',
    'Mercedes': 'Mercedes tiene una tradición artesanal en cuero, talabartería y quesos que la ubica como punto de interés cultural…',
    'Marcos PAZ': 'Marcos Paz es uno de los municipios de mayor crecimiento del conurbano sur-oeste: invernáculos, cría de aves y…',
    'Parque Industrial Ensenada': 'La zona industrial que rodea al astillero y la refinería: proveedores metalúrgicos, talleres navales y empresas de…',
    'Cañuelas-Brandsen': 'El periurbano sur de La Plata: tambos tecnificados, invernáculos de tomate y verduras frescas para el AMBA.',
    'Laguna de Lobos': 'Laguna de referencia regional',
    'Quesos artesanales de Los Toldos': 'La ruta del queso de Los Toldos: producción láctea artesanal que complementa la visita histórica con un dato…',
    'Centro industrial PyME de Chacabuco': 'Las PyMEs metalmecánicas y agroalimentarias de Chacabuco que proveen servicios al campo del noroeste bonaerense',
    'Centro productivo de Chivilcoy': 'Chivilcoy es la ciudad del interior bonaerense más completa: servicios rurales, hospital regional y cooperativas…',
    'Hospital Regional de Chivilcoy': 'Hospital de referencia del sudoeste interior: cobertura de salud para productores y familias del interior bonaerense…',
    'Puerto La Plata': 'El puerto histórico de La Plata-Ensenada que integra la logística industrial del cordón platense: petróleo, acero y…',
    'General Las Heras': 'El periurbano sur de CABA: invernáculos, tambo y producción de verduras frescas para el AMBA.',
    'Pehuajó': 'Pehuajó es el centro de servicios del interior profundo del noroeste: salud, educación y cooperativas que articulan a…',
    'Campo productivo de Lobos': 'Agricultura de soja/maíz y ganadería de cría en el corredor centro-sur bonaerense',
    'Centro histórico y cultural de Azul': 'El casco histórico de Azul: arquitectura del siglo XIX, museo y biblioteca que reflejan la identidad cultural del…',
    'Universidad de Mercedes / Centro educativo': 'El centro educativo de Mercedes forma a los jóvenes del interior sur que quieren acceder a la educación universitaria',
    'Suipacha': 'Suipacha combina campo productivo y turismo rural con estancias históricas a 100km de CABA.',
    'Reserva Costanera de Punta Indio': 'Punta Indio tiene la única reserva de costas del Río de la Plata de la Provincia: humedales, fauna silvestre y…',
    'Campo productivo mixto de Azul': 'Agricultura y ganadería mixta del centro bonaerense.',
    'Campo productivo integrado pampeano': 'Bolívar representa al productor pampeano estándar: agricultura y ganadería mixta, cooperativas de servicios y vida…',
    'Agro productivo de Bragado': 'Bragado es uno de los municipios más productivos del interior bonaerense: alta tecnología agropecuaria y rendimientos…',
    'Campo productivo de 25 de Mayo': 'Agricultura de alta productividad y ganadería mixta en el interior sur bonaerense.',
    'Cooperativa agropecuaria de Pehuajó': 'La cooperativa que organiza a los productores del interior profundo del noroeste y los integra con el mercado nacional',
    'Campo productivo de Tapalqué': 'Tapalqué representa el interior agropecuario bonaerense más genuino: campo ganadero, agricoltura de soja y comunidad…',
    'Escuela Agropecuaria de Tapalqué': 'La escuela técnica agropecuaria que forma a los hijos de los productores del Interior: el nexo entre la tradición…',
    'Campo ganadero de Lincoln': 'El campo ganadero de cría y recría del noroeste bonaerense: productores medianos con tradición de décadas',
    'Ganadería y tambo de Carlos Casares': 'Carlos Casares concentra la ganadería de élite y el tambo tecnificado del interior bonaerense.',
    'Campo mixto de 9 de Julio': 'La transición soja-tambo del interior bonaerense: productores que combinan agricultura de renta con producción láctea',
    'Cooperativa y servicios rurales de Bolívar': 'La cooperativa local de Bolívar que integra servicios al productor: acopio, crédito y asesoramiento técnico',
    'Saladillo': 'Saladillo es un municipio productivo del interior sur: ganadería, soja y servicios rurales.',
    'Historia y cultura de Bragado': 'La tradición histórica del interior bonaerense: arquitectura del siglo XIX y comunidad rural con identidad propia',
    'Centro urbano de Lincoln y servicios rurales': 'Lincoln es el hub de servicios rurales del noroeste bonaerense: veterinarios, maquinistas y proveedores del campo',
    'Centro urbano de 9 de Julio': 'La ciudad de 9 de Julio es el centro de servicios del interior bonaerense más importante del noroeste: salud,…',
    'Alberti': 'El campo bonaerense de escala media del interior: ganadería, soja y una comunidad rural tradicional con cooperativas…',
    'Navarro': 'Navarro es un municipio de campo tradicional del interior sur con historia de fundación temprana en la PBA',
    'Campo de General Pinto': 'El norte remoto del interior bonaerense: ganadería extensiva y escasa densidad poblacional.',
    'General Villegas': 'El extremo oeste de la provincia: campo de secano, ganadería extensiva y una comunidad rural aislada que produce sin…',
    'Agro productivo de General Arenales': 'Agricultura de soja y girasol en el noroeste bonaerense.',
    'Campo de Roque Pérez': 'Interior agropecuario del sur interior: campo ganadero y agricultura de soja en zona de cuenca del Salado inferior',
    'Campo del occidente profundo': 'El extremo occidental de la Provincia: campo ganadero extensivo, comunidad rural sólida y la PBA que casi nadie conoce',
    'Museo Fangio + Papa de Balcarce': 'Juan Manuel Fangio —cinco veces campeón mundial de F1, el más grande de la historia— nació en Balcarce.',
    'Laguna de Chascomús': 'La laguna a 115km de CABA más clásica del veraneo bonaerense.',
    'Museo Lítico de Miramar': 'Hallazgos paleontológicos de relevancia mundial',
    'Dolores': 'Fundada en 1817, Dolores fue la primera ciudad del interior de la PBA.',
    'Sociedad Rural de Dolores': 'Una de las Sociedades Rurales más antiguas del país, representando al ganadero profundo de la cuenca del Salado',
    'Chascomús': 'En 1952, Chascomús eligió a la primera mujer intendenta de Argentina.',
    'Escuela Agropecuaria de Rauch': 'La escuela técnica agropecuaria de Rauch forma a los hijos de los productores del interior con capacitación práctica…',
    'Feria Regional de Chascomús': 'Encuentro de productores del Salado',
    'Pesca deportiva del pejerrey': 'Chascomús tiene los mejores campeonatos de pesca del pejerrey de la Provincia.',
    'Las Flores': 'Las Flores tiene cabañas ganaderas de primer nivel con reproductores de genética certificada y remates que convocan a…',
    'Cría de bovinos de élite': 'Las cabañas de Las Flores producen los toros y vaquillonas de genética superior que mejoran los rodeos de la cuenca…',
    'Centro Histórico y Museo de Chascomús': 'El casco histórico de Chascomús con sus iglesias del siglo XIX, el Museo Pampeano y la arquitectura colonial del…',
    'Estación Ferroviaria': 'Símbolo del pasado productivo',
    'McCain Argentina': 'La mayor planta de procesamiento de papa congelada de Argentina en el municipio que lleva el nombre del alimento más…',
    'INTA Balcarce': 'El Centro de Investigación Agropecuaria del INTA en Balcarce es uno de los principales del país: papa, ganadería y…',
    'Haras Nacionales': 'Institución nacional emblemática',
    'Ganadería del interior profundo del Salado': 'Campo ganadero extensivo de la cuenca del Salado: bovinos de cría en lotes con pastizal natural.',
    'Ayacucho': 'La Sociedad Rural de Ayacucho representa al ganadero del Salado sur: productores influyentes en carne y genética…',
    'Laguna de Monte': 'Reserva de humedales con biodiversidad notable',
    'Laguna del Monte': 'La Laguna del Monte es uno de los destinos turísticos lacustres más accesibles del sur bonaerense: pejerrey, vela y…',
    'Marismas y Reserva del Tuyú': 'Las marismas del Tuyú en General Madariaga: fauna costera, caza deportiva regulada y naturaleza del litoral atlántico…',
    'Lobería': 'Lobería tiene una tradición quesera artesanal conocida en la zona sur: quesos de pasta dura y semidura de producción…',
    'Producción papera de Balcarce': 'Los campos de papa de Balcarce: siembra, cosecha y tecnología de producción que convirtió a este municipio en…',
    'Centro urbano y servicios de Dolores': 'El centro de servicios rurales de la cuenca del Salado interior: salud, educación y comercio para los productores de…',
    'Laguna y turismo lacustre de General Belgrano': 'La laguna de General Belgrano: turismo local, pesca deportiva y esparcimiento para el interior sur del Salado',
    'Sierra de los Padres': 'El paraje serrano de Balcarce: turismo rural en el corredor entre Tandil y Mar del Plata.',
    'Campo ganadero de la cuenca del Salado': 'Campo de cría y recría del Salado: ganadería extensiva sobre pastizal natural en el interior bonaerense profundo',
    'Campo ganadero y agrícola de Rauch': 'Ganadería de cría y agricultura de soja del interior de la cuenca del Salado.',
    'Ganadería extensiva del Salado sur': 'Campo ganadero de cría y recría en el interior profundo de la cuenca del Salado.',
    'Campo agroproductivo de Maipú': 'Agricultura y ganadería del interior central del Salado.',
    'Centro urbano y Feria Rural de Las Flores': 'La feria rural de Las Flores reúne anualmente a productores y ganaderos de toda la cuenca.',
    'Centro comunitario rural de Rauch': 'El club y las instituciones sociales de Rauch mantienen el tejido comunitario del interior: deporte, cultura y…',
    'Turismo de proximidad': 'San Miguel del Monte como destino de fin de semana para el conurbano sur: campo, laguna y naturaleza a 80km de CABA',
    'Campo ganadero de General Belgrano': 'Ganadería de cría y agricultura en el interior sur del Salado.',
    'Turismo rural del corredor costero interior': 'El turismo rural y de pesca del interior costero: caza regulada, pesca deportiva y campo abierto',
    'Campo ganadero del norte del Salado': 'Ganadería de cría y tambo del norte de la cuenca del Salado.',
    'Campo ganadero extensivo de Ayacucho': 'Ganadería de cría y ciclo completo en el sur de la cuenca del Salado.',
    'Campo y ganadería del interior costero': 'Ganadería extensiva y campo costero en el litoral atlántico interior.',
    'Producción agropecuaria de Lobería': 'Ganadería y agricultura mixta del interior sur bonaerense.',
    'Campo ganadero de Castelli': 'Ganadería extensiva del interior sur del Salado.',
    'Centro de Ayacucho': 'Hub de servicios para los productores del Salado sur: veterinarios, proveedores de insumos y comercio rural',
    'Centro de servicios de Maipú': 'Hub de servicios rurales del interior central del Salado: comercio, salud y educación para el productor del interior',
    'Centro de servicios de General Belgrano': 'Hub de servicios rurales del interior sur: educación, salud y comercio para los productores del Salado',
    'Campo agropecuario de San Cayetano': 'Agricultura y ganadería del litoral interior sur: producción de cereales y bovinos en el borde de la cuenca costera',
    'Historia y patrimonio de Ayacucho': 'El casco histórico de Ayacucho con su iglesia y arquitectura del siglo XIX.',
    'Tradición histórica gaucha de Castelli': 'El gaucho de la cuenca del Salado: tradición de la jineteada, la doma y la vida rural del interior profundo',
    'Club social y deportivo de Lobería': 'El tejido social de Lobería: clubes, asociaciones y eventos que mantienen viva la comunidad rural del interior sur',
    'Centro de servicios de San Cayetano': 'Hub de servicios rurales del interior sur profundo.',
    'Parque Provincial Tornquist': 'Las únicas sierras de la Provincia de Buenos Aires.',
    'Guaminí': 'En 2014, Guaminí fue el PRIMER municipio de Argentina en adoptar agroecología como política pública, generando la…',
    'Tres Arroyos': 'Tres Arroyos es el centro de la producción cerealera del sur: trigo, girasol y soja con cooperativas centenarias.',
    'Coronel Suárez': 'Coronel Suárez es la capital del calzado del interior bonaerense: Piccadilly, Price Shoes y decenas de fábricas de…',
    'Cooperativas cerealeras históricas de Tres Arroyos': 'Las cooperativas centenarias de Tres Arroyos son modelo de organización del productor cerealero: acopio, venta y…',
    'Lago Epecuén': 'El Lago Epecuén tiene aguas hipersalinas comparables al Mar Muerto: históricamente elegidas para tratar reumatismo y…',
    'Villarino': 'El único polo hortícola del sur bonaerense: producción bajo riego en zona árida gracias al Canal Laprida y el Río…',
    'Carmen de Patagones': 'La ciudad más austral de la Provincia: en 1827 ganó la única batalla en que Argentina venció a Brasil.',
    'Cerro Tres Picos': 'El Cerro Tres Picos es el punto más alto de la Provincia de Buenos Aires (1.239m).',
    'Lagunas de Guaminí': 'Las 4 lagunas de Guaminí (Monte, Cochicó, Alsina, Venado) tienen el mejor pejerrey deportivo del sur bonaerense.',
    'Cooperativas y PyMEs del calzado': 'Las cooperativas de producción de calzado del sur bonaerense: modelos de integración productiva con valor agregado en…',
    'Zanja de Alsina': 'La Zanja de Alsina (1877): la única frontera del siglo XIX todavía visitable en Argentina.',
    'Ganadería del sur': 'La ganadería del sur bonaerense: bovinos de ciclo completo en campo patagónico.',
    'Valle Bonaerense del Colorado': 'El Valle Bonaerense del Río Colorado produce frutas y verduras para el sur del país.',
    'Identidad inmigrante': 'La comunidad de alemanes del Volga, españoles e italianos que fundaron Coronel Suárez le da una identidad…',
    'Historia del Lago Epecuén y la inundación de 1985': 'El testimonio histórico de la catástrofe del Lago Epecuén: la evacuación de 1500 personas en 15 días y la historia de…',
    'Carhué': 'La ciudad de Carhué es la base operativa para visitar Villa Epecuén y el Lago: balneario termal, gastronomía y…',
    'Villa La Angostura bonaerense': 'El pueblo de Sierra de la Ventana: arquitectura pintoresca en el pie de la sierra, sin el precio de la Patagonia.',
    'Estancias en la Sierra': 'Las estancias al pie de la sierra ofrecen turismo rural con el telón de fondo de las sierras: cabalgatas, senderismo…',
    'Ecoturismo y Reservas de la Sierra': 'El corredor ecoturístico de la Sierra de la Ventana: reservas privadas, observación de fauna autóctona y rutas de…',
    'Colonias agrícolas del sur': 'Las colonias agrícolas de origen inmigrante del sur de Villarino: alemanes, italianos y polacos que convirtieron el…',
    'Litoral atlántico sur': 'El litoral sur bonaerense en Coronel Rosales: playas naturales, fauna costera y el paisaje donde la Provincia termina…',
    'Río Negro': 'El Río Negro en Patagones: el límite entre la PBA y Río Negro, entre la Pampa y la Patagonia.',
    'Historia colonial del Fuerte del Carmen': 'El Fuerte del Carmen de Patagones (1779): el fuerte colonial más austral del Virreinato del Río de la Plata.',
    'Punta Alta': 'Punta Alta es la ciudad más importante del sur-litoral bonaerense: base de la economía del partido, servicios y…',
    'Sesquicentenario 2026': 'Guaminí cumple 150 años en 2026 (fundado el 30 de marzo de 1876).',
    'Centro histórico y cultural de Tres Arroyos': 'El casco histórico de Tres Arroyos: arquitectura del sur bonaerense, museos e identidad cultural de la ciudad más…',
    'Río Colorado': 'El Río Colorado marca el límite sur de la Provincia de Buenos Aires.',
    'Laprida': 'Laprida recuerda al prócer Francisco Narciso de Laprida, presidente del Congreso que declaró la Independencia.',
    'Campo productivo de Coronel Suárez': 'Agricultura y ganadería del sur bonaerense que complementa al cluster industrial del calzado.',
    'Sierra Chica bonaerense en Benito Juárez': 'El extremo sur de las sierras bonaerenses en Benito Juárez: un paisaje único que une la llanura y la sierra en el sur…',
    'Campo ganadero de Laprida': 'Ganadería del sur interior bonaerense: bovinos de cría en el límite entre la pampa y el sur árido',
    'Saavedra': 'Saavedra es el acceso norte al corredor de la Sierra de la Ventana.',
    'Puerto de Coronel Dorrego': 'El puerto de Coronel Dorrego sobre el Atlántico sur.',
    'Puán': 'Puán está al pie de las sierras del sur: el corredor entre la Sierra de la Ventana y el límite sur de la Provincia.',
    'Benito Juárez': 'Ganadería y agricultura mixta del sur interior de la Provincia.',
    'Campo de Coronel Dorrego': 'Ganadería y cereales del litoral sur bonaerense.',
    'Campo productivo de Coronel Pringles': 'Agro del interior sur bonaerense: ganadería de cría y cereales.',
    'Producción agropecuaria del sur extremo': 'La ganadería y agricultura del sur extremo de la Provincia: condiciones áridas, producción extensiva y la resiliencia…',
    'Campo del sur interior': 'Ganadería extensiva y producción agropecuaria del interior sur.',
    'Daireaux': 'Ganadería extensiva y soja del interior sur bonaerense.',
    'General La Madrid': 'Agro del interior sur de la Provincia: ganadería y cereales en la transición entre la pampa húmeda y la pampa semiárida',
    'Salliqueló': 'Ganadería y agricultura del interior sur.',
    'Tres Lomas': 'El interior más remoto del sur bonaerense: campo extensivo, comunidad rural pequeña y la Provincia que pocos conocen…',
    'Pellegrini': 'El interior profundo del sur bonaerense: campo ganadero extensivo y comunidad rural aislada que produce sin…',
    'Agro del sur semiárido': 'Ganadería extensiva en zona de transición semiárida del sur profundo bonaerense',
    'Servicio rural y comunidad de Adolfo G. Chaves': 'Los servicios comunitarios del interior sur: educación, salud y tejido social del campo profundo bonaerense',
    'Centro de servicios del sur interior': 'Hub de servicios rurales del sur interior: salud, educación y comercio para el productor del sur profundo',
    # ── Nuevos privados 2ª ronda ──
    'Cooperativa Obrera': 'Una de las 20 cooperativas de consumo más grandes del mundo; desde 1926 le gana al supermercado en Bahía Blanca sin un solo accionista',
    'Ternium Argentina': 'La planta siderúrgica integrada más grande de Argentina: 4.000 empleados, el acero de cada puente e infraestructura del país',
    'Profertil': 'El mayor productor de fertilizantes nitrogenados de América Latina; sin esta planta Argentina no puede fertilizar su propia cosecha',
    'Cervecería y Maltería Quilmes': 'Inmigrantes suizos que llegaron a vender hielo en 1888 y hoy producen 20M de litros/mes: la marca de cerveza más icónica de Argentina',
    'Sinergium Biotech': 'La única empresa privada de Argentina que fabrica vacunas y biofármacos a escala industrial: millones de dosis anuales desde Garín, Escobar',
    'Papel Prensa': 'La única fábrica de papel de diario de Argentina: sin este predio en San Pedro no hay ningún periódico impreso en el país',
    'Los Grobo': 'El pool de siembra más conocido del mundo nació en 25 de Mayo: lo que inventaron en los 80 cambió la agricultura de América del Sur',
}

# ── SEMÁFORO POLÍTICO — lugares PRIVADO ─────────────────────────────────────
# V=Receptivo 🟢 | A=Evaluar 🟡 | R=Evitar 🔴
# Solo aplica a lugares con acc==PRIVADO
REC_DICT = {
    'La Juanita':'V','MadyGraf':'V','Cooperativa Obrera':'V','CATA Cooperativa':'V',
    'La Ballenita':'V','Y-TEC':'V','Antares':'V','Mestrina':'V',
    'Ecoturismo Ventana':'V','Cagnoli':'V','Piscicultura Salado':'V',
    'Plantín':'V','Cooperativa Apícola':'V','Cooperativa Hortícola':'V',
    'Toyota':'A','TenarisSiderca':'A','Ternium Argentina':'A','Loma Negra':'A',
    'Bioceres':'A','Fric-Rot':'A','San Miguel S.A':'A','Semino':'A',
    'Pesquera Bariloche':'A','PBBPolisur':'A','Profertil':'A','Sinergium':'A',
    'Cervecería y Maltería Quilmes':'A','Cumelén':'A','El Ombú Grande':'A',
    'Calzados Guante':'A','La Lacteo':'A','Los Grobo':'A','Conarpesa':'A',
    'Mastellone':'A',
    'Papel Prensa':'R',
}
REC_META = {'V':('#1b4332','#d8f3dc','🟢 Receptivo'),
            'A':('#78350f','#fef3c7','🟡 Evaluar'),
            'R':('#7f1d1d','#fee2e2','🔴 Evitar')}

def get_rec(name):
    nl = name.lower()
    for k, v in REC_DICT.items():
        if k.lower() in nl:
            return v
    return 'A'   # default: evaluar

# ── CLASIFICACIÓN COMUNICACIONAL ────────────────────────────────────────────
_AL = {  # key → etiqueta corta para popup
    'industria':'Industria','rural':'Rural','transporte':'Transporte',
    'construccion':'Construcción','educacion':'Educación','salud':'Salud',
    'comercio':'Comercio','gastronomia':'Gastronomía/Tur.','seguridad':'Seguridad',
    'extractivismo':'Extractivismo','energia':'Agua/Gas/Elec.','comunicacion':'Comunicación',
    'tecnologia':'Tecnología','serv_prof':'Serv. Profesionales','finanzas':'Finanzas',
    'emp_publico':'Emp. Público','arte':'Arte/Recreación','afil_pj':'Afil. PJ',
    'afil_ucr':'Afil. UCR','afin_peron':'Afines Peronismo','afin_lib':'Afines Libertarios',
    'afin_jxc':'Afines JxC','afin_izq':'Afines Izq.','auh':'AUH',
    'crojo':'Círculo Rojo','coop_ing':'Coop./Monotrib. Social','informales':'Informales',
    'asalariados':'Asalariados','cta_propia':'Cta. Propia','jubilados':'Jubilados/Pens.',
    'priv':'Sector Privado','dir':'Directores/Gerentes','operarios':'Operarios/Oficios',
    'admin':'Personal Admin.','prof_cient':'Prof. Científicos','tecnicos':'Técnicos',
    'trab_agro':'Trab. Agropecuarios','map_sub18':'MaPadres Sub-18',
    'map_7_13':'MaPadres 7–13','con_auto':'Con Auto','sin_os':'Sin Obra Social',
    'pami':'PAMI','desempleo':'Desempleados','medicos':'Médicos','docentes':'Docentes',
    'vota_siempre':'Votan Siempre','primer_voto':'Primer Voto',
    'amarillos':'Amarillos','azules':'Azules','celestes':'Celestes',
    'naranjas':'Naranjas','rojos':'Rojos','verdes':'Verdes','violetas':'Violetas',
    'conserv':'Conservadores','cosmop':'Cosmopolitas','desenc':'Desencantados',
    'mater':'Materialistas','progres':'Progresistas','s_pop':'Sectores Populares',
    'subsist':'Subsistentes','tradicion':'Tradicionalistas',
    'emp_pymes':'Empleadores PyME','empl_pymes':'Empleados PyME',
}
def _ks(keys): return ' · '.join(_AL.get(k, k) for k in keys)

# (emoji, label, reach_core, color,
#  core_kws, sec_kws, trans_kws,
#  match_keywords)
CATS = [
    ('⚡','Energía / Soberanía','4–7M','#c55b0b',
     ['energia','extractivismo','jubilados','pami','sin_os','informales'],
     ['asalariados','industria','map_sub18','azules','celestes','mater'],
     ['vota_siempre','amarillos','naranjas','rojos','emp_publico'],
     ['ypf','atucha','cnea','astilleros río santiago','pbbpolisur','nuclear','refinería','y-tec','ytec','destiler','petroq','base naval','armada','rompehielo','energía eléctrica']),
    ('🔬','Ciencia / Tecnología','2–3.5M','#3f4db5',
     ['tecnologia','educacion','prof_cient','tecnicos','amarillos','cosmop'],
     ['comunicacion','serv_prof','progres','azules','cta_propia'],
     ['docentes','medicos','emp_pymes','map_7_13','afin_izq'],
     ['inta ','conicet','bioceres','inti ','universidad nacional','tecnolog','laborator','biotech','piscicultura','y-tec']),
    ('🤝','Cooperativas / Eco. Social','3–5M','#7e3af2',
     ['coop_ing','auh','informales','desempleo','s_pop','subsist','naranjas','rojos'],
     ['afin_peron','afil_pj','empl_pymes','asalariados','amarillos'],
     ['map_sub18','vota_siempre','cta_propia','progres'],
     ['cooperativa','madygraf','la juanita','trabajo recuperado','economía social','monotributo social','🔄 alt. priv. — cooperativa']),
    ('🎣','Pesca / Puertos','2.5–4M','#1d3461',
     ['extractivismo','gastronomia','operarios','naranjas','rojos'],
     ['rural','transporte','amarillos','mater','crojo'],
     ['map_sub18','informales','afin_peron','vota_siempre'],
     ['pesquera','pesca ','puerto ','langostino','merluza','marisco','conarpesa','flota pesquera','🔄 alt. priv. — pesquera bariloche']),
    ('🥩','Cadena Cárnica','3.5–5M','#b5284f',
     ['industria','rural','operarios','trab_agro','empl_pymes','naranjas','rojos'],
     ['transporte','asalariados','priv','mater','desenc','emp_pymes','crojo'],
     ['map_sub18','informales','afin_peron','afil_pj'],
     ['frigorífico','ganadería','feedlot','cárnico','matadero','cabaña bovina','cabaña ganadera','genética bovina','cunicultura']),
    ('🌾','Agroindustria / Campo','3–5M','#2d6a4f',
     ['rural','trab_agro','industria','emp_pymes','conserv','tradicion'],
     ['empl_pymes','asalariados','mater','desenc','cta_propia','dir'],
     ['map_sub18','informales','celestes','azules'],
     ['tambo','lechería','semino','molinos juan','semillas','silo','agropecuaria','granja','apícola','hortíco','viticultura','citricultura','cata ','cata tres','la lacteo','cabañas cumelén','cooperativa apícola','estancia','rio colorado']),
    ('⚙️','Industria / Manufactura','3–5M','#c9a84c',
     ['industria','operarios','tecnicos','priv','empl_pymes','con_auto'],
     ['asalariados','construccion','transporte','mater','desenc','azules'],
     ['map_sub18','celestes','afil_pj','emp_pymes'],
     ['toyota','ternium','siderar','metalúrg','automotriz','autopart','fric-rot','rexnord','plantin','mestrina','loma negra','cemento','calzados guante','cervecería','antares','astilleros mestrina','manufactur']),
    ('🏛️','Patrimonio / Identidad','3.5–6M','#8a6800',
     ['afin_peron','afil_pj','naranjas','rojos','gastronomia','jubilados'],
     ['conserv','tradicion','mater','vota_siempre','pami','crojo'],
     ['map_sub18','s_pop','subsist','desenc'],
     ['museo','casa museo','monumento','eva perón','los toldos','chapadmalal','epecuén','fuerte','histórico','patrimoni','turístico complejo','villa epecuén','fuerte del carmen','complejo vial','paso de los libres','batalla','astillero río santiago']),
]

# ── EJES ESTRATÉGICOS (overlay candidato) ────────────────────────────────────
# Qué narrativa/relato del candidato activa cada visita
# (emoji, label, color_bg, color_border, keywords)
EJES_MAP = [
    ('🇦🇷','Soberanía','#ede9fe','#7c3aed',
     ['atucha','base naval','cnea','astilleros río santiago','ypf','destiler','rompehielo',
      'armada','nuclear','fragata','lancha','fuerza aérea','regimiento','pbbpolisur','y-tec','ytec']),
    ('⚙️','Producción','#fef3c7','#b45309',
     ['toyota','tenaris','siderar','loma negra','serenísima','fric-rot','rexnord','calzados',
      'cervecería','antares','plantin','astilleros mestrina','manufactur','metalúrg','automotriz',
      'autopart','cemento','frigorifico','industri']),
    ('🌾','Campo','#d1fae5','#2d6a4f',
     ['inta ','cata ','cata tres','cooperativa agr','cooperativa apícola','semino','tambo',
      'lechería','semillas','granja','apícola','hortíco','estancia','agropecuaria','molinos juan',
      'la lacteo','cumelén','piscicultura','río colorado']),
    ('🔬','Ciencia','#dbeafe','#3f4db5',
     ['conicet','bioceres','inti ','laborator','biotech','inidep','universidad nacional',
      'tecnolog','y-tec','ytec','cnea']),
    ('🤝','Eco. Social','#ede9fe','#7e3af2',
     ['cooperativa','la juanita','madygraf','trabajo recuperado','economía social',
      'monotributo social','coop. apícola','🔄 alt. priv. — cooperativa']),
    ('🏛️','Identidad','#fefce8','#8a6800',
     ['eva perón','los toldos','epecuén','fuerte del carmen','chapadmalal',
      'casa museo','histórico','patrimoni','batalla','complejo vial','complejo turístico']),
    ('🎣','Mar / Recursos','#e0f2fe','#1d3461',
     ['pesquera','pesca ','puerto ','conarpesa','langostino','merluza','marisco','flota']),
    ('🏔️','Territorio','#dcfce7','#166534',
     ['parque provincial','ventana','tornquist','sierras','lago','ecotur',
      'balneario','villa serrana','termas','complejo tur','turístico']),
]

def get_eje(p):
    """Devuelve (emoji, label, color_bg, color_border) o None."""
    text = (p[0] + ' ' + (p[7] if len(p)>7 else '')).lower()
    for emoji, label, cbg, cborder, kws in EJES_MAP:
        if any(k in text for k in kws):
            return (emoji, label, cbg, cborder)
    return None

def get_cat(p):
    """Devuelve (emoji, label, reach, color, info_str) o None.
    info_str usa || como separador de secciones para el popup."""
    text = (p[0] + ' ' + (p[7] if len(p)>7 else '')).lower()
    for emoji, label, reach, color, core, sec, trans, kws in CATS:
        if any(k in text for k in kws):
            info = (f'{emoji} {label}||'
                    f'Reach CORE: {reach} (Meta PBA)||'
                    f'● CORE: {_ks(core)}||'
                    f'◐ SECUNDARIA: {_ks(sec)}||'
                    f'○ TRANSVERSAL: {_ks(trans)}')
            return (emoji, label, reach, color, info)
    return None

def get_hook(p):
    """Devuelve el hook de una línea para mostrar en tabla."""
    name = p[0]
    for k, v in HOOKS.items():
        if k.lower() in name.lower():
            return v
    return ''

HALLAZGOS = {
    'Toyota':'Única planta de Toyota en Argentina',
    'TenarisSiderca':'40% de los tubos de YPF',
    'Loma Negra':'40% del cemento de Argentina',
    'Central Nuclear Atucha':'34% de la energía nuclear del país',
    'Tambo robot':'Único tambo robotizado de PBA',
    'Villa Epecuén':'Ciudad sumergida 25 años, visible desde satélite',
    'Casa Museo Eva Perón':'Lugar de nacimiento de Eva Perón',
    'Astilleros Río Santiago':'Astillero estatal más grande de Argentina',
    'Destilería YPF':'Refinería más grande de Argentina',
    'Base Naval Puerto Belgrano':'La base naval más grande de América del Sur',
    'La Serenísima':'1 de cada 3 litros de leche en Argentina',
}

def get_acceso(p):
    c = (p[0]+' '+p[8]).lower()
    for k in PRIVADO_KW:
        if k in c: return 'PRIVADO'
    for k in NACIONAL_KW:
        if k in c: return 'NACIONAL'
    return 'PROTOCOLAR'

def get_hallazgo(p):
    for k,v in HALLAZGOS.items():
        if k.lower() in p[0].lower(): return v
    return None

# Clusters
raw_con = [p for p in conurbano.CONURBANO if 'pilar' not in p[0].lower()]
raw_con += [
    ('Malvinas Argentinas — El único municipio con nombre soberano','Malvinas Argentinas',8,8,10,9,7,'El nombre del municipio es en sí mismo un símbolo patriótico.','vecinos, organizaciones civiles'),
    ('La Serenísima / Mastellone Hermanos — La leche de los argentinos','General Rodríguez',8,9,9,9,8,'Planta principal de la marca más icónica de lácteos de Argentina.','mastellone, empresa privada'),
]
raw_cor = list(otros.CORREDOR) + [
    ('Museo del Hombre y Transporte — Luján','Luján',6,7,7,6,8,'Museo histórico sobre movilidad.','municipio, cultura'),
    ('Capilla del Señor — Centro histórico colonial','Exaltación de la Cruz',6,7,8,6,7,'Centro colonial declarado patrimonio.','municipio, patrimonio'),
]
raw_sal = list(interior.SALADO) + [
    ('Laguna de Lobos — Turismo rural','Lobos',6,7,8,6,7,'Laguna de referencia regional.','municipio, turismo'),
    ('Museo Lítico de Miramar','General Alvarado',6,8,9,7,7,'Hallazgos paleontológicos de relevancia mundial.','municipio, ciencia'),
    ('Laguna de Monte — Reserva natural','San Miguel del Monte',5,7,8,6,7,'Reserva de humedales con biodiversidad notable.','municipio, ambiente'),
    ('Feria Regional de Chascomús','Chascomús',6,7,7,7,7,'Encuentro de productores del Salado.','municipio, productores'),
    ('Haras Nacionales — Sede Central','San Miguel del Monte',6,7,8,7,7,'Institución nacional emblemática.','haras, nacion'),
    ('Estación Ferroviaria — General Belgrano','General Belgrano',5,7,8,6,7,'Símbolo del pasado productivo.','municipio, historia'),
]

import data_alternativas_privadas as _alt_mod
import data_nuevos_relatos as _new_mod

CLUSTERS = {
    'CIUDADES':  top50(ciudades.CIUDADES),
    'CONURBANO': top50(raw_con),
    'CORREDOR':  top50(raw_cor),
    'COSTERO':   top50(otros.COSTERO),
    'INTERIOR':  top50(interior.INTERIOR),
    'SALADO':    top50(raw_sal),
    'SUR':       top50(sur_m.SUR),
}
# Agregar nuevos relatos DESPUÉS de top50 (siempre incluidos)
for _cl, _news in _new_mod.NUEVOS_POR_CLUSTER.items():
    CLUSTERS[_cl] = CLUSTERS[_cl] + _news
# Agregar alternativas privadas DESPUÉS de top50 (siempre incluidas)
for _cl, _alts in _alt_mod.ALTERNATIVAS_POR_CLUSTER.items():
    CLUSTERS[_cl] = CLUSTERS[_cl] + _alts

all_places = [(cl,p) for cl,data in CLUSTERS.items() for p in data]
total_priv = sum(1 for cl,p in all_places if get_acceso(p)=='PRIVADO')
total_nac  = sum(1 for cl,p in all_places if get_acceso(p)=='NACIONAL')
total_prot = sum(1 for cl,p in all_places if get_acceso(p)=='PROTOCOLAR')

# ── Embed doc helper ─────────────────────────────────────────────────────────
def embed_doc(path):
    with open(path, encoding='utf-8') as f: html = f.read()
    styles = re.findall(r'<style[^>]*>(.*?)</style>', html, re.DOTALL)
    body   = re.search(r'<body[^>]*>(.*?)</body>', html, re.DOTALL|re.IGNORECASE)
    return f'<style>{"".join(styles)}</style>{body.group(1) if body else ""}'

# ── Render: place card (top-5 visual) ───────────────────────────────────────
def place_card(cl, p, rank):
    meta = CLUSTER_META[cl]
    clr  = meta['color']
    acc  = get_acceso(p)
    icon, tc, bg, adesc = ACC_STYLE[acc]
    hallazgo = get_hallazgo(p)
    ie,pc,ut,rs,lv,tot = score_detail(p)
    cat = get_cat(p)
    h_badge = (f'<div class="h-badge">🔍 {hallazgo}</div>') if hallazgo else ''
    cat_badge = ''
    if cat:
        cemoji, clabel, creach, ccolor, cinfo = cat
        cat_badge = (f'<span class="pc-cat-chip" style="background:{ccolor}18;border:1px solid {ccolor}55;color:{ccolor}" '
                     f'data-info="{cinfo}" title="{clabel} — {creach}">{cemoji} {creach}</span>')
    return f'''<div class="pc" style="--cl:{clr}">
  <div class="pc-rank">#{rank}</div>
  <div class="pc-acc" style="background:{bg};color:{tc}">{icon} {acc} <span class="acc-sub">— {adesc}</span></div>
  <div class="pc-name">{p[0]}</div>
  <div class="pc-muni">📍 {p[1]}</div>
  {h_badge}
  <div class="pc-scores">
    <div class="pc-total td-score-val" data-sc="IE:{ie}|PC:{pc}|UT:{ut}|RS:{rs}|LV:{lv}" title="Click para ver composición del score">{tot:.2f}</div>
    {cat_badge}
  </div>
  <p class="pc-just">{p[7]}</p>
</div>'''

# ── Render: compact card (top-5 horizontal row) ─────────────────────────────
def place_card_compact(cl, p, rank):
    clr  = CLUSTER_META[cl]['color']
    acc  = get_acceso(p)
    icon, tc, bg, _ = ACC_STYLE[acc]
    ie,pc,ut,rs,lv,tot = score_detail(p)
    cat = get_cat(p)
    eje = get_eje(p)
    hallazgo = get_hallazgo(p)
    # Eje badge
    eje_html = ''
    if eje:
        ee, el, ebg, ebd = eje
        eje_html = f'<span class="p5-eje" style="background:{ebg};border-color:{ebd};color:{ebd}">{ee} {el}</span>'
    # Audiencia chip
    cat_html = ''
    if cat:
        cemoji, clabel, creach, ccolor, cinfo = cat
        cat_html = (f'<span class="p5-cat cat-chip" style="background:{ccolor}18;border-color:{ccolor}55;color:{ccolor}" '
                    f'data-info="{cinfo}" title="{clabel}">{cemoji} {creach}</span>')
    h_dot = ' <span style="font-size:.6rem;color:#f59e0b">🔍</span>' if hallazgo else ''
    # Acceso (mini)
    acc_mini = f'<span class="p5-acc" style="background:{bg};color:{tc}">{icon} {acc}</span>'
    # Semáforo político (solo PRIVADO)
    rec_html = ''
    if acc == 'PRIVADO':
        rv = get_rec(p[0])
        rfg, rbg, rlbl = REC_META[rv]
        rec_html = (f'<span class="p5-rec" style="background:{rbg};color:{rfg};'
                    f'border:1px solid {rfg}44;border-radius:3px;padding:1px 5px;'
                    f'font-size:.6rem;font-weight:700;white-space:nowrap">{rlbl}</span>')
    return (f'<div class="pc5" style="--cl:{clr}">'
            f'<div class="p5-top">'
            f'<span class="p5-rank" style="background:{clr}">#{rank}</span>'
            f'{acc_mini}'
            f'{rec_html}'
            f'</div>'
            f'<div class="p5-name">{p[0]}{h_dot}</div>'
            f'<div class="p5-muni">📍 {p[1]}</div>'
            f'<div class="p5-bottom">'
            f'<span class="p5-score td-score-val" data-sc="IE:{ie}|PC:{pc}|UT:{ut}|RS:{rs}|LV:{lv}" title="Click para composición">{tot:.2f}</span>'
            f'{eje_html}'
            f'{cat_html}'
            f'</div>'
            f'</div>')

# ── Render: list item (places 6-50) ─────────────────────────────────────────
def place_list_item(cl, p, rank):
    clr = CLUSTER_META[cl]['color']
    acc = get_acceso(p)
    icon, tc, bg, _ = ACC_STYLE[acc]
    ie,pc,ut,rs,lv,tot = score_detail(p)
    hallazgo = get_hallazgo(p)
    h = f' <span class="li-h">🔍</span>' if hallazgo else ''
    rec_html = ''
    if acc == 'PRIVADO':
        rv = get_rec(p[0])
        rfg, rbg, rlbl = REC_META[rv]
        rec_html = (f'<span style="background:{rbg};color:{rfg};border:1px solid {rfg}44;'
                    f'border-radius:3px;padding:1px 4px;font-size:.6rem;font-weight:700;'
                    f'white-space:nowrap;margin-left:4px">{rlbl}</span>')
    return (f'<div class="li" data-cl="{cl}" data-acc="{acc}">'
            f'<span class="li-rank" style="background:{clr}">{rank}</span>'
            f'<div class="li-body">'
            f'<span class="li-name">{p[0]}{h}</span>'
            f'<span class="li-muni">📍 {p[1]}{rec_html}</span>'
            f'</div>'
            f'<span class="li-acc" style="background:{bg};color:{tc}">{icon} {acc}</span>'
            f'<span class="li-score">{tot:.2f}</span>'
            f'</div>')

# ── Render: full cluster section ─────────────────────────────────────────────
def cluster_section(cl, places):
    meta = CLUSTER_META[cl]
    clr  = meta['color']
    srt  = sorted(places, key=score, reverse=True)
    top5 = srt[:5]
    rest = srt[5:]
    uid  = cl.lower()
    cards = '\n'.join(place_card_compact(cl, p, i+1) for i,p in enumerate(top5))
    items = '\n'.join(place_list_item(cl, p, i+6) for i,p in enumerate(rest))
    return f'''<section class="cl-section" id="cl-{uid}" data-cl="{cl}">
  <div class="cl-header" style="background:{clr}">
    <div class="cl-title">{meta["icon"]} {cl}</div>
    <div class="cl-desc">{meta["desc"]}</div>
    <div class="cl-badge">{len(places)} lugares</div>
  </div>
  <div class="top5-grid">{cards}</div>
  <button class="expand-btn" onclick="toggleList('{uid}')">
    <span id="btn-{uid}">▼ Ver lugares 6–{len(places)}</span>
  </button>
  <div class="cl-list" id="list-{uid}" style="display:none">
    {items}
  </div>
</section>'''

# ── Render: Recorrida Territorial ────────────────────────────────────────────

def _cl_pills():
    parts = []
    for cl, meta in CLUSTER_META.items():
        clr = meta["color"]
        icon = meta["icon"]
        parts.append(f'<button class="fpill" onclick="filterCl(\'{cl}\',this)" style="--pc:{clr}">{icon} {cl}</button>')
    return ''.join(parts)


def _places_js():
    """Genera const LUGARES=[...] con todos los lugares para el mapa."""
    def esc(s): return str(s).replace('\\','\\\\').replace('"','\\"').replace('\n',' ').replace('\r','')
    items = []
    for cl, p in all_places:
        acc = get_acceso(p)
        _, tc, bg, _ = ACC_STYLE[acc]
        ie, pc2, ut, rs, lv, tot = score_detail(p)
        cat = get_cat(p)
        eje = get_eje(p)
        hook = get_hook(p)
        lat, lng = _get_coords(p[1], p[0])
        clr = CLUSTER_META[cl]['color']
        cat_s = f'{cat[0]} {cat[2]}' if cat else ''   # emoji + reach
        eje_s = f'{eje[0]} {eje[1]}' if eje else ''   # emoji + label
        just = esc((p[7] if len(p)>7 else '')[:160])
        rec_s = get_rec(p[0]) if acc == 'PRIVADO' else ''
        items.append(
            f'{{n:"{esc(p[0])}",m:"{esc(p[1])}",cl:"{cl}",clr:"{clr}",'
            f'acc:"{acc}",bg:"{bg}",tc:"{tc}",'
            f'tot:{tot:.2f},ie:{ie},pc:{pc2},ut:{ut},rs:{rs},lv:{lv},'
            f'lat:{lat},lng:{lng},'
            f'eje:"{esc(eje_s)}",cat:"{esc(cat_s)}",'
            f'hook:"{esc(hook)}",just:"{just}",rec:"{rec_s}"}}'
        )
    return '<script>const LUGARES=[' + ',\n'.join(items) + '];</script>'

def _svg_map():
    """SVG con contorno aproximado de PBA, etiquetas y onClick directo por índice."""
    import html as _html
    W, H = 1100, 620
    LAT_MIN_M, LAT_MAX_M = -41.5, -32.8
    LNG_MIN_M, LNG_MAX_M = -65.0, -56.0

    def proj(lat, lng):
        x = (lng - LNG_MIN_M) / (LNG_MAX_M - LNG_MIN_M) * W
        y = (LAT_MAX_M - lat) / (LAT_MAX_M - LAT_MIN_M) * H
        return round(x, 1), round(y, 1)

    # Contorno APROXIMADO de la provincia de Buenos Aires (sentido horario)
    pba_pts = [
        (-33.9,-59.0),(-33.5,-59.5),(-33.3,-60.0),(-33.3,-60.5),
        (-33.8,-61.3),(-34.3,-62.0),(-34.8,-62.7),(-35.5,-62.5),
        (-36.0,-62.5),(-36.5,-62.8),(-37.0,-63.0),(-37.6,-62.8),
        (-38.2,-63.3),(-38.8,-63.5),(-39.5,-63.5),(-40.2,-63.3),
        (-40.9,-63.0),(-40.8,-62.2),(-40.4,-61.5),(-39.8,-60.8),
        (-39.5,-60.0),(-39.0,-59.5),(-38.7,-62.2),  # back-fill
        # costa atlantica sur->norte
        (-40.8,-62.7),(-40.5,-62.0),(-39.9,-61.5),
        (-39.0,-59.5),(-38.6,-58.5),(-38.0,-57.5),
        (-37.3,-57.1),(-36.5,-56.7),(-36.0,-56.8),
        (-35.0,-57.0),(-34.3,-57.2),(-34.0,-57.5),
        (-34.5,-58.5),(-34.3,-58.9),(-34.0,-58.8),
        (-33.9,-59.0),
    ]
    # Simplificar: usar un polígono más limpio
    pba_outline = [
        # Norte - frontera con Entre Ríos y Santa Fe
        (-33.3,-60.5),(-33.4,-60.0),(-33.5,-59.4),(-33.8,-59.0),
        # NE - Buenos Aires (ciudad) y Río de la Plata
        (-34.0,-58.8),(-34.4,-58.4),(-34.6,-58.4),(-34.9,-57.9),
        # Costa atlántica
        (-35.0,-57.0),(-35.5,-56.9),(-36.3,-56.7),
        (-37.1,-57.0),(-37.5,-57.2),(-38.0,-57.5),
        (-38.5,-58.4),(-38.8,-59.2),(-39.1,-59.8),
        (-39.5,-60.5),(-39.9,-61.2),(-40.3,-61.8),(-40.8,-62.7),
        # Sur - frontera con Rio Negro
        (-40.8,-63.0),(-40.8,-64.0),
        # Oeste - frontera con La Pampa y Córdoba
        (-40.0,-63.5),(-39.0,-63.3),(-38.0,-63.2),
        (-37.0,-62.8),(-36.0,-62.5),(-35.0,-62.0),
        (-34.3,-62.0),(-33.8,-61.3),(-33.5,-61.0),
        (-33.3,-60.5),
    ]
    pts_str = " ".join(f"{proj(la,ln)[0]},{proj(la,ln)[1]}" for la,ln in pba_outline)

    # Referencias geográficas (lat, lng, texto, tamaño)
    LABELS = [
        (-34.9,-57.9,"La Plata",9,True),
        (-38.0,-57.6,"Mar del Plata",9,True),
        (-38.72,-62.27,"Bahía Blanca",9,True),
        (-34.6,-60.9,"Junín",8,False),
        (-33.3,-60.2,"San Nicolás",8,False),
        (-36.7,-60.3,"Olavarría",8,False),
        (-37.3,-59.1,"Tandil",8,False),
        (-38.4,-60.3,"Tres Arroyos",8,False),
        (-40.8,-62.9,"Patagones",8,False),
        (-35.5,-58.0,"Chascomús",8,False),
        (-34.9,-57.2,"Punta Indio",8,False),
    ]

    # Fondo: océano
    ocean = f'<rect width="{W}" height="{H}" fill="#c8ddf0"/>'
    # Tierra (toda la extensión como tierra, el polígono recortará)
    land = f'<rect width="{W}" height="{H}" fill="#e8e0d0"/>'
    # Polígono PBA
    poly = f'<polygon points="{pts_str}" fill="#eef5e4" stroke="#6b8c42" stroke-width="1.5" opacity=".95"/>'
    
    # Grid de grados
    grid = []
    for g in range(-65, -55):
        x, _ = proj(LAT_MIN_M, g)
        grid.append(f'<line x1="{x:.0f}" y1="0" x2="{x:.0f}" y2="{H}" stroke="rgba(100,130,180,.2)" stroke-width=".5"/>')
    for g in range(-42, -32):
        _, y = proj(g, LNG_MIN_M)
        grid.append(f'<line x1="0" y1="{y:.0f}" x2="{W}" y2="{y:.0f}" stroke="rgba(100,130,180,.2)" stroke-width=".5"/>')

    # Etiquetas geográficas
    label_els = []
    for la, ln, txt, sz, bold in LABELS:
        x, y = proj(la, ln)
        fw = "bold" if bold else "normal"
        col = "#2c3e50" if bold else "#4a5568"
        label_els.append(
            f'<text x="{x}" y="{y}" font-size="{sz}" font-family="system-ui,sans-serif" '
            f'font-weight="{fw}" fill="{col}" text-anchor="middle" '
            f'style="pointer-events:none;text-shadow:0 0 3px white">{_html.escape(txt)}</text>'
        )

    # Círculos con onclick directo por índice
    circles = []
    for idx, (cl, p) in enumerate(all_places):
        lat, lng = _get_coords(p[1], p[0])
        x, y = proj(lat, lng)
        clr = CLUSTER_META[cl]["color"]
        nm = _html.escape(p[0], quote=True)
        circles.append(
            f'<circle cx="{x}" cy="{y}" r="5" fill="{clr}" stroke="white" stroke-width="1.5" '
            f'opacity=".85" onclick="mpc(event,{idx})" style="cursor:pointer">'
            f'<title>{nm} — {_html.escape(p[1])}</title></circle>'
        )

    # Leyenda
    leg_items = []
    for i, (cl, meta) in enumerate(CLUSTER_META.items()):
        ly = 24 + i * 19
        leg_items.append(f'<circle cx="20" cy="{ly}" r="6" fill="{meta["color"]}"/>')
        leg_items.append(
            f'<text x="31" y="{ly+5}" font-size="11" font-family="system-ui,sans-serif" '
            f'font-weight="bold" fill="#0f2944">{cl}</text>'
        )
    n_cl = len(CLUSTER_META)
    leg_h = n_cl * 19 + 18
    leg_bg = (f'<rect x="7" y="7" width="120" height="{leg_h}" rx="6" '
              f'fill="rgba(255,255,255,.93)" stroke="#cbd5e1" stroke-width="1"/>'
              f'<text x="15" y="20" font-size="9.5" font-family="system-ui,sans-serif" '
              f'font-weight="bold" fill="#64748b">CLUSTERS</text>')

    hint = (f'<rect x="0" y="{H-22}" width="{W}" height="22" fill="rgba(255,255,255,.6)"/>'
            f'<text x="{W//2}" y="{H-7}" font-size="9.5" font-family="system-ui,sans-serif" '
            f'fill="rgba(0,0,0,.5)" text-anchor="middle">'
            f'Click en cualquier punto para ver información detallada</text>')

    return (
        f'<svg id="pba-map-svg" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" '
        f'style="width:100%;height:auto;display:block;border-radius:8px;'
        f'box-shadow:inset 0 0 0 1px #c8d5e8" onclick="svgBgClick(event)">'
        + ocean + land + poly
        + ''.join(grid)
        + ''.join(label_els)
        + ''.join(circles)
        + leg_bg + ''.join(leg_items)
        + hint
        + '</svg>'
    )

def _ordered_places():
    """Ordena la tabla: score DESC, con cada alternativa privada
    insertada justo debajo del lugar más relevante de su municipio."""
    regular = [(cl, p) for cl, p in all_places if '🔄' not in p[0]]
    alts    = [(cl, p) for cl, p in all_places if '🔄' in p[0]]
    regular_sorted = sorted(regular, key=lambda x: score(x[1]), reverse=True)

    # Para cada municipio, índice del PRIMER (mayor score) lugar regular
    muni_first_idx = {}
    for i, (cl, p) in enumerate(regular_sorted):
        if p[1] not in muni_first_idx:
            muni_first_idx[p[1]] = i

    result = list(regular_sorted)
    offset = 0  # corrección por inserciones previas
    # Procesar alts en orden de score DESC
    for cl_alt, p_alt in sorted(alts, key=lambda x: score(x[1]), reverse=True):
        muni = p_alt[1]
        base_idx = muni_first_idx.get(muni, len(result) - 1)
        # Insertar justo después del primer lugar regular de ese municipio
        # + las alts ya insertadas para ese municipio (agrupar)
        insert_at = base_idx + offset + 1
        # Avanzar si ya hay otras alternativas del mismo municipio en esa posición
        while insert_at < len(result) and '🔄' in result[insert_at][1][0]:
            insert_at += 1
        result.insert(insert_at, (cl_alt, p_alt))
        offset += 1
    return result

def _build_table_data():
    """Genera HTML de la tabla completa de lugares"""
    all_sorted = _ordered_places()
    rows = []
    for i, (cl, p) in enumerate(all_sorted, 1):
        acc = get_acceso(p)
        icon, tc, bg, _ = ACC_STYLE[acc]
        ie, pc2, ut, rs, lv, tot = score_detail(p)
        clr = CLUSTER_META[cl]['color']
        hallazgo = get_hallazgo(p)
        h_mark = ' 🔍' if hallazgo else ''
        is_alt = '🔄' in p[0]
        row_style = ' style="background:#eafaf1;border-left:4px solid #2d6a4f"' if is_alt else ''
        hook = get_hook(p)
        hook_cell = f'<td class="td-hook">{hook}</td>' if hook else '<td class="td-hook td-hook-empty">—</td>'
        cat = get_cat(p)
        if cat:
            cemoji, clabel, creach, ccolor, cinfo = cat
            cat_cell = (
                f'<td class="td-cat">'
                f'<span class="cat-chip" style="background:{ccolor}18;border-color:{ccolor}55;color:{ccolor}" '
                f'data-info="{cinfo}" '
                f'title="{clabel} — {creach} (Meta PBA). Click para ver audiencias.">'
                f'{cemoji} {creach}'
                f'</span>'
                f'</td>'
            )
            cat_attr = f' data-cat="{clabel}"'
        else:
            cat_cell = '<td class="td-cat td-cat-empty">—</td>'
            cat_attr = ' data-cat=""'
        rows.append(
            f'<tr data-cl="{cl}" data-acc="{acc}" data-score="{tot}" '
            f'data-ie="{ie}" data-pc="{pc2}" data-ut="{ut}" data-rs="{rs}" data-lv="{lv}"'
            f'{cat_attr}{row_style}>'
            f'<td class="td-rn">{i}</td>'
            f'<td class="td-name">{p[0]}{h_mark}</td>'
            f'<td class="td-muni">{p[1]}</td>'
            f'<td><span class="cl-dot2" style="background:{clr}"></span>{cl}</td>'
            f'<td class="td-num td-score-val" data-sc="IE:{ie}|PC:{pc2}|UT:{ut}|RS:{rs}|LV:{lv}" title="Click para ver composición">{tot:.2f}</td>'
            f'<td class="td-num td-sc">{ie}</td>'
            f'<td class="td-num td-sc">{pc2}</td>'
            f'<td class="td-num td-sc">{ut}</td>'
            f'<td class="td-num td-sc">{rs}</td>'
            f'<td class="td-num td-sc">{lv}</td>'
            f'<td><span class="acc-chip" style="background:{bg};color:{tc}">{icon} {acc}</span></td>'
            f'{hook_cell}'
            f'{cat_cell}'
            f'</tr>'
        )
    return '\n'.join(rows)

def render_recorrida():
    top3_global = sorted(all_places, key=lambda x: score(x[1]), reverse=True)[:3]
    top3_li = ''.join(
        f'<div class="top3-item"><span class="t3r">#{i+1}</span>'
        f'<div><div class="t3n">{p[0]}</div>'
        f'<div class="t3m">📍 {p[1]} · {cl} · <strong>{score(p):.2f}</strong></div></div></div>'
        for i,(cl,p) in enumerate(top3_global)
    )
    clusters_html = '\n'.join(cluster_section(cl, data) for cl,data in CLUSTERS.items())
    return f'''
<div class="rec-hero">
  <div class="rh-left">
    <div class="rh-tag">RECORRIDA TERRITORIAL</div>
    <h2>{len(all_places)} Lugares Estratégicos · 7 Clusters · PBA 2026</h2>
    <p>Priorizados por Impacto Electoral (calculado desde datos reales), Potencial Comunicacional, Unicidad, Representatividad y Logística. Las filas <span style="color:#2d6a4f;font-weight:700">verdes</span> son alternativas privadas a visitas que requieren protocolo.</p>
  </div>
  <div class="rh-right">
    <div class="rh-stat"><span class="rs-n">{total_priv}</span><span class="rs-l">🏭 Privado</span></div>
    <div class="rh-stat"><span class="rs-n">{total_nac}</span><span class="rs-l">🏛️ Nacional</span></div>
    <div class="rh-stat"><span class="rs-n">{total_prot}</span><span class="rs-l">🤝 Protocolar</span></div>
    <div class="rh-stat"><span class="rs-n">{len(all_places)}</span><span class="rs-l">Total lugares</span></div>
  </div>
</div>

<div class="top3-strip">
  <div class="t3-label">⭐ Top 3 Global</div>
  {top3_li}
</div>

<div class="filter-bar">
  <span class="fb-label">Filtrar:</span>
  <div class="filter-pills" id="fpills">
    <button class="fpill active" onclick="filterCl('',this)">Todos</button>
    {_cl_pills()}
  </div>
  <select id="facc" onchange="filterAcc(this.value)">
    <option value="">Todos los accesos</option>
    <option value="PRIVADO">🏭 Privado</option>
    <option value="NACIONAL">🏛️ Nacional</option>
    <option value="PROTOCOLAR">🤝 Protocolar</option>
    <option value="ALTPRIV">🔄 Solo Alt. Privadas</option>
  </select>
  <button class="map-toggle-btn" id="map-toggle-btn" onclick="toggleMap()">🗺️ Ver mapa</button>
</div>

<div id="map-wrap" style="display:none;margin:0 16px 16px;border-radius:12px;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,.15)">
  <div id="main-map" style="height:520px;width:100%"></div>
</div>

<div id="clusters-wrap">
  {clusters_html}
</div>

<div class="full-table-section">
  <div class="fts-header">
    <div class="fts-title">📋 Los 350 lugares — tabla completa</div>
    <div class="fts-sub">Hacé clic en los encabezados de columna para ordenar · Los filtros de arriba aplican también a esta tabla</div>
    <input class="fts-search" id="tbl-search" placeholder="🔍 Buscar lugar o municipio..." oninput="tblSearch()">
  </div>
  <div class="tbl-scroll">
    <table id="main-tbl" class="main-tbl">
      <thead>
        <tr>
          <th class="th-rn" onclick="sortTbl(0)">#<span class="sort-icon">⇅</span></th>
          <th onclick="sortTbl(1)">Lugar<span class="sort-icon">⇅</span></th>
          <th onclick="sortTbl(2)">Municipio<span class="sort-icon">⇅</span></th>
          <th onclick="sortTbl(3)">Cluster<span class="sort-icon">⇅</span></th>
          <th onclick="sortTbl(4)" class="th-num" title="Click en cualquier score para ver la composición detallada">Score 📊<span class="sort-icon">⇅</span></th>
          <th onclick="sortTbl(5)" class="th-num th-sc">IE<span class="sort-icon">⇅</span></th>
          <th onclick="sortTbl(6)" class="th-num th-sc">PC<span class="sort-icon">⇅</span></th>
          <th onclick="sortTbl(7)" class="th-num th-sc">UT<span class="sort-icon">⇅</span></th>
          <th onclick="sortTbl(8)" class="th-num th-sc">RS<span class="sort-icon">⇅</span></th>
          <th onclick="sortTbl(9)" class="th-num th-sc">LV<span class="sort-icon">⇅</span></th>
          <th onclick="sortTbl(10)">Acceso<span class="sort-icon">⇅</span></th>
          <th class="th-hook">¿Por qué aquí?</th>
          <th class="th-cat" onclick="sortTbl(12)" title="Categoría comunicacional y alcance estimado en Meta PBA">📡 Alcance<span class="sort-icon">⇅</span></th>
        </tr>
        <tr class="filter-row">
          <td></td>
          <td><input class="col-filter" placeholder="Buscar..." oninput="colFilter()" data-col="1"></td>
          <td><input class="col-filter" placeholder="Buscar..." oninput="colFilter()" data-col="2"></td>
          <td>
            <select class="col-filter" onchange="colFilter()" data-col="3">
              <option value="">Todos</option>
              <option>CIUDADES</option><option>CONURBANO</option><option>CORREDOR</option>
              <option>COSTERO</option><option>INTERIOR</option><option>SALADO</option><option>SUR</option>
            </select>
          </td>
          <td></td><td class="td-sc"></td><td class="td-sc"></td><td class="td-sc"></td><td class="td-sc"></td><td class="td-sc"></td>
          <td>
            <select class="col-filter" onchange="colFilter()" data-col="10">
              <option value="">Todos</option>
              <option>PRIVADO</option><option>NACIONAL</option><option>PROTOCOLAR</option>
            </select>
          </td>
          <td><input class="col-filter" placeholder="Buscar hook..." oninput="colFilter()" data-col="11"></td>
          <td>
            <select class="col-filter" onchange="catFilter()" id="catFilterSel">
              <option value="">Todas</option>
              <option value="Energía / Soberanía">⚡ Energía</option>
              <option value="Ciencia / Tecnología">🔬 Ciencia</option>
              <option value="Cooperativas / Eco. Social">🤝 Cooperativas</option>
              <option value="Pesca / Puertos">🎣 Pesca</option>
              <option value="Cadena Cárnica">🥩 Cárnica</option>
              <option value="Agroindustria / Campo">🌾 Campo</option>
              <option value="Industria / Manufactura">⚙️ Industria</option>
              <option value="Patrimonio / Identidad">🏛️ Patrimonio</option>
            </select>
          </td>
        </tr>
      </thead>
      <tbody id="tbl-body">{_build_table_data()}</tbody>
    </table>
  </div>
  <div class="tbl-count" id="tbl-count">350 lugares</div>
</div>'''

# ── Metodología & Estrategia (= overlay + perfil + metodología) ──────────────

def _cl_crits():
    parts = []
    for cl, m in CLUSTER_META.items():
        clr = m["color"]; icon = m["icon"]; desc = m["desc"]
        parts.append(f'<div class="crit" style="border-color:{clr}"><h5>{icon} {cl}</h5><p>{desc}</p></div>')
    return ''.join(parts)

def render_metod():
    # Extraer body del overlay
    ov_html = embed_doc(BASE_HTML + 'Overlay_Estrategico_Perfil_Candidato.html')
    return f'''
<div class="met-hero">
  <h2>🔬 Metodología & Estrategia</h2>
  <p>Modelo de scoring, perfil del candidato y análisis estratégico de recorrida territorial.</p>
</div>

<div class="met-tabs">
  <button class="mt active" onclick="showMet('scoring',this)">📐 Scoring</button>
  <button class="mt" onclick="showMet('perfil',this)">🎯 Perfil &amp; Ejes</button>
  <button class="mt" onclick="showMet('overlay',this)">📊 Análisis Overlay</button>
</div>

<div id="met-scoring" class="met-panel active">
<div class="metod-wrap">
  <div class="ms">
    <h3>Fórmula de scoring</h3>
    <div class="formula">Score = IE×0.25 + PC×0.25 + UT×0.20 + RS×0.15 + LV×0.15</div>
    <div class="crit-grid">
      <div class="crit" style="border-color:#1d4ed8">
        <h5>IE — Impacto Electoral (25%)</h5>
        <p><strong>Calculado desde datos reales.</strong><br>
        IE = 0.50 × Padrón_norm + 0.30 × Competitividad_2023 + 0.20 × Tendencia_2025<br>
        Fuente: ResultadosPBA_2023_2025.xlsx · 134 municipios cubiertos</p>
      </div>
      <div class="crit" style="border-color:#7c3aed">
        <h5>PC — Potencial Comunicacional (25%)</h5>
        <p>Impacto mediático y social. Hallazgos únicos, narrativa visual, viralidad. Evaluación experta.</p>
      </div>
      <div class="crit" style="border-color:#b45309">
        <h5>UT — Unicidad Territorial (20%)</h5>
        <p>¿Es único en PBA o en Argentina? Alta UT = no hay otro igual.</p>
      </div>
      <div class="crit" style="border-color:#dc2626">
        <h5>RS — Representatividad Sectorial (15%)</h5>
        <p>Amplitud del auditorio: productores, trabajadores, jóvenes, comunidades.</p>
      </div>
      <div class="crit" style="border-color:#059669">
        <h5>LV — Logística de Visita (15%)</h5>
        <p>Distancia, accesibilidad, nivel de coordinación requerida.</p>
      </div>
    </div>
  </div>
  <div class="ms">
    <h3>🔒 Niveles de acceso político</h3>
    <div class="acc-explainer">
      <div class="ae-item" style="border-color:#1b4332;background:#d8f3dc">
        <div class="ae-icon">🏭</div>
        <div><strong>PRIVADO</strong><br><span>Empresa, cooperativa, fundación. Coordinación directa sin intermediación política. El intendente local no tiene rol.</span></div>
      </div>
      <div class="ae-item" style="border-color:#1d3461;background:#dde3f5">
        <div class="ae-icon">🏛️</div>
        <div><strong>NACIONAL</strong><br><span>INTA, CONICET, Armada, universidades nacionales. Coordinar con autoridad nacional; municipio queda al margen.</span></div>
      </div>
      <div class="ae-item" style="border-color:#5c3317;background:#fef3c7">
        <div class="ae-icon">🤝</div>
        <div><strong>PROTOCOLAR</strong><br><span>Como intendente en ejercicio visitando otro municipio, se notifica al intendente local. Evaluar alineación política antes de confirmar.</span></div>
      </div>
    </div>
  </div>
  <div class="ms">
    <h3>🗂️ Los 7 Clusters territoriales</h3>
    <div class="crit-grid">
      {_cl_crits()}
    </div>
  </div>
</div>
</div>

<div id="met-perfil" class="met-panel" style="display:none">
<div class="metod-wrap">
  <div class="ms">
    <h3>🎯 Perfil del candidato — Premisas estratégicas</h3>
    <div class="perfil-grid">
      <div class="pf-card" style="border-color:#1d4ed8">
        <div class="pf-icon">🏛️</div>
        <h4>Identidad política</h4>
        <p>Peronismo propio. Distancia explícita del kirchnerismo y del MDF. Espacio político autónomo con raíz peronista sin las cargas del período 2019-2023.</p>
      </div>
      <div class="pf-card" style="border-color:#1d6b3e">
        <div class="pf-icon">🏭</div>
        <h4>Gestión municipal</h4>
        <p>Imagen positiva entre quienes lo conocen. Empatía ciudadana probada. Gestión reconocida como eficiente y cercana.</p>
      </div>
      <div class="pf-card" style="border-color:#7c3aed">
        <div class="pf-icon">🇦🇷</div>
        <h4>Eje soberanía y patriotismo</h4>
        <p>Causa Malvinas. Fuerzas armadas. Energía nacional (Atucha, YPF). Producción estratégica. Industria argentina. Este eje eleva el IE de lugares como la Base Naval y la Destilería YPF.</p>
      </div>
      <div class="pf-card" style="border-color:#b45309">
        <div class="pf-icon">⚙️</div>
        <h4>Eje producción y desarrollo</h4>
        <p>Industria, campo, PyME, empleo, educación, ciencia. Los hallazgos (Toyota, TenarisSiderca, Loma Negra) son el núcleo de este eje.</p>
      </div>
      <div class="pf-card" style="border-color:#0077b6">
        <div class="pf-icon">✝️🕌</div>
        <h4>Posición religiosa</h4>
        <p>Laico. Respetuoso de todos los credos. Apertura explícita a la comunidad evangélica (importante en CONURBANO y INTERIOR). Basílica de Luján: posible visita, sin performance religiosa.</p>
      </div>
      <div class="pf-card" style="border-color:#8b3a3a">
        <div class="pf-icon">⚠️</div>
        <h4>Zonas de cuidado</h4>
        <p>Sin referencias a Pilar (municipio de gestión). Evitar lugares con asociación directa a gestión K anterior. Astilleros Río Santiago: visitar la planta, no la dirigencia sindical. UNLP: laboratorios/incubadoras, no espacios políticos.</p>
      </div>
    </div>
  </div>
  <div class="ms">
    <h3>🗺️ Mapa de ajustes por perfil</h3>
    <div class="adj-table">
      <div class="adj-row header"><span>Lugar</span><span>Ajuste</span><span>Razón</span></div>
      <div class="adj-row"><span>Casa Museo Eva Perón</span><span class="up">IE → 10 (override)</span><span>Máxima sintonía simbólica con el peronismo no K</span></div>
      <div class="adj-row"><span>Base Naval Puerto Belgrano</span><span class="up">PC, UT → 10</span><span>Eje soberanía: la mayor base naval de América del Sur</span></div>
      <div class="adj-row"><span>TenarisSiderca</span><span class="up">PC, UT → 10</span><span>Industria estratégica, único en Argentina</span></div>
      <div class="adj-row"><span>Loma Negra</span><span class="up">PC, UT, RS → 9</span><span>40% del cemento argentino — eje producción</span></div>
      <div class="adj-row"><span>La Serenísima</span><span class="up">PC, UT, RS → 9</span><span>Icono de la industria alimentaria argentina</span></div>
      <div class="adj-row"><span>Atucha I y II</span><span class="up">PC, UT → 10</span><span>Energía soberana — relato patriótico potente</span></div>
      <div class="adj-row"><span>Basílica de Luján</span><span class="down">PC → 7 (baja)</span><span>Candidato laico: no debe performar religiosidad</span></div>
    </div>
  </div>
</div>
</div>

<div id="met-overlay" class="met-panel" style="display:none">
  {ov_html}
</div>'''

# ── Fichas ───────────────────────────────────────────────────────────────────
FICHAS = [
    {'nombre':'San Nicolás',    'cluster':'CIUDADES', 'tags':['CIUDADES · Cabecera de Sección','Puerto · Eje Paraná','Industria Pesada'],
     'est':'Ficha_Campana_SAN_NICOLAS.html', 'nar':'Ficha_Campana_SAN_NICOLAS_narrativa.html'},
    {'nombre':'Lobos',          'cluster':'SALADO',   'tags':['SALADO · Cuenca del Salado','Ganadería extensiva','Historia peronista'],
     'est':'Ficha_Campana_LOBOS.html',       'nar':'Lobos_Narrativa.html'},
    {'nombre':'Tapalqué',       'cluster':'INTERIOR', 'tags':['INTERIOR · Pampa húmeda','Municipio rural profundo','Identidad agropecuaria'],
     'est':'Ficha_Campana_TAPALQUE.html',    'nar':'Tapalque_Narrativa.html'},
    {'nombre':'Coronel Suárez', 'cluster':'SUR',      'tags':['SUR · Sierra bonaerense','Agroindustria regional','Comunidades inmigrantes'],
     'est':'Ficha_Campana_CORONEL_SUAREZ.html','nar':'CoronelSuarez_Narrativa.html'},
    {'nombre':'Guaminí',        'cluster':'SUR',      'tags':['SUR · Sierra bonaerense','Lagunas y naturaleza','Turismo productivo'],
     'est':'Ficha_Campana_GUAMINI.html',     'nar':'Guamini_Narrativa.html'},
]

def render_fichas():
    out = []
    for f in FICHAS:
        clr  = CLUSTER_META[f['cluster']]['color']
        icon = CLUSTER_META[f['cluster']]['icon']
        tags = ''.join(
            f'<span class="ftag ftag-cl">{t}</span>' if i == 0 else f'<span class="ftag">{t}</span>'
            for i, t in enumerate(f['tags'])
        )
        out.append(f'''<div class="fc">
  <div class="fc-top" style="background:{clr}">
    <div class="fc-cl">{icon} {f["cluster"]}</div>
    <div class="fc-nm">{f["nombre"]}</div>
    <div class="fc-tgs">{tags}</div>
  </div>
  <div class="fc-btns">
    <a href="{f["est"]}" target="_blank" class="fc-btn">
      <span>📋</span><span class="fc-btn-lbl">Ficha estructurada</span>
    </a>
    <a href="{f["nar"]}" target="_blank" class="fc-btn">
      <span>📝</span><span class="fc-btn-lbl">Ficha narrativa</span>
    </a>
  </div>
</div>''')
    return '\n'.join(out)

# ── CSS ──────────────────────────────────────────────────────────────────────
CSS = '''
:root{--dark:#0f2944;--acc:#FACC15;--bg:#eef1f5;--radius:10px}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:"Segoe UI",system-ui,Arial,sans-serif;background:var(--bg);color:#1e293b;font-size:14px;line-height:1.5}

/* ── NAV ── */
.mnav{background:var(--dark);position:sticky;top:0;z-index:300;box-shadow:0 3px 12px rgba(0,0,0,.4)}
.ntop{display:flex;align-items:center;justify-content:space-between;padding:11px 28px;border-bottom:1px solid rgba(255,255,255,.08)}
.ntop h1{font-size:.95rem;font-weight:800;color:#fff;letter-spacing:.2px}
.ntop .vtag{background:var(--acc);color:var(--dark);font-size:.65rem;font-weight:800;padding:2px 9px;border-radius:20px}
.ntabs{display:flex;padding:0 20px;gap:0}
.ntab{padding:11px 20px;cursor:pointer;font-size:.82rem;font-weight:600;color:rgba(255,255,255,.5);background:none;border:none;border-bottom:3px solid transparent;white-space:nowrap;transition:.15s}
.ntab:hover{color:rgba(255,255,255,.85)}.ntab.active{color:var(--acc);border-bottom-color:var(--acc)}
.tsec{display:none}.tsec.active{display:block}

/* ── RECORRIDA TERRITORIAL ── */
.rec-hero{background:linear-gradient(130deg,#0f2944 0%,#1a3a5c 50%,#1d6b3e 100%);color:#fff;padding:2.2rem 2.5rem;display:flex;gap:2rem;flex-wrap:wrap;align-items:center}
.rh-left{flex:1;min-width:260px}
.rh-tag{font-size:.68rem;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;color:var(--acc);margin-bottom:.5rem}
.rh-left h2{font-size:1.5rem;font-weight:800;margin-bottom:.4rem}
.rh-left p{font-size:.85rem;opacity:.8;max-width:560px}
.rh-right{display:flex;gap:1rem;flex-wrap:wrap}
.rh-stat{background:rgba(255,255,255,.12);border-radius:8px;padding:12px 18px;text-align:center;min-width:80px}
.rs-n{display:block;font-size:1.6rem;font-weight:800;color:var(--acc)}
.rs-l{display:block;font-size:.68rem;color:rgba(255,255,255,.75);margin-top:2px}
.top3-strip{background:#fff;border-bottom:1px solid #e2e8f0;padding:12px 28px;display:flex;align-items:center;gap:16px;flex-wrap:wrap}
.t3-label{font-size:.72rem;font-weight:800;text-transform:uppercase;color:#94a3b8;min-width:80px}
.top3-item{display:flex;align-items:center;gap:8px}
.t3r{background:var(--dark);color:var(--acc);font-weight:800;font-size:.75rem;padding:2px 7px;border-radius:5px}
.t3n{font-size:.82rem;font-weight:700;color:var(--dark)}
.t3m{font-size:.72rem;color:#64748b}
.filter-bar{background:#fff;padding:12px 28px;display:flex;align-items:center;gap:12px;flex-wrap:wrap;border-bottom:1px solid #e2e8f0;position:sticky;top:60px;z-index:200}
.fb-label{font-size:.75rem;font-weight:700;color:#94a3b8;text-transform:uppercase}
.filter-pills{display:flex;gap:6px;flex-wrap:wrap}
.fpill{padding:5px 12px;border:1.5px solid #e2e8f0;border-radius:20px;background:#fff;font-size:.76rem;font-weight:600;cursor:pointer;color:#475569;transition:.15s}
.fpill:hover{border-color:var(--pc,#1a3a5c);color:var(--pc,#1a3a5c)}
.fpill.active{background:var(--pc,var(--dark));border-color:var(--pc,var(--dark));color:#fff}
.filter-bar select{padding:5px 9px;border:1.5px solid #e2e8f0;border-radius:8px;font-size:.77rem;color:#475569}
.pba-lf-popup .leaflet-popup-content-wrapper{border-radius:10px;box-shadow:0 4px 20px rgba(0,0,0,.18);padding:0}
.pba-lf-popup .leaflet-popup-content{margin:12px 14px;font-family:system-ui,sans-serif}
.map-toggle-btn{margin-left:auto;padding:6px 14px;background:#0f2944;color:#fff;border:none;border-radius:8px;font-size:.77rem;font-weight:700;cursor:pointer;transition:.15s}
.map-toggle-btn:hover,.map-toggle-btn.active{background:#1d4e89}

/* ── CLUSTER SECTION ── */
.cl-section{margin:24px 28px;border-radius:var(--radius);overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,.08)}
.cl-section.hidden{display:none}
.cl-header{display:flex;align-items:center;gap:12px;padding:14px 20px;color:#fff}
.cl-title{font-size:1.05rem;font-weight:800}
.cl-desc{font-size:.78rem;opacity:.8;flex:1}
.cl-badge{background:rgba(255,255,255,.2);border-radius:20px;padding:3px 10px;font-size:.72rem;font-weight:700}

/* ── PLACE CARDS (top 5) ── */
.pc-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:0;background:#f8fafc}
.pc{background:#fff;margin:12px;border-radius:8px;padding:14px;border-top:3px solid var(--cl);box-shadow:0 1px 4px rgba(0,0,0,.06);position:relative}
.pc-rank{position:absolute;top:12px;right:12px;background:var(--cl);color:#fff;width:26px;height:26px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:800}
.pc-acc{font-size:.68rem;font-weight:700;padding:3px 8px;border-radius:4px;display:inline-flex;align-items:center;gap:4px;margin-bottom:6px}
.acc-sub{font-weight:400;opacity:.8}
.pc-name{font-size:.9rem;font-weight:800;color:#0f2944;margin-bottom:3px;line-height:1.3;padding-right:28px}
.pc-muni{font-size:.72rem;color:#64748b;margin-bottom:6px}
.h-badge{background:#fef9c3;border:1px solid #eab308;border-radius:4px;padding:2px 7px;font-size:.67rem;font-weight:700;color:#713f12;display:inline-block;margin-bottom:6px}
.pc-scores{display:flex;align-items:center;gap:10px;background:#f8fafc;border-radius:6px;padding:7px 10px;margin:6px 0}
.pc-total{font-size:1.6rem;font-weight:900;color:var(--cl);min-width:50px;cursor:pointer;border-bottom:2px dotted var(--cl)}
.pc-total:hover{opacity:.75}
.pc-cat-chip{display:inline-block;border-radius:20px;padding:3px 10px;font-size:.72rem;font-weight:800;cursor:pointer;white-space:nowrap}
/* ── TOP-5 COMPACT CARDS ─────────────────────────── */
.top5-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;padding:14px 16px 4px}
.pc5{background:#fff;border-radius:8px;border:1.5px solid #e2e8f0;border-top:3px solid var(--cl);padding:10px 12px;display:flex;flex-direction:column;gap:6px;min-width:0}
.p5-top{display:flex;align-items:center;gap:6px;flex-wrap:wrap}
.p5-rank{font-size:.7rem;font-weight:900;color:#fff;border-radius:50%;width:20px;height:20px;display:inline-flex;align-items:center;justify-content:center;flex-shrink:0}
.p5-acc{font-size:.6rem;font-weight:700;padding:2px 6px;border-radius:4px;white-space:nowrap}
.p5-name{font-size:.78rem;font-weight:700;color:#0f2944;line-height:1.3;overflow:hidden;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical}
.p5-muni{font-size:.68rem;color:#64748b}
.p5-bottom{display:flex;flex-wrap:wrap;align-items:center;gap:5px;margin-top:auto;padding-top:4px;border-top:1px solid #f1f5f9}
.p5-score{font-size:1.1rem;font-weight:900;color:var(--cl);cursor:pointer;border-bottom:1.5px dotted var(--cl);line-height:1}
.p5-score:hover{opacity:.7}
.p5-eje{font-size:.6rem;font-weight:700;border:1px solid;border-radius:20px;padding:2px 7px;white-space:nowrap}
.p5-cat{font-size:.6rem !important;padding:2px 7px !important}
.dim b{display:block;font-size:.58rem;color:#94a3b8;font-weight:700;margin-bottom:1px}
.dim small{font-size:.5rem;color:#16a34a;font-weight:700}
.pc-just{font-size:.76rem;color:#475569;line-height:1.45;margin-top:4px}

/* ── EXPAND BUTTON ── */
.expand-btn{width:100%;padding:10px;background:#f8fafc;border:none;border-top:1px solid #e2e8f0;cursor:pointer;font-size:.8rem;font-weight:600;color:#64748b;transition:.15s}
.expand-btn:hover{background:#f1f5f9;color:#1a3a5c}

/* ── LIST ITEMS (6-50) ── */
.cl-list{background:#fff;border-top:1px solid #f1f5f9}
.li{display:flex;align-items:center;gap:10px;padding:9px 20px;border-bottom:1px solid #f8fafc;transition:.1s}
.li:hover{background:#f8fafc}
.li.hidden-li{display:none}
.li-rank{background:var(--cl,#1a3a5c);color:#fff;font-size:.68rem;font-weight:800;width:22px;height:22px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.li-body{flex:1;min-width:0}
.li-name{font-size:.82rem;font-weight:600;color:#1e293b;display:block;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.li-muni{font-size:.7rem;color:#94a3b8}
.li-h{color:#eab308}
.li-acc{font-size:.66rem;font-weight:700;padding:2px 7px;border-radius:4px;flex-shrink:0}
.li-score{font-size:.85rem;font-weight:800;color:var(--dark);min-width:36px;text-align:right}

/* ── METODOLOGÍA ── */
.met-hero{background:linear-gradient(130deg,#0f2944,#1a3a5c);color:#fff;padding:1.6rem 2rem}
.met-hero h2{font-size:1.3rem;font-weight:800;margin-bottom:.3rem}
.met-hero p{font-size:.83rem;opacity:.75}
.met-tabs{display:flex;background:#fff;border-bottom:2px solid #e2e8f0;padding:0 24px;gap:0}
.mt{padding:11px 20px;border:none;background:none;cursor:pointer;font-size:.83rem;font-weight:600;color:#64748b;border-bottom:2px solid transparent;margin-bottom:-2px;transition:.15s}
.mt:hover{color:var(--dark)}.mt.active{color:var(--dark);border-bottom-color:var(--dark)}
.met-panel{padding:0}.met-panel.active{display:block}
.metod-wrap{max-width:900px;margin:0 auto;padding:24px}
.ms{background:#fff;border-radius:var(--radius);padding:20px;margin-bottom:14px;box-shadow:0 2px 6px rgba(0,0,0,.06)}
.ms h3{font-size:.95rem;font-weight:800;color:var(--dark);border-bottom:2px solid var(--acc);padding-bottom:6px;margin-bottom:12px}
.ms p,.ms li{font-size:.83rem;color:#374151;line-height:1.55}
.ms ul{margin-left:1.1rem;margin-top:5px}
.formula{background:#f0f2f5;border-radius:6px;padding:12px 16px;font-family:monospace;font-size:.88rem;margin:8px 0;border-left:3px solid var(--dark)}
.crit-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:10px;margin-top:10px}
.crit{background:#f8fafc;border-radius:7px;padding:12px;border-left:3px solid}
.crit h5{font-size:.82rem;font-weight:700;margin-bottom:4px}.crit p{font-size:.76rem;color:#475569}
.acc-explainer{display:flex;flex-direction:column;gap:10px;margin-top:8px}
.ae-item{display:flex;gap:14px;align-items:flex-start;padding:12px 14px;border-radius:7px;border-left:4px solid}
.ae-icon{font-size:1.4rem;flex-shrink:0}
.ae-item strong{display:block;font-size:.85rem;margin-bottom:2px}
.ae-item span{font-size:.78rem;color:#374151}
/* Perfil */
.perfil-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:12px;margin-top:12px}
.pf-card{background:#f8fafc;border-radius:8px;padding:14px;border-left:4px solid}
.pf-icon{font-size:1.4rem;margin-bottom:6px}
.pf-card h4{font-size:.85rem;font-weight:700;color:var(--dark);margin-bottom:4px}
.pf-card p{font-size:.78rem;color:#475569;line-height:1.5}
.adj-table{margin-top:12px;border-radius:7px;overflow:hidden;border:1px solid #e2e8f0}
.adj-row{display:grid;grid-template-columns:2fr 1.2fr 2fr;gap:0;padding:9px 14px;border-bottom:1px solid #f1f5f9;font-size:.78rem}
.adj-row.header{background:var(--dark);color:#fff;font-weight:700;font-size:.72rem}
.adj-row:last-child{border-bottom:none}
.adj-row:nth-child(even){background:#f8fafc}
.up{color:#15803d;font-weight:700}.down{color:#dc2626;font-weight:700}

/* ── FICHAS ── */
.fichas-sec{padding:24px 28px}
.fichas-sec h2{font-size:1.1rem;font-weight:800;color:var(--dark);margin-bottom:4px}
.fichas-sec p{font-size:.82rem;color:#64748b;margin-bottom:20px}
.fichas-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:16px}
.fc{background:#fff;border-radius:var(--radius);box-shadow:0 2px 8px rgba(0,0,0,.08);overflow:hidden}
.fc-top{padding:16px 18px 14px;color:#fff}
.fc-cl{font-size:.68rem;font-weight:700;text-transform:uppercase;letter-spacing:.8px;opacity:.8;margin-bottom:4px}
.fc-nm{font-size:1.1rem;font-weight:800;margin-bottom:8px}
.fc-tgs{display:flex;flex-wrap:wrap;gap:5px}
.ftag{background:rgba(255,255,255,.2);color:#fff;font-size:.67rem;padding:2px 7px;border-radius:10px;font-weight:600}
.ftag-cl{background:rgba(255,255,255,.92);color:#1a1a2e;font-size:.7rem;padding:3px 9px;font-weight:800;letter-spacing:.02em}
.th-hook{min-width:220px;max-width:320px;font-size:.75rem}
.td-hook{font-size:.72rem;color:#1d6b3e;font-style:italic;max-width:300px;line-height:1.35;padding:6px 8px}
.td-hook-empty{color:#cbd5e1 !important;font-style:normal !important}
.th-sc{display:none !important}
.td-sc{display:none !important}
.td-score-val{cursor:pointer;border-bottom:1px dotted #94a3b8;color:var(--dark)}
.td-score-val:hover{background:#e0f2fe !important}
.th-cat{min-width:100px;font-size:.72rem}
.td-cat{text-align:center;padding:4px 8px}
.td-cat-empty{color:#cbd5e1;text-align:center}
.cat-chip{display:inline-block;border:1px solid;border-radius:20px;padding:3px 10px;font-size:.72rem;font-weight:800;cursor:help;white-space:nowrap;letter-spacing:.01em}
.fc-btns{display:flex;border-top:1px solid #f1f5f9}
.fc-btn{flex:1;display:flex;flex-direction:column;align-items:center;padding:12px 8px;text-decoration:none;color:var(--dark);transition:.1s;gap:3px;border-right:1px solid #f1f5f9}
.fc-btn:last-child{border-right:none}
.fc-btn:hover{background:#f8fafc}
.fc-btn>span:first-child{font-size:1.2rem}
.fc-btn-lbl{font-size:.67rem;font-weight:700;text-transform:uppercase;letter-spacing:.5px;color:#64748b}

/* ── TABLA COMPLETA 350 ── */
.full-table-section{margin:24px 28px 32px;border-radius:var(--radius);box-shadow:0 2px 10px rgba(0,0,0,.10);overflow:hidden;background:#fff}
.fts-header{padding:16px 20px 12px;border-bottom:1px solid #e2e8f0;display:flex;flex-wrap:wrap;align-items:center;gap:10px}
.fts-title{font-size:.95rem;font-weight:800;color:var(--dark);flex:1}
.fts-sub{font-size:.72rem;color:#94a3b8;flex-basis:100%}
.fts-search{padding:7px 12px;border:1.5px solid #e2e8f0;border-radius:8px;font-size:.8rem;width:280px;outline:none}
.fts-search:focus{border-color:var(--dark)}
.tbl-scroll{overflow-x:auto;max-height:65vh;overflow-y:auto}
.main-tbl{width:100%;border-collapse:collapse;font-size:.78rem}
.main-tbl thead{position:sticky;top:0;z-index:10}
.main-tbl thead tr:first-child th{background:var(--dark);color:#fff;padding:9px 8px;text-align:left;cursor:pointer;white-space:nowrap;user-select:none}
.main-tbl thead tr:first-child th:hover{background:#1d4e89}
.main-tbl thead tr:first-child th.sort-asc{background:#1d4e89}
.main-tbl thead tr:first-child th.sort-desc{background:#1d4e89}
.sort-icon{margin-left:4px;opacity:.5;font-size:.7rem}
.th-num{text-align:center !important}
.th-rn{width:36px}
.filter-row td{background:#f8fafc;padding:4px 6px;border-bottom:2px solid var(--dark)}
.col-filter{width:100%;padding:4px 6px;border:1px solid #e2e8f0;border-radius:4px;font-size:.74rem;background:#fff}
.main-tbl tbody tr{border-bottom:1px solid #f1f5f9;transition:.1s}
.main-tbl tbody tr:hover{background:#f0f7ff}
.main-tbl tbody tr.hidden-row{display:none}
.main-tbl td{padding:7px 8px;vertical-align:middle}
.td-rn{color:#94a3b8;font-size:.7rem;text-align:center}
.td-name{font-weight:600;color:#0f2944;max-width:320px}
.td-muni{color:#475569;white-space:nowrap}
.td-num{text-align:center;font-weight:700}
.cl-dot2{display:inline-block;width:7px;height:7px;border-radius:50%;margin-right:5px}
.acc-chip{font-size:.65rem;font-weight:700;padding:2px 7px;border-radius:4px;white-space:nowrap}
.tbl-count{padding:8px 20px;font-size:.75rem;color:#94a3b8;text-align:right;border-top:1px solid #f1f5f9}
'''

JS = '''
function showTab(id){
  document.querySelectorAll('.tsec').forEach(s=>s.classList.remove('active'));
  document.querySelectorAll('.ntab').forEach(t=>t.classList.remove('active'));
  document.getElementById('s-'+id).classList.add('active');
  document.getElementById('t-'+id).classList.add('active');
}

function showMet(id, btn){
  document.querySelectorAll('.met-panel').forEach(p=>p.style.display='none');
  document.querySelectorAll('.mt').forEach(b=>b.classList.remove('active'));
  document.getElementById('met-'+id).style.display='block';
  btn.classList.add('active');
}

function toggleList(uid){
  const list = document.getElementById('list-'+uid);
  const btn  = document.getElementById('btn-'+uid);
  const open = list.style.display==='block';
  list.style.display = open ? 'none' : 'block';
  btn.textContent = open ? '▼ Ver lugares 6–50' : '▲ Ocultar lista';
}

let activeCl = '', activeAcc = '';
function filterCl(cl, btn){
  activeCl = cl;
  document.querySelectorAll('.fpill').forEach(b=>b.classList.remove('active'));
  btn.classList.add('active');
  applyFilter();
}
function filterAcc(val){ activeAcc=val; applyFilter(); }
function applyFilter(){
  document.querySelectorAll('.cl-section').forEach(s=>{
    const clMatch = !activeCl || s.dataset.cl===activeCl;
    s.classList.toggle('hidden', !clMatch);
  });
  document.querySelectorAll('.li').forEach(li=>{
    let accMatch = !activeAcc || li.dataset.acc===activeAcc;
    if(activeAcc==='ALTPRIV') accMatch = (li.textContent||'').includes('🔄');
    li.classList.toggle('hidden-li', !accMatch);
  });
}
// ── MAPA INTERACTIVO (canvas puro, sin CDN) ──────────────────────────────────
var _LATMIN=-41.2,_LATMAX=-33.3,_LNGMIN=-64.0,_LNGMAX=-56.5;
var _mcx=0,_mcy=0,_msc=1,_mdrag=false,_mdx=0,_mdy=0,_mmov=false;
var _mcan=null,_mctx=null,_mW=0;

function _mproj(lat,lng){
  return [(_mW)*(_msc)*((lng-_LNGMIN)/(_LNGMAX-_LNGMIN))+_mcx,
          520*(_msc)*((_LATMAX-lat)/(_LATMAX-_LATMIN))+_mcy];
}

function _mdraw(){
  if(!_mctx) return;
  var ctx=_mctx,W=_mW,H=520,i,pt,p,r,ci;
  ctx.clearRect(0,0,W,H);
  ctx.fillStyle='#d4e9f7'; ctx.fillRect(0,0,W,H);
  ctx.strokeStyle='rgba(255,255,255,.3)'; ctx.lineWidth=0.5;
  var lng,lat;
  for(lng=-64;lng<=-56;lng++){pt=_mproj(_LATMIN,lng);ctx.beginPath();ctx.moveTo(pt[0],0);ctx.lineTo(pt[0],H);ctx.stroke();}
  for(lat=-41;lat<=-33;lat++){pt=_mproj(lat,_LNGMIN);ctx.beginPath();ctx.moveTo(0,pt[1]);ctx.lineTo(W,pt[1]);ctx.stroke();}
  var lgs=window.LUGARES;
  for(i=0;i<lgs.length;i++){
    p=lgs[i]; pt=_mproj(p.lat,p.lng);
    if(pt[0]<-20||pt[0]>W+20||pt[1]<-20||pt[1]>H+20) continue;
    r=Math.min(Math.max(3,5*_msc),16);
    ctx.beginPath();ctx.arc(pt[0],pt[1],r,0,6.28);
    ctx.fillStyle=p.clr+'bb';ctx.fill();
    ctx.strokeStyle='rgba(255,255,255,.8)';ctx.lineWidth=1.5;ctx.stroke();
  }
  var CLS=[['CIUDADES','#c0392b'],['CONURBANO','#2c3e50'],['CORREDOR','#1a5276'],
           ['COSTERO','#0e6655'],['INTERIOR','#7d6608'],['SALADO','#784212'],['SUR','#4a235a']];
  ctx.fillStyle='rgba(255,255,255,.9)';ctx.fillRect(8,8,110,CLS.length*17+14);
  ctx.strokeStyle='#dde';ctx.lineWidth=1;ctx.strokeRect(8,8,110,CLS.length*17+14);
  for(ci=0;ci<CLS.length;ci++){
    ctx.beginPath();ctx.arc(22,22+ci*17,5,0,6.28);ctx.fillStyle=CLS[ci][1];ctx.fill();
    ctx.fillStyle='#0f2944';ctx.font='bold 10px system-ui,sans-serif';
    ctx.fillText(CLS[ci][0],31,27+ci*17);
  }
  ctx.fillStyle='rgba(0,0,0,.35)';ctx.font='9px system-ui,sans-serif';
  ctx.textAlign='right';ctx.fillText('rueda=zoom  arrastrar=mover  click=info',W-8,H-6);ctx.textAlign='left';
}

// ── MAPA LEAFLET + OSM ───────────────────────────────────────────────────────
var _lmap=null;

function mpc(){}     // no-op (era para SVG)
function svgBgClick(){}

function toggleMap(){
  var wrap=document.getElementById('map-wrap');
  var btn=document.getElementById('map-toggle-btn');
  if(!wrap) return;
  var open=wrap.style.display==='none';
  wrap.style.display=open?'block':'none';
  if(btn){ btn.textContent=open?'✕ Cerrar mapa':'🗺️ Ver mapa'; btn.classList.toggle('active',open); }
  if(open){
    // doble rAF para que el browser compute dimensiones antes de Leaflet
    requestAnimationFrame(function(){
      requestAnimationFrame(function(){
        if(!_lmap) _linitMap();
        else _lmap.invalidateSize();
      });
    });
  }
}

function _linitMap(){
  if(!window.L){ setTimeout(_linitMap,300); return; }
  var mapDiv=document.getElementById('main-map');
  if(!mapDiv) return;

  _lmap=L.map('main-map',{zoomControl:true,attributionControl:true}).setView([-37.2,-60.0],7);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
    attribution:'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    maxZoom:18
  }).addTo(_lmap);

  var CL_COLORS={CIUDADES:'#c0392b',CONURBANO:'#2c3e50',CORREDOR:'#1a5276',
    COSTERO:'#0e6655',INTERIOR:'#7d6608',SALADO:'#784212',SUR:'#4a235a'};

  if(window.LUGARES){
    window.LUGARES.forEach(function(p){
      var icon=L.divIcon({
        html:'<div style="width:11px;height:11px;border-radius:50%;background:'+p.clr+';border:2px solid #fff;box-shadow:0 1px 5px rgba(0,0,0,.45)"></div>',
        className:'',iconSize:[11,11],iconAnchor:[5,5],popupAnchor:[0,-8]
      });
      var ej=p.eje?'<span style="font-size:.6rem;font-weight:700;padding:2px 6px;border-radius:10px;background:#f1f5f9;color:#374151;border:1px solid #e2e8f0">'+p.eje+'</span>':'';
      var ca=p.cat?'<span style="font-size:.6rem;font-weight:700;padding:2px 6px;border-radius:10px;background:#dbeafe;color:#1e40af">'+p.cat+'</span>':'';
      var hk=p.hook?'<div style="font-size:.68rem;font-style:italic;color:#b45309;margin:4px 0;line-height:1.3">&#128269; '+p.hook+'</div>':'';
      var sc='<div style="margin:4px 0;font-size:.7rem;color:#64748b"><b style="font-size:.9rem;color:'+p.clr+';font-weight:900">'+p.tot+'</b>&nbsp; IE:'+p.ie+' &middot; PC:'+p.pc+' &middot; UT:'+p.ut+' &middot; RS:'+p.rs+' &middot; LV:'+p.lv+'</div>';
      var ju=p.just?'<div style="font-size:.67rem;color:#475569;margin-top:5px;border-top:1px solid #f1f5f9;padding-top:5px;line-height:1.4">'+p.just.substring(0,180)+'&hellip;</div>':'';
      var html='<div style="font-family:system-ui,sans-serif;min-width:210px;max-width:260px">'+
        '<div style="display:flex;align-items:center;gap:6px;margin-bottom:5px">'+
        '<span style="background:'+p.bg+';color:'+p.tc+';font-size:.58rem;font-weight:700;padding:1px 6px;border-radius:3px">'+p.acc+'</span>'+
        '<span style="font-size:.6rem;color:'+p.clr+';font-weight:800">'+p.cl+'</span></div>'+
        '<div style="font-size:.82rem;font-weight:700;color:#0f2944;line-height:1.3;margin-bottom:2px">'+p.n+'</div>'+
        '<div style="font-size:.68rem;color:#64748b;margin-bottom:3px">&#128205; '+p.m+'</div>'+
        hk+sc+
        '<div style="display:flex;gap:4px;flex-wrap:wrap;margin-bottom:3px">'+ej+ca+'</div>'+
        ju+'</div>';
      L.marker([p.lat,p.lng],{icon:icon}).addTo(_lmap).bindPopup(html,{maxWidth:280,className:'pba-lf-popup'});
    });
  }

  // Leyenda clusters
  var leg=L.control({position:'bottomright'});
  leg.onAdd=function(){
    var d=L.DomUtil.create('div');
    d.style.cssText='background:rgba(255,255,255,.93);padding:8px 10px;border-radius:8px;box-shadow:0 2px 8px rgba(0,0,0,.18);font-family:system-ui,sans-serif;font-size:.7rem;line-height:1.7';
    d.innerHTML='<b style="font-size:.65rem;color:#64748b;display:block;margin-bottom:3px">CLUSTERS</b>'+
      Object.entries(CL_COLORS).map(function(kv){
        return '<span style="display:inline-block;width:9px;height:9px;border-radius:50%;background:'+kv[1]+';margin-right:5px;vertical-align:middle"></span>'+
               '<span style="color:#1e293b">'+kv[0]+'</span>';
      }).join('<br>');
    return d;
  };
  leg.addTo(_lmap);
  _lmap.invalidateSize();
}

// ── TABLA COMPLETA — búsqueda global, filtro por columna, cat, sort ──────────
let tblSortCol=-1, tblSortAsc=true;

function _rows(){ return Array.from(document.querySelectorAll('#tbl-body tr')); }

function applyTblFilters(){
  let vis=0;
  _rows().forEach(r=>{
    const ok = r.dataset.sm!=='0' && r.dataset.cm!=='0' && r.dataset.ctm!=='0';
    r.style.display = ok ? '' : 'none';
    if(ok) vis++;
  });
  const cnt=document.getElementById('tbl-count');
  if(cnt) cnt.textContent = vis+' lugar'+(vis!==1?'es':'');
}

function tblSearch(){
  const q=(document.getElementById('tbl-search').value||'').toLowerCase();
  _rows().forEach(r=>{ r.dataset.sm = (!q||r.textContent.toLowerCase().includes(q))?'1':'0'; });
  applyTblFilters();
}

function colFilter(){
  const filters=[];
  document.querySelectorAll('.col-filter[data-col]').forEach(el=>{
    const col=parseInt(el.dataset.col), val=(el.value||'').toLowerCase().trim();
    if(val) filters.push({col,val});
  });
  _rows().forEach(r=>{
    r.dataset.cm = filters.every(f=>{
      const c=r.cells[f.col]; return c && c.textContent.toLowerCase().includes(f.val);
    })?'1':'0';
  });
  applyTblFilters();
}

function catFilter(){
  const sel=document.getElementById('catFilterSel');
  const val=sel ? sel.value.toLowerCase() : '';
  _rows().forEach(r=>{
    const rc=(r.getAttribute('data-cat')||'').toLowerCase();
    r.dataset.ctm = (!val||rc.includes(val))?'1':'0';
  });
  applyTblFilters();
}

function sortTbl(col){
  const tbody=document.getElementById('tbl-body');
  if(!tbody) return;
  const rows=Array.from(tbody.querySelectorAll('tr'));
  const numCols=[0,4,5,6,7,8,9];
  const asc = tblSortCol===col ? !tblSortAsc : true;
  tblSortCol=col; tblSortAsc=asc;
  rows.sort((a,b)=>{
    const ca=a.cells[col]?a.cells[col].textContent.trim():'';
    const cb=b.cells[col]?b.cells[col].textContent.trim():'';
    if(numCols.includes(col)){
      const na=parseFloat(ca)||0, nb=parseFloat(cb)||0;
      return asc ? na-nb : nb-na;
    }
    return asc ? ca.localeCompare(cb,'es') : cb.localeCompare(ca,'es');
  });
  rows.forEach(r=>tbody.appendChild(r));
  document.querySelectorAll('#main-tbl thead tr:first-child th').forEach((th,i)=>{
    const ic=th.querySelector('.sort-icon');
    if(ic) ic.textContent = i===col?(asc?'↑':'↓'):'⇅';
  });
}

// ── POPUP DE ALCANCE (click en chip) ─────────────────────────────────────────
document.addEventListener('DOMContentLoaded', function(){

  const popup=document.createElement('div');
  popup.id='reach-popup';
  popup.style.cssText='position:fixed;z-index:9999;background:#0f2944;color:#fff;border-radius:10px;padding:14px 18px;max-width:340px;box-shadow:0 8px 32px rgba(0,0,0,.4);font-size:.8rem;display:none;line-height:1.5';
  document.body.appendChild(popup);
  const SCORE_DEF = {
    'IE': ['Impacto Electoral','Peso del municipio en la elección provincial. Se calcula desde datos reales: padrón (50%), competitividad 2023 (30%) y tendencia PJ 2025 (20%).','×0.25'],
    'PC': ['Potencial Comunicacional','Qué tan amplia y simbólica es la repercusión mediática esperada de la visita.','×0.25'],
    'UT': ['Unicidad Territorial','Qué tan singular e irrepetible es este lugar dentro de la provincia.','×0.20'],
    'RS': ['Representatividad Sectorial','Peso del sector productivo o social del lugar a nivel provincial.','×0.15'],
    'LV': ['Logística de Visita','Accesibilidad, tiempo de traslado y viabilidad operativa.','×0.15'],
  };

  document.addEventListener('click',function(e){
    const scoreCell=e.target.closest('.td-score-val');
    if(scoreCell){
      e.stopPropagation();
      const raw=scoreCell.getAttribute('data-sc')||'';
      const vals={};
      raw.split('|').forEach(p=>{ const [k,v]=p.split(':'); vals[k]=v; });
      const lugar=scoreCell.closest('tr').cells[1].textContent.trim();
      const total=scoreCell.textContent.trim();
      popup.innerHTML='<div style="font-size:.9rem;font-weight:800;margin-bottom:4px">📊 Score: '+total+'</div>'+
        '<div style="font-size:.7rem;opacity:.6;margin-bottom:10px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,.15)">'+lugar+'</div>'+
        Object.entries(SCORE_DEF).map(([k,[nombre,desc,peso]])=>{
          const v=vals[k]||'—';
          const pct=parseFloat(v)*parseFloat(peso)*10||0;
          return '<div style="margin-bottom:8px;padding:6px 8px;background:rgba(255,255,255,.08);border-radius:5px">'+
            '<div style="display:flex;justify-content:space-between;margin-bottom:3px">'+
            '<span style="font-weight:800;font-size:.8rem">'+k+' <span style="opacity:.55;font-size:.65rem">'+peso+'</span></span>'+
            '<span style="font-size:.85rem;font-weight:800;color:#7dd3fc">'+v+'</span></div>'+
            '<div style="font-size:.7rem;font-weight:600;margin-bottom:2px">'+nombre+'</div>'+
            '<div style="font-size:.65rem;opacity:.65">'+desc+'</div></div>';
        }).join('')+
        '<div style="margin-top:6px;font-size:.65rem;opacity:.4;text-align:right">click fuera para cerrar</div>';
      const r=scoreCell.getBoundingClientRect();
      popup.style.display='block';
      const pw=popup.offsetWidth, ph=popup.offsetHeight;
      let top=r.bottom+8, left=r.left-pw/2;
      if(top+ph>window.innerHeight) top=r.top-ph-8;
      if(left+pw>window.innerWidth) left=window.innerWidth-pw-12;
      popup.style.top=Math.max(8,top)+'px';
      popup.style.left=Math.max(8,left)+'px';
      return;
    }
    const chip=e.target.closest('.cat-chip,.pc-cat-chip');
    if(chip){
      e.stopPropagation();
      const tip=chip.getAttribute('data-info')||chip.getAttribute('title')||'';
      const parts=tip.split('||');
      const lvlStyle={
        '●':'background:rgba(16,185,129,.18);border-left:3px solid #10b981',
        '◐':'background:rgba(245,158,11,.15);border-left:3px solid #f59e0b',
        '○':'background:rgba(148,163,184,.15);border-left:3px solid #94a3b8',
      };
      popup.innerHTML='<div style="font-size:.95rem;font-weight:800;margin-bottom:10px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,.2)">'+
        (parts[0]||'')+'</div>'+
        '<div style="font-size:.72rem;opacity:.7;margin-bottom:10px">'+
        (parts[1]||'')+'</div>'+
        parts.slice(2).map(l=>{
          const icon=l.charAt(0);
          const st=lvlStyle[icon]||'';
          return '<div style="'+st+';border-radius:4px;padding:5px 8px;margin-bottom:5px;font-size:.72rem">'+l+'</div>';
        }).join('')+
        '<div style="margin-top:8px;font-size:.65rem;opacity:.45;text-align:right">click fuera para cerrar</div>';
      const r=chip.getBoundingClientRect();
      popup.style.display='block';
      const pw=popup.offsetWidth, ph=popup.offsetHeight;
      let top=r.bottom+8, left=r.left;
      if(top+ph>window.innerHeight) top=r.top-ph-8;
      if(left+pw>window.innerWidth) left=window.innerWidth-pw-12;
      popup.style.top=Math.max(8,top)+'px';
      popup.style.left=Math.max(8,left)+'px';
    } else {
      popup.style.display='none';
    }
  });
});
'''

# ── Construct ─────────────────────────────────────────────────────────────────
html = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>PBA — Archivo Maestro 2026</title>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">
<style>{CSS}</style>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script>{JS}</script>
</head>
<body>

<nav class="mnav">
  <div class="ntop">
    <h1>🗺️ PBA — Archivo Maestro 2026</h1>
    <span class="vtag">v3 · IE desde datos reales</span>
  </div>
  <div class="ntabs">
    <button id="t-inm"  class="ntab active" onclick="showTab('inm')">📖 Inmersión Provincial</button>
    <button id="t-rec"  class="ntab"        onclick="showTab('rec')">🗺️ Recorrida Territorial</button>
    <button id="t-fich" class="ntab"        onclick="showTab('fich')">📋 Fichas Municipales</button>
    <button id="t-met"  class="ntab"        onclick="showTab('met')">🔬 Metodología &amp; Estrategia</button>
  </div>
</nav>

<div id="s-inm" class="tsec active">
  {embed_doc(BASE_HTML + "Inmersion_Provincial_PBA_2026.html")}
</div>

<div id="s-rec" class="tsec">
  {render_recorrida()}
</div>

<div id="s-fich" class="tsec">
  <div class="fichas-sec">
    <h2>📋 Fichas Municipales</h2>
    <p>Cada municipio incluye su ficha estructurada (datos, indicadores, contexto electoral) y su ficha narrativa (relato estratégico para recorrida).</p>
    <div class="fichas-grid">{render_fichas()}</div>
  </div>
</div>

<div id="s-met" class="tsec">
  {render_metod()}
</div>

{_places_js()}
</body></html>'''

with open(OUTPUT, 'w', encoding='utf-8') as f:
    f.write(html)

kb = os.path.getsize(OUTPUT) // 1024
print(f"✅ PBA_Maestro_2026.html — {kb} KB")
