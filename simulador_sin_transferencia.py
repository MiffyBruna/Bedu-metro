import random
from datetime import date, datetime, time, timedelta
from djkstra_una_estacion import linea_1, linea_2,linea_3, linea_4, linea_5, linea_6, linea_7, linea_8, linea_9, linea_A, linea_B, linea_12

# Lista de estaciones de la Línea 1

# Agrupa todas las líneas en una lista
todas_las_lineas = [linea_1, linea_2, linea_3, linea_4, linea_5, linea_6, linea_7, linea_8, linea_9, linea_A, linea_B, linea_12]

nombre_de_lineas = {
    '1': linea_1, '2': linea_2, '3': linea_3,
    '4': linea_4, '5': linea_5, '6': linea_6,
    '7': linea_7, '8': linea_8, '9': linea_9,
    'A': linea_A, 'B': linea_B, '12': linea_12
}

def simulate_commuter_journey():
    # Selecciona una línea al azar
    linea_abordada, stations = random.choice(list(nombre_de_lineas.items()))
    # Elige una estación de inicio y una de destino al azar
    start_index = random.randint(0, len(stations) - 1)
    end_index = random.randint(0, len(stations) - 1)
    
    # Asegurarnos que la estación de inicio y destino no sean la misma
    while end_index == start_index:
        end_index = random.randint(0, len(stations) - 1)

    # Determina las estaciones del viaje
    if start_index < end_index:
        journey_stations = stations[start_index:end_index + 1]
    else:
        journey_stations = stations[end_index:start_index + 1][::-1]

    # Elige una duración al azar para el viaje, entre 3 y 5 minutos
    journey_time_minutes = random.randint(3, 5)

    # Generar una fecha aleatoria 
    start_date = date(2023, 1, 1)
    end_date = date(2024, 2, 2)
    random_days = (end_date - start_date).days
    random_day = start_date + timedelta(days=random.randint(0, random_days))

    # Definir los rangos de horario para cada día de la semana
    day_of_week = random_day.weekday()
    if day_of_week < 5:  # De lunes a viernes
        hour_range = (5, 23)
    elif day_of_week == 5:  # Sábado
        hour_range = (6, 23)
    else:  # Domingo
        hour_range = (7, 23)

    # Generar una hora aleatoria dentro del rango especificado
    start_hour = random.randint(*hour_range)
    start_minute = random.randint(0, 59)

    # Crear un objeto datetime con la fecha y hora aleatorias
    start_time = datetime.combine(random_day, time(hour=start_hour, minute=start_minute))



    # Calcula la hora de fin del viaje
    end_time = start_time + timedelta(minutes=journey_time_minutes)

    #Generar aleatoriamente compras, e interactua con app
    interactua_con_app = random.choice(["Si", "No"])
    compras_en_app = random.randint(1, 3)

    # Regresa un diccionario con los detalles del viaje
    return { 
        "HoraDeEntrada": start_time.strftime("%H:%M:%S"),
        "HoraDeSalida": end_time.strftime("%H:%M:%S"),
        "Fecha": start_time.strftime("%d/%m/%Y"),
        "InteractuaConApp": interactua_con_app,
        "ComprasEnApp": compras_en_app,
        "Ruta": journey_stations,
        "Estación de entrada":  stations[start_index],
        "Estación de salida":  stations[start_index],
        "Lineas que fueron usadas": [stations[start_index]],
    }


# Número de pasajeros a simular
num_commuters = 4
# Genera los viajes para cada pasajero
commuter = [simulate_commuter_journey() for _ in range(num_commuters)]


for i, trip in enumerate(commuter, 1):
    print(f"Commuter {i}: {trip}")
