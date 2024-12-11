print("When running this program, it combines all the separated DDS images in the directory into whole images.\nDeveloper: ВарКомНадзор (wfom)\nLink to the group in VKontakte: https://vk.com/wf_module \nLink to the group in Telegram: https://t.me/+ASA1xbLPnIQ0ZDUy \nLink to GitHub: https://github.com/wfom \nProgram version: v0.2")

import os

def combine_dds_files(input_dds):
    dds_null = input_dds
    name_dds = input_dds[:-2].split("\\")[-1]
    filename = input_dds[:-2]
    number = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    files = []
    files += [f for f in all if f.endswith(f'{name_dds}.{[n for n in number]}')]
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
