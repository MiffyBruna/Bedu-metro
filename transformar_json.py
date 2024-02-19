# import pandas as pd
# import json

# file_path = '/Users/czarat/Developer/Bedu-metro/150mil_5am_11am_data.json'  # Asegúrate de que la ruta al archivo sea correcta
# with open(file_path, 'r') as file:
#     data = json.load(file)

# rows_list = []
# for id_usuario, registros in data.items():
#     for registro in registros:
#         registro['Ruta'] = json.dumps(registro['Ruta'], ensure_ascii=False)
#         registro['Lineas que fueron usadas'] = json.dumps(registro['Lineas que fueron usadas'])
#         registro['ID_USUARIO'] = id_usuario
#         rows_list.append(registro)

# df = pd.DataFrame(rows_list)
# csv_file_path = "/Users/czarat/Developer/Bedu-metro/usuarios_rango_amplio0.csv"
# df.to_csv(csv_file_path, index=False, encoding='utf-8-sig')


# Define the paths for your original and new CSV files
original_csv_path = '/Users/czarat/Developer/Bedu-metro/usuarios_rango_amplio0.csv'
new_csv_path = '/Users/czarat/Developer/Bedu-metro/usuarios_rango_amplio_correcto.csv'

# Open the original CSV file for reading and the new CSV file for writing
with open(original_csv_path, 'r', encoding='utf-8') as original_file, \
     open(new_csv_path, 'w', encoding='utf-8') as new_file:

    # Iterate over each line in the original file
    for line in original_file:
        # Replace the inner double quotes with single quotes (or any other marker you prefer)
        modified_line = line.replace('""', "'")
        
        # Write the modified line to the new file
        new_file.write(modified_line)
