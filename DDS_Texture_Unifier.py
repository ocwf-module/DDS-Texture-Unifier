import os

working_directory = os.getcwd()
print(f'Working directory: {working_directory}')
what_remove = int(input('Delete source files (*.dds.0, *.dds.1, *.dds.2, etc.) to reduce space? Select a number and press [Enter]:\n0 - No\n1 - Yes\n\nYour choice: '))

def combine_dds_files(input_dds, all_files):
    filename = input_dds[:-2]
    related_files = sorted([file for file in all_files if file.startswith(filename) and not file.endswith(".dds.0")], key=lambda x: int(x.split('.')[-1]), reverse=True)
    general = b''
    with open(input_dds, 'rb') as dds_null:
        start = dds_null.read(128)
        end = dds_null.read()
    for file in related_files:
        with open(file, 'rb') as dds_num:
            general += dds_num.read()
    output_file = start + general + end
    with open(filename, 'wb') as completion:
        completion.write(output_file)
        print(f'Merging of the [{filename}] file has been completed successfully')
    if what_remove == 1:
        os.remove(input_dds)
        for file in related_files:
            try:
                os.remove(file)
            except:
                None

def all_files():
    all_files = []
    for root, dirs, files in os.walk(working_directory):
        for file in files:
            full_path = os.path.join(root, file)
            all_files.append(full_path)
    return all_files

def find_files_with_extension():
    all_dds0 = []
    for root, dirs, files in os.walk(working_directory):
        for file in files:
            if file.endswith('.dds.0'):
                full_path = os.path.join(root, file)
                all_dds0.append(full_path)
    return all_dds0

all_files = all_files()
all_dds0 = find_files_with_extension()

for dds in all_dds0:
    combine_dds_files(dds, all_files)

input('The program has been completed successfully! To close the program, press [Enter]...')
