# 📊 Sistema de Control de Horas y Sobretiempo

Este proyecto consiste en un programa desarrollado en **Python** diseñado para gestionar, calcular y clasificar las horas laborales semanales de un equipo de trabajo mediante el uso de estructuras bidimensionales (matrices) y programación modular (funciones).

## 📋 Descripción del Problema
El programa procesa una matriz donde cada fila representa a un miembro del equipo y registra su nombre junto a las horas trabajadas de Lunes a Viernes. El sistema calcula automáticamente el total de horas acumuladas y determina si el recurso excedió el umbral legal de 40 horas semanales.

### Lógica de Negocio:
* **Horario Estándar:** Total de horas semanales $\le$ 40 horas.
* **Sobretiempo:** Total de horas semanales $>$ 40 horas.

---

## 🛠️ Requerimientos del Sistema (Estructura de Requisitos)

| Identificación | Descripción | Entradas | Resultados o salidas |
| :--- | :--- | :--- | :--- |
| **RF1: Matriz de Datos** | Estructurar una matriz ($4 \times 6$) para registrar nombres y horas diarias. | Datos predefinidos de lunes a viernes. | Matriz cargada en memoria. |
| **RF2: Cálculo de Horas** | Módulo que extrae las horas mediante *slicing* y realiza la sumatoria. | Lista con las 5 horas diarias de un recurso. | Valor numérico del total de horas. |
| **RF3: Clasificación** | Evaluar mediante lógica condicional si se supera el umbral de 40 horas. | Total de horas semanales (RF2). | Texto: "Sobretiempo" o "Horario Estándar". |
| **RF4: Reporte General** | Recorrer la matriz e imprimir el informe con formato tabular en consola. | Resultados procesados de todo el equipo. | Tabla organizada impresa en pantalla. |

---

## 🚀 Instrucciones de Ejecución

Para ejecutar este programa localmente, asegúrate de tener instalado Python 3 y sigue estos pasos:

1. Clona este repositorio o descarga el archivo `main.py`.
2. Abre la terminal o consola de comandos en la carpeta del archivo.
3. Ejecuta el siguiente comando:
   ```bash
   python main.py

============================================================
RECURSO         | HORAS TOTALES | CLASIFICACIÓN  
============================================================
Ana Gómez       | 40            | Horario Estándar
Carlos Ruiz     | 44            | Sobretiempo    
Sofía Pérez     | 35            | Horario Estándar
David Lyon      | 42            | Sobretiempo    
============================================================
