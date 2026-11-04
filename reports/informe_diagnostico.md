# Informe de Diagnóstico de Calidad de Datos

**Proyecto:** Optimización del Mantenimiento Predictivo y Consumo Energético en Flotas de Vehículos Eléctricos e Híbridos.

## 1. Descripción de los Datasets

- **ev_battery_kaggle.csv (1000 filas, 5 columnas):** Datos de telemetría de celdas de litio, ciclos y temperatura.
- **estaciones_carga_colombia.csv (500 filas, 5 columnas):** Registros de demanda energética en la infraestructura nacional.

## 2. Hallazgos Principales de Calidad

Ambos conjuntos presentan un nivel de madurez "Crudo" (Raw). Se evidencian tres tipos de problemas estructurales:

1. **Contaminación de tipos:** Textos inyectados en métricas continuas (ej. "%" en SoH y "Sin lectura" en kWh) forzaron las variables a tipo `object`.
2. **Valores ausentes (NaNs):** Fallas de reporte en telemetría de temperatura (16 registros) y omisiones administrativas en el operador (51 registros).
3. **Errores de captura:** Presencia de números negativos incompatibles con la física (-500 ciclos) y errores de digitación en variables categóricas espaciales ("Medelín").

## 3. Conclusiones y Viabilidad

Los datos **no están listos** para la fase de modelado predictivo o entrenamiento algorítmico. Se requiere diseñar un _Pipeline_ (tubería) de limpieza en Pandas que estandarice los _dtypes_, trate los valores nulos (mediante imputación estadística o descarte) y corrija las inconsistencias detectadas. Una vez ejecutada esta limpieza, el proyecto será viable.
