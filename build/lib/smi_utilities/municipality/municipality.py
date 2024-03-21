from django.db.models import TextChoices


class Municipality(TextChoices):
    """
    Enumeration representing municipalities in Chile.
    """

    ARICA = "Arica"
    AYSEN = "Aysén"
    ALGARROBO = "Algarrobo"
    ALHUE = "Alhué"
    ALTO_BIOBIO = "Alto Biobío"
    ALTO_DEL_CARMEN = "Alto del Carmen"
    ALTO_HOSPICIO = "Alto Hospicio"
    ANCUD = "Ancud"
    ANDACOLLO = "Andacollo"
    ANGOL = "Angol"
    ANTARTICA = "Antártica"
    ANTOFAGASTA = "Antofagasta"
    ANTUCO = "Antuco"
    ARAUCO = "Arauco"
    BUIN = "Buin"
    BULNES = "Bulnes"
    CABILDO = "Cabildo"
    CABO_DE_HORNOS = "Cabo de Hornos"
    CABRERO = "Cabrero"
    CALAMA = "Calama"
    CALBUCO = "Calbuco"
    CALDERA = "Caldera"
    CALERA = "Calera"
    CALERA_DE_TANGO = "Calera de Tango"
    CALLE_LARGA = "Calle Larga"
    CAMARONES = "Camarones"
    CAMINA = "Camiña"
    CANELA = "Canela"
    CANETE = "Cañete"
    CARAHUE = "Carahue"
    CARTAGENA = "Cartagena"
    CASABLANCA = "Casablanca"
    CASTRO = "Castro"
    CATEMU = "Catemu"
    CAUQUENES = "Cauquenes"
    CERRILLOS = "Cerrillos"
    CERRO_NAVIA = "Cerro Navia"
    CHAITEN = "Chaitén"
    CHANCO = "Chanco"
    CHANARAL = "Chañaral"
    CHEPICA = "Chépica"
    CHIGUAYANTE = "Chiguayante"
    CHILE_CHICO = "Chile Chico"
    CHILLAN = "Chillán"
    CHILLAN_VIEJO = "Chillán Viejo"
    CHIMBARONGO = "Chimbarongo"
    CHOLCHOL = "Cholchol"
    CHONCHI = "Chonchi"
    CISNES = "Cisnes"
    COBQUECURA = "Cobquecura"
    COCHAMO = "Cochamó"
    COCHRANE = "Cochrane"
    CODEGUA = "Codegua"
    COELEMU = "Coelemu"
    COYHAIQUE = "Coyhaique"
    COIHUECO = "Coihueco"
    COINCO = "Coinco"
    COLBUN = "Colbún"
    COLCHANE = "Colchane"
    COLINA = "Colina"
    COLLIPULLI = "Collipulli"
    COLTAUCO = "Coltauco"
    COMBARBALA = "Combarbalá"
    CONCEPCION = "Concepción"
    CONCHALI = "Conchalí"
    CONCON = "Concón"
    CONSTITUCION = "Constitución"
    CONTULMO = "Contulmo"
    COPIAPO = "Copiapó"
    COQUIMBO = "Coquimbo"
    CORONEL = "Coronel"
    CORRAL = "Corral"
    CUNCO = "Cunco"
    CURACAUTIN = "Curacautín"
    CURACAVI = "Curacaví"
    CURACO_DE_VELEZ = "Curaco de Vélez"
    CURANILAHUE = "Curanilahue"
    CURARREHUE = "Curarrehue"
    CUREPTO = "Curepto"
    CURICO = "Curicó"
    DALCAHUE = "Dalcahue"
    DIEGO_DE_ALMAGRO = "Diego de Almagro"
    DONIHUE = "Doñihue"
    EL_BOSQUE = "El Bosque"
    EL_CARMEN = "El Carmen"
    EL_MONTE = "El Monte"
    EL_QUISCO = "El Quisco"
    EL_TABO = "El Tabo"
    EMPEDRADO = "Empedrado"
    ERCILLA = "Ercilla"
    ESTACION_CENTRAL = "Estación Central"
    FLORIDA = "Florida"
    FREIRE = "Freire"
    FREIRINA = "Freirina"
    FRESIA = "Fresia"
    FRUTILLAR = "Frutillar"
    FUTALEUFU = "Futaleufú"
    FUTRONO = "Futrono"
    GALVARINO = "Galvarino"
    GENERAL_LAGOS = "General Lagos"
    GORBEA = "Gorbea"
    GRANEROS = "Graneros"
    GUAITECAS = "Guaitecas"
    HIJUELAS = "Hijuelas"
    HUALAIHUE = "Hualaihué"
    HUALANE = "Hualañé"
    HUALPEN = "Hualpén"
    HUALQUI = "Hualqui"
    HUARA = "Huara"
    HUASCO = "Huasco"
    HUECHURABA = "Huechuraba"
    ILLAPEL = "Illapel"
    INDEPENDENCIA = "Independencia"
    IQUIQUE = "Iquique"
    ISLA_DE_PASCUA = "Isla de Pascua"
    ISLA_DE_MAIPO = "Isla de Maipo"
    JUAN_FERNANDEZ = "Juan Fernández"
    LA_CISTERNA = "La Cisterna"
    LA_CRUZ = "La Cruz"
    LA_ESTRELLA = "La Estrella"
    LA_FLORIDA = "La Florida"
    LA_GRANJA = "La Granja"
    LA_HIGUERA = "La Higuera"
    LA_LIGUA = "La Ligua"
    LA_PINTANA = "La Pintana"
    LA_REINA = "La Reina"
    LA_SERENA = "La Serena"
    LA_UNION = "La Unión"
    LAGO_RANCO = "Lago Ranco"
    LAGO_VERDE = "Lago Verde"
    LAGUNA_BLANCA = "Laguna Blanca"
    LAJA = "Laja"
    LAMPA = "Lampa"
    LANCO = "Lanco"
    LAS_CABRAS = "Las Cabras"
    LAS_CONDES = "Las Condes"
    LAUTARO = "Lautaro"
    LEBU = "Lebu"
    LICANTEN = "Licantén"
    LIMACHE = "Limache"
    LINARES = "Linares"
    LITUECHE = "Litueche"
    LLAILLAY = "Llaillay"
    LLANQUIHUE = "Llanquihue"
    LO_BARNECHEA = "Lo Barnechea"
    LO_ESPEJO = "Lo Espejo"
    LO_PRADO = "Lo Prado"
    LOLOL = "Lolol"
    LONCOCHE = "Loncoche"
    LONGAVI = "Longaví"
    LONQUIMAY = "Lonquimay"
    LOS_ALAMOS = "Los Álamos"
    LOS_ANDES = "Los Andes"
    LOS_ANGELES = "Los Ángeles"
    LOS_LAGOS = "Los Lagos"
    LOS_MUERMOS = "Los Muermos"
    LOS_SAUCES = "Los Sauces"
    LOS_VILOS = "Los Vilos"
    LOTA = "Lota"
    LUMACO = "Lumaco"
    MACHALI = "Machalí"
    MACUL = "Macul"
    MAFIL = "Máfil"
    MAIPU = "Maipú"
    MALLOA = "Malloa"
    MARCHIHUE = "Marchihue"
    MARIA_ELENA = "María Elena"
    MARIA_PINTO = "María Pinto"
    MARIQUINA = "Mariquina"
    MAULE = "Maule"
    MAULLIN = "Maullín"
    MEJILLONES = "Mejillones"
    MELIPEUCO = "Melipeuco"
    MELIPILLA = "Melipilla"
    MOLINA = "Molina"
    MONTE_PATRIA = "Monte Patria"
    MOSTAZAL = "Mostazal"
    MULCHEN = "Mulchén"
    NACIMIENTO = "Nacimiento"
    NANCAGUA = "Nancagua"
    NATALES = "Natales"
    NAVIDAD = "Navidad"
    NEGRETE = "Negrete"
    NINHUE = "Ninhue"
    NOGALES = "Nogales"
    NUEVA_IMPERIAL = "Nueva Imperial"
    NIQUEN = "Ñiquén"
    NUNOA = "Ñuñoa"
    OHIGGINS = "O'Higgins"
    OLIVAR = "Olivar"
    OLLAGUE = "Ollagüe"
    OLMUE = "Olmué"
    OSORNO = "Osorno"
    OVALLE = "Ovalle"
    PADRE_HURTADO = "Padre Hurtado"
    PADRE_LAS_CASAS = "Padre Las Casas"
    PAIGUANO = "Paiguano"
    PAILLACO = "Paillaco"
    PAINE = "Paine"
    PALENA = "Palena"
    PALMILLA = "Palmilla"
    PANGUIPULLI = "Panguipulli"
    PANQUEHUE = "Panquehue"
    PAPUDO = "Papudo"
    PAREDONES = "Paredones"
    PARRAL = "Parral"
    PEDRO_AGUIRRE_CERDA = "Pedro Aguirre Cerda"
    PELARCO = "Pelarco"
    PELLUHUE = "Pelluhue"
    PEMUCO = "Pemuco"
    PENCAHUE = "Pencahue"
    PENCO = "Penco"
    PENAFLOR = "Peñaflor"
    PEÑALOLÉN = "Peñalolén"
    PERALILLO = "Peralillo"
    PERQUENCO = "Perquenco"
    PETORCA = "Petorca"
    PEUMO = "Peumo"
    PICA = "Pica"
    PICHIDEGUA = "Pichidegua"
    PICHILEMU = "Pichilemu"
    PINTO = "Pinto"
    PIRQUE = "Pirque"
    PITRUFQUEN = "Pitrufquén"
    PLACILLA = "Placilla"
    PORTEZUELO = "Portezuelo"
    PORVENIR = "Porvenir"
    POZO_ALMONTE = "Pozo Almonte"
    PRIMAVERA = "Primavera"
    PROVIDENCIA = "Providencia"
    PUCHUNCAVI = "Puchuncaví"
    PUCON = "Pucón"
    PUDAHUEL = "Pudahuel"
    PUENTE_ALTO = "Puente Alto"
    PUERTO_MONTT = "Puerto Montt"
    PUERTO_OCTAY = "Puerto Octay"
    PUERTO_VARAS = "Puerto Varas"
    PUMANQUE = "Pumanque"
    PUNITAQUI = "Punitaqui"
    PUNTA_ARENAS = "Punta Arenas"
    PUQUELDON = "Puqueldón"
    PUREN = "Purén"
    PURRANQUE = "Purranque"
    PUTAENDO = "Putaendo"
    PUTRE = "Putre"
    PUYEHUE = "Puyehue"
    QUEILEN = "Queilén"
    QUELON = "Quellón"
    QUEMCHI = "Quemchi"
    QUILACO = "Quilaco"
    QUILICURA = "Quilicura"
    QUILLECO = "Quilleco"
    QUILLON = "Quillón"
    QUILLOTA = "Quillota"
    QUILPUE = "Quilpué"
    QUINCHAO = "Quinchao"
    QUINTA_DE_TILCOCO = "Quinta de Tilcoco"
    QUINTA_NORMAL = "Quinta Normal"
    QUINTERO = "Quintero"
    QUIRIHUE = "Quirihue"
    RANCAGUA = "Rancagua"
    RANQUIL = "Ránquil"
    RAUCO = "Rauco"
    RECOLETA = "Recoleta"
    RENAICO = "Renaico"
    RENCA = "Renca"
    RENGO = "Rengo"
    REQUINOA = "Requínoa"
    RETIRO = "Retiro"
    RINCONADA = "Rinconada"
    RIO_BUENO = "Río Bueno"
    RIO_CLARO = "Río Claro"
    RIO_HURTADO = "Río Hurtado"
    RIO_IBANEZ = "Río Ibáñez"
    RIO_NEGRO = "Río Negro"
    RIO_VERDE = "Río Verde"
    ROMERAL = "Romeral"
    SAAVEDRA = "Saavedra"
    SAGRADA_FAMILIA = "Sagrada Familia"
    SALAMANCA = "Salamanca"
    SAN_ANTONIO = "San Antonio"
    SAN_BERNARDO = "San Bernardo"
    SAN_CARLOS = "San Carlos"
    SAN_CLEMENTE = "San Clemente"
    SAN_ESTEBAN = "San Esteban"
    SAN_FABIAN = "San Fabián"
    SAN_FELIPE = "San Felipe"
    SAN_FERNANDO = "San Fernando"
    SAN_GREGORIO = "San Gregorio"
    SAN_IGNACIO = "San Ignacio"
    SAN_JAVIER = "San Javier"
    SAN_JOAQUIN = "San Joaquín"
    SAN_JOSE_DE_MAIPO = "San José de Maipo"
    SAN_JUAN_DE_LA_COSTA = "San Juan de la Costa"
    SAN_MIGUEL = "San Miguel"
    SAN_NICOLAS = "San Nicolás"
    SAN_PABLO = "San Pablo"
    SAN_PEDRO = "San Pedro"
    SAN_PEDRO_DE_ATACAMA = "San Pedro de Atacama"
    SAN_PEDRO_DE_LA_PAZ = "San Pedro de la Paz"
    SAN_RAFAEL = "San Rafael"
    SAN_RAMON = "San Ramón"
    SAN_ROSENDO = "San Rosendo"
    SAN_VICENTE = "San Vicente"
    SANTA_BARBARA = "Santa Bárbara"
    SANTA_CRUZ = "Santa Cruz"
    SANTA_JUANA = "Santa Juana"
    SANTA_MARIA = "Santa María"
    SANTIAGO = "Santiago"
    SANTO_DOMINGO = "Santo Domingo"
    SIERRA_GORDA = "Sierra Gorda"
    TALAGANTE = "Talagante"
    TALCA = "Talca"
    TALCAHUANO = "Talcahuano"
    TALTAL = "Taltal"
    TEMUCO = "Temuco"
    TENO = "Teno"
    TEODORO_SCHMIDT = "Teodoro Schmidt"
    TIERRA_AMARILLA = "Tierra Amarilla"
    TILTIL = "Tiltil"
    TIMAUKEL = "Timaukel"
    TIRUA = "Tirúa"
    TOCOPILLA = "Tocopilla"
    TOLTEN = "Toltén"
    TOME = "Tomé"
    TORRES_DEL_PAINE = "Torres del Paine"
    TORTEL = "Tortel"
    TRAIGUEN = "Traiguén"
    TREGUACO = "Treguaco"
    TUCAPEL = "Tucapel"
    VALDIVIA = "Valdivia"
    VALLENAR = "Vallenar"
    VALPARAISO = "Valparaíso"
    VICHUQUEN = "Vichuquén"
    VICTORIA = "Victoria"
    VICUNA = "Vicuña"
    VILCUN = "Vilcún"
    VILLA_ALEGRE = "Villa Alegre"
    VILLA_ALEMANA = "Villa Alemana"
    VILLARRICA = "Villarrica"
    VINA_DEL_MAR = "Viña del Mar"
    VITACURA = "Vitacura"
    YERBAS_BUENAS = "Yerbas Buenas"
    YUMBEL = "Yumbel"
    YUNGAY = "Yungay"
    ZAPALLAR = "Zapallar"