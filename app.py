import streamlit as st
import streamlit.components.v1 as components

# Configuración de la página
st.set_page_config(
    page_title="Metodología de Investigación - Juan Samaja",
    page_icon="📊",
    layout="wide"
)

def render_mermaid(diagram_code):
    """
    Renderiza un diagrama Mermaid en Streamlit.
    Ajustamos las puntas de las flechas para que coincidan con el color de las líneas.
    """
    html = f"""
    <div class="mermaid">
    {diagram_code}
    </div>
    <script type="module">
      import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
      mermaid.initialize({{
        startOnLoad: true,
        theme: 'default',
        flowchart: {{
          arrowMarkerAbsolute: false,
          useMaxWidth: false,
          curve: 'basis'
        }},
        themeVariables: {{
          fontSize: '14px',
          lineColor: '#333', // Color de las líneas
          primaryColor: '#fff',
          primaryBorderColor: '#333',
          arrowheadColor: '#333' // Flechas del mismo color que las líneas
        }}
      }});
    </script>
    """
    components.html(html, height=600)

# Diagrama general del proceso de investigación
DIAGRAMA_GENERAL = """
flowchart TD
    %% Definición de estilos
    classDef instancia fill:#f0f8ff,stroke:#333,stroke-width:2px
    classDef fase fill:#f9f9f9,stroke:#666,stroke-width:1px
    classDef momento fill:#fff,stroke:#999,stroke-width:1px
    classDef decision fill:#f9f9f9,stroke:#333,stroke-width:1px
    classDef data fill:#fff0f5,stroke:#666,stroke-width:1px
    classDef document fill:#fff,stroke:#666,stroke-width:1px,stroke-dasharray: 5 5

    %% Nodo principal
    A[Proceso de Investigación Científica] --> B

    %% Instancias principales
    B[1. Instancia Conceptual] --> C[Fase 1: Planteamientos]
    B --> D[Fase 2: Formulación]
    E[2. Instancia Empírica] --> F[Fase 3: Diseño del Objeto]
    E --> G[Fase 4: Diseño de Procedimientos]
    H[3. Instancia Operativa] --> I[Fase 5: Recolección]
    H --> J[Fase 6: Análisis]
    K[4. Instancia Expositiva] --> L[Fase 7: Informes Parciales]
    K --> M[Fase 8: Informe Final]

    %% Conexiones entre fases
    C --> D
    D --> E
    F --> G
    G --> H
    I --> J
    J --> K
    L --> M

    %% Aplicación de estilos
    class B,E,H,K instancia
    class C,D,F,G,I,J,L,M fase
"""

# Función para mostrar la metodología
def mostrar_metodologia():
    st.header("Metodología de la Investigación Científica")
    st.subheader("Según Juan Samaja")
    st.markdown("""
    La metodología propuesta por Juan Samaja organiza el proceso de investigación científica
    en 4 instancias de validación, cada una con sus respectivas fases y momentos.
    """)

    # Selector de instancia de validación
    instancia = st.selectbox(
        "Seleccione una instancia de validación:",
        [
            "1. Instancia de Validación Conceptual",
            "2. Instancia de Validación Empírica",
            "3. Instancia de Validación Operativa",
            "4. Instancia de Validación Expositiva"
        ]
    )

    if instancia == "1. Instancia de Validación Conceptual":
        mostrar_instancia_conceptual()
    elif instancia == "2. Instancia de Validación Empírica":
        mostrar_instancia_empirica()
    elif instancia == "3. Instancia de Validación Operativa":
        mostrar_instancia_operativa()
    elif instancia == "4. Instancia de Validación Expositiva":
        mostrar_instancia_expositiva()

