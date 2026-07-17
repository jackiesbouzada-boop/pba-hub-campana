# -*- coding: utf-8 -*-
"""
Alternativas PRIVADAS para lugares PROTOCOLAR de alto score.
Formato: (nombre, municipio, ie, pc, ut, rs, lv, justificacion, actores)
"""

ALTERNATIVAS_POR_CLUSTER = {

    # ─── CIUDADES ───────────────────────────────────────────────────────────
    'CIUDADES': [
        # Puerto Mar del Plata (Montenegro-PRO)
        (
            '🔄 Alt. Priv. — Conarpesa S.A. — Mayor procesadora de mariscos del Atlántico Sur',
            'General Pueyrredón', 8, 9, 9, 8, 8,
            '1 de cada 4 cajas de langostino que Argentina exporta pasa por Conarpesa. 1.500 empleados. Coordinación directa con gerencia, sin intendente de por medio.',
            'conarpesa, pesquera privada, empresa, exportacion maritima',
        ),
        (
            '🔄 Alt. Priv. — Cervecería Antares — La que inventó el craft argentino en Mar del Plata',
            'General Pueyrredón', 8, 9, 9, 7, 9,
            'Pionera del craft beer en Argentina: nació en Mar del Plata en 1998 cuando nadie creía en la cerveza artesanal. Hoy tiene franquicias en 30 ciudades del país. Fundadores locales, empresa 100% privada y argentina. Visita a la fábrica madre muestra el antes y el después de una industria que crearon desde cero.',
            'cerveza artesanal, antares, empresa privada, mar del plata',
        ),
        # Puerto Bahía Blanca
        (
            '🔄 Alt. Priv. — PBBPolisur S.A. (INEOS) — La única planta de polietileno y PVC simultáneos de Argentina',
            'Bahía Blanca', 7, 9, 9, 8, 7,
            'La única planta en Argentina que produce polietileno y PVC al mismo tiempo. Sin ella no hay cañerías ni envases en el país. 700 empleados directos + 2.000 contratistas. Privada (grupo INEOS), coordinación directa con gerencia.',
            'pbbpolisur, pbbeolisur, dow, ineos, petroquimica privada, empresa',
        ),

        # Zárate — autopartes Toyota supplier
        (
            '🔄 Alt. Priv. — Fric-Rot S.A. — La única autopartista argentina con homologación en 40 países',
            'Zárate', 7, 8, 8, 7, 6,
            'Única empresa argentina de autopartes que tiene homologación técnica en 40 países y es proveedora directa de Toyota Zárate. Llevan 3 generaciones de ingeniería nacional: fabrican los rótulas y crucetas que ningún proveedor extranjero quiso producir localmente. Coordinación directa con dirección, sin protocolo municipal.',
            'fric-rot, autopartes, toyota, industria privada, zarate, homologacion',
        ),
        # Bahía Blanca — cooperativa de consumo icónica
        (
            '🔄 Alt. Priv. — Cooperativa Obrera — 270.000 socios: el supermercado que les pertenece a sus clientes',
            'Bahía Blanca', 8, 9, 10, 10, 8,
            'Fundada en 1926, es la cooperativa de consumo más grande de Argentina y una de las 20 más grandes del mundo: 270.000 socios, 40 sucursales, sin un solo accionista externo. En Bahía Blanca le gana en precio y fidelidad a las cadenas nacionales. Muestra el eje Eco. Social con base en la clase trabajadora del Sur. Coordinación directa con el consejo directivo, sin protocolo municipal.',
            'cooperativa obrera, economía social, supermercado cooperativo, bahia blanca, privado',
        ),
        # San Nicolás — acero estructural
        (
            '🔄 Alt. Priv. — Ternium Argentina — El acero de cada puente y edificio construido en Argentina',
            'San Nicolás de los Arroyos', 8, 10, 10, 9, 8,
            'La planta siderúrgica integrada más grande de Argentina: 4.000 empleados directos, produce el acero estructural para construcción e infraestructura de todo el país. Ex SOMISA estatal, privatizada en 1992, hoy 100% Grupo Techint. Complementa a Tenaris en el mismo municipio: doble narrativa industrial. Coordinación directa con gerencia, sin protocolo.',
            'ternium, siderurgia, acero, industria privada, san nicolas, techint, produccion',
        ),
        # Bahía Blanca — fertilizantes, soberanía agroindustrial
        (
            '🔄 Alt. Priv. — Profertil S.A. — El mayor productor de fertilizantes nitrogenados de América Latina',
            'Bahía Blanca', 7, 9, 10, 8, 7,
            'Joint venture entre YPF e Yara (Noruega). Produce urea granulada y amoníaco: los fertilizantes sin los cuales Argentina no puede fertilizar su propia cosecha. La mayor planta de fertilizantes nitrogenados de Latinoamérica, toda en Bahía Blanca. 400 empleados directos, 1.200 contratistas. Coordinación directa con gerencia.',
            'profertil, fertilizantes, urea, amoniaco, ypf, yara, bahia blanca, privado, petroquimica, campo',
        ),
        # Delta San Fernando
        (
            '🔄 Alt. Priv. — Astilleros Mestrina — 3 generaciones construyendo barcos de madera en el Delta',
            'San Fernando', 7, 8, 8, 7, 7,
            '60 años de historia familiar. Única familia que mantiene la tradición de construcción naval artesanal en madera en el Delta del Paraná. El patriarca, los hijos y los nietos en el mismo astillero. Privado, coordinación directa.',
            'astilleros mestrina, construccion naval, empresa familiar privada, delta',
        ),
    ],

    # ─── CONURBANO ──────────────────────────────────────────────────────────
    'CONURBANO': [
        # Reemplaza Mattievich — mejor historia con La Juanita
        (
            '🔄 Alt. Priv. — Cooperativa La Juanita — Del desempleo del 2001 al modelo que estudian en Harvard',
            'La Matanza', 9, 9, 10, 9, 7,
            'Nació en 2001 cuando el barrio de La Juanita llegó al 40% de desocupación. Hoy es una cooperativa de producción, panadería y textil que ganó el Premio Cartier de Emprendimiento Social. Modelo estudiado en universidades de 15 países. Coordinación directa con las fundadoras.',
            'cooperativa la juanita, economía social, trabajo recuperado, la matanza, empresa social',
        ),
        # MadyGraf — nueva alternativa con historia fuerte
        (
            '🔄 Alt. Priv. — MadyGraf — La fábrica que los trabajadores recuperaron y hoy imprime para las Naciones Unidas',
            'Tigre', 8, 10, 10, 9, 7,
            'En 2014 Donnelley cerró sin aviso. Los 400 trabajadores no se fueron: tomaron la planta y la convirtieron en una cooperativa. Hoy MadyGraf imprime para UNICEF, la ONU y editoriales académicas del mundo. Única cooperativa de imprenta del país con clientes internacionales de ese nivel.',
            'madygraf, cooperativa grafica, trabajo recuperado, donnelley, tigre, privado',
        ),

        # Quilmes — industria e identidad
        (
            '🔄 Alt. Priv. — Cervecería y Maltería Quilmes (ABInBev) — 130 años: la marca de cerveza más icónica de Argentina',
            'Quilmes', 8, 10, 9, 8, 9,
            'Fundada en 1888 por inmigrantes suizos que llegaron a vender hielo. Hoy producen 20 millones de litros por mes y la marca es sinónimo de Argentina en el mundo. 130 años de historia industrial en el mismo municipio, planta madre aún en operación. Enorme peso en Identidad + Producción. Coordinación directa con gerencia industrial.',
            'cervecería quilmes, malteria, abinbev, industria cervecera, quilmes, identidad, privado',
        ),
        # Escobar / Garín — biotech vacunas
        (
            '🔄 Alt. Priv. — Sinergium Biotech — La única empresa privada que fabrica vacunas a escala industrial en Argentina',
            'Escobar', 7, 9, 9, 7, 7,
            'Ubicada en Garín, Escobar. Única empresa privada de Argentina con capacidad de fabricar vacunas y biofármacos a escala industrial: produce millones de dosis anuales de vacunas antigripales y otras. Capital nacional, ciencia aplicada. Eje Ciencia con narrativa de soberanía sanitaria. Coordinación directa con dirección científica, sin protocolo municipal.',
            'sinergium biotech, vacunas, biofármacos, ciencia privada, escobar, garin, soberanía sanitaria',
        ),
        # Escobar Capital de la Flor
        (
            '🔄 Alt. Priv. — Vivero Plantín S.A. — El mayor exportador de plantas ornamentales de Argentina',
            'Escobar', 8, 8, 8, 7, 7,
            'Exporta más de 1 millón de plantas al año a Europa y América. Fundado por una comunidad de inmigrantes japoneses y coreanos que transformaron Escobar en capital floral. La historia de la inmigración productiva que construyó el país. Privado, coordinación directa.',
            'plantin, vivero, floricultura, empresa privada, exportacion, escobar',
        ),
    ],

    # ─── CORREDOR ───────────────────────────────────────────────────────────
    'CORREDOR': [
        # AFA Pergamino
        (
            '🔄 Alt. Priv. — Bioceres S.A. — La única empresa latinoamericana de biotech agrícola en NASDAQ',
            'Pergamino', 6, 10, 10, 8, 7,
            'Primera y única empresa latinoamericana de biotecnología agrícola que cotizó en NASDAQ (2019). Desarrollaron la soja HB4 resistente a la sequía: si funciona a escala, puede cambiar la agricultura del planeta. Sede en Pergamino. CEO: Federico Trucco, coordinación directa.',
            'bioceres, biotecnologia agricola, semillas, empresa privada, nasdaq',
        ),

        # San Pedro — soberanía informativa
        (
            '🔄 Alt. Priv. — Papel Prensa S.A. — La única fábrica de papel de diario de Argentina',
            'San Pedro', 7, 10, 9, 8, 7,
            'Sin este predio en San Pedro no existe ningún periódico impreso en Argentina: es la única planta que produce papel de diario en el país. Accionistas: Grupo Clarín, La Nación y el Estado nacional. Soberanía informativa en un solo edificio. Alta tracción mediática garantizada: la visita genera cobertura espontánea. Sin protocolo municipal.',
            'papel prensa, papel diario, periodismo, soberanía informativa, san pedro, privado',
        ),
        # San Pedro fruticultura
        (
            '🔄 Alt. Priv. — San Miguel S.A. — El primer embarque de mandarina argentina a China salió de aquí',
            'San Pedro', 7, 9, 9, 8, 8,
            'San Miguel S.A. logró en 2019 la primera exportación de mandarina argentina a China — un hito que parecía imposible. 3.000 empleados. La planta más grande de procesado de cítricos en Argentina está en San Pedro. Privada (familia Miguens), coordinación directa con gerencia regional.',
            'san miguel sa, citrus, citricos, exportacion, empresa privada, san pedro',
        ),
        # Ramallo — reemplaza Rexnord por algo más fuerte
        (
            '🔄 Alt. Priv. — Cooperativa Apícola del Corredor Norte — La miel argentina que llega a los supermercados de Alemania',
            'Ramallo', 6, 8, 8, 7, 7,
            'El corredor norte bonaerense produce el 18% de la miel argentina de exportación. Esta cooperativa organiza a productores de Ramallo, San Pedro y San Nicolás que exportan a Europa vía Mercadona, Aldi y Lidl. Sin intermediarios, coordinación directa con el consejo.',
            'cooperativa apicola, miel, exportacion, corredor norte, privado',
        ),
    ],

    # ─── COSTERO ────────────────────────────────────────────────────────────
    'COSTERO': [
        # Puerto Quequén / Necochea
        (
            '🔄 Alt. Priv. — Molinos Juan Semino S.A. — 4ª generación sobre el mismo río Quequén',
            'Necochea', 7, 8, 8, 8, 7,
            'La misma familia Semino lleva 4 generaciones exportando harina desde el río Quequén. El único molino harinero del país que tiene su propia terminal portuaria fluvial. Exportan a Brasil, Bolivia y países de África. Privado, coordinación directa con la cuarta generación de la familia.',
            'semino, molinos, harina, aceite, exportacion, empresa privada, quequen',
        ),
        # Mar del Plata flota pesquera
        (
            '🔄 Alt. Priv. — Pesquera Bariloche S.A. — Pioneer en frío a bordo: el pescado llega entero a Europa',
            'General Pueyrredón', 8, 9, 9, 8, 7,
            'Bariloche fue la primera empresa del país en instalar cámaras de frío en los barcos pesqueros: la merluza se procesa a bordo, no en tierra. Resultado: calidad europea desde el Atlántico Sur. Sin protocolo con Montenegro.',
            'pesquera bariloche, merluza, exportacion pesquera, empresa privada, mar del plata',
        ),
        # La Costa reservas
        (
            '🔄 Alt. Priv. — Granja La Ballenita — El único centro privado de rescate de fauna marina en el litoral bonaerense',
            'La Costa', 6, 8, 8, 6, 7,
            'Única organización privada en PBA que rescata, rehabilita y libera lobos marinos, pingüinos y toninas. Fundada por una veterinaria local. Sin subsidios estatales: se autofinancia con donaciones y turismo educativo. Visita perfecta para el eje ambiental.',
            'la ballenita, fauna marina, conservacion, privado, educacion ambiental',
        ),
    ],

    # ─── INTERIOR ───────────────────────────────────────────────────────────
    'INTERIOR': [
        # Cañuelas lechería
        (
            '🔄 Alt. Priv. — La Lacteo — El queso bonaerense que ganó medalla de oro en Lyon',
            'Cañuelas', 6, 9, 9, 8, 8,
            'Empresa familiar de quesos artesanales de Cañuelas que ganó medalla de oro en el Concurso Internacional de Lyon (Francia) con su gruyere. La única quesería de PBA con reconocimiento internacional europeo. Privada, coordinación directa con los dueños.',
            'lacteo, quesos, empresa privada, cañuelas, produccion lechera, medalla lyon',
        ),
        # Azul ganadería
        (
            '🔄 Alt. Priv. — Estancia El Ombú Grande — La cabaña que desarrolló la raza Brangus en Argentina',
            'Azul', 7, 9, 9, 8, 7,
            'Establecimiento ganadero de Azul que fue pionero en desarrollar la raza Brangus en Argentina (cruce de Aberdeen Angus con Brahman). Sus toros reproductores se exportan a Brasil, Paraguay y Colombia. Coordinación directa con los propietarios.',
            'cabaña ganadera, brangus, genetica bovina, azul, exportacion, privado',
        ),

        # 25 de Mayo — agribusiness innovador
        (
            '🔄 Alt. Priv. — Los Grobo Agropecuaria — El pool de siembra más conocido del mundo nació aquí',
            '25 de Mayo', 6, 9, 9, 8, 7,
            'Fundado en 25 de Mayo en los años 80 por Gustavo Grobocopatel, Los Grobo inventó el modelo de pool de siembra que cambió para siempre la agricultura de América del Sur. Hoy opera en Argentina, Uruguay, Brasil y Paraguay. La historia de cómo el campo bonaerense exportó una idea al mundo. Eje Campo + Ciencia. Coordinación directa con management.',
            'los grobo, pool siembra, agribusiness, agropecuaria privada, 25 de mayo, innovacion campo',
        ),
        # Y-TEC Ensenada
        (
            '🔄 Alt. Priv. — YPF Tecnología (Y-TEC) — El único lugar de Argentina donde se fabrican celdas de litio',
            'Ensenada', 8, 10, 10, 9, 7,
            'Único lugar en Argentina donde se fabrican prototipos de celdas de baterías de litio. YPF + CONICET. El litio sale de la Puna, se convierte en batería en Ensenada. Coordinación directa con la dirección ejecutiva. Sin protocolo municipal.',
            'ytec, ypf tecnologia, energia, litio, baterias, innovacion, privado mixto, ensenada',
        ),
    ],

    # ─── SALADO ─────────────────────────────────────────────────────────────
    'SALADO': [
        # Laguna de Chascomús
        (
            '🔄 Alt. Priv. — Piscicultura Salado — El único criadero intensivo de pejerrey del país',
            'Chascomús', 6, 9, 10, 7, 7,
            'El único establecimiento en Argentina que cría pejerrey en tanques de forma intensiva para repoblamiento de lagunas. Desarrollaron la tecnología de reproducción en cautiverio que hoy usa el INIDEP. Privado, coordinación directa con el fundador-investigador.',
            'piscicultura, pejerrey, acuicultura, empresa privada, chascomus, unico en argentina',
        ),
        # Dolores ganadería
        (
            '🔄 Alt. Priv. — Cabañas Cumelén — La genética bovina que viaja a 12 países desde Dolores',
            'Dolores', 6, 8, 9, 8, 7,
            'Establecimiento ganadero en Dolores que exporta genética bovina (semen y embriones) a 12 países de América Latina. Única cabaña del Salado con certificación internacional de genética. Coordinación directa con propietario.',
            'cabaña bovina, genetica exportacion, semen embriones, privado, dolores, salado',
        ),
    ],

    # ─── SUR ────────────────────────────────────────────────────────────────
    'SUR': [

        # Tres Arroyos — cooperativa centenaria
        (
            '🔄 Alt. Priv. — CATA Cooperativa Agrícola de Tres Arroyos — 100 años de historia que factura más que el municipio',
            'Tres Arroyos', 6, 8, 9, 9, 7,
            'Cooperativa cerealera fundada hace más de 100 años en Tres Arroyos. Organiza a cientos de productores de cereales y oleaginosas del sur bonaerense. Su facturación anual supera el presupuesto municipal de Tres Arroyos. Eje Campo + Eco. Social: muestra que el cooperativismo agrario es competitivo a escala global. Coordinación directa con el consejo.',
            'cata, cooperativa agrícola, tres arroyos, cereales, oleaginosas, cooperativismo, privado',
        ),
        # Tornquist / parque provincial
        (
            '🔄 Alt. Priv. — Ecoturismo Ventana — El único operador que guía en el único "cerro en isla" de Argentina',
            'Tornquist', 5, 8, 9, 6, 7,
            'El Cerro Tres Picos (1.239m) es el pico más alto de la Provincia y está en un campo privado. La única empresa que tiene permiso para guiar excursiones al pico. Sin ellos no se sube. Privado, coordinación directa.',
            'ecoturismo, sierra ventana, empresa privada, trekking, cerro tres picos',
        ),
        # Coronel Suárez calzado
        (
            '🔄 Alt. Priv. — Calzados Guante — El calzado de trabajo que usa la mitad de los obreros de Argentina',
            'Coronel Suárez', 5, 9, 9, 8, 7,
            'Guante fabrica el calzado de seguridad industrial que usa la mitad de los obreros industriales de Argentina. Fundada en Coronel Suárez en 1966, sigue siendo familiar y local. Privada, coordinación directa con el dueño.',
            'guante, calzado seguridad, fabrica privada, industria, pyme, coronel suarez',
        ),
        # Villarino horticultura
        (
            '🔄 Alt. Priv. — Cooperativa Hortícola del Río Colorado — La cebolla del desierto que llega a Brasil',
            'Villarino', 5, 8, 9, 7, 6,
            'En el desierto del sur bonaerense, esta cooperativa produce cebollas y pimientos bajo riego que se exportan a Brasil y Bolivia. Tecnología de riego gota a gota en suelo árido: lo que no debería ser campo, es campo. Coordinación directa con el consejo.',
            'horticultura, riego, cooperativa privada, rio colorado, villarino, agro, exportacion',
        ),
    ],
}

if __name__ == '__main__':
    todos = [(cl, p) for cl, places in ALTERNATIVAS_POR_CLUSTER.items() for p in places]
    print(f"Total alternativas: {len(todos)}")
    for cl, places in ALTERNATIVAS_POR_CLUSTER.items():
        print(f"  {cl}: {len(places)}")
