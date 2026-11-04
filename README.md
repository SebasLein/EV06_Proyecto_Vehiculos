# EV06 - Diagnóstico de calidad de datos

# Proyecto: Analítica para Vehículos Eléctricos (EV06)

**Autor:** Sebastian Lein Castro Grajales - Análisis y Desarrollo de Software (SENA)

## Descripción

Diagnóstico inicial de calidad de datos para predecir la degradación de baterías de litio y evaluar el consumo de estaciones de carga eléctrica.

## Estructura del Repositorio

- `data/raw/`: Datasets originales (.csv).
- `notebooks/`: Cuaderno de Jupyter (`diagnostico_calidad.ipynb`) con el código de exploración en Pandas.
- `reports/`: Informe técnico de hallazgos (`informe_diagnostico.md`).
- `requirements.txt`: Dependencias del entorno virtual.

## Cómo reproducir este diagnóstico

1. Clona el repositorio.
2. Crea un entorno virtual: `python -m venv .venv`
3. Activa el entorno e instala dependencias: `pip install -r requirements.txt`
4. Ejecuta JupyterLab: `jupyter lab` y abre la carpeta `notebooks/`.
