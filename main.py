# 1. DEFINICIÓN DEL MÓDULO (FUNCIÓN)
def clasificar_jornada(fila_recurso):
    """
    Función que recibe la fila de un recurso, calcula sus horas totales
    y clasifica su jornada laboral.
    """
    # El nombre está en la posición 0
    nombre = fila_recurso[0]
    
    # Las horas están desde la posición 1 hasta el final
    horas_dias = fila_recurso[1:]
    
    # Lógica de Negocio: Calcular la suma de horas
    total_horas = sum(horas_dias)
    
    # Lógica de Negocio: Clasificar según el umbral de 40 horas
    if total_horas > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"
        
    return nombre, total_horas, clasificacion


# 2. CREACIÓN DE LA MATRIZ (Datos de ejemplo)
# Formato: [Nombre, Lunes, Martes, Miércoles, Jueves, Viernes]
matriz_trabajo = [
    ["Ana Gómez", 8, 8, 8, 8, 8],          # Total: 40 horas
    ["Carlos Ruiz", 9, 10, 8, 9, 8],       # Total: 44 horas
    ["Sofía Pérez", 7, 7, 8, 6, 7],        # Total: 35 horas
    ["David Lyon", 8, 9, 9, 8, 8]          # Total: 42 horas
]


# 3. PROCESAMIENTO Y SALIDA
print("=" * 60)
print(f"{'RECURSO':<15} | {'HORAS TOTALES':<13} | {'CLASIFICACIÓN':<15}")
print("=" * 60)

# Recorremos la matriz fila por fila usando un ciclo
for fila in matriz_trabajo:
    # Llamamos al módulo para que procese la fila actual
    nombre, total, jornada = clasificar_jornada(fila)
    
    # Imprimimos la salida con formato alineado
    print(f"{nombre:<15} | {total:<13} | {jornada:<15}")

print("=" * 60)