# Funciones para mostrar detalles de cada instancia
def mostrar_instancia_conceptual():
    st.subheader("1. Instancia de Validación Conceptual")
    tab1, tab2 = st.tabs(["Fase 1: Planteamientos", "Fase 2: Formulación"])
    with tab1:
        st.markdown("""
        ### Fase 1: Planteamientos
        Objetivo: Familiarizarse con el problema y justificar la importancia del estudio.
        #### Momentos:
        - Examen y discusión de los problemas.
        - Examen y discusión de las hipótesis.
        - Revisión de conocimientos previos.
        - Revisión de contextos materiales e institucionales.
        """)
    with tab2:
        st.markdown("""
        ### Fase 2: Formulación
        Objetivo: Lograr definiciones conceptuales y análisis de redes conceptuales.
        #### Momentos:
        - Formulación del problema central.
        - Formulación de la hipótesis sustantiva.
        - Explicitación de relaciones lógicas.
        - Adopción y formulación de objetivos.
        """)

def mostrar_instancia_empirica():
    st.subheader("2. Instancia de Validación Empírica")
    tab1, tab2 = st.tabs(["Fase 3: Diseño del Objeto", "Fase 4: Diseño de Procedimientos"])
    with tab1:
        st.markdown("""
        ### Fase 3: Diseño del Objeto
        Objetivo: Decidir el objeto empírico de la investigación.
        #### Momentos:
        - Análisis de la estructura del objeto.
        - Análisis de la hipótesis y su estructura.
        - Análisis de praxis sobre el objeto.
        - Dimensionamiento de variables.
        """)
    with tab2:
        st.markdown("""
        ### Fase 4: Diseño de Procedimientos
        Objetivo: Definir procedimientos para la recolección de datos.
        #### Momentos:
        - Examen de muestras posibles.
        - Examen de operaciones implicadas.
        - Determinación de recursos y contextos.
        - Diseño de instrumentos de medición.
        """)

def mostrar_instancia_operativa():
    st.subheader("3. Instancia de Validación Operativa")
    tab1, tab2 = st.tabs(["Fase 5: Recolección", "Fase 6: Análisis"])
    with tab1:
        st.markdown("""
        ### Fase 5: Recolección
        Objetivo: Realizar la recolección y procesamiento de datos.
        #### Momentos:
        - Realización de pruebas piloto.
        - Recolección de información.
        - Procesamiento de datos.
        - Tabulación y graficación.
        """)
    with tab2:
        st.markdown("""
        ### Fase 6: Análisis
        Objetivo: Analizar e interpretar los datos.
        #### Momentos:
        - Discusión de resultados.
        - Interpretación de datos.
        """)

def mostrar_instancia_expositiva():
    st.subheader("4. Instancia de Validación Expositiva")
    tab1, tab2 = st.tabs(["Fase 7: Informes Parciales", "Fase 8: Informe Final"])
    with tab1:
        st.markdown("""
        ### Fase 7: Informes Parciales
        Objetivo: Evaluar el período de investigación.
        #### Momentos:
        - Evaluación del período.
        - Análisis de resultados.
        - Reconocimiento de nuevos problemas.
        """)
    with tab2:
        st.markdown("""
        ### Fase 8: Informe Final
        Objetivo: Preparar y presentar el informe final.
        #### Momentos:
        - Reconocimiento de destinatarios.
        - Delimitación y ordenamiento de tesis.
        - Desarrollo de argumentos.
        - Redacción y exposición.
        """)

# Menú principal
opcion = st.sidebar.selectbox(
    "Menú",
    ["Inicio", "Diagrama General", "Metodología"]
)

if opcion == "Inicio":
    st.title("Bienvenido a la Metodología de Juan Samaja")
    st.markdown("""
    Esta aplicación te guiará a través de las **cuatro instancias de validación** 
    propuestas por Juan Samaja para el proceso de investigación científica.
    """)

elif opcion == "Diagrama General":
    st.subheader("Diagrama General del Proceso de Investigación")
    render_mermaid(DIAGRAMA_GENERAL)

elif opcion == "Metodología":
    mostrar_metodologia()