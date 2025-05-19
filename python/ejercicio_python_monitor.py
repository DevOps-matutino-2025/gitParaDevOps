import time
from datetime import datetime
import psutil  # Importar psutil
#import random  # Ya no necesitamos random

metricas = []

def recopilar_metricas(duracion_segundos=10, intervalo=1):
    print(f"Recopilando métricas reales durante {duracion_segundos} segundos...")
    tiempo_inicio = time.time()
    tiempo_fin = tiempo_inicio + duracion_segundos

    while time.time() < tiempo_fin:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cpu_uso = psutil.cpu_percent(interval=None)  # Uso de CPU
        memoria_uso = psutil.virtual_memory().percent  # Uso de memoria
        disco_uso = psutil.disk_usage('/').percent  # Uso de disco (raíz)

        metrica = {
            "timestamp": timestamp,
            "cpu_uso": cpu_uso,
            "memoria_uso": memoria_uso,
            "disco_uso": disco_uso
        }

        metricas.append(metrica)
        print(f"Métrica recopilada: {metrica}")
        time.sleep(intervalo)

def analizar_metricas():
    if not metricas:
        return "No hay métricas para analizar."

    cpu_promedio = calcular_promedio("cpu")
    memoria_promedio = calcular_promedio("memoria")
    disco_promedio = calcular_promedio("disco")

    cpu_max = uso_maximo("cpu")
    memoria_max = uso_maximo("memoria")
    disco_max = uso_maximo("disco") # No se usa
    informe = f"""
    === INFORME DE RECURSOS DEL SISTEMA ===
    Período: {metricas[0]['timestamp']} - {metricas[-1]['timestamp']}
    Número de muestras: {len(metricas)}

    CPU:
      - Uso promedio: {cpu_promedio:.2f}%
      - Uso máximo: {cpu_max:.2f}%

    Memoria:
      - Uso promedio: {memoria_promedio:.2f}%
      - Uso máximo: {memoria_max:.2f}%

    Disco:
      - Uso promedio: {disco_promedio:.2f}%

    === ALERTAS ===
    {generar_alertas()}
    """
    return informe

def generar_alertas():
    alertas = []
    for metrica in metricas:
        if metrica["cpu_uso"] > 90:
            alertas.append(f"ALERTA CRÍTICA: Uso de CPU alto ({metrica['cpu_uso']:.2f}%) en {metrica['timestamp']}")
        elif metrica["cpu_uso"] > 75:
            alertas.append(f"ALERTA: Uso de CPU elevado ({metrica['cpu_uso']:.2f}%) en {metrica['timestamp']}")
        
        if metrica["memoria_uso"] > 90:
            alertas.append(f"ALERTA CRÍTICA: Uso de Memoria alta ({metrica['memoria_uso']:.2f}%) en {metrica['timestamp']}")
        elif metrica["memoria_uso"] > 75:
            alertas.append(f"ALERTA: Uso de Memoria elevada ({metrica['memoria_uso']:.2f}%) en {metrica['timestamp']}")

        if metrica["disco_uso"] > 90:
            alertas.append(f"ALERTA CRÍTICA: Uso de Disco alto ({metrica['disco_uso']:.2f}%) en {metrica['timestamp']}")
        elif metrica["disco_uso"] > 75:
            alertas.append(f"ALERTA: Uso de Disco elevado ({metrica['disco_uso']:.2f}%) en {metrica['timestamp']}")

    return "\n    ".join(alertas) if alertas else "No se detectaron alertas."

def calcular_promedio(device):
    total = 0
    for metrica in metricas:
        total += metrica[f"{device}_uso"]
    return total / len(metricas) if metricas else 0

def uso_maximo(device):
    maximo = 0
    for metrica in metricas:
        maximo = max(maximo, metrica[f"{device}_uso"])
    return maximo

# Ejecución para demo interactiva
if __name__ == "__main__":
    recopilar_metricas(duracion_segundos=5, intervalo=1)
    informe = analizar_metricas()
    print(informe)