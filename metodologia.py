import streamlit as st

def mostrar_metodologia():
    st.header("Metodología de la Investigación Científica")
    st.subheader("Según Juan Samaja")
    
    # Descripción general
    st.markdown("""
    La metodología propuesta por Juan Samaja organiza el proceso de investigación científica
    en 4 instancias de validación, cada una con sus respectivas fases y momentos.
    """)
    
    # Selector de instancia de validación
    instancia = st.selectbox(
        "Seleccione una instancia de validación:",
        ["1. Instancia de Validación Conceptual", 
         "2. Instancia de Validación Empírica",
         "3. Instancia de Validación Operativa",
         "4. Instancia de Validación Expositiva"]
    )
    
    # Contenido según la instancia seleccionada
    if instancia == "1. Instancia de Validación Conceptual":
        mostrar_instancia_conceptual()
    elif instancia == "2. Instancia de Validación Empírica":
        mostrar_instancia_empirica()
    elif instancia == "3. Instancia de Validación Operativa":
        mostrar_instancia_operativa()
    elif instancia == "4. Instancia de Validación Expositiva":
        mostrar_instancia_expositiva()

def mostrar_instancia_conceptual():
    st.subheader("1. Instancia de Validación Conceptual")
    
    st.markdown("""
    Esta instancia se enfoca en la validación de las hipótesis sustantivas por referencia a las teorías 
    y hechos que se consideran bien establecidos.
    """)
    
    # Pestañas para las fases
    tab1, tab2 = st.tabs(["Fase 1: Planteamientos", "Fase 2: Formulación"])
    
    with tab1:
        st.markdown("""
        ### Fase 1: Planteamientos
        
        El objeto general de esta fase es familiarizarse lo más que se pueda y profundizar el conocimiento 
        del proceso en el que se presenta el problema, además de confirmar el interés o importancia de 
        dicho proceso a fin de justificar el esfuerzo de investigación que se propone emprender.
        
        #### Momentos:
        
        * **Examen y discusión de los problemas** (el problema central y los problemas conexos)
        * **Examen y discusión de las hipótesis** que evocan los problemas
        * **Apropiación y revisión de los conocimientos previos**, propios o análogos (tanto de carácter teórico, cuanto de hechos científicamente establecidos)
        * **Revisión y discusión sobre los contextos materiales e institucionales** de los problemas (deliberaciones sobre el interés, la justificabilidad y el impacto que puede llegar a tener si se alcanzaran resultados positivos)
        """)
        
    with tab2:
        st.markdown("""
        ### Fase 2: Formulación
        
        El objeto central de la fase formulativa es el de lograr las definiciones conceptuales y los análisis 
        de las estructuras de las redes conceptuales implícitas en el problema, en las hipótesis, en el marco 
        teórico y en los objetivos.
        
        #### Momentos:
        
        * **Formulación del problema central** y los problemas conexos de la investigación
        * **Formulación de la hipótesis sustantiva** y de las principales hipótesis de trabajo, es decir, explicitación de las principales categorías puestas en juego y del tipo de conexiones o vínculos que se predican entre ellas
        * **Explicitación de las relaciones lógicas** implícitas en los conocimientos previos, específicos o de las analogías ("Marco referencial" o "Marco teórico")
        * **Adopción y formulación de los objetivos**
        """)

def mostrar_instancia_empirica():
    st.subheader("2. Instancia de Validación Empírica")
    
    st.markdown("""
    Esta instancia se encarga de validar las hipótesis instrumentales o indicadoras, lo que 
    tradicionalmente se conoce como "establecer la validez de los datos".
    """)
    
    # Pestañas para las fases
    tab1, tab2 = st.tabs(["Fase 3: Diseño del objeto", "Fase 4: Diseño de los procedimientos"])
    
    with tab1:
        st.markdown("""
        ### Fase 3: Diseño del objeto
        
        Esta fase empieza a poner en juego la segunda instancia de validación. El objeto general de esta fase 
        es decidir cuál será el objeto empírico de la investigación. Esto quiere decir: escoger los tipos de 
        unidades de análisis, las variables y las fuentes que se emplearán en el estudio.
        
        #### Momentos:
        
        * **Análisis de la estructura del objeto** de la investigación y de sus diversos niveles de integración; traducción de estas poblaciones "teóricamente posibles" a universos de unidades de análisis bien delimitados ("Universos")
        * **Análisis de la hipótesis y de su estructura** (de sus componentes y relaciones); traducción de estos "espacios de atributos, teóricamente posibles" a universos de variables, bien delimitados ("Universo de variables" o "Espacio de atributos")
        * **Análisis de las praxis sobre el objeto y disponibilidad** o accesibilidad a las fuentes de datos que esta praxis genera; incluye un primer examen de las hipótesis de validez que se pondrán en juego ("Fuentes de datos")
        * **Dimensionamiento de las variables** y análisis de la relevancia de las dimensiones encontradas, a fin de establecer criterios de validez, para definirlas operacionalmente ("Definiciones operacionales")
        """)
        
    with tab2:
        st.markdown("""
        ### Fase 4: Diseño de los procedimientos
        
        Esta fase tiene como objeto la toma de decisiones acerca de los procedimientos mediante los que se 
        determinarán en cada caso las unidades de análisis que se someterán a estudio; las dimensiones y 
        procedimientos que se aplicarán para ubicarlas en las respectivas categorías de las variables y 
        el tratamiento que se les dará a posteriori de la recolección.
        
        #### Momentos:
        
        * **Examen de las muestras posibles**; determinación del tamaño y de las técnicas de muestreo, conforme a los objetivos de la investigación ("Muestreo")
        * **Examen de las operaciones implicadas** en la reconstrucción de las variables y de las relaciones de cada variable con las restantes, según las hipótesis sustantivas, a fin de establecer el plan de tratamiento y análisis de los datos ("Plan de tratamiento y análisis")
        * **Determinación precisa de los recursos y contextos** de aplicación de los instrumentos de medición (determinación de tiempos, espacios y demás recursos de ejecución) (Se incluyen diseños de pruebas de confiabilidad) ("Plan de actividades en los contextos")
        * **Determinación precisa de los procedimientos de los indicadores**, y diseño y construcción de los instrumentos con los que se producirán y registrarán los datos (por ejemplo: cédula de encuesta, planillas de observaciones, cuestionarios, fichas clínicas o epidemiológicas. Se incluyen diseños de las pruebas de validez.) ("Instrumentos de medición")
        """)

