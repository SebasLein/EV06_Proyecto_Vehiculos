import pandas as pd
import numpy as np

# --- 1. Generar Dataset 1: Baterías EV (Kaggle) ---
np.random.seed(42)
baterias_data = {
    'bateria_id': [f'BAT_{i:04d}' for i in range(1, 1001)],
    'ciclos_carga': np.random.randint(10, 2000, 1000),
    'temp_max_celda_C': np.random.uniform(25.0, 45.0, 1000),
    'c_rate': np.random.choice(['0.5C', '1.0C', '2.0C', 'Desconocido'], 1000),
    'soh_porcentaje': np.random.uniform(70.0, 100.0, 1000)
}
df_bat = pd.DataFrame(baterias_data)

df_bat.loc[10:25, 'temp_max_celda_C'] = np.nan 
df_bat.loc[50, 'ciclos_carga'] = -500 
df_bat['soh_porcentaje'] = df_bat['soh_porcentaje'].apply(lambda x: f"{x:.2f}%") 

# --- 2. Generar Dataset 2: Estaciones de Carga (Datos Abiertos Colombia) ---
estaciones_data = {
    'estacion_id': [f'EST_{i:03d}' for i in range(1, 501)],
    'municipio': np.random.choice(['Medellín', 'Bogotá', 'Cali', 'Barranquilla', 'Envigado'], 500),
    'operador': np.random.choice(['EPM', 'Celsia', 'Enel', 'E-Mobility'], 500),
    'kwh_entregados_mes': np.random.uniform(500.0, 5000.0, 500),
    'fecha_reporte': pd.date_range(start='2026-01-01', periods=500, freq='D')
}
df_est = pd.DataFrame(estaciones_data)

df_est.loc[100:150, 'operador'] = np.nan 
# SOLUCIÓN: Convertir la columna a object antes de inyectar el texto
df_est['kwh_entregados_mes'] = df_est['kwh_entregados_mes'].astype(object)
df_est.loc[200:205, 'kwh_entregados_mes'] = "Sin lectura" 
df_est.loc[300, 'municipio'] = "Medelín" 

df_bat.to_csv('data/raw/ev_battery_kaggle.csv', index=False, sep=';')
df_est.to_csv('data/raw/estaciones_carga_colombia.csv', index=False, sep=';')

print("¡Archivos CSV generados con éxito en la carpeta data/raw/!")