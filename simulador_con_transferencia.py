import random
from datetime import date, datetime, time, timedelta
from lineas import  linea_1, linea_2,linea_3, linea_4, linea_5, linea_6, linea_7, linea_8, linea_9, linea_A, linea_B, linea_12
from djkstra_con_transferencias import dijkstra, metro_graph

todas_las_estaciones = list(set().union(linea_1, linea_2, linea_3, linea_4, linea_5, linea_6, linea_7, linea_8, linea_9, linea_A, linea_B, linea_12))

def simulate_commuter_journey():
    start_station = random.choice(todas_las_estaciones)
    end_station = random.choice(todas_las_estaciones)
    
    # Asegurarnos que la estación de inicio y destino no sean la misma
    while end_station == start_station:
        end_station = random.choice(todas_las_estaciones)


    station_count, journey_stations,lines_rider_transfered = dijkstra(metro_graph, start_station, end_station)

    # Elige una duración al azar del viaje por estación
    journey_time_minutes = (station_count - 1) * random.randint(3, 5)

    # Generar una fecha y hora aleatorias
    start_date = date(2023, 1, 1)
    end_date = date(2024, 2, 2)
    random_days = random.randint(0, (end_date - start_date).days)
    random_day = start_date + timedelta(days=random_days)
    start_time = datetime.combine(random_day, time(random.randint(5, 23), random.randint(0, 59)))

    # Calcula la hora de fin del viaje
    end_time = start_time + timedelta(minutes=journey_time_minutes)


    #Generar aleatoriamente compras, e interactua con app
    interactua_con_app = random.choice(["Si", "No"])
    compras_en_app = random.randint(1, 3)

    return {
        "HoraDeEntrada": start_time.strftime("%H:%M:%S"),
        "HoraDeSalida": end_time.strftime("%H:%M:%S"),
        "Fecha": start_time.strftime("%d/%m/%Y"),
        "InteractuaConApp": interactua_con_app,
        "ComprasEnApp": compras_en_app,
        "Ruta": journey_stations,
        "Estación de entrada": start_station,
        "Estación de salida": end_station,
        "Lineas que fueron usadas": lines_rider_transfered,
    }
    

num_commuters = 1  # Cantidad de entradas
commuter_journeys = [simulate_commuter_journey() for _ in range(num_commuters)]

for journey in commuter_journeys:
    print(journey)