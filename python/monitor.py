## Ejercicio Monitoreo de recursos del sistema
## Este ejercicio simula la recopilación y análisis de métricas del sistema, una tarea común en DevOps.

import time
from datetime import datetime
import random # usar import psutil en vez de random



metricas = []

def recopilar_metricas(duracion_segundos=10, intervalo=1):
    print(f"Recopilando métricas reales durante {duracion_segundos} segundos...")
    tiempo_inicio = time.time()
    tiempo_fin = tiempo_inicio + duracion_segundos

    while time.time() < tiempo_fin:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cpu_uso = random.uniform(0, 100) # sustituir el uso de random por psutil.cpu_percent(interval=None)
        memoria_uso = random.uniform(0, 100) # usar psutil.virtual_memory().percent
        disco_uso = random.uniform(0, 100) # psutil.disk_usage('/').percent

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
    memoria_max = uso_maximo("cpu")
    disco_max = uso_maximo("cpu")

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
      - Uso máximo: {disco_max:.2f}%

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
        
        # agregar las alertas tanto para el uso de memoria como para el uso de disco



    return "\n    ".join(alertas) if alertas else "No se detectaron alertas."

def calcular_promedio(device):
    # calcular correctamente
    return random.uniform(0, 100)

def uso_maximo(device):
    # calcular correctamente
    return random.uniform(0, 100)

# Ejecución para demo interactiva
if __name__ == "__main__":
    recopilar_metricas(duracion_segundos=5, intervalo=1)
    informe = analizar_metricas()
    print(informe)
