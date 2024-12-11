print("When running this program, it combines all the separated DDS images in the directory into whole images.\nDeveloper: ВарКомНадзор (wfom)\nLink to the group in VKontakte: https://vk.com/wf_module \nLink to the group in Telegram: https://t.me/+ASA1xbLPnIQ0ZDUy \nLink to GitHub: https://github.com/wfom \nProgram version: v0.1")

import os

def combine_dds_files(input_dds):
    dds_null = input_dds
    name_dds = input_dds[:-2].split("\\")[-1]
    filename = input_dds[:-2]
    files = []
    files += [f for f in all if f.endswith(f'{name_dds}.16')]
    files += [f for f in all if f.endswith(f'{name_dds}.15')]
    files += [f for f in all if f.endswith(f'{name_dds}.14')]
    files += [f for f in all if f.endswith(f'{name_dds}.13')]
    files += [f for f in all if f.endswith(f'{name_dds}.12')]
    files += [f for f in all if f.endswith(f'{name_dds}.11')]
    files += [f for f in all if f.endswith(f'{name_dds}.10')]
    files += [f for f in all if f.endswith(f'{name_dds}.9')]
    files += [f for f in all if f.endswith(f'{name_dds}.8')]
    files += [f for f in all if f.endswith(f'{name_dds}.7')]
    files += [f for f in all if f.endswith(f'{name_dds}.6')]
    files += [f for f in all if f.endswith(f'{name_dds}.5')]
    files += [f for f in all if f.endswith(f'{name_dds}.4')]
    files += [f for f in all if f.endswith(f'{name_dds}.3')]
    files += [f for f in all if f.endswith(f'{name_dds}.2')]
    files += [f for f in all if f.endswith(f'{name_dds}.1')]
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

def find_files_with_extension():
    all_dds0 = []
    current_dir = os.path.dirname(os.path.abspath(__file__))
    for root, dirs, files in os.walk(current_dir):
        for file in files:
            if file.endswith('.dds.0'):
                full_path = os.path.join(root, file)
                all_dds0.append(full_path)
                
    return all_dds0

def all_files():
    all = []
    current_dir = os.path.dirname(os.path.abspath(__file__))
    for root, dirs, files in os.walk(current_dir):
        for file in files:
            full_path = os.path.join(root, file)
            all.append(full_path)
    return all

all = all_files()
all_dds0 = find_files_with_extension()

for dds in all_dds0:
    combine_dds_files(dds)

input('The program has been completed successfully! To close the program, press [Enter]...')
