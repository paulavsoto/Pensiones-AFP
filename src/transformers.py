# src/transformers.py
import pandas as pd
from pathlib import Path

# Definimos la ruta base del proyecto (dos niveles arriba de src)
BASE_DIR = Path(__file__).parent.parent

def procesar_afp():
    """
    Lee el archivo datos_analisis.xlsx desde data/raw/,
    aplica las transformaciones de limpieza y devuelve el DataFrame limpio.
    """
    # 1. Cargar datos crudos
    ruta_raw = BASE_DIR / "data" / "raw" / "datos_analisis.xlsx"
    df = pd.read_excel(ruta_raw)
    
    # 2. Limpieza (exactamente como en tu notebook)
    # Eliminar filas donde y7 == -88
    df = df[df['y7'] != -88]
    
    # Crear columnas dicotómicas para sexo y área
    df['sexo_dic'] = df['sexo'].replace({1: 0, 2: 1})
    df['area_dic'] = df['area'].replace({1: 0, 2: 1})
    
    # (Opcional) Si deseas agregar más transformaciones, aquí es el lugar
    
    # 3. Retornar el DataFrame limpio
    return df

def guardar_procesado(df):
    """
    Guarda el DataFrame limpio en data/processed/ como un archivo Excel.
    """
    ruta_salida = BASE_DIR / "data" / "processed" / "datos_procesados.xlsx"
    df.to_excel(ruta_salida, index=False)
    print(f"✅ Archivo procesado guardado en: {ruta_salida}")