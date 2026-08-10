# Pensiones AFP — Impacto de la educación en el monto de jubilación

Proyecto de análisis de datos que explora la relación entre los años de educación y el monto de la jubilación pagado por las Administradoras de Fondos de Pensiones (AFP) en Chile, utilizando datos de la **Encuesta CASEN 2022**.

## Objetivo

Responder a la pregunta: **¿existe una relación significativa entre el nivel educacional de los jubilados y el monto de sus jubilaciones entregadas por las AFP?**

Se contrasta la hipótesis mediante cinco modelos de regresión lineal (simple y múltiple), incorporando variables de control como sexo, área (urbana/rural) y sus interacciones con la escolaridad.

## Fuentes de datos

| Fuente | Descripción |
|---|---|
| Encuesta CASEN 2022 | Caracterización socioeconómica de hogares y personas (Ministerio de Desarrollo Social y Familia) |

## Estructura del proyecto

```
├── data/
│   ├── raw/            # Datos originales sin procesar (Excel)
│   └── processed/      # Datos limpios, listos para análisis
├── notebooks/
│   └── Casen_2022_excel.ipynb   # Análisis exploratorio y modelos de regresión
├── src/
│   └── transformers.py # Funciones de limpieza y transformación de datos
├── main.py              # Punto de entrada del pipeline
├── requirements.txt      # Dependencias del proyecto
└── README.md
```

## Pipeline de datos

El procesamiento de datos está separado del análisis exploratorio, siguiendo un enfoque de ingeniería de datos:

1. **`src/transformers.py`** contiene `procesar_afp()`, que carga `data/raw/datos_analisis.xlsx`, filtra registros inválidos (código `-88` en `y7`) y genera variables dicotómicas (`sexo_dic`, `area_dic`).
2. **`main.py`** orquesta el pipeline: llama a `procesar_afp()` y guarda el resultado en `data/processed/` mediante `guardar_procesado()`.
3. **`notebooks/Casen_2022_excel.ipynb`** consume los datos ya procesados (importando directamente `procesar_afp()` desde `src`) para el análisis exploratorio y los modelos de regresión — no repite lógica de limpieza.

## Cómo ejecutar el pipeline

```bash
# 1. Clonar el repositorio
git clone <url-del-repositorio>
cd pensiones

# 2. Crear entorno virtual e instalar dependencias
python -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate
pip install -r requirements.txt

# 3. Correr el pipeline
python main.py
```

Esto genera `data/processed/datos_procesados.xlsx`. Luego, para explorar el análisis:

```bash
jupyter notebook notebooks/Casen_2022_excel.ipynb
```

## Variables principales

| Variable | Descripción | Tipo |
|---|---|---|
| `esc` | Años de escolaridad | Discreta |
| `y2803c` | Jubilación o pensión de vejez corregida | Continua |
| `sexo` | Sexo (1 = hombre, 2 = mujer) | Categórica dicotómica |
| `area` | Área urbana/rural | Categórica dicotómica |
| `region` | Región de residencia | Categórica |
| `edad` | Edad | Discreta |

## Metodología

Se ajustan cinco modelos mediante `statsmodels.OLS`:

1. Regresión simple agrupada por región
2. Regresión simple sobre la muestra total
3. Regresión múltiple con sexo e interacción sexo × escolaridad
4. Regresión múltiple solo con interacción sexo × escolaridad
5. Regresión múltiple con interacción área × escolaridad

Los resultados se comparan mediante una tabla `Stargazer` y se evalúan según significancia estadística (valor p), R² ajustado, AIC y BIC.

## Principales hallazgos

- La escolaridad tiene un efecto positivo y significativo sobre el monto de la jubilación en todos los modelos.
- La interacción entre escolaridad y sexo es negativa: a igual nivel educativo, el retorno de la escolaridad sobre el monto de jubilación es menor para las mujeres que para los hombres.

## Próximos pasos

- Incorporar variables previsionales adicionales (años de cotización).
- Automatizar la generación de gráficos y tabla comparativa de modelos dentro del pipeline.
- Agregar pruebas unitarias para `src/transformers.py`.

## Fuentes / Bibliografía

- Asociación de AFP Chile — https://www.aafp.cl/
- Superintendencia de Pensiones — https://www.spensiones.cl/
- Ministerio de Desarrollo Social y Familia, Encuesta CASEN 2022 — https://observatorio.ministeriodesarrollosocial.gob.cl/encuesta-casen-2022# Pensiones-AFP
