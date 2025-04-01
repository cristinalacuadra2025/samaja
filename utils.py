import streamlit as st
import streamlit.components.v1 as components

def render_mermaid(diagram_code):
    """
    Renderiza un diagrama Mermaid en Streamlit.
    
    Args:
        diagram_code (str): Código del diagrama en sintaxis Mermaid
    """
    # HTML para renderizar Mermaid
    html = f"""
    <div class="mermaid">
    {diagram_code}
    </div>
    
    <script type="module">
      import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
      mermaid.initialize({{ startOnLoad: true, theme: 'default' }});
    </script>
    """
    
    # Renderizar HTML
    components.html(html, height=800)

# Diagrama general del proceso de investigación
DIAGRAMA_GENERAL = """
flowchart TD
    %% Definición de estilos sin colores
    classDef instancia fill:white,stroke:#333,stroke-width:2px
    classDef fase fill:white,stroke:#333,stroke-width:1px
    
    %% Nodo principal
    A[Proceso de Investigación Científica] --> B
    
    %% Instancias principales
    B[1. INSTANCIA DE VALIDACIÓN CONCEPTUAL] --> C
    B[1. INSTANCIA DE VALIDACIÓN CONCEPTUAL] --> D
    E[2. INSTANCIA DE VALIDACIÓN EMPÍRICA] --> F
    E[2. INSTANCIA DE VALIDACIÓN EMPÍRICA] --> G
    H[3. INSTANCIA DE VALIDACIÓN OPERATIVA] --> I
    H[3. INSTANCIA DE VALIDACIÓN OPERATIVA] --> J
    K[4. INSTANCIA DE VALIDACIÓN EXPOSITIVA] --> L
    K[4. INSTANCIA DE VALIDACIÓN EXPOSITIVA] --> M
    
    %% Fases
    C[Fase 1: Planteamientos] -->|Momentos a-d| C1{Examen de problemas<br>Conocimientos previos<br>Relaciones lógicas<br>Objetivos}
    D[Fase 2: Formulación] -->|Momentos a-d| D1{Hipótesis sustantivas<br>Marco teórico<br>Modelo del objeto<br>Consecuencias contrastables}
    
    F[Fase 3: Diseño del objeto] -->|Momentos a-d| F1[(Definición de<br>matriz de datos:<br>UA, V)]
    G[Fase 4: Diseño de procedimientos] -->|Momentos a-d| G1[(Operacionalización:<br>I, R)]
    
    I[Fase 5: Recolección y procesamiento] -->|Momentos a-d| I1[(Llenado de<br>matriz de datos)]
    J[Fase 6: Tratamiento y análisis] -->|Momentos a-d| J1[(Análisis de<br>matriz de datos)]
    
    L[Fase 7: Informes parciales] -->|Momentos a-d| L1>Comunicación<br>de avances]
    M[Fase 8: Exposición sistemática] -->|Momentos a-f| M1>Informe<br>final]
    
    %% Conexiones entre fases
    C1 --> D
    D1 --> E
    F1 --> G
    G1 --> H
    I1 --> J
    J1 --> K
    L1 --> M
    
    %% Aplicación de estilos
    class B,E,H,K instancia
    class C,D,F,G,I,J,L,M fase
    
    %% Leyenda
    Z1[Instancia de Validación] -.-> Z2[Fase]
    Z2 -.-> Z3{Momentos}
    Z3 -.-> Z4[(Matriz de Datos)]
    Z4 -.-> Z5>Informes]
"""

# Diagrama detallado de la Instancia de Validación Conceptual
DIAGRAMA_INSTANCIA_CONCEPTUAL = """
flowchart TD
    classDef instancia fill:#f0f8ff,stroke:#333,stroke-width:3px
    classDef fase fill:white,stroke:#666,stroke-width:2px
    classDef momento fill:white,stroke:#999,stroke-width:1px
    classDef decision fill:#f9f9f9,stroke:#333,stroke-width:1px
    
    A([INICIO: Instancia de Validación Conceptual]) --> B
    
    B{{INSTANCIA DE VALIDACIÓN CONCEPTUAL}}
    B --> |Validación de hipótesis sustantivas| C
    
    C[Fase 1: Planteamientos] 
    C --> |"Familiarización con el problema"| D{Examen y discusión<br>de los problemas}
    D --> E{Examen y discusión<br>de las hipótesis}
    E --> F{Apropiación y revisión<br>de conocimientos previos}
    F --> G{Revisión y discusión<br>sobre contextos}
    
    G --> H[Fase 2: Formulación]
    H --> |"Definiciones conceptuales"| I{Formulación del<br>problema central}
    I --> J{Formulación de<br>hipótesis sustantiva}
    J --> K{Explicitación de<br>relaciones lógicas}
    K --> L{Adopción y formulación<br>de objetivos}
    
    L --> M[(Matriz conceptual<br>de la investigación)]
    
    M --> N([FIN: Hacia Instancia de Validación Empírica])
    
    class B instancia
    class C,H fase
    class D,E,F,G,I,J,K,L decision
"""