def mostrar_instancia_operativa():
    st.subheader("3. Instancia de Validación Operativa")
    
    st.markdown("""
    Esta instancia está encargada de validar las hipótesis operativas o de generalización, lo que 
    tradicionalmente se conoce como "establecer la confiabilidad de los datos y la confiabilidad 
    de la muestra".
    """)
    
    # Pestañas para las fases
    tab1, tab2 = st.tabs(["Fase 5: Recolección y procesamiento", "Fase 6: Tratamiento y análisis de datos"])
    
    with tab1:
        st.markdown("""
        ### Fase 5: Recolección y procesamiento
        
        Esta fase tiene como objetivo llevar a cabo la recolección de los datos y su procesamiento. Como 
        se ha dicho anteriormente, estos momentos forman parte de la instancia de la "validación operativa", 
        puesto que el investigador deberá poder justificar la forma cómo ha procedido realmente para 
        seleccionar cada sujeto de estudio, y la manera concreta cómo ha efectuado las mediciones es 
        conforme al criterio de confiabilidad.
        
        #### Momentos:
        
        * **Realización de pruebas piloto** y demás controles del plan de actividades ("Pilotajes"; incluye la ejecución de las pruebas de confiabilidad)
        * **Recolección, registros y controles** de la información en terreno, laboratorio o gabinete ("Recolección")
        * **Procesamiento de la información** (cómputos y demás operaciones de síntesis conforme al plan, tratamiento y análisis de datos). (Se incluye la ejecución de las pruebas de validez) ("Procesamientos")
        * **Tabulación, graficación y otras formas** de presentaciones resumidas de los datos procesados para su discusión y análisis ("Tabulación y Graficación")
        """)
        
    with tab2:
        st.markdown("""
        ### Fase 6: Tratamiento y análisis de datos
        
        Esta fase tiene como objeto la discusión y la interpretación de los datos a la luz del plan de 
        análisis y de las hipótesis formuladas (tanto hipótesis sustantivas, cuanto de las hipótesis 
        de validez y de generalización).
        
        #### Momentos:
        
        * **Discusión y análisis** de lo que se observa en las tablas, gráficos y demás instrumentos de presentación de datos ("Lectura de resultados"; incluye la revisión de los resultados a la luz de las hipótesis de validez y de generalización)
        """)

def mostrar_instancia_expositiva():
    st.subheader("4. Instancia de Validación Expositiva")
    
    st.markdown("""
    Esta instancia está encargada de validar las hipótesis retóricas, esto es, el esquema expositivo 
    y la estrategia de argumentación o de exposición demostrativa.
    """)
    
    # Pestañas para las fases
    tab1, tab2 = st.tabs(["Fase 7: Elaboración de informes parciales", "Fase 8: Exposición de la investigación"])
    
    with tab1:
        st.markdown("""
        ### Fase 7: Elaboración de informes parciales
        
        El objeto es la evaluación del período o tramo del proceso de investigación que se informa por 
        referencia al plan de actividades y a las metas trazadas.
        
        #### Momentos:
        
        * **Examen y evaluación del período** o tramo del proceso de investigación que se informa por referencia al plan de actividades y a las metas trazadas ("Evaluación de lo actuado")
        * **Análisis y evaluación de los resultados** que se han logrado, de los materiales ya escritos, selección y ordenamiento de las tablas, gráficos y otros resúmenes más significativos ("Ordenamiento de los materiales")
        * **Reconocimiento y examen de los nuevos problemas** que los resultados han dejado planteados, y revisión de los nuevos diseños que se deducen de los exámenes anteriores ("Balance y perspectivas")
        """)
        
    with tab2:
        st.markdown("""
        ### Fase 8: Exposición de la investigación: el informe final
        
        El objeto es la preparación y presentación del informe final de la investigación a los 
        destinatarios relevantes.
        
        #### Momentos:
        
        * **Reconocimiento y valoración de los destinatarios** posibles de la exposición (relevamiento de adversarios y jueces). Selección de destinatarios particulares ("Marco retórico")
        * **Delimitación, análisis y ordenamiento** de la tesis que se quiere presentar. Elección de tesis adversarias y evaluación de ordenamientos posibles ("Preparación de la tesis")
        * **Desarrollo de los argumentos** destinados a:
            * Validar conceptualmente las tesis (selección de referencias y explicitación de deudas intelectuales). (incluye control de citas y paráfrasis)
            * Validar empíricamente las tesis (presentación de los datos y su procesamiento)
            * Validar operativamente las tesis (discusión de la validez y confiabilidad de los datos)
        * **Redacción y presentación** del informe final ("Exposición")
        """)
