import os

what_remove = int(input('Delete source files (*.dds.0, *.dds.1, *.dds.2, etc.) to reduce space? Select a number and press [Enter]:\n0 - No\n1 - Yes\n\nYour choice: '))

def combine_dds_files(input_dds):
    dds_null = input_dds
    filename = input_dds[:-2]
    files = []
    files += [f for f in all if f.endswith(f'{filename}.16')]
    files += [f for f in all if f.endswith(f'{filename}.15')]
    files += [f for f in all if f.endswith(f'{filename}.14')]
    files += [f for f in all if f.endswith(f'{filename}.13')]
    files += [f for f in all if f.endswith(f'{filename}.12')]
    files += [f for f in all if f.endswith(f'{filename}.11')]
    files += [f for f in all if f.endswith(f'{filename}.10')]
    files += [f for f in all if f.endswith(f'{filename}.9')]
    files += [f for f in all if f.endswith(f'{filename}.8')]
    files += [f for f in all if f.endswith(f'{filename}.7')]
    files += [f for f in all if f.endswith(f'{filename}.6')]
    files += [f for f in all if f.endswith(f'{filename}.5')]
    files += [f for f in all if f.endswith(f'{filename}.4')]
    files += [f for f in all if f.endswith(f'{filename}.3')]
    files += [f for f in all if f.endswith(f'{filename}.2')]
    files += [f for f in all if f.endswith(f'{filename}.1')]
    with open(dds_null, 'rb') as first_file:
        start = first_file.read(128)
        end = first_file.read()
    general = b''
    for file in files:
        with open(file, 'rb') as infile:
            general += infile.read()
    data = start + general + end
    with open(filename, 'wb') as outfile:
        outfile.write(data)
        print(f'Merging of the [{filename}] file has been completed successfully')
    if what_remove == 1:
        os.remove(dds_null)
        for file in files:
            try:
                os.remove(file)
            except:
                None

def all_files():
    all = []
    current_dir = os.getcwd()
    print(f'Working directory: {current_dir}')
    for root, dirs, files in os.walk(current_dir):
        for file in files:
            full_path = os.path.join(root, file)
            all.append(full_path)
    return all

def find_files_with_extension():
    all_dds0 = []
    current_dir = os.getcwd()
    for root, dirs, files in os.walk(current_dir):
        for file in files:
            if file.endswith('.dds.0'):
                full_path = os.path.join(root, file)
                all_dds0.append(full_path)
                
    return all_dds0

all = all_files()
all_dds0 = find_files_with_extension()

for dds in all_dds0:
    combine_dds_files(dds)

input('The program has been completed successfully! To close the program, press [Enter]...')
