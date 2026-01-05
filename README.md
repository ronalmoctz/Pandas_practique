# 💻 Laptops Data Analysis Project

[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)](https://python.org)
[![Pandas](https://img.shields.io/badge/Pandas-Latest-green?style=flat-square&logo=pandas)](https://pandas.pydata.org)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)](README.md)

---

## 📌 Descripción del Proyecto

Análisis y limpieza de datos de laptops usando **Python y pandas** para demostrar habilidades prácticas de Data Wrangling y ETL. Ideal para portafolios de trabajo.

### Objetivos Principales
- ✅ Limpieza y transformación de datos reales
- ✅ Manejo de duplicados y valores faltantes
- ✅ Análisis exploratorio: agrupación, ordenamiento, filtrado
- ✅ Código reproducible y documentado
- ✅ Ejemplos listos para entrevistas técnicas

---

## 🛠️ Tech Stack

| Tecnología | Descripción |
|-----------|------------|
| **Python** 🐍 | Lenguaje base |
| **Pandas** 📊 | Manipulación y análisis de datos |
| **Jupyter Notebook** 📓 | Análisis exploratorio interactivo |
| **Git** 🔀 | Control de versiones |

---

## 📂 Estructura del Proyecto

```
Pandas_practique/
├── 📄 README.md                          # Este archivo
├── 📄 pyproject.toml                     # Configuración del proyecto
├── 📄 test.py                            # Scripts de prueba
├── 📓 heart_failure.ipynb                # Análisis dataset corazón
├── 📓 laptop_dataset.ipynb               # Análisis dataset laptops
│
└── 📁 dataset/
    ├── laptop_price.csv                  # 💾 Dataset principal (laptops)
    ├── heart_failure_clinical_records_dataset.csv
    └── players_20.csv
```

---

## 🚀 Quick Start

### Requisitos Previos
- Python 3.8+
- pip o uv

### Instalación

**1️⃣ Clonar/descargar el repositorio**
```bash
git clone https://github.com/tu-usuario/Pandas_practique.git
cd Pandas_practique
```

**2️⃣ Crear entorno virtual**
```bash
python -m venv .venv
```

**3️⃣ Activar entorno**
```bash
# Windows
.\.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

**4️⃣ Instalar dependencias**
```bash
pip install -r requirements.txt
# o
uv sync  # si usas uv (más rápido)
```

**5️⃣ Ejecutar notebooks o scripts**
```bash
jupyter notebook laptop_dataset.ipynb
# o
python test.py
```

---

## 📚 Conceptos Clave Aprendidos

### 1. Manejo de Duplicados
```python
# Identificar duplicados
dupli_last = df.duplicated('Company', keep='last')

# Eliminar duplicados
df.drop_duplicates(['Company'], keep='first')
```

> ⚠️ **NOTA IMPORTANTE:** `keep='last'` y `keep='first'` respetan el **orden actual** del DataFrame. Para ordenar por **valor** (ej: precio máximo), debes **ordenar primero** con `sort_values()`.

### 2. Seleccionar Precio Máximo/Mínimo por Grupo
```python
# Más caro por compañía
max_price = df.sort_values(['Company', 'Price_euros'], 
                           ascending=[True, False]) \
             .drop_duplicates('Company', keep='first') \
             [['Company', 'Price_euros']]

# Más barato por compañía
min_price = df.sort_values(['Company', 'Price_euros'], 
                           ascending=[True, True]) \
             .drop_duplicates('Company', keep='first') \
             [['Company', 'Price_euros']]
```

### 3. Alternativa con GroupBy (Más Eficiente) ⭐
```python
# Obtener índice del máximo por grupo
idx = df.groupby('Company')['Price_euros'].idxmax()
most_expensive = df.loc[idx][['Company', 'Price_euros']]

# Obtener índice del mínimo por grupo
idx = df.groupby('Company')['Price_euros'].idxmin()
cheapest = df.loc[idx][['Company', 'Price_euros']]
```

---

## 🎯 Ejemplo Práctico Completo

### Problema
Extraer la laptop **más cara** de cada compañía, manteniendo datos ordenados.

### Solución (2 métodos)

### Método A: Sort + Drop Duplicates ✨
```python
import pandas as pd

df = pd.read_csv('dataset/laptop_price.csv')

# Ordenar por compañía (A-Z) y precio (mayor-menor)
# Luego tomar la primera = la más cara
most_expensive = (
    df.sort_values(['Company', 'Price_euros'], 
                   ascending=[True, False])
      .drop_duplicates(subset='Company', keep='first')
      .reset_index(drop=True)
      [['Company', 'Price_euros']]
)

print(most_expensive)
```

**Ventajas:**
- 👍 Muy legible y fácil de entender
- 👍 Ideal para explicar en entrevistas

---

### Método B: GroupBy + idxmax ⚡
```python
import pandas as pd

df = pd.read_csv('dataset/laptop_price.csv')

# Obtener índice de máximo precio por compañía
idx = df.groupby('Company')['Price_euros'].idxmax()

# Seleccionar esas filas y ordenar
most_expensive = (
    df.loc[idx]
      .sort_values('Company')
      .reset_index(drop=True)
      [['Company', 'Price_euros']]
)

print(most_expensive)
```

**Ventajas:**
- ⚡ Más rápido en datasets grandes (millones de filas)
- 🎯 Más explícito en intención

---

## Salida Esperada
```
      Company  Price_euros
0        ASUS          1500
1         Dell          1800
2          HP          1200
...
```

---

## ⚙️ Habilidades Técnicas Demostradas

| Habilidad | Descripción |
|-----------|------------|
| 🔄 **ETL** | Extracción, transformación y carga de datos |
| 📊 **EDA** | Análisis exploratorio de datos |
| 🧹 **Data Cleaning** | Manejo de duplicados, nulos, outliers |
| 🔍 **Grouping & Aggregation** | `groupby()`, `agg()`, `pivot_table()` |
| 📈 **Sorting & Filtering** | `sort_values()`, `query()`, `loc[]`, `iloc[]` |
| 📝 **Documentación** | Código limpio, README profesional |

---

## 💡 Tips para Entrevistas Técnicas

### ❓ Pregunta típica: "¿Cuál es la diferencia entre `drop_duplicates(..., keep='last')` y `groupby().idxmax()`?"

**Respuesta profesional:**

| Aspecto | `drop_duplicates` | `groupby().idxmax()` |
|--------|-------------------|-------------------|
| **Orden** | Respeta orden actual del DF | Define orden explícitamente |
| **Valor** | Requiere sort previo | Busca máximo automáticamente |
| **Velocidad** | O(n log n) | O(n) |
| **Legibilidad** | Más intuitivo | Más explícito |
| **Caso de uso** | Datos pequeños-medianos | Datasets masivos |

**Conclusión:**
- `keep='last'` respeta el **orden actual** del DataFrame
- Para obtener el valor máximo, **siempre ordena primero** por esa columna
- `groupby().idxmax()` es más **eficiente** y **explícito** en intención

---

### ❓ Pregunta: "¿Cómo manejaste los datos duplicados?"

**Estructura de respuesta:**
```
1. ✅ Identifiqué duplicados con df.duplicated()
2. ✅ Analicé qué fila mantener (estrategia: más caro, más reciente, etc.)
3. ✅ Apliqué drop_duplicates() con keep= apropiado
4. ✅ Validé con .shape y sample() después
5. ✅ Generé reportes de limpieza (ej: "Eliminé 250 duplicados de 5000 filas")
```

---

## 📖 Recursos Útiles

- 🔗 [Pandas Documentation](https://pandas.pydata.org/docs/)
- 🔗 [Real Python - Pandas Tutorials](https://realpython.com/learning-paths/pandas-data-science/)
- 🔗 [DataCamp - Data Cleaning](https://www.datacamp.com)
- 🔗 [Kaggle Datasets](https://www.kaggle.com/datasets)

---

## 🤝 Contribuciones

Este es un proyecto de aprendizaje. Sugerencias y mejoras son bienvenidas.

---

## 📧 Contacto & Links

- **Email:** tu-email@gmail.com
- **LinkedIn:** [linkedin.com/in/tu-perfil](https://linkedin.com)
- **GitHub:** [github.com/tu-usuario](https://github.com)
- **Portfolio:** [tu-sitio.com](https://tu-sitio.com)

---

## ⭐ Si te fue útil, ¡no olvides dejar una estrella!

```
⭐⭐⭐⭐⭐  Star this repo si aprendiste algo nuevo
```

---

**Última actualización:** Enero 2026 | **Estado:** 🟢 Activo | **Version:** 2.0