# Diagrama detallado de la Instancia de Validación Empírica
DIAGRAMA_INSTANCIA_EMPIRICA = """
flowchart TD
    classDef instancia fill:#f0fff0,stroke:#333,stroke-width:3px
    classDef fase fill:white,stroke:#666,stroke-width:2px
    classDef momento fill:white,stroke:#999,stroke-width:1px
    classDef decision fill:#f9f9f9,stroke:#333,stroke-width:1px
    classDef data fill:#fff0f5,stroke:#666,stroke-width:1px
    
    A([INICIO: Instancia de Validación Empírica]) --> B
    
    B{{INSTANCIA DE VALIDACIÓN EMPÍRICA}}
    B --> |Validación de hipótesis indicadoras| C
    
    C[Fase 3: Diseño del objeto] 
    C --> |"Definición del objeto empírico"| D{Análisis de estructura<br>del objeto}
    D --> |"Unidades de análisis"| E{Análisis de hipótesis<br>y su estructura}
    E --> |"Variables"| F{Análisis de praxis<br>sobre el objeto}
    F --> |"Fuentes de datos"| G{Dimensionamiento<br>de variables}
    
    G --> |"Definiciones operacionales"| H[(Matriz de datos:<br>Unidades y Variables)]
    
    H --> I[Fase 4: Diseño de los procedimientos]
    I --> |"Procedimientos de medición"| J{Examen de<br>muestras posibles}
    J --> |"Técnicas de muestreo"| K{Examen de operaciones<br>para variables}
    K --> |"Plan de análisis"| L{Determinación de<br>recursos y contextos}
    L --> |"Plan de actividades"| M{Determinación de<br>procedimientos de indicadores}
    
    M --> |"Instrumentos"| N[(Matriz de datos:<br>Indicadores y Valores)]
    
    N --> O([FIN: Hacia Instancia de Validación Operativa])
    
    class B instancia
    class C,I fase
    class D,E,F,G,J,K,L,M decision
    class H,N data
"""

# Diagrama detallado de la Instancia de Validación Operativa
DIAGRAMA_INSTANCIA_OPERATIVA = """
flowchart TD
    classDef instancia fill:#fff0f5,stroke:#333,stroke-width:3px
    classDef fase fill:white,stroke:#666,stroke-width:2px
    classDef momento fill:white,stroke:#999,stroke-width:1px
    classDef decision fill:#f9f9f9,stroke:#333,stroke-width:1px
    classDef data fill:#f0f8ff,stroke:#666,stroke-width:1px
    classDef process fill:white,stroke:#666,stroke-width:1px
    
    A([INICIO: Instancia de Validación Operativa]) --> B
    
    B{{INSTANCIA DE VALIDACIÓN OPERATIVA}}
    B --> |Validación de hipótesis operativas| C
    
    C[Fase 5: Recolección y procesamiento] 
    C --> |"Ejecución de la recolección"| D[Realización de<br>pruebas piloto]
    D --> |"Pilotajes"| E[Recolección y registros<br>de información]
    E --> |"Recolección"| F[Procesamiento<br>de información]
    F --> |"Procesamientos"| G[Tabulación y<br>graficación]
    
    G --> |"Presentación de datos"| H[(Matriz de datos<br>completa)]
    
    H --> I[Fase 6: Tratamiento y análisis de datos]
    I --> |"Interpretación de datos"| J{Discusión y análisis<br>de resultados}
    J --> |"Verificación de hipótesis"| K[(Resultados<br>validados)]
    
    K --> L([FIN: Hacia Instancia de Validación Expositiva])
    
    class B instancia
    class C,I fase
    class D,E,F,G process
    class J decision
    class H,K data
"""

# Diagrama detallado de la Instancia de Validación Expositiva
DIAGRAMA_INSTANCIA_EXPOSITIVA = """
flowchart TD
    classDef instancia fill:#fffacd,stroke:#333,stroke-width:3px
    classDef fase fill:white,stroke:#666,stroke-width:2px
    classDef momento fill:white,stroke:#999,stroke-width:1px
    classDef decision fill:#f9f9f9,stroke:#333,stroke-width:1px
    classDef document fill:white,stroke:#666,stroke-width:1px,stroke-dasharray: 5 5
    
    A([INICIO: Instancia de Validación Expositiva]) --> B
    
    B{{INSTANCIA DE VALIDACIÓN EXPOSITIVA}}
    B --> |Validación de hipótesis retóricas| C
    
    C[Fase 7: Elaboración de informes parciales] 
    C --> |"Evaluación del proceso"| D[Examen y evaluación<br>del período]
    D --> |"Evaluación de lo actuado"| E[Análisis y evaluación<br>de resultados]
    E --> |"Ordenamiento de materiales"| F[Reconocimiento de<br>nuevos problemas]
    F --> |"Balance y perspectivas"| G>Informes<br>parciales]
    
    G --> H[Fase 8: Exposición de la investigación]
    H --> |"Presentación final"| I[Reconocimiento de<br>destinatarios]
    I --> |"Marco retórico"| J[Delimitación y<br>ordenamiento de tesis]
    J --> |"Preparación de tesis"| K[Desarrollo de<br>argumentos]
    K --> |"Validación de tesis"| L[Redacción y<br>presentación]
    
    L --> |"Exposición"| M>Informe Final<br>de Investigación]
    
    M --> N([FIN: Proceso de Investigación Completo])
    
    class B instancia
    class C,H fase
    class D,E,F,I,J,K,L momento
    class G,M document
"""
