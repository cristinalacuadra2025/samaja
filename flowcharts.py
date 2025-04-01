import streamlit as st
from utils import (
    render_mermaid, 
    DIAGRAMA_GENERAL, 
    DIAGRAMA_INSTANCIA_CONCEPTUAL, 
    DIAGRAMA_INSTANCIA_EMPIRICA, 
    DIAGRAMA_INSTANCIA_OPERATIVA, 
    DIAGRAMA_INSTANCIA_EXPOSITIVA
)

def mostrar_diagramas():
    st.header("Diagramas de Flujo (Flowcharts)")
    st.subheader("Basados en la norma ISO 5807:1985")
    
    # Descripción
    st.markdown("""
    Los siguientes diagramas representan visualmente la metodología de investigación científica
    propuesta por Juan Samaja, utilizando símbolos similares a los establecidos en la norma 
    ISO 5807:1985.
    
    Cada diagrama se ha implementado utilizando la sintaxis de Mermaid, una biblioteca para
    la generación de diagramas a partir de texto.
    """)
    
    # Selector de diagrama
    tipo_diagrama = st.radio(
        "Seleccione un diagrama:",
        ["Diagrama General", 
         "Instancia de Validación Conceptual", 
         "Instancia de Validación Empírica", 
         "Instancia de Validación Operativa", 
         "Instancia de Validación Expositiva"]
    )
    
    # Mostrar diagrama seleccionado
    if tipo_diagrama == "Diagrama General":
        mostrar_diagrama_general()
    elif tipo_diagrama == "Instancia de Validación Conceptual":
        mostrar_diagrama_conceptual()
    elif tipo_diagrama == "Instancia de Validación Empírica":
        mostrar_diagrama_empirico()
    elif tipo_diagrama == "Instancia de Validación Operativa":
        mostrar_diagrama_operativo()
    elif tipo_diagrama == "Instancia de Validación Expositiva":
        mostrar_diagrama_expositivo()
    
    # Opción para mostrar código Mermaid
    with st.expander("Ver código Mermaid"):
        if tipo_diagrama == "Diagrama General":
            st.code(DIAGRAMA_GENERAL, language="text")
        elif tipo_diagrama == "Instancia de Validación Conceptual":
            st.code(DIAGRAMA_INSTANCIA_CONCEPTUAL, language="text")
        elif tipo_diagrama == "Instancia de Validación Empírica":
            st.code(DIAGRAMA_INSTANCIA_EMPIRICA, language="text")
        elif tipo_diagrama == "Instancia de Validación Operativa":
            st.code(DIAGRAMA_INSTANCIA_OPERATIVA, language="text")
        elif tipo_diagrama == "Instancia de Validación Expositiva":
            st.code(DIAGRAMA_INSTANCIA_EXPOSITIVA, language="text")

def mostrar_diagrama_general():
    st.subheader("Diagrama General del Proceso de Investigación Científica")
    
    st.markdown("""
    Este diagrama muestra la estructura completa del proceso de investigación científica según
    Juan Samaja, con sus cuatro instancias de validación y ocho fases.
    
    #### Leyenda de símbolos ISO 5807:
    
    * **Proceso (rectángulo)**: Representa una fase o actividad
    * **Decisión (rombo)**: Representa un momento de evaluación o selección
    * **Datos (cilindro)**: Representa una matriz de datos o información
    * **Documento (rectángulo con ondulación)**: Representa informes o documentos
    * **Terminal (rectángulo redondeado)**: Representa inicio o fin de proceso
    * **Conector (círculo)**: Conecta flujos de proceso
    """)
    
    render_mermaid(DIAGRAMA_GENERAL)

def mostrar_diagrama_conceptual():
    st.subheader("Diagrama de la Instancia de Validación Conceptual")
    
    st.markdown("""
    Este diagrama detalla las fases y momentos de la Instancia de Validación Conceptual,
    que incluye las fases de Planteamientos y Formulación.
    """)
    
    render_mermaid(DIAGRAMA_INSTANCIA_CONCEPTUAL)

def mostrar_diagrama_empirico():
    st.subheader("Diagrama de la Instancia de Validación Empírica")
    
    st.markdown("""
    Este diagrama detalla las fases y momentos de la Instancia de Validación Empírica,
    que incluye las fases de Diseño del objeto y Diseño de los procedimientos.
    """)
    
    render_mermaid(DIAGRAMA_INSTANCIA_EMPIRICA)

def mostrar_diagrama_operativo():
    st.subheader("Diagrama de la Instancia de Validación Operativa")
    
    st.markdown("""
    Este diagrama detalla las fases y momentos de la Instancia de Validación Operativa,
    que incluye las fases de Recolección y procesamiento y Tratamiento y análisis de datos.
    """)
    
    render_mermaid(DIAGRAMA_INSTANCIA_OPERATIVA)

def mostrar_diagrama_expositivo():
    st.subheader("Diagrama de la Instancia de Validación Expositiva")
    
    st.markdown("""
    Este diagrama detalla las fases y momentos de la Instancia de Validación Expositiva,
    que incluye las fases de Elaboración de informes parciales y Exposición de la investigación.
    """)
    
    render_mermaid(DIAGRAMA_INSTANCIA_EXPOSITIVA)
