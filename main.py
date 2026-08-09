# main.py
from src.transformers import procesar_afp, guardar_procesado

if __name__ == "__main__":
    print("🚀 Iniciando pipeline de la AFP...")
    
    # 1. Procesar los datos
    df_limpio = procesar_afp()
    
    # 2. Guardar el resultado
    guardar_procesado(df_limpio)
    
    print("🎯 Pipeline finalizado con éxito.")