import pandas as pd
import numpy as np
import random

# Configurar semilla para reproducibilidad
np.random.seed(42)
random.seed(42)

def generar_dataset_pericarditis(n_total=10000):
    """
    Genera un dataset para diagnóstico de Pericarditis Aguda
    
    Probabilidades para casos POSITIVOS:
    - Dolor de pecho: 85-90%
    - Roce pericárdico: <33% (usamos ~30%)
    - Cambios ECG: hasta 60%
    - Derrame pericárdico: hasta 60%
    
    Para casos NEGATIVOS, usamos probabilidades mucho menores para simular
    otras condiciones o pacientes sanos.
    """
    
    n_positivos = n_total // 2  # 5000 casos positivos
    n_negativos = n_total // 2  # 5000 casos negativos
    
    datos = []
    
    # Generar casos POSITIVOS (Pericarditis Aguda)
    for i in range(n_positivos):
        # Dolor de pecho: 85-90% en casos positivos
        dolor_pecho = np.random.random() < np.random.uniform(0.85, 0.90)
        
        # Roce pericárdico: ~30% en casos positivos
        roce_pericardico = np.random.random() < 0.30
        
        # Cambios ECG: hasta 60% en casos positivos
        cambios_ecg = np.random.random() < np.random.uniform(0.45, 0.60)
        
        # Derrame pericárdico: hasta 60% en casos positivos
        derrame_pericardico = np.random.random() < np.random.uniform(0.45, 0.60)
        
        # Agregar algunas variables adicionales para hacer el dataset más realista
        edad = np.random.normal(45, 15)  # Edad promedio con desviación
        edad = max(18, min(85, int(edad)))  # Limitar entre 18 y 85 años
        
        sexo = random.choice(['M', 'F'])
        
        # Síntomas adicionales que pueden aparecer en pericarditis
        fiebre = np.random.random() < 0.40  # 40% de casos con fiebre
        disnea = np.random.random() < 0.35  # 35% con dificultad respiratoria
        fatiga = np.random.random() < 0.50  # 50% con fatiga
        
        datos.append({
            'id_paciente': f'P_{i+1:05d}',
            'edad': edad,
            'sexo': sexo,
            'dolor_pecho': dolor_pecho,
            'roce_pericardico': roce_pericardico,
            'cambios_ecg': cambios_ecg,
            'derrame_pericardico': derrame_pericardico,
            'fiebre': fiebre,
            'disnea': disnea,
            'fatiga': fatiga,
            'diagnostico': 1  # Positivo para Pericarditis Aguda
        })
    
    # Generar casos NEGATIVOS (No Pericarditis)
    for i in range(n_negativos):
        # Probabilidades mucho menores para casos negativos
        # Dolor de pecho: 20-30% (puede ser por otras causas)
        dolor_pecho = np.random.random() < np.random.uniform(0.20, 0.30)
        
        # Roce pericárdico: muy raro en casos negativos (~2%)
        roce_pericardico = np.random.random() < 0.02
        
        # Cambios ECG: ocasionales (~15%)
        cambios_ecg = np.random.random() < 0.15
        
        # Derrame pericárdico: poco frecuente (~10%)
        derrame_pericardico = np.random.random() < 0.10
        
        edad = np.random.normal(50, 18)
        edad = max(18, min(85, int(edad)))
        
        sexo = random.choice(['M', 'F'])
        
        # Síntomas menos frecuentes en casos negativos
        fiebre = np.random.random() < 0.15
        disnea = np.random.random() < 0.25
        fatiga = np.random.random() < 0.30
        
        datos.append({
            'id_paciente': f'N_{i+1:05d}',
            'edad': edad,
            'sexo': sexo,
            'dolor_pecho': dolor_pecho,
            'roce_pericardico': roce_pericardico,
            'cambios_ecg': cambios_ecg,
            'derrame_pericardico': derrame_pericardico,
            'fiebre': fiebre,
            'disnea': disnea,
            'fatiga': fatiga,
            'diagnostico': 0  # Negativo para Pericarditis Aguda
        })
    
    # Crear DataFrame
    df = pd.DataFrame(datos)
    
    # Mezclar los datos para que no estén agrupados por diagnóstico
    df = df.sample(frac=1).reset_index(drop=True)
    
    # Renumerar ID de pacientes
    df['id_paciente'] = [f'PAC_{i+1:05d}' for i in range(len(df))]
    
    return df

# Generar el dataset
dataset = generar_dataset_pericarditis(10000)

# Mostrar estadísticas del dataset
print("=== ESTADÍSTICAS DEL DATASET GENERADO ===\n")
print(f"Total de registros: {len(dataset)}")
print(f"Casos positivos: {sum(dataset['diagnostico'] == 1)} ({sum(dataset['diagnostico'] == 1)/len(dataset)*100:.1f}%)")
print(f"Casos negativos: {sum(dataset['diagnostico'] == 0)} ({sum(dataset['diagnostico'] == 0)/len(dataset)*100:.1f}%)")

print("\n=== PREVALENCIA DE SÍNTOMAS EN CASOS POSITIVOS ===")
casos_positivos = dataset[dataset['diagnostico'] == 1]
print(f"Dolor de pecho: {sum(casos_positivos['dolor_pecho'])/len(casos_positivos)*100:.1f}%")
print(f"Roce pericárdico: {sum(casos_positivos['roce_pericardico'])/len(casos_positivos)*100:.1f}%")
print(f"Cambios ECG: {sum(casos_positivos['cambios_ecg'])/len(casos_positivos)*100:.1f}%")
print(f"Derrame pericárdico: {sum(casos_positivos['derrame_pericardico'])/len(casos_positivos)*100:.1f}%")

print("\n=== PREVALENCIA DE SÍNTOMAS EN CASOS NEGATIVOS ===")
casos_negativos = dataset[dataset['diagnostico'] == 0]
print(f"Dolor de pecho: {sum(casos_negativos['dolor_pecho'])/len(casos_negativos)*100:.1f}%")
print(f"Roce pericárdico: {sum(casos_negativos['roce_pericardico'])/len(casos_negativos)*100:.1f}%")
print(f"Cambios ECG: {sum(casos_negativos['cambios_ecg'])/len(casos_negativos)*100:.1f}%")
print(f"Derrame pericárdico: {sum(casos_negativos['derrame_pericardico'])/len(casos_negativos)*100:.1f}%")

print("\n=== PRIMEROS 10 REGISTROS DEL DATASET ===")
print(dataset.head(10))

print(f"\n=== INFORMACIÓN GENERAL ===")
print(dataset.info())

print(f"\n=== ESTADÍSTICAS DESCRIPTIVAS ===")
print(dataset.describe())

# Guardar el dataset en CSV
dataset.to_csv('dataset_pericarditis_aguda.csv', index=False)
print(f"\n✅ Dataset guardado como 'dataset_pericarditis_aguda.csv'")

# Mostrar distribución por edad y sexo
print(f"\n=== DISTRIBUCIÓN POR EDAD ===")
print(f"Edad promedio: {dataset['edad'].mean():.1f} años")
print(f"Edad mínima: {dataset['edad'].min()} años")
print(f"Edad máxima: {dataset['edad'].max()} años")

print(f"\n=== DISTRIBUCIÓN POR SEXO ===")
print(dataset['sexo'].value_counts())
print(dataset['sexo'].value_counts(normalize=True) * 100)