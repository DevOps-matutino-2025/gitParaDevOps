## Ejercicio Monitoreo de recursos del sistema
## Este ejercicio simula la recopilación y análisis de métricas del sistema, una tarea común en DevOps.

import time
from datetime import datetime
import random # usar import psutil en vez de random
import psutil



metricas = []

def recopilar_metricas(duracion_segundos=10, intervalo=1):
    print(f"Recopilando métricas reales durante {duracion_segundos} segundos...")
    tiempo_inicio = time.time()
    tiempo_fin = tiempo_inicio + duracion_segundos

    while time.time() < tiempo_fin:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cpu_uso = psutil.cpu_percent(interval=None) # sustituir el uso de random por psutil.cpu_percent(interval=None)
        memoria_uso = psutil.virtual_memory().percent # usar 
        disco_uso = psutil.disk_usage('/').percent # 

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

    #cpu_promedio = calcular_promedio("cpu")
    #memoria_promedio = calcular_promedio("memoria")
    #disco_promedio = calcular_promedio("disco")
    
    cpu_promedio = sum(m['cpu_uso'] for m in metricas) / len(metricas)
    memoria_promedio = sum(m['memoria_uso'] for m in metricas) / len(metricas)
    disco_promedio = sum(m['disco_uso'] for m in metricas) / len(metricas)

    #cpu_max = uso_maximo("cpu")
    #memoria_max = uso_maximo("memoria")
    #disco_max = uso_maximo("disco")
    
    cpu_max = max(m['cpu_uso'] for m in metricas)
    memoria_max = max(m['memoria_uso'] for m in metricas)
    disco_max = max(m['disco_uso'] for m in metricas)

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
            
        if metrica["memoria_uso"] > 90:
            alertas.append(f"ALERTA CRÍTICA: Uso de CPU alto ({metrica['memoria_uso']:.2f}%) en {metrica['timestamp']}")
        elif metrica["memoria_uso"] > 75:
            alertas.append(f"ALERTA: Uso de CPU elevado ({metrica['memoria_uso']:.2f}%) en {metrica['timestamp']}")
            
        if metrica["disco_uso"] > 90:
            alertas.append(f"ALERTA CRÍTICA: Uso de CPU alto ({metrica['disco_uso']:.2f}%) en {metrica['timestamp']}")
        elif metrica["disco_uso"] > 75:
            alertas.append(f"ALERTA: Uso de CPU elevado ({metrica['disco_uso']:.2f}%) en {metrica['timestamp']}")
        
        # agregar las alertas tanto para el uso de memoria como para el uso de disco



    return "\n    ".join(alertas) if alertas else "No se detectaron alertas."

def calcular_promedio(device):
    # calcular correctamente
    # metricas [ {'memoria_uso': 50, 'cpu_uso':34}, {'memoria_uso': 50, 'cpu_uso':42}, {'memoria_uso': 50, 'cpu_uso':5}, {'memoria_uso': 50, 'cpu_uso':80}]
    suma = 0
    if device == "cpu":
    	for m in metricas:
        	suma += m['cpu_uso']
    elif device == "memoria":
    	for m in metricas:
        	suma += m['memoria_uso']
    elif device == "disco":
    	for m in metricas:
        	suma += m['disco_uso']
    promedio = suma / len(metricas)
    return promedio


def uso_maximo(device):
    # calcular correctamente
    maximo = -1
    if device == "cpu":
    	for m in metricas:
    	    if m['cpu_uso'] > maximo:
    	        maximo = m['cpu_uso']
    if device == "memoria":
    	for m in metricas:
    	    if m['memoria_uso'] > maximo:
    	        maximo = m['memoria_uso']
    if device == "disco":
    	for m in metricas:
    	    if m['disco_uso'] > maximo:
    	        maximo = m['disco_uso']
    return maximo


# Ejecución para demo interactiva
if __name__ == "__main__":
    recopilar_metricas(duracion_segundos=5, intervalo=1)
    informe = analizar_metricas()
    print(informe)
    
    
# Que necesito instalar
# sudo apt install python3-pip
# sudo apt install python3-ven

# Creando el entrono virtual
# python -m venv [carpeta]

# Activar el entorno virtual
# cd [carpeta]
# source bin/activate

# instalar paquetes
# pip3 install psutil
