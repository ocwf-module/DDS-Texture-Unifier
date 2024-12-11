import os

def combine_dds_files(output_file):
    dds_null = [f for f in os.listdir('.') if f.endswith('.dds.0')]
    files = []
    files += [f for f in os.listdir('.') if f.endswith('.dds.6')]
    files += [f for f in os.listdir('.') if f.endswith('.dds.5')]
    files += [f for f in os.listdir('.') if f.endswith('.dds.4')]
    files += [f for f in os.listdir('.') if f.endswith('.dds.3')]
    files += [f for f in os.listdir('.') if f.endswith('.dds.2')]
    files += [f for f in os.listdir('.') if f.endswith('.dds.1')]

    for dds0 in dds_null:
        with open(dds0, 'rb') as first_file:
            start = first_file.read(128)
            end = first_file.read()
    
    # Объединяем остальные части в порядке убывания номеров
    general = b'' # Переменная для хранения промежуточных данных
    for file in files:
        with open(file, 'rb') as infile:
            general += infile.read()
    
    # Формируем итоговую последовательность данных
    combined_data = start + general + end
    
    # Сохраняем результат в новый файл
    with open(output_file, 'wb') as outfile:
        outfile.write(combined_data)

if __name__ == "__main__":
    combine_dds_files('output.dds')
